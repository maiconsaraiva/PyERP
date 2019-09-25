# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyFile
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

FILE_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("User"), 'field': 'user_id'},
]

FILE_SHORT = ['name', 'note', 'user_id']


class FileListView(LoginRequiredMixin, FatherListView):
    model = PyFile
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['title'] = 'Files'
        context['detail_url'] = 'base:file-detail'
        context['add_url'] = 'base:file-add'
        context['fields'] = FILE_FIELDS
        return context


class FileDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyFile
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FileDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:files', 'name': 'Files'}]
        context['update_url'] = 'base:file-update'
        context['delete_url'] = 'base:file-delete'
        context['fields'] = FILE_FIELDS
        return context


class FileCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyFile
    fields = FILE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FileCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create File'
        context['breadcrumbs'] = [{'url': 'base:files', 'name': 'Files'}]
        context['back_url'] = reverse('base:files')
        return context


class FileUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyFile
    fields = FILE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(FileUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:files', 'name': 'Files'}]
        context['back_url'] = reverse('base:file-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteFile(self, pk):
    file = PyFile.objects.get(id=pk)
    file.delete()
    return redirect(reverse('base:files'))
