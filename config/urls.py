from django.urls import include, path

urlpatterns = [
    path("lab7/", include("lab7.urls")),
    path("", include("lab8.urls")),
]
