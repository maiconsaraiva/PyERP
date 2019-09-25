"""uRLs para company
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.company import (
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyUpdateView,
    CompanyDeleteView, change_active_company)

urlpatterns = [
    path(
        '',
        login_required(CompanyListView.as_view()),
        name='companies'
    ),
    path(
        'add/',
        login_required(CompanyCreateView.as_view()),
        name='company-add'
    ),
    path(
        '<int:pk>/',
        login_required(CompanyDetailView.as_view()),
        name='company-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(CompanyUpdateView.as_view()),
        name='company-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(CompanyDeleteView.as_view()),
        name='company-delete'
    ),
    path(
        '<int:company>/change-company/',
        login_required(change_active_company),
        name='change-company'
    ),
]
