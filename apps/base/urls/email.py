"""The store routes
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.email import (
    EmailCreateView, EmailDeleteView, EmailDetailView, EmailListView,
    EmailUpdateView)

urlpatterns = [
    path('emails', login_required(EmailListView.as_view()), name='emails'),
    path('email/add/', login_required(EmailCreateView.as_view()), name='email-add'),
    path('email/<int:pk>/', login_required(EmailDetailView.as_view()), name='email-detail'),
    path('email/<int:pk>/update', login_required(EmailUpdateView.as_view()), name='email-update'),
    path('email/<int:pk>/delete/', login_required(EmailDeleteView.as_view()), name='email-delete'),
]
