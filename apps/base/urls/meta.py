"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.meta import (
    MetaDeleteView, MetaCreateView, MetaDetailView, MetaListView, MetaUpdateView)

urlpatterns = [
    path('metas', MetaListView.as_view(), name='metas'),
    path('meta/add/', MetaCreateView.as_view(), name='meta-add'),
    path('meta/<int:pk>/', MetaDetailView.as_view(), name='meta-detail'),
    path('meta/<int:pk>/update', MetaUpdateView.as_view(), name='meta-update'),
    path('meta/<int:pk>/delete/', MetaDeleteView.as_view(), name='meta-delete'),
]
