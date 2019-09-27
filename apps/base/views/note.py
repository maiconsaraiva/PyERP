# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog, PyNote
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

NOTE_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("Color"), 'field': 'color'},
]

NOTE_SHORT = ['name', 'note', 'color']


class NoteListView(LoginRequiredMixin, FatherListView):
    model = PyNote
    template_name = 'base/note_list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['title'] = 'Notes'
        context['detail_url'] = 'base:note-detail'
        context['add_url'] = 'base:note-add'
        context['fields'] = NOTE_FIELDS
        return context


class NoteDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyNote
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:notes', 'name': 'Notes'}]
        context['update_url'] = 'base:note-update'
        context['delete_url'] = 'base:note-delete'
        context['fields'] = NOTE_FIELDS
        return context


class NoteCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyNote
    fields = NOTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Note'
        context['breadcrumbs'] = [{'url': 'base:notes', 'name': 'Notes'}]
        context['back_url'] = reverse('base:notes')
        return context


class NoteUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyNote
    fields = NOTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:notes', 'name': 'Notes'}]
        context['back_url'] = reverse('base:note-detail', kwargs={'pk': context['object'].pk})
        return context



class NoteDeleteView(FatherDeleteView):
    model = PyNote
    success_url = 'base:notes'
