# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyTax

TAX_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Amount"), 'field': 'amount'},
    {'string': _("Include Price"), 'field': 'include_price'},
]

TAX_SHORT = ['name', 'amount', 'include_price']


class TaxListView(LoginRequiredMixin, ListView):
    model = PyTax
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaxListView, self).get_context_data(**kwargs)
        context['title'] = 'Taxs'
        context['detail_url'] = 'base:tax-detail'
        context['add_url'] = 'base:tax-add'
        context['fields'] = TAX_FIELDS
        return context


class TaxDetailView(LoginRequiredMixin, DetailView):
    model = PyTax
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaxDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'Taxs'}]
        context['update_url'] = 'base:tax-update'
        context['delete_url'] = 'base:tax-delete'
        context['fields'] = TAX_FIELDS
        return context


class TaxCreateView(LoginRequiredMixin, CreateView):
    model = PyTax
    fields = TAX_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaxCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Tax'
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'Taxs'}]
        context['back_url'] = reverse('base:taxs')
        return context


class TaxUpdateView(LoginRequiredMixin, UpdateView):
    model = PyTax
    fields = TAX_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(TaxUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:taxs', 'name': 'taxs'}]
        context['back_url'] = reverse('base:tax-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteTax(self, pk):
    tax = PyFaq.objects.get(id=pk)
    tax.delete()
    return redirect(reverse('base:taxs'))
