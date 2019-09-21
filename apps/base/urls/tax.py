"""uRLs para tax
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.tax import (
    DeleteTax, TaxAutoComplete, TaxCreateView, TaxDetailView, TaxListView,
    TaxUpdateView)

urlpatterns = [
    path(
        '',
        login_required(TaxListView.as_view()),
        name='taxs'
    ),
    path(
        'add/',
        login_required(TaxCreateView.as_view()),
        name='tax-add'
    ),
    path(
        '<int:pk>/',
        login_required(TaxDetailView.as_view()),
        name='tax-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(TaxUpdateView.as_view()),
        name='tax-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(DeleteTax),
        name='tax-delete'
    ),

    # ====================== Rutas de Auto Completado ====================== #
    path(
        'tax-autocomplete',
        login_required(TaxAutoComplete.as_view()),
        name='tax-autocomplete'
    ),
]
