# Librerias Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyLog
from ..forms.product import ProductForm
from ..models import PyProduct
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

PRODUCT_FIELDS = [
    {'string': _("Code"), 'field': 'code'},
    {'string': _("Bar Code"), 'field': 'bar_code'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("UOM"), 'field': 'uom_id'},
    {'string': _("Tax"), 'field': 'tax'},
    {'string': _("Category"), 'field': 'category_id'},
    {'string': _("Brand"), 'field': 'brand_id'},
    {'string': _("Web Category"), 'field': 'web_category_id'},
    {'string': _("Price"), 'field': 'price'},
    {'string': _("Cost"), 'field': 'cost'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Youtube Video"), 'field': 'youtube_video'},
]

LEAD_FIELDS_SHORT = [
    'name',
    'uom_id',
    'category_id',
    'tax',
    'web_category_id',
    'brand_id',
    'code',
    'bar_code',
    'price',
    'cost',
    'type',
    'web_active',
    'pos_active',
    'share',
    'img',
    'youtube_video',
    'description',
]


class ProductListView(LoginRequiredMixin, FatherListView):
    model = PyProduct
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['detail_url'] = 'base:product-detail'
        context['add_url'] = 'base:product-add'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProduct
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['detail_name'] = 'Producto: %s' % context['object'].name
        context['update_url'] = 'base:product-update'
        context['delete_url'] = 'base:product-delete'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProduct
    # fields = LEAD_FIELDS_SHORT
    form_class = ProductForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear producto'
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['back_url'] = reverse('base:products')
        return context


class ProductUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProduct
    # fields = LEAD_FIELDS_SHORT
    form_class = ProductForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:products', 'name': 'Productos'}]
        context['back_url'] = reverse('base:product-detail', kwargs={'pk': context['object'].pk})
        return context


def DeleteProduct(request, pk):
    model = PyProduct
    eval(model.objects.get(id=pk).delete())
    PyLog(
        name=model._meta.object_name,
        note='{}Delete:'.format(model._meta.verbose_name)
    ).save()
    return redirect(reverse('base:products'))
