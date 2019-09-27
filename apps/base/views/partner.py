# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyPartner
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

PARTNER_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Street"), 'field': 'street'},
    {'string': _("Country"), 'field': 'country_id'},
    {'string': _("Phone"), 'field': 'phone'},
    {'string': _("Email"), 'field': 'email'},
    {'string': _("For Invoice"), 'field': 'for_invoice'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("No Email"), 'field': 'not_email'},
    {'string': _("Parent"), 'field': 'parent_id'},
    {'string': _("Type"), 'field': 'type'},
]

PARTNER_FIELDS_SHORT = [
    'name',
    'street',
    'country_id',
    'email',
    'phone',
    'note',
    'customer',
    'provider',
    'for_invoice',
    'not_email',
    'parent_id',
    'type',
    'active'
]


class CustomerListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    queryset = PyPartner.objects.all()
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'base:partner-detail'
        context['add_url'] = 'base:partner-add'
        context['fields'] = PARTNER_FIELDS
        return context


class ProviderListView(LoginRequiredMixin, FatherListView):
    model = PyPartner
    template_name = 'base/list.html'
    queryset = PyPartner.objects.filter(provider=True).all()
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProviderListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'base:partner-detail'
        context['add_url'] = 'base:partner-add'
        context['fields'] = PARTNER_FIELDS
        return context


class PartnerDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyPartner
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:partners', 'name': 'Partners'}]
        context['update_url'] = 'base:partner-update'
        context['delete_url'] = 'base:partner-delete'
        context['fields'] = PARTNER_FIELDS
        return context


class PartnerCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyPartner
    fields = ['name', 'email', 'phone', 'customer', 'provider']
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear partner'
        context['breadcrumbs'] = [{'url': 'base:partners', 'name': 'Partners'}]
        context['back_url'] = reverse('base:partners')
        return context


class PartnerUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyPartner
    fields = PARTNER_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PartnerUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:partners', 'name': 'Partners'}]
        context['back_url'] = reverse('base:partner-detail', kwargs={'pk': context['object'].pk})
        return context


class PartnerDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyPartner
    success_url = 'base:partners'


class PartnerAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyPartner
    """
    def get_queryset(self):
        queryset = PyPartner.objects.all()
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
