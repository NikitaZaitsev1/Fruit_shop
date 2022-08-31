from django.urls import path

from marketplace.views import ProductListView, ProductDetailView, ProductDeleteView, cat_detail_view, AddProductView, \
    EditProductView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list_page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_page'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='product_edit_page'),
    path('product/new/', AddProductView.as_view(), name='product_new_page'),
    path('product/<int:pk>/remove', ProductDeleteView.as_view(), name='product_delete_page'),
    path('category/<str:pk>/', cat_detail_view, name='cat_detail_page'),
]
