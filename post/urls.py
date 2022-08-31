from django.urls import path
from post.views import PostListView, PostDetailView, PostDeleteView, \
    TagDetailView, AddPostView, EditPostView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail_page'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail_page'),
    path('post/new/', AddPostView.as_view(), name='post_new_page'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='post_edit_page'),
    path('post/<int:pk>/remove', PostDeleteView.as_view(), name='post_delete_page'),
]
