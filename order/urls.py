from django.urls import path

from order.views import OrderDetailView, AddOrderView

urlpatterns = [
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail_page'),
    path('order/new/', AddOrderView.as_view(), name='order_new_page'),

]
