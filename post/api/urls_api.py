from django.urls import path, include, re_path

from post.views import PostApiList, PostApiDestroy, PostApiUpdate

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # TODO solve create method problem
    path('api/v1/post/', PostApiList.as_view()),
    path('api/v1/post/<int:pk>/', PostApiUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>/', PostApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
