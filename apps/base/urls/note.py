"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.note import (
    NoteCreateView, NoteDeleteView, NoteDetailView, NoteListView,
    NoteUpdateView)

urlpatterns = [
    path('notes', NoteListView.as_view(), name='notes'),
    path('note/add/', NoteCreateView.as_view(), name='note-add'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
