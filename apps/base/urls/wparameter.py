"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.wparameter import (
    WParameterCreateView, WParameterDeleteView, WParameterDetailView,
    WParameterListView, WParameterUpdateView)

urlpatterns = [
    path('wparameters', WParameterListView.as_view(), name='wparameters'),
    path('wparameter/add/', WParameterCreateView.as_view(), name='wparameter-add'),
    path('wparameter/<int:pk>/', WParameterDetailView.as_view(), name='wparameter-detail'),
    path('wparameter/<int:pk>/update', WParameterUpdateView.as_view(), name='wparameter-update'),
    path('wparameter/<int:pk>/delete/', WParameterDeleteView.as_view(), name='wparameter-delete'),
]
