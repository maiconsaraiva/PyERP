"""uRLs para gestionar los paises
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.country import (
    CountryAutoComplete, CountryCreateView, CountryDeleteView,
    CountryDetailView, CountryListView, CountryUpdateView)

urlpatterns = [
    path(
        '',
        login_required(CountryListView.as_view()),
        name='countries'
    ),
    path(
        'add/',
        login_required(CountryCreateView.as_view()),
        name='country-add'
    ),
    path(
        '<int:pk>/',
        login_required(CountryDetailView.as_view()),
        name='country-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(CountryUpdateView.as_view()),
        name='country-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(CountryDeleteView.as_view()),
        name='country-delete'
    ),

    # ====================== Rutas de Auto Completado ====================== #
    path(
        'country-autocomplete',
        CountryAutoComplete.as_view(),
        name='country-autocomplete'
    ),
]
