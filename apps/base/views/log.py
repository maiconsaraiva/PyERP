# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

LOG_FIELDS = [
    {'string': _("Created On"), 'field': 'created_on'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
]

LOG_SHORT = ['name', 'note']


class LogListView(LoginRequiredMixin, FatherListView):
    model = PyLog
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)
        context['title'] = 'Logs'
        context['detail_url'] = 'base:log-detail'
        context['add_url'] = 'base:log-add'
        context['fields'] = LOG_FIELDS
        return context


class LogDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyLog
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LogDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:logs', 'name': 'Logs'}]
        context['update_url'] = 'base:log-update'
        context['delete_url'] = 'base:log-delete'
        context['fields'] = LOG_FIELDS
        return context


class LogCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyLog
    fields = LOG_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LogCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Log'
        context['breadcrumbs'] = [{'url': 'base:logs', 'name': 'Logs'}]
        context['back_url'] = reverse('base:logs')
        return context


class LogUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyLog
    fields = LOG_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(LogUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:logs', 'name': 'Logs'}]
        context['back_url'] = reverse('base:log-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteLog(self, pk):
    log = PyLog.objects.get(id=pk)
    log.delete()
    return redirect(reverse('base:logs'))
