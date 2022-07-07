from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView

from marketplace.forms import ProductForm
from marketplace.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['-published_date']

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
    category_products = Product.objects.filter(category=pk)
    category = Category.objects.filter(product=pk)
    cat_menu = Category.objects.all()
    return render(request, 'cat_detail.html', {
        'cats': pk,
        'category_products': category_products,
        'category':category,
        'cat_menu': cat_menu
    })


def product_new_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail_page', pk=product.pk)
    else:
        product_form = ProductForm()
        return render(request, 'product_new.html', {'product_form': product_form})


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail_page', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'product_form': form})
