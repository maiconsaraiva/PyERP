"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.parameter import (
    ParameterDeleteView, ParameterCreateView, ParameterDetailView,
    ParameterListView, ParameterUpdateView)

urlpatterns = [
    path('parameters', ParameterListView.as_view(), name='parameters'),
    path('parameter/add/', ParameterCreateView.as_view(), name='parameter-add'),
    path('parameter/<int:pk>/', ParameterDetailView.as_view(), name='parameter-detail'),
    path('parameter/<int:pk>/update', ParameterUpdateView.as_view(), name='parameter-update'),
    path('parameter/<int:pk>/delete/', ParameterDeleteView.as_view(), name='parameter-delete'),
]
