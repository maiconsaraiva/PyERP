# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.variant import (
    VariantCreateView, VariantDeleteView, VariantDetailView, VariantListView,
    VariantUpdateView)

urlpatterns = [
    path('variants', VariantListView.as_view(), name='variants'),
    path('variant/add/', VariantCreateView.as_view(), name='variant-add'),
    path('variant/<int:pk>/', VariantDetailView.as_view(), name='variant-detail'),
    path('variant/<int:pk>/update', VariantUpdateView.as_view(), name='variant-update'),
    path('variant/<int:pk>/delete/', VariantDeleteView.as_view(), name='variant-delete'),
]
