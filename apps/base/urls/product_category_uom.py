"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.product_category_uom import (
    DeleteProductCategoryUOM, ProductCategoryUOMCreateView,
    ProductCategoryUOMDetailView, ProductCategoryUOMListView,
    ProductCategoryUOMUpdateView)

urlpatterns = [
    path('product-category-uom', ProductCategoryUOMListView.as_view(), name='product-category-uom'),
    path('product-category-uom/add/', ProductCategoryUOMCreateView.as_view(), name='product-category-uom-add'),
    path('product-category-uom/<int:pk>/', ProductCategoryUOMDetailView.as_view(), name='product-category-uom-detail'),
    path('product-category-uom/<int:pk>/update', ProductCategoryUOMUpdateView.as_view(), name='product-category-uom-update'),
    path('product-category-uom/<int:pk>/delete/', DeleteProductCategoryUOM, name='product-category-uom-delete'),
]
