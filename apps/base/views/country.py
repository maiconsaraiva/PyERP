# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyCountry

COUNTRY_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

COUNTRY_SHORT = ['name']


class CountryListView(LoginRequiredMixin, ListView):
    model = PyCountry
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CountryListView, self).get_context_data(**kwargs)
        context['title'] = _("Countries")
        context['detail_url'] = 'base:country-detail'
        context['add_url'] = 'base:country-add'
        context['fields'] = COUNTRY_FIELDS
        return context


class CountryDetailView(LoginRequiredMixin, DetailView):
    model = PyCountry
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CountryDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:countries', 'name': _("Countries")}]
        context['update_url'] = 'base:country-update'
        context['delete_url'] = 'base:country-delete'
        context['fields'] = COUNTRY_FIELDS
        return context


class CountryCreateView(LoginRequiredMixin, CreateView):
    model = PyCountry
    fields = COUNTRY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CountryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Country Create'
        context['breadcrumbs'] = [{'url': 'base:countries', 'name': _("Countries")}]
        context['back_url'] = reverse('base:countries')
        return context


class CountryUpdateView(LoginRequiredMixin, UpdateView):
    model = PyCountry
    fields = COUNTRY_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CountryUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:countries', 'name': _("Countries")}]
        context['back_url'] = reverse('base:country-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteCountry(self, pk):
    country = PyCountry.objects.get(id=pk)
    country.delete()
    return redirect(reverse('base:countries'))
