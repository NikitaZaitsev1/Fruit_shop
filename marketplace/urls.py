from django.urls import path

from marketplace.views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list_page'),
]
