# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

# Librerias en carpetas locales
from ..models import PyLog
from ..models import PyProductCategory
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

CATEGORY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

CATEGORY_FIELDS_SHORT = ['name', 'parent_id']


class ProductCategoryListView(LoginRequiredMixin, FatherListView):
    model = PyProductCategory
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categorías de Productos'
        context['detail_url'] = 'base:product-category-detail'
        context['add_url'] = 'base:product-category-add'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductCategoryDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductCategory
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-category', 'name': 'Categorias de Productos'}]
        context['update_url'] = 'base:product-category-update'
        context['delete_url'] = 'base:product-category-delete'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductCategoryCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Categoria de Productos'
        context['breadcrumbs'] = [{'url': 'base:product-category', 'name': 'Categoria de Producto'}]
        context['back_url'] = reverse('base:product-category')
        return context


class ProductCategoryUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:product-category', 'name': 'Categoria de Producto'}]
        context['back_url'] = reverse('base:product-category-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteProductCategory(request, pk):
    model = PyProductCategory
    eval(model.objects.get(id=pk).delete())
    PyLog(
        name=model._meta.object_name,
        note='{}Delete:'.format(model._meta.verbose_name)
    ).save()
    return redirect(reverse('base:product-category'))
