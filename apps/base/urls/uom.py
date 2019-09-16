"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.uom import (
    DeleteUom, UomCreateView, UomDetailView, UomListView, UomUpdateView)

urlpatterns = [
    path('uoms', UomListView.as_view(), name='uoms'),
    path('uom/add/', UomCreateView.as_view(), name='uom-add'),
    path('uom/<int:pk>/', UomDetailView.as_view(), name='uom-detail'),
    path('uom/<int:pk>/update', UomUpdateView.as_view(), name='uom-update'),
    path('uom/<int:pk>/delete/', DeleteUom, name='uom-delete'),
]
