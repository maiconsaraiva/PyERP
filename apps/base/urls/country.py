"""uRLs para gestionar los paises
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.country import (
    CountryAutoComplete, CountryCreateView, CountryDeleteView,
    CountryDetailView, CountryListView, CountryUpdateView)

app_name = 'PyCountry'

urlpatterns = [
    path('', CountryListView.as_view(), name='list'),
    path('add/', CountryCreateView.as_view(), name='add'),
    path('<int:pk>/', CountryDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CountryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CountryDeleteView.as_view(), name='delete'),

    # ====================== Rutas de Auto Completado ====================== #
    path('autocomplete', CountryAutoComplete.as_view(), name='autocomplete'),
]
