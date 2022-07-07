from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from home.forms import FeedBackForm
from home.models import FeedBack
from home.api.permissions import IsAdminOrReadOnly
from home.api.serializers import FeedBackSerializer


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


"""API VIEWS"""


class FeedBackApiList(ListCreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FeedBackAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class FeedBackApiUpdate(RetrieveUpdateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    pagination_class = FeedBackAPIListPagination


class FeedBackApiDestroy(RetrieveDestroyAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (IsAdminOrReadOnly,)
