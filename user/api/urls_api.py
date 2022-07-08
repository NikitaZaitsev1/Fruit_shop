from django.urls import path, include, re_path

from user.views import UserApiList, UserApiUpdate, UserApiDestroy

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/user/', UserApiList.as_view()),
    path('api/v1/user/<int:pk>/', UserApiUpdate.as_view()),
    path('api/v1/userdelete/<int:pk>/', UserApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
