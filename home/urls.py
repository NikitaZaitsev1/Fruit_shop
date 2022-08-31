from django.urls import path
from home.views import HomeView, AboutView, ContactFormView, FeedBackView
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("home/", HomeView.as_view(), name="home_page"),
    path("", lambda request: redirect(reverse("home_page"))),
    path("about/", AboutView.as_view(), name="about_page"),
    path("contact/", ContactFormView.as_view(), name="contact_page"),
    path("feedback/", FeedBackView.as_view(), name="feedback_page"),
]
