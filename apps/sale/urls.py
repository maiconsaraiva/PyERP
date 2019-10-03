"""Rutas del módulo de ordenes de venta
"""
# Django Library
from django.urls import path

# Localfolder Library
from .reports.saleorderpdf import sale_order_pdf
from .views import (
    ProductAutoComplete, SaleOrderAddView, SaleOrderDeleteView,
    SaleOrderDetailView, SaleOrderEditView, SaleOrderListView)

app_name = 'PySaleOrder'

urlpatterns = [
    # ========================== Sale Orders URL's ========================= #
    path('sale-order', SaleOrderListView.as_view(), name='list'),
    path('sale-order/<int:pk>', SaleOrderDetailView.as_view(), name='detail'),
    path('sale-order/add/', SaleOrderAddView.as_view(), name='add'),
    path(
        'sale-order/edit/<int:pk>',
        SaleOrderEditView.as_view(),
        name='update'
    ),
    path(
        'sale-order/delete/<int:pk>',
        SaleOrderDeleteView.as_view(),
        name='delete'
    ),
    # ====================== Sale Orders Reports URL's ===================== #
    path(
        'sale-order-pdf/<int:pk>',
        sale_order_pdf,
        name='sale-order-pdf'
    ),
    # ==================== Auto completado de Productos ==================== #
    path(
        'product-autocomplete',
        ProductAutoComplete.as_view(),
        name='product-autocomplete'
    ),
]
