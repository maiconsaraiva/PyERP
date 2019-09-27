"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.page import (
    PageCreateView, PageDeleteView, PageDetailView, PageListView,
    PageUpdateView)

app_name = 'PyPage'

urlpatterns = [
    path('', PageListView.as_view(), name='list'),
    path('add/', PageCreateView.as_view(), name='add'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('<int:pk>/update', PageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='delete'),
]
