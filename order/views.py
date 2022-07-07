from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView
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




# def order_new_view(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.customer = request.user
#             order.published_date = timezone.now()
#
#             #TODO: delete
#             # order_products = Product.objects.filter(order=pk)
#             # for item in order_products:
#             #     Order.objects.create(order=order,
#             #                          product=item.name,
#             #                          price=item.price,
#             #                          )
#
#             order.save()
#             return redirect('order_detail_page', pk=order.pk)
#     else:
#         order_form = OrderForm()
#         return render(request, 'order_new.html', {'order_form': order_form})

def order_new_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('order_detail_page', pk=order.pk)
    else:
        order_form = OrderForm()
        return render(request, 'order_new.html', {'order_form': order_form})


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
    # authentication_classes = (TokenAuthentication,)
    pagination_class = OrderAPIListPagination


class OrderApiDestroy(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly,)