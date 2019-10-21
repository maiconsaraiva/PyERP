# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

# Localfolder Library
from ..models import PyAccountMove

ACCOUNTMOVE_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
        ]

ACCOUNTMOVE_FIELDS_SHORT = ['code','name','state']


class AccountMoveListView(LoginRequiredMixin, ListView):
    model = PyAccountMove
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveListView, self).get_context_data(**kwargs)
        context['title'] = 'Asiento Contable'
        context['detail_url'] = 'base:account-move-detail'
        context['add_url'] = 'base:account-move-add'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveDetailView(LoginRequiredMixin, DetailView):
    model = PyAccountMove
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(AccountMoveDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Asiento Contable'}]
        context['update_url'] = 'base:account-move-update'
        context['delete_url'] = 'base:account-move-delete'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveCreateView(LoginRequiredMixin, CreateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Asiento'
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Crear Asiento'}]
        context['back_url'] = reverse('base:account-move')
        return context


class AccountMoveUpdateView(LoginRequiredMixin, UpdateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:account-move', 'name': 'Asiento Contable'}]
        context['back_url'] = reverse('base:account-move-detail', kwargs={'pk': context['object'].pk})
        return context


class AccountMoveDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyAccountMove
