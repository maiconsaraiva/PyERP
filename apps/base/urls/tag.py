"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.tag import (
    TagDeleteView, TagCreateView, TagDetailView, TagListView, TagUpdateView)

urlpatterns = [
    path('tags', TagListView.as_view(), name='tags'),
    path('tag/add/', TagCreateView.as_view(), name='tag-add'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('tag/<int:pk>/update', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
