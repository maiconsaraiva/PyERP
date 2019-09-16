"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.image import (
    DeleteImage, ImageCreateView, ImageDetailView, ImageListView,
    ImageUpdateView)

urlpatterns = [
    path('images', ImageListView.as_view(), name='images'),
    path('image/add/', ImageCreateView.as_view(), name='image-add'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('image/<int:pk>/update', ImageUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete/', DeleteImage, name='image-delete'),
]
