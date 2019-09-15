# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyProductCategoryUOM

CATEGORY_UOM_FIELDS = [
    {'string': 'Name', 'field': 'name'},
]

CATEGORY_UOM_FIELDS_SHORT = ['name']


class ProductCategoryUOMListView(LoginRequiredMixin, ListView):
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


class ProductCategoryUOMDetailView(LoginRequiredMixin, DetailView):
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


class ProductCategoryUOMCreateView(LoginRequiredMixin, CreateView):
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


class ProductCategoryUOMUpdateView(LoginRequiredMixin, UpdateView):
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


@login_required(login_url="base:login")
def DeleteProductCategoryUOM(self, pk):
    product_category_uom = PyProductCategoryUOM.objects.get(id=pk)
    product_category_uom.delete()
    return redirect(reverse('base:product-category-uom'))
