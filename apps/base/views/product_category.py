# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyProductCategory

CATEGORY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

CATEGORY_FIELDS_SHORT = ['name', 'parent_id']


class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = PyProductCategory
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categorías de Productos'
        context['detail_url'] = 'product-category-detail'
        context['add_url'] = 'base:product-category-add'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductCategoryDetailView(LoginRequiredMixin, DetailView):
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


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
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


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
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
def DeleteProductCategory(self, pk):
    product_category = PyProductCategory.objects.get(id=pk)
    product_category.delete()
    return redirect(reverse('product-category'))
