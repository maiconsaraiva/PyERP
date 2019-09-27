"""uRLs para partner
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.partner import (
    PartnerAutoComplete, PartnerCreateView, PartnerDeleteView,
    PartnerDetailView, PartnerUpdateView)

urlpatterns = [
    path(
        'add/',
        login_required(PartnerCreateView.as_view()),
        name='partner-add'
    ),
    path(
        '<int:pk>/',
        login_required(PartnerDetailView.as_view()),
        name='partner-detail'
    ),
    path(
        '<int:pk>/update',
        login_required(PartnerUpdateView.as_view()),
        name='partner-update'
    ),
    path(
        '<int:pk>/delete/',
        login_required(PartnerDeleteView.as_view()),
        name='partner-delete'
    ),

    # ====================== Rutas de Auto Completado ====================== #
    path(
        'partner-autocomplete',
        login_required(PartnerAutoComplete.as_view()),
        name='partner-autocomplete'
    ),
]
