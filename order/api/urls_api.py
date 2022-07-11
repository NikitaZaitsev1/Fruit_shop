from django.urls import path, include, re_path

from order.views import OrderApiList, OrderApiUpdate, OrderApiDestroy

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/order/', OrderApiList.as_view()),
    path('api/v1/order/<int:pk>/', OrderApiUpdate.as_view()),
    path('api/v1/orderdelete/<int:pk>/', OrderApiDestroy.as_view()),
]
