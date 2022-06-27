from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from home.forms import FeedBackForm


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


def contacts_view(request):
    form = FeedBackForm()
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("contact_page"))

    context = {
        "feedback_form": form,
        "field_name": ["Full Name", "Email", "Phone", "Message"]
    }
    return render(request, "contact.html", context)


class FruitsView(TemplateView):
    template_name = "fruits.html"
