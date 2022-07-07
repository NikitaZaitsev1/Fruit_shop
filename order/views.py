from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from order.forms import OrderForm
from order.models import Order


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
