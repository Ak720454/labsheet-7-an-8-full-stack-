from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={"placeholder": "Your full name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )
    subject = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "What is this about?"}),
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Write your feedback (min 10 characters)"}),
    )
