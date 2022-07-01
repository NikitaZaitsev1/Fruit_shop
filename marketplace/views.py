from django.views.generic import ListView

from marketplace.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['-published_date']
