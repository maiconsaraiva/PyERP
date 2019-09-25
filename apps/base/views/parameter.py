# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyParameter
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

PARAMETER_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Value"), 'field': 'value'},
]

PARAMETER_SHORT = ['name', 'value']


class ParameterListView(LoginRequiredMixin, FatherListView):
    model = PyParameter
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ParameterListView, self).get_context_data(**kwargs)
        context['title'] = 'Parameters'
        context['detail_url'] = 'base:parameter-detail'
        context['add_url'] = 'base:parameter-add'
        context['fields'] = PARAMETER_FIELDS
        return context


class ParameterDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyParameter
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ParameterDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:parameters', 'name': 'Parameters'}]
        context['update_url'] = 'base:parameter-update'
        context['delete_url'] = 'base:parameter-delete'
        context['fields'] = PARAMETER_FIELDS
        return context


class ParameterCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyParameter
    fields = PARAMETER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ParameterCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Parameters'
        context['breadcrumbs'] = [{'url': 'base:parameters', 'name': 'Parameters'}]
        context['back_url'] = reverse('base:parameters')
        return context


class ParameterUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyParameter
    fields = PARAMETER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ParameterUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:parameters', 'name': 'Parameters'}]
        context['back_url'] = reverse('base:parameter-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteParameter(self, pk):
    parameter = PyParameter.objects.get(id=pk)
    parameter.delete()
    return redirect(reverse('base:parameters'))
