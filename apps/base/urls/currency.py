"""uRLs para gestionar las monedas
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.currency import (
    CurrencyAutoComplete, CurrencyCreateView, CurrencyDetailView,
    CurrencyListView, CurrencyUpdateView, DeleteCurrency)

urlpatterns = [
    path(
        '',
        login_required(CurrencyListView.as_view()),
        name='currencies'
    ),
    path(
        'add/',
        login_required(CurrencyCreateView.as_view()),
        name='currency-add'
    ),
    path(
        '<int:pk>/',
        login_required(CurrencyDetailView.as_view()),
        name='currency-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(CurrencyUpdateView.as_view()),
        name='currency-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(DeleteCurrency),
        name='currency-delete'
    ),

    # ====================== Rutas de Auto Completado ====================== #
    path(
        'currency-autocomplete',
        CurrencyAutoComplete.as_view(),
        name='currency-autocomplete'
    ),
]
