from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from post.forms import PostForm
from post.models import Post, Tag
from post.api.permissions import IsAdminOrReadOnly
from post.api.serializers import PostSerializer


class PostListView(ListView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'tag'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'

    def get_success_url(self):
        return reverse_lazy('post_detail_page', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse_lazy('post_detail_page', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list_page')


"""API VIEWS"""


class PostApiList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostApiUpdate(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PostAPIListPagination


class PostApiDestroy(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
