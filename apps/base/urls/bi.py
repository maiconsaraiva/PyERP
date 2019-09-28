"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.bi import (
    BiCreateView, BiDeleteView, BiDetailView, BiListView, BiUpdateView)

app_name = 'PyBi'

urlpatterns = [
    path('bi', BiListView.as_view(), name='list'),
    path('bi/add/', BiCreateView.as_view(), name='add'),
    path('bi/<int:pk>/', BiDetailView.as_view(), name='detail'),
    path('bi/<int:pk>/update', BiUpdateView.as_view(), name='update'),
    path('bi/<int:pk>/delete/', BiDeleteView.as_view(), name='delete'),
]
