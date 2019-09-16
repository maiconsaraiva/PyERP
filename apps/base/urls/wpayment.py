"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.wpayment import (
    DeleteWPayment, WPaymentCreateView, WPaymentDetailView, WPaymentListView,
    WPaymentUpdateView)

urlpatterns = [
    path('wpayments', WPaymentListView.as_view(), name='wpayments'),
    path('wpayment/add/', WPaymentCreateView.as_view(), name='wpayment-add'),
    path('wpayment/<int:pk>/', WPaymentDetailView.as_view(), name='wpayment-detail'),
    path('wpayment/<int:pk>/update', WPaymentUpdateView.as_view(), name='wpayment-update'),
    path('wpayment/<int:pk>/delete/', DeleteWPayment, name='wpayment-delete'),
]
