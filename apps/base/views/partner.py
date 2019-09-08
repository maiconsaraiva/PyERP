# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyLog, PyPartner

PARTNER_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Dirección', 'field': 'street'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
    {'string': 'Para Facturar', 'field': 'for_invoice'},
    {'string': 'Creado por', 'field': 'created_by'},
    {'string': 'Creado', 'field': 'created_on'},
    {'string': 'Notas', 'field': 'note'},
    {'string': 'No Email', 'field': 'not_email'},
]

PARTNER_FIELDS_SHORT = ['name', 'street', 'email', 'phone', 'note', 'customer', 'provider', 'for_invoice', 'not_email']


class CustomerListView(LoginRequiredMixin, ListView):
    model = PyPartner
    template_name = 'base/list.html'
    queryset = PyPartner.objects.filter(customer=True).all()
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['title'] = 'Partners'
        context['detail_url'] = 'base:partner-detail'
        context['add_url'] = 'base:partner-add'
        context['fields'] = PARTNER_FIELDS
        return context


class ProviderListView(LoginRequiredMixin, ListView):
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


class PartnerDetailView(LoginRequiredMixin, DetailView):
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


class PartnerCreateView(LoginRequiredMixin, CreateView):
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

    """
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(PartnerCreateView, self).get_form(form_class)
        form.fields['rut'].widget.attrs = {'placeholder': '00.000.000-0'}
        return form"""


class PartnerUpdateView(UpdateView):
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
    """
    def form_valid(self, form):
        rut = form.data.get('rut')
        if validarRut(rut):
            self.object.rut = check_rut(rut, 1)
        else:
            form.add_error('rut', 'Formato de RUT inválido')
            return self.form_invalid(form)
        return super(PartnerUpdateView, self).form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(PartnerUpdateView, self).get_form(form_class)
        form.fields['rut'].widget.attrs = {'placeholder': '00.000.000-0'}
        return form"""


@login_required(login_url="base:login")
def DeletePartner(self, pk):
    partner = PyPartner.objects.get(id=pk)
    partner.delete()
    PyLog(name='Partner', note='PartnerDelete:').save()
    return redirect(reverse('partners'))


class PartnerAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Taxonomia (sub especie)
    """

    def get_queryset(self):

        queryset = PyPartner.objects.all()

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)

        return queryset
