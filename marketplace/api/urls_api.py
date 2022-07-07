from django.urls import path, include, re_path

from marketplace.views import ProductApiList, ProductApiUpdate, ProductApiDestroy

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # TODO solve create method problem
    path('api/v1/product/', ProductApiList.as_view()),
    path('api/v1/product/<int:pk>/', ProductApiUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', ProductApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
