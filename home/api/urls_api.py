from django.urls import path, include, re_path

from home.views import FeedBackApiList, FeedBackApiDestroy, FeedBackApiUpdate

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    #TODO solve create method problem
    path('api/v1/feedback/', FeedBackApiList.as_view()),
    path('api/v1/feedback/<int:pk>/', FeedBackApiUpdate.as_view()),
    path('api/v1/feedbackdelete/<int:pk>/', FeedBackApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
