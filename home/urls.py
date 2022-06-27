from django.urls import path
from home.views import HomeView, AboutView, FruitsView, contacts_view
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("home/", HomeView.as_view(), name="home_page"),
    path("", lambda request: redirect(reverse("home_page"))),
    path("about/", AboutView.as_view(), name="about_page"),
    path("contact/",contacts_view, name="contact_page"),
    path("fruits/", FruitsView.as_view(), name="fruits_page"),
]
