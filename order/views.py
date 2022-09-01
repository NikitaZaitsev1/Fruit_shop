from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, CreateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from order.forms import OrderForm
from order.models import Order
from order.api.permissions import IsAdminOrReadOnly
from order.api.serializers import OrderSerializer


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'order'


class AddOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_new.html'

    def get_success_url(self):
        return reverse_lazy('order_detail_page', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


"""API VIEWS"""


class OrderApiList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class OrderApiUpdate(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = OrderAPIListPagination


class OrderApiDestroy(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly,)
