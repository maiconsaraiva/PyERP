# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyLog, PyTax
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

TAX_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Amount"), 'field': 'amount'},
    {'string': _("Include Price"), 'field': 'include_price'},
]

TAX_SHORT = ['name', 'amount', 'include_price']


class TaxListView(LoginRequiredMixin, FatherListView):
    model = PyTax
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(TaxListView, self).get_context_data(**kwargs)
        context['title'] = 'Taxs'
        context['detail_url'] = 'base:tax-detail'
        context['add_url'] = 'base:tax-add'
        context['fields'] = TAX_FIELDS
        return context


class TaxDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyTax
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TaxDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'Taxs'}]
        context['update_url'] = 'base:tax-update'
        context['delete_url'] = 'base:tax-delete'
        context['fields'] = TAX_FIELDS
        return context


class TaxCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyTax
    fields = TAX_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(TaxCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Tax'
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'Taxs'}]
        context['back_url'] = reverse('base:taxs')
        return context


class TaxUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyTax
    fields = TAX_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(TaxUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'taxs'}]
        context['back_url'] = reverse('base:tax-detail', kwargs={'pk': context['object'].pk})
        return context


class TaxDeleteView(FatherDeleteView):
    model = PyTax
    success_url = 'base:taxs'


# ========================================================================== #
class TaxAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyPartner
    """

    def get_queryset(self):

        queryset = PyTax.objects.all()

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)

        return queryset
