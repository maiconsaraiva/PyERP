"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.file import (
    DeleteFile, FileCreateView, FileDetailView, FilelListView, FilelUpdateView)

urlpatterns = [
    path('files', FilelListView.as_view(), name='files'),
    path('file/add/', FileCreateView.as_view(), name='file-add'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('file/<int:pk>/update', FilelUpdateView.as_view(), name='file-update'),
    path('file/<int:pk>/delete/', DeleteFile, name='file-delete'),
]