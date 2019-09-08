# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyCron

CRON_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Activo', 'field': 'active'},
    {'string': 'Ejecutar Cada', 'field': 'interval_type'},
    {'string': 'Modelo', 'field': 'model_name'},
    {'string': 'Método', 'field': 'function'},
    {'string': 'Número de Llamadas', 'field': 'number_call'},
    {'string': 'Creado en', 'field': 'created_on'},
]

CRON_SHORT = ['name', 'active', 'interval_type', 'model_name', 'function', 'number_call']


class CronListView(LoginRequiredMixin, ListView):
    model = PyCron
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CronListView, self).get_context_data(**kwargs)
        context['title'] = 'Crons'
        context['detail_url'] = 'cron-detail'
        context['add_url'] = 'base:cron-add'
        context['fields'] = CRON_FIELDS
        return context


class CronDetailView(LoginRequiredMixin, DetailView):
    model = PyCron
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CronDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'crons', 'name': 'Crons'}]
        context['update_url'] = 'cron-update'
        context['delete_url'] = 'cron-delete'
        context['fields'] = CRON_FIELDS
        return context


class CronCreateView(LoginRequiredMixin, CreateView):
    model = PyCron
    fields = CRON_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CronCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Cron'
        context['breadcrumbs'] = [{'url': 'crons', 'name': 'Crons'}]
        context['back_url'] = reverse('crons')
        return context


class CronUpdateView(LoginRequiredMixin, UpdateView):
    model = PyCron
    fields = CRON_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CronUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'crons', 'name': 'Crons'}]
        context['back_url'] = reverse('cron-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteCron(self, pk):
    cron = PyCron.objects.get(id=pk)
    cron.delete()
    return redirect(reverse('crons'))
