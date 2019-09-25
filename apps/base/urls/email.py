"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.email import (
    DeleteEmail, EmailCreateView, EmailDetailView, EmailListView, EmailUpdateView)

urlpatterns = [
    path('emails', EmailListView.as_view(), name='emails'),
    path('email/add/', EmailCreateView.as_view(), name='email-add'),
    path('email/<int:pk>/', EmailDetailView.as_view(), name='email-detail'),
    path('email/<int:pk>/update', EmailUpdateView.as_view(), name='email-update'),
    path('email/<int:pk>/delete/', DeleteEmail, name='email-delete'),
]
