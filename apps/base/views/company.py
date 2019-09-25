# Librerias Django
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyCompany, PyUser
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

COMPANY_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Street"), 'field': 'street'},
    {'string': _("Phone"), 'field': 'phone'},
    {'string': _("Email"), 'field': 'email'},
    {'string': _("Country"), 'field': 'country'},
    {'string': _("Currency"), 'field': 'currency_id'},
    {'string': _("Slogan"), 'field': 'slogan'},
    {'string': _("Postal Code"), 'field': 'postal_code'},
]

COMPANY_FIELDS_SHORT = [
    'name',
    'street',
    'city',
    'phone',
    'email',
    'postal_code',

    'social_facebook',
    'social_instagram',
    'social_linkedin',
    'social_youtube',
    'social_whatsapp',

    'latitude',
    'longitude',

    'country',
    'currency_id',
    'slogan',
    'logo',

    'main_color',
    'font_color',

    'description'
]


# ========================================================================== #
class CompanyListView(FatherListView):
    model = PyCompany
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        context['title'] = 'Compañías'
        context['detail_url'] = 'base:company-detail'
        context['add_url'] = 'base:company-add'
        context['fields'] = COMPANY_FIELDS
        return context


# ========================================================================== #
class CompanyDetailView(FatherDetailView):
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


# ========================================================================== #
class CompanyCreateView(FatherCreateView):
    model = PyCompany
    fields = COMPANY_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Compañía'
        context['breadcrumbs'] = [{'url': 'base:companies', 'name': 'Compañías'}]
        context['back_url'] = reverse('base:companies')
        return context


# ========================================================================== #
class CompanyUpdateView(FatherUpdateView):
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


# ========================================================================== #
def change_active_company(request, company):
    user = PyUser.objects.get(pk=request.user.pk)
    user.active_company = PyCompany.objects.get(pk=company)
    user.save()
    print('Usuario: {}, Compañía: {}'.format(user, company))

    return redirect(request.META.get('HTTP_REFERER'))


# ========================================================================== #
def DeleteCompany(self, pk):
    company = PyCompany.objects.get(id=pk)
    company.delete()

    return redirect(reverse('base:companies'))
