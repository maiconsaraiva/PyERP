# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.product import (
    DeleteProduct, ProductCreateView, ProductDetailView, ProductListView,
    ProductUpdateView)

urlpatterns = [
    path('', login_required(ProductListView.as_view()), name='products'),
    path(
        'add/',
        login_required(ProductCreateView.as_view()),
        name='product-add'
    ),
    path(
        '<int:pk>/',
        login_required(ProductDetailView.as_view()),
        name='product-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(ProductUpdateView.as_view()),
        name='product-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(DeleteProduct),
        name='product-delete'
    ),
]
