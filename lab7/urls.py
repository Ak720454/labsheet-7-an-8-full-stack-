from django.urls import path

from . import views

app_name = "lab7"

urlpatterns = [
    path("fruits/", views.fruits, name="fruits"),
    path("students/", views.students, name="students"),
]
