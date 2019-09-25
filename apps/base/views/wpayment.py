# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog, PyWPayment
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

WPAYMENT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Web Active"), 'field': 'web_active'},
]

WPAYMENT_SHORT = ['name','web_active']


class WPaymentListView(LoginRequiredMixin, FatherListView):
    model = PyWPayment
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WPaymentListView, self).get_context_data(**kwargs)
        context['title'] = 'Payments'
        context['detail_url'] = 'base:wpayment-detail'
        context['add_url'] = 'base:wpayment-add'
        context['fields'] = WPAYMENT_FIELDS
        return context


class WPaymentDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyWPayment
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WPaymentDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:wpayments', 'name': 'Payments'}]
        context['update_url'] = 'base:wpayment-update'
        context['delete_url'] = 'base:wpayment-delete'
        context['fields'] = WPAYMENT_FIELDS
        return context


class WPaymentCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyWPayment
    fields = WPAYMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WPaymentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Payment'
        context['breadcrumbs'] = [{'url': 'base:wpayments', 'name': 'Payments'}]
        context['back_url'] = reverse('base:wpayments')
        return context


class WPaymentUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyWPayment
    fields = WPAYMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(WPaymentUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:wpayments', 'name': 'Payments'}]
        context['back_url'] = reverse('base:wpayment-detail', kwargs={'pk': context['object'].pk})
        return context



class WPaymentDeleteView(FatherDeleteView):
    model = PyWPayment
    success_url = 'base:wpayments'
