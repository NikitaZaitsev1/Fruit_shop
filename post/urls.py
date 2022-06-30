from django.urls import path
from post.views import PostListView, PostDetailView, tag_detail_view, post_new_view, post_edit_view, PostDeleteView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail_page'),
    path('tag/<int:pk>/', tag_detail_view, name='tag_detail_page'),
    path('post/new/', post_new_view, name='post_new_page'),
    path('post/edit/<int:pk>', post_edit_view, name='post_edit_page'),
    path('post/<int:pk>/remove', PostDeleteView.as_view(), name='post_delete_page'),
]
