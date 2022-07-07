from django.urls import path

from order.views import order_new_view, OrderDetailView

urlpatterns = [
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail_page'),
    path('order/new/', order_new_view, name='order_new_page'),

]
