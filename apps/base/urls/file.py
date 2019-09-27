"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.file import (
    FileCreateView, FileDeleteView, FileDetailView, FileListView,
    FileUpdateView)

urlpatterns = [
    path('files', FileListView.as_view(), name='files'),
    path('file/add/', FileCreateView.as_view(), name='file-add'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('file/<int:pk>/update', FileUpdateView.as_view(), name='file-update'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),
]
