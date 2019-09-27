# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.product_brand import (
    ProductBrandCreateView, ProductBrandDeleteView, ProductBrandDetailView,
    ProductBrandListView, ProductBrandUpdateView)

urlpatterns = [
    path('product-brand', ProductBrandListView.as_view(), name='product-brand'),
    path('product-brand/add/', ProductBrandCreateView.as_view(), name='product-brand-add'),
    path('product-brand/<int:pk>/', ProductBrandDetailView.as_view(), name='product-brand-detail'),
    path('product-brand/<int:pk>/update', ProductBrandUpdateView.as_view(), name='product-brand-update'),
    path('product-brand/<int:pk>/delete/', ProductBrandDeleteView.as_view(), name='product-brand-delete'),
]
