"""The store routes
"""
# Django Library
# Librerias Django
from django.urls import path

# Localfolder Library
# Librerias en carpetas locales
from ..views.image import (
    ImageCreateView, ImageDeleteView, ImageDetailView, ImageListView,
    ImageUpdateView)

app_name = 'PyImage'

urlpatterns = [
    path('', ImageListView.as_view(), name='list'),
    path('add/', ImageCreateView.as_view(), name='add'),
    path('<int:pk>/', ImageDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ImageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ImageDeleteView.as_view(), name='delete'),
]
