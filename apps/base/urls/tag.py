"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.tag import (
    TagCreateView, TagDeleteView, TagDetailView, TagListView, TagUpdateView)

app_name = 'PyTag'

urlpatterns = [
    path('', TagListView.as_view(), name='list'),
    path('add/', TagCreateView.as_view(), name='add'),
    path('<int:pk>/', TagDetailView.as_view(), name='detail'),
    path('<int:pk>/update', TagUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TagDeleteView.as_view(), name='delete'),
]
