"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.faq import (
    FaqCreateView, FaqDeleteView, FaqDetailView, FaqListView, FaqUpdateView)

urlpatterns = [
    path('faqs', FaqListView.as_view(), name='faqs'),
    path('faq/add/', FaqCreateView.as_view(), name='faq-add'),
    path('faq/<int:pk>/', FaqDetailView.as_view(), name='faq-detail'),
    path('faq/<int:pk>/update', FaqUpdateView.as_view(), name='faq-update'),
    path('faq/<int:pk>/delete/', FaqDeleteView.as_view(), name='faq-delete'),
]
