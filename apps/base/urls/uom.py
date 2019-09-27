"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.uom import (
    UomCreateView, UomDeleteView, UomDetailView, UomListView, UomUpdateView)

app_name = 'PyUom'

urlpatterns = [
    path('', UomListView.as_view(), name='list'),
    path('add/', UomCreateView.as_view(), name='add'),
    path('<int:pk>/', UomDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UomUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UomDeleteView.as_view(), name='delete'),
]
