# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .web_father import FatherDetailView, FatherListView, FatherUpdateView, FatherCreateView

# Librerias en carpetas locales
from ..models import PyWParameter

WPARAMETER_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Value"), 'field': 'value'},
]

WPARAMETER_SHORT = ['name', 'value']


class WParameterListView(LoginRequiredMixin, FatherListView):
    model = PyWParameter
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WParameterListView, self).get_context_data(**kwargs)
        context['title'] = 'Web Parameters'
        context['detail_url'] = 'base:wparameter-detail'
        context['add_url'] = 'base:wparameter-add'
        context['fields'] = WPARAMETER_FIELDS
        return context


class WParameterDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyWParameter
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WParameterDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:wparameters', 'name': 'Web Parameters'}]
        context['update_url'] = 'base:wparameter-update'
        context['delete_url'] = 'base:wparameter-delete'
        context['fields'] = WPARAMETER_FIELDS
        return context


class WParameterCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyWParameter
    fields = WPARAMETER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WParameterCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Web Parameters'
        context['breadcrumbs'] = [{'url': 'base:wparameters', 'name': 'Web Parameters'}]
        context['back_url'] = reverse('base:wparameters')
        return context


class WParameterUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyWParameter
    fields = WPARAMETER_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WParameterUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:wparameters', 'name': 'Web Parameters'}]
        context['back_url'] = reverse('base:wparameter-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteWParameter(self, pk):
    wparameter = PyParameter.objects.get(id=pk)
    wparameter.delete()
    return redirect(reverse('base:wparameters'))
