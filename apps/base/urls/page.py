"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.page import (
    PageDeleteView, PageCreateView, PageDetailView, PageListView, PageUpdateView)

urlpatterns = [
    path('page-backend', PageListView.as_view(), name='page-backend'),
    path('page/add/', PageCreateView.as_view(), name='page-add'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('page/<int:pk>/update', PageUpdateView.as_view(), name='page-update'),
    path('page/<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
]
