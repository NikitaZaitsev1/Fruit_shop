from django.urls import path
from user.views import log_out, SignUpView, log_in
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path("login/", log_in, name="login_page"),
    path("signup/", SignUpView.as_view(), name="signup_page"),
    path("logout/", log_out, name="logout_page"),
    path("", lambda request: redirect(reverse("login_page"))),
]
