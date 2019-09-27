# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyCurrency
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

CURRENCY_FIELDS = [
    {'string': _('Country'), 'field': 'country'},
    {'string': _('Courrency'), 'field': 'name'},
    {'string': _('Alias'), 'field': 'alias'},
    {'string': _('Simbol'), 'field': 'symbol'},
    {'string': _('Position'), 'field': 'position'},
]

CURRENCY_SHORT = ['country', 'name', 'alias', 'symbol', 'position']


class CurrencyListView(LoginRequiredMixin, FatherListView):
    model = PyCurrency
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyListView, self).get_context_data(**kwargs)
        context['title'] = 'Monedas'
        context['detail_url'] = 'base:currency-detail'
        context['add_url'] = 'base:currency-add'
        context['fields'] = CURRENCY_FIELDS
        return context


class CurrencyDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyCurrency
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['update_url'] = 'base:currency-update'
        context['delete_url'] = 'base:currency-delete'
        context['fields'] = CURRENCY_FIELDS
        return context


class CurrencyCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyCurrency
    fields = CURRENCY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Moneda'
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['back_url'] = reverse('base:currencies')
        return context


class CurrencyUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyCurrency
    fields = CURRENCY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CurrencyUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:currencies', 'name': 'Monedas'}]
        context['back_url'] = reverse('base:currency-detail', kwargs={'pk': context['object'].pk})
        return context



class CurrencyDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyCurrency
    success_url = 'base:currencies'


class CurrencyAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyCurrency
    """
    def get_queryset(self):

        queryset = PyCurrency.objects.all()

        if self.q:
            queryset = queryset.filter(Q(name__icontains=self.q) | Q(country__name__icontains=self.q))

        return queryset
