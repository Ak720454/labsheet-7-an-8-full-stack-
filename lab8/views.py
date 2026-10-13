import logging

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm

contact_logger = logging.getLogger("lab8.contact")


def home(request):
    return render(request, "lab8/home.html")


def about(request):
    return render(request, "lab8/about.html")


def contact(request):
    """Task 8.3: validate the form, then forward feedback to the server logs."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact_logger.info(
                "CONTACT FEEDBACK | name=%s | email=%s | subject=%s | message=%s",
                data["name"], data["email"], data["subject"],
                data["message"].replace("\n", " "),
            )
            # Task 8.2: flash message shown by the master template on the next page
            messages.success(request, "Thank you! Your feedback has been received.")
            return redirect("lab8:contact")
        messages.error(request, "Please correct the errors below and try again.")
    else:
        form = ContactForm()
    return render(request, "lab8/contact.html", {"form": form})
