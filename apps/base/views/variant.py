# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog, PyVariant
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

VARIANT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

VARIANT_SHORT = ['name']


class VariantListView(LoginRequiredMixin, FatherListView):
    model = PyVariant
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantListView, self).get_context_data(**kwargs)
        context['title'] = 'Variants'
        context['detail_url'] = 'base:variant-detail'
        context['add_url'] = 'base:variant-add'
        context['fields'] = VARIANT_FIELDS
        return context


class VariantDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyVariant
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['update_url'] = 'base:variant-update'
        context['delete_url'] = 'base:variant-delete'
        context['fields'] = VARIANT_FIELDS
        return context


class VariantCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyVariant
    fields = VARIANT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Variant'
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['back_url'] = reverse('base:variants')
        return context


class VariantUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyVariant
    fields = VARIANT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(VariantUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:variants', 'name': 'Variants'}]
        context['back_url'] = reverse('base:variant-detail', kwargs={'pk': context['object'].pk})
        return context



class VariantDeleteView(FatherDeleteView):
    model = PyVariant
    success_url = 'base:variants'
