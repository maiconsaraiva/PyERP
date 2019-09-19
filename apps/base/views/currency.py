# Librerias Django
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyCurrency

CURRENCY_FIELDS = [
    {'string': _('Country'), 'field': 'country'},
    {'string': _('Courrency'), 'field': 'name'},
    {'string': _('Alias'), 'field': 'alias'},
    {'string': _('Simbol'), 'field': 'symbol'},
    {'string': _('Position'), 'field': 'position'},
]

CURRENCY_SHORT = ['country', 'name', 'alias', 'symbol', 'position']


class CurrencyListView(ListView):
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


class CurrencyDetailView(DetailView):
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


class CurrencyCreateView(CreateView):
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


class CurrencyUpdateView(UpdateView):
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



def DeleteCurrency(self, pk):
    currency = PyCurrency.objects.get(id=pk)
    currency.delete()
    return redirect(reverse('base:currencies'))


class CurrencyAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyCurrency
    """

    def get_queryset(self):

        queryset = PyCurrency.objects.all()

        if self.q:
            queryset = queryset.filter(Q(name__icontains=self.q) | Q(country__name__icontains=self.q))

        return queryset
