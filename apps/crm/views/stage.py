# Librerias Django
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Librerias en carpetas locales
from ..models.stage import PyStage

""" BEGIN STAGE """
STAGE_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

STAGE_FIELDS_SHORT = ['name']


class StageListView(LoginRequiredMixin, ListView):
    model = PyStage
    template_name = 'base/list.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(StageListView, self).get_context_data(**kwargs)
        context['title'] = 'Etapas'
        context['detail_url'] = 'stage-detail'
        context['add_url'] = 'stage-add'
        context['fields'] = STAGE_FIELDS
        return context

class StageDetailView(LoginRequiredMixin, DetailView):
    model = PyStage
    template_name = 'base/detail.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(StageDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapas'}]
        context['update_url'] = 'stage-update'
        context['delete_url'] = 'stage-delete'
        context['fields'] = STAGE_FIELDS
        return context

class StageCreateView(LoginRequiredMixin, CreateView):
    model = PyStage
    fields = STAGE_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(StageCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Etapa'
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapa'}]
        context['back_url'] = reverse('stage')
        return context

class StageUpdateView(LoginRequiredMixin, UpdateView):
    model = PyStage
    fields = STAGE_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(StageUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'stage', 'name': 'Etapa'}]
        context['back_url'] = reverse('stage-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="login")
def DeleteStage(self, pk):
    lead = PyStage.objects.get(id=pk)
    lead.delete()
    return redirect(reverse('stage'))
""" END STAGE """
