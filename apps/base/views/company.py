# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import translation

# Librerias en carpetas locales
from ...base.models import PyCompany

COMPANY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Teléfono', 'field': 'phone'},
    {'string': 'Email', 'field': 'email'},
    {'string': 'Giro', 'field': 'giro'},
    {'string': 'Moneda', 'field': 'currency_id'},
]

COMPANY_FIELDS_SHORT = ['name', 'city', 'phone', 'email', 'social_facebook', 'social_instagram', 'social_linkedin', 'currency_id']


class CompanyListView(ListView):
    model = PyCompany
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['title'] = 'Compañías'
        context['detail_url'] = 'base:company-detail'
        context['add_url'] = 'base:company-add'
        context['fields'] = COMPANY_FIELDS
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = PyCompany
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:companies', 'name': 'Compañia'}]
        context['update_url'] = 'base:company-update'
        context['delete_url'] = 'base:company-delete'
        context['fields'] = COMPANY_FIELDS
        return context


class CompanyCreateView(CreateView):
    model = PyCompany
    fields = COMPANY_FIELDS_SHORT
    template_name = 'base/form.html'
    # login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Compañía'
        context['breadcrumbs'] = [{'url': 'base:companies', 'name': 'Compañías'}]
        context['back_url'] = reverse('base:companies')
        return context


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = PyCompany
    fields = COMPANY_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:companies', 'name': 'Compañías'}]
        context['back_url'] = reverse('base:company-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteCompany(self, pk):
    company = PyCompany.objects.get(id=pk)
    company.delete()
    return redirect(reverse('companies'))
