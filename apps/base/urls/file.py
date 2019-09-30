"""The store routes
"""
# Django Library
# Librerias Django
from django.urls import path

# Localfolder Library
# Librerias en carpetas locales
from ..views.file import (
    FileCreateView, FileDeleteView, FileDetailView, FileListView,
    FileUpdateView)

app_name = 'PyFile'

urlpatterns = [
    path('', FileListView.as_view(), name='list'),
    path('add/', FileCreateView.as_view(), name='add'),
    path('<int:pk>/', FileDetailView.as_view(), name='detail'),
    path('<int:pk>/update', FileUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', FileDeleteView.as_view(), name='delete'),
]
