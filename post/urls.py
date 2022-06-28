from django.urls import path
from post.views import PostListView, PostDetailView, tag_detail_view, post_new_view

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail_page'),
    path('tag/<int:pk>/', tag_detail_view, name='tag_detail_page'),
    path('post/new/', post_new_view, name='post_new_page'),
]
