# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyProductBrand
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

BRAND_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

BRAND_FIELDS_SHORT = ['name']


class ProductBrandListView(LoginRequiredMixin, FatherListView):
    model = PyProductBrand
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductBrandListView, self).get_context_data(**kwargs)
        context['title'] = 'Product Brand'
        context['detail_url'] = 'base:product-brand-detail'
        context['add_url'] = 'base:product-brand-add'
        context['fields'] = BRAND_FIELDS
        return context


class ProductBrandDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductBrand
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductBrandDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-brand', 'name': 'Product Brand'}]
        context['update_url'] = 'base:product-brand-update'
        context['delete_url'] = 'base:product-brand-delete'
        context['fields'] = BRAND_FIELDS
        return context


class ProductBrandCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductBrand
    fields = BRAND_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductBrandCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Brand'
        context['breadcrumbs'] = [{'url': 'base:product-brand', 'name': 'Product Brand'}]
        context['back_url'] = reverse('base:product-brand')
        return context


class ProductBrandUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductBrand
    fields = BRAND_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductBrandUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-brand', 'name': 'Product Brand'}]
        context['back_url'] = reverse('base:product-brand-detail', kwargs={'pk': context['object'].pk})
        return context



class ProductBrandDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyProductBrand
    success_url = 'base:product-brand'
