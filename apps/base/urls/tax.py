"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.tax import (
    DeleteTax, TaxCreateView, TaxDetailView, TaxListView, TaxUpdateView)

urlpatterns = [
    path('taxs', TaxListView.as_view(), name='taxs'),
    path('tax/add/', TaxCreateView.as_view(), name='tax-add'),
    path('tax/<int:pk>/', TaxDetailView.as_view(), name='tax-detail'),
    path('tax/<int:pk>/update', TaxUpdateView.as_view(), name='tax-update'),
    path('tax/<int:pk>/delete/', DeleteTax, name='tax-delete'),
]
