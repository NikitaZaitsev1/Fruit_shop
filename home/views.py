from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from home.forms import FeedBackForm
from home.models import FeedBack
from home.api.permissions import IsAdminOrReadOnly
from home.api.serializers import FeedBackSerializer
from marketplace.models import Product
from post.models import Post


class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['published_date']

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:3]
        return context

    def post_detail_view(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', context={'post': post})


class AboutView(TemplateView):
    template_name = "about.html"


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = FeedBackForm
    success_url = reverse_lazy('feedback_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FeedBackView(TemplateView):
    template_name = "feedback_success.html"


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
    pagination_class = FeedBackAPIListPagination


class FeedBackApiDestroy(RetrieveDestroyAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (IsAdminOrReadOnly,)
