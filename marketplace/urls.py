from django.urls import path

from marketplace.views import ProductListView, cat_detail_view, ProductDetailView, ProductDeleteView, product_new_view, \
    product_edit_view

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list_page'),
    path('category/<int:pk>/', cat_detail_view, name='cat_detail_page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_page'),
    path('product/edit/<int:pk>', product_edit_view, name='product_edit_page'),
    path('product/new/', product_new_view, name='product_new_page'),
    path('product/<int:pk>/remove', ProductDeleteView.as_view(), name='product_delete_page'),

]
