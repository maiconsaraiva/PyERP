# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ...base.models import PyProductWebCategory

CATEGORY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

CATEGORY_FIELDS_SHORT = ['name', 'parent_id']


class ProductWebCategoryListView(LoginRequiredMixin, ListView):
    model = PyProductWebCategory
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categorías Web de Productos'
        context['detail_url'] = 'product-webcategory-detail'
        context['add_url'] = 'base:product-webcategory-add'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductWebCategoryDetailView(LoginRequiredMixin, DetailView):
    model = PyProductWebCategory
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categorias Web de Productos'}]
        context['update_url'] = 'product-webcategory-update'
        context['delete_url'] = 'product-webcategory-delete'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductWebCategoryCreateView(LoginRequiredMixin, CreateView):
    model = PyProductWebCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Categoria Web de Productos'
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categoria Web de Producto'}]
        context['back_url'] = reverse('product-category')
        return context


class ProductWebCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = PyProductWebCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductWebCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-webcategory', 'name': 'Categoria Web de Producto'}]
        context['back_url'] = reverse('product-webcategory-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteProductWebCategory(self, pk):
    product_category = PyProductWebCategory.objects.get(id=pk)
    product_category.delete()
    return redirect(reverse('product-webcategory'))
