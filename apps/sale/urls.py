"""Rutas del módulo de ordenes de venta
"""
# Librerias Django
from django.urls import path

# Librerias de terceros
from .reports.saleorderpdf import sale_order_pdf
from .views import (
    SaleOrderAddView, SaleOrderDeleteView, SaleOrderDetailAddView,
    SaleOrderDetailDeleteView, SaleOrderDetailEditView, SaleOrderEditView,
    SaleOrderListView, ProductAutoComplete)

app_name = 'sale'

urlpatterns = [
    # ========================== Sale Orders URL's ========================= #
    path('sale-order', SaleOrderListView.as_view(), name='sale-order'),
    path('sale-order/add/', SaleOrderAddView.as_view(), name='sale-order-add'),
    path(
        'sale-order/edit/<int:pk>',
        SaleOrderEditView.as_view(),
        name='sale-order-edit'
    ),
    path(
        'sale-order/delete/<int:pk>',
        SaleOrderDeleteView.as_view(),
        name='sale-order-delete'
    ),
    # ====================== Sale Orders Detail URL's ====================== #
    path(
        'sale-order-detail/add/<int:saleorder_pk>',
        SaleOrderDetailAddView.as_view(),
        name='sale-order-detail-add'
    ),
    path(
        'sale-order-detail/edit/<int:pk>',
        SaleOrderDetailEditView.as_view(),
        name='sale-order-detail-edit'
    ),
    path(
        'sale-order-detail/delete/<int:pk>',
        SaleOrderDetailDeleteView.as_view(),
        name='sale-order-detail-delete'
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
