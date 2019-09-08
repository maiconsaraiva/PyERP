# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias de terceros
# from apps.sale.models import PySaleOrderDetail
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PyProduct

PRODUCT_FIELDS = [
    {'string': 'Código', 'field': 'code'},
    {'string': 'Código Barra', 'field': 'bar_code'},
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría', 'field': 'category_id'},
    {'string': 'Categoría Web', 'field': 'web_category_id'},
    {'string': 'Precio', 'field': 'price'},
    {'string': 'Costo', 'field': 'cost'},
    {'string': 'tipo', 'field': 'type'},
    {'string': 'Creado', 'field': 'created_on'},
    {'string': 'Descripción', 'field': 'description'},
    {'string': 'Creado', 'field': 'created_on'},
]

LEAD_FIELDS_SHORT = ['name', 'category_id', 'web_category_id', 'code', 'price', 'cost', 'type', 'description', 'web_active']


class ProductListView(LoginRequiredMixin, ListView):
    model = PyProduct
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['detail_url'] = 'product-detail'
        context['add_url'] = 'base:product-add'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = PyProduct
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['detail_name'] = 'Producto: %s' % context['object'].name
        context['update_url'] = 'product-update'
        context['delete_url'] = 'product-delete'
        context['fields'] = PRODUCT_FIELDS
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear producto'
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['back_url'] = reverse('products')
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = PyProduct
    fields = LEAD_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'products', 'name': 'Productos'}]
        context['back_url'] = reverse('product-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteProduct(self, pk):
    product = PyProduct.objects.get(id=pk)
    product.delete()
    return redirect(reverse('products'))

"""
class ProductAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        _sale_order = self.forwarded.get('sale_order', None)

        if _sale_order:
            product_sale_order = PySaleOrderDetail.objects.filter(sale_order=_sale_order).values("product")
            queryset = PyProduct.objects.filter(~Q(pk__in=product_sale_order))
        else:
            queryset = PyProduct.objects.all()

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)

        return queryset"""
