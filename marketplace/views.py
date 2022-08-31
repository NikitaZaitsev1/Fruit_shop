from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from marketplace.forms import ProductForm
from marketplace.models import Product, Category
from marketplace.api.permissions import IsAdminOrReadOnly
from marketplace.api.serializers import ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['?']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list_page')


def cat_detail_view(request, pk):
    category_products = Product.objects.filter(category=pk).order_by('?')
    category = Category.objects.filter(product=pk)
    cat_menu = Category.objects.all()
    return render(request, 'cat_detail.html', {
        'cats': pk,
        'category_products': category_products,
        'category': category,
        'cat_menu': cat_menu
    })


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_new.html'

    def get_success_url(self):
        return reverse_lazy('product_detail_page', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'

    def get_success_url(self):
        return reverse_lazy('product_detail_page', kwargs={'pk': self.object.pk})


"""API VIEWS"""


class ProductApiList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductApiUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ProductAPIListPagination


class ProductApiDestroy(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
