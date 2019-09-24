"""uRLs para tax
"""
# Librerias Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Librerias en carpetas locales
from ..views.sequence import (
    DeleteSequence, SequenceCreateView, SequenceDetailView, SequenceListView,
    SequenceUpdateView)

urlpatterns = [
    path('',
        login_required(SequenceListView.as_view()),
        name='sequences'),
    path(
        'add/',
        login_required(SequenceCreateView.as_view()),
        name='sequence-add'),
    path(
        '<int:pk>/',
        login_required(SequenceDetailView.as_view()),
        name='sequence-detail'),
    path(
        '<int:pk>/update',
        login_required(SequenceUpdateView.as_view()),
        name='sequence-update'),
    path(
        '<int:pk>/delete/',
        login_required(DeleteSequence),
        name='sequence-delete'),
]
