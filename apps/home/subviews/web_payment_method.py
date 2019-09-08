# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..submodels.web_payment_methods import PyWebPaymentMethod

WPM_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
]

WPM_SHORT = ['name']


class WebPaymentMethodListView(LoginRequiredMixin, ListView):
    model = PyWebPaymentMethod
    template_name = 'base/list.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(WebPaymentMethodListView, self).get_context_data(**kwargs)
        context['title'] = 'Métodos de Pagos Webs'
        context['detail_url'] = 'web-payment-method-detail'
        context['add_url'] = 'web-payment-method-add'
        context['fields'] = WPM_FIELDS
        return context


class WebPaymentMethodDetailView(LoginRequiredMixin, DetailView):
    model = PyWebPaymentMethod
    template_name = 'base/detail.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(WebPaymentMethodDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'web-payment-methods', 'name': 'Métodos de Pagos Webs'}]
        context['update_url'] = 'web-payment-method-update'
        context['delete_url'] = 'web-payment-method-delete'
        context['fields'] = WPM_FIELDS
        return context


class WebPaymentMethodCreateView(LoginRequiredMixin, CreateView):
    model = PyWebPaymentMethod
    fields = WPM_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(WebPaymentMethodCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Métodos de Pagos Web'
        context['breadcrumbs'] = [{'url': 'web-payment-methods', 'name': 'Métodos de Pagos Web'}]
        context['back_url'] = reverse('web-payment-methods')
        return context


class WebPaymentMethodUpdateView(LoginRequiredMixin, UpdateView):
    model = PyWebPaymentMethod
    fields = WPM_SHORT
    template_name = 'base/form.html'
    login_url = "/base/login"

    def get_context_data(self, **kwargs):
        context = super(WebPaymentMethodUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'web-payment-methods', 'name': 'Métodos de Pagos Web'}]
        context['back_url'] = reverse('web-payment-method-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="login")
def DeleteWebPaymentMethod(self, pk):
    web_payment_method = PyWebPaymentMethod.objects.get(id=pk)
    web_payment_method.delete()
    return redirect(reverse('web-payment-methods'))
