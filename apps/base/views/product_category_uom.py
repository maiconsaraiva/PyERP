# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

# Librerias en carpetas locales
from ..models import PyLog, PyProductCategoryUOM
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

CATEGORY_UOM_FIELDS = [
    {'string': 'Name', 'field': 'name'},
]

CATEGORY_UOM_FIELDS_SHORT = ['name']


class ProductCategoryUOMListView(LoginRequiredMixin, FatherListView):
    model = PyProductCategoryUOM
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUOMListView, self).get_context_data(**kwargs)
        context['title'] = 'UOM Category'
        context['detail_url'] = 'base:product-category-uom-detail'
        context['add_url'] = 'base:product-category-uom-add'
        context['fields'] = CATEGORY_UOM_FIELDS
        return context


class ProductCategoryUOMDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductCategoryUOM
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUOMDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-category-uom', 'name': 'Category UOM'}]
        context['update_url'] = 'base:product-category-uom-update'
        context['delete_url'] = 'base:product-category-uom-delete'
        context['fields'] = CATEGORY_UOM_FIELDS
        return context


class ProductCategoryUOMCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductCategoryUOM
    fields = CATEGORY_UOM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUOMCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Category'
        context['breadcrumbs'] = [{'url': 'base:product-category-uom', 'name': 'Category UOM'}]
        context['back_url'] = reverse('base:product-category-uom')
        return context


class ProductCategoryUOMUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductCategoryUOM
    fields = CATEGORY_UOM_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUOMUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-category-uom', 'name': 'Category UOM'}]
        context['back_url'] = reverse('base:product-category-uom-detail', kwargs={'pk': context['object'].pk})
        return context



class ProductCategoryUOMDeleteView(FatherDeleteView):
    model = PyProductCategoryUOM
    success_url = 'base:product-category-uom'
