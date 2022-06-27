from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from post.models import Post, Tag


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'


# class TagDetailView(ListView):
#     model = Tag
#     template_name = 'tag_detail.html'
#     pk_url_kwarg = 'pk'
#     context_object_name = 'tag'

def tag_detail_view(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'tag_detail.html', context={'tag': tag})
