"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.attribute import (
    DeleteAttribute , AttributeCreateView, AttributeDetailView, AttributeListView, AttributeUpdateView)


urlpatterns = [
    path('attributes', AttributeListView.as_view(), name='attributes'),
    path('attribute/add/', AttributeCreateView.as_view(), name='attribute-add'),
    path('attribute/<int:pk>/', AttributeDetailView.as_view(), name='attribute-detail'),
    path('attribute/<int:pk>/update', AttributeUpdateView.as_view(), name='attribute-update'),
    path('attribute/<int:pk>/delete/', DeleteAttribute, name='attribute-delete'),
]