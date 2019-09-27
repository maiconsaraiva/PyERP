"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.uom import (
    UomCreateView, UomDeleteView, UomDetailView, UomListView, UomUpdateView)

urlpatterns = [
    path('', UomListView.as_view(), name='uoms'),
    path('add/', UomCreateView.as_view(), name='uom-add'),
    path('<int:pk>/', UomDetailView.as_view(), name='uom-detail'),
    path('<int:pk>/update', UomUpdateView.as_view(), name='uom-update'),
    path('<int:pk>/delete/', UomDeleteView.as_view(), name='uom-delete'),
]
