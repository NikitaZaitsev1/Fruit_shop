from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView
from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from order.models import Order
from post.models import Post, Tag
from user.forms import SignUpForm, LoginForm, AddTagForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from user.models import User
from user.api.permissions import IsAdminOrReadOnly
from user.api.serializers import UserSerializer
from user.service import send
from user.tasks import send_welcome_email


class UserView(ListView):
    model = User
    template_name = "users.html"
    paginate_by = 2


class UserDetailView(TemplateView):
    template_name = "user.html"

    def get_context_data(self, *args, **kwargs):
        orders = Order.objects.all()
        posts = Post.objects.all()
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context["orders"] = orders
        context["posts"] = posts
        return context


class ApiDocView(TemplateView):
    template_name = "api_doc.html"


def log_in(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.auth(request)
            next_url = request.GET.get("next")
            if next_url is not None:
                return redirect(next_url)
            return redirect(reverse("home_page"))
        context.update(login_form=login_form)
    return render(request, "login.html", context)


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse("login_page")

    def form_valid(self, form):
        form.save()
        send_welcome_email.delay(form.instance.email)
        return super().form_valid(form)


class AddTagView(CreateView):
    model = Tag
    form_class = AddTagForm
    template_name = 'add_tag.html'

    def get_success_url(self):
        return reverse_lazy('user_page')

    def form_valid(self, form):
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("home_page"))


"""API VIEWS"""


class UserApiList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserApiUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UserAPIListPagination


class UserApiDestroy(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)
