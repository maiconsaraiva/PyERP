"""Sub Vistas del módulo
"""
# Standard Library
import logging

# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView
from django.shortcuts import render
from django.core import serializers

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

# Localfolder Library
from .forms import PRODUCT_FORMSET, SaleOrderForm
from .models import PySaleOrder, PySaleOrderDetail
from apps.base.models import PyProduct, PyTax

LOGGER = logging.getLogger(__name__)

OBJECT_LIST_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Partner'), 'field': 'partner_id'},
    {'string': ('Date'), 'field': 'date_order'},
    {'string': ('Net Amount'), 'field': 'amount_untaxed', 'align': 'text-right', 'humanize': True},
    {'string': ('Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
    {'string': _('Status'), 'field': 'state'},
]

OBJECT_DETAIL_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Partner'), 'field': 'partner_id'},
    {'string': ('Date'), 'field': 'date_order'},
    {'string': _('Status'), 'field': 'state'},
]

DETAIL_OBJECT_LIST_FIELDS = [
    {'string': _('Description'), 'field': 'product_id'},
    {'string': _('Quantity'), 'field': 'quantity', 'align': 'text-center', 'humanize': True},
    {'string': ('Price'), 'field': 'price', 'align': 'text-right', 'humanize': True},
    {'string': _('Discount'), 'field': 'discount', 'align': 'text-right', 'humanize': True},
    {'string': _('Tax'), 'field': 'tax_id'},
    {'string': _('Sub Total'), 'field': 'amount_total', 'align': 'text-right', 'humanize': True},
]

OBJECT_FORM_FIELDS = [
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': _('Estatus'), 'field': 'state'},
]

LEAD_FIELDS_SHORT = ['name', 'partner_id', 'state']


# ========================================================================== #
class SaleOrderListView(LoginRequiredMixin, FatherListView):
    """Lista de las ordenes de venta
    """
    model = PySaleOrder
    # template_name = 'sale/saleorderlist.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class SaleOrderDetailView(LoginRequiredMixin, FatherDetailView):
    model = PySaleOrder
    template_name = 'sale/detail.html'
    extra_context = {
        'master_fields': OBJECT_DETAIL_FIELDS,
        'detail_fields': DETAIL_OBJECT_LIST_FIELDS
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        context['print_url'] = '{}:pdf'.format(object_name)
        context['detail'] = PySaleOrderDetail.objects.filter(
            active=True,
            company_id=self.request.user.active_company_id,
            sale_order_id=self.object.pk
        )
        return context


# ========================================================================== #
class SaleOrderAddView(LoginRequiredMixin, FatherCreateView):
    """Vista para agregar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'sale/saleorderform.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = 'PySaleOrder:sale-order-add'
        if self.request.POST:
            context['products'] = PRODUCT_FORMSET(self.request.POST)
        else:
            context['products'] = PRODUCT_FORMSET()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        product = context['products']
        with transaction.atomic():
            form.instance.uc = self.request.user.pk
            self.object = form.save()
            if product.is_valid():
                product.instance = self.object
                product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('PySaleOrder:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class SaleOrderEditView(LoginRequiredMixin, FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'sale/saleorderform.html'

    def get_context_data(self, **kwargs):
        _pk = self.kwargs.get(self.pk_url_kwarg)
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        context['action_url'] = 'PySaleOrder:update'
        context['print_url'] = '{}:pdf'.format(object_name)
        if self.request.POST:
            context['form'] = SaleOrderForm(self.request.POST, instance=self.object)
            context['products'] = PRODUCT_FORMSET(self.request.POST, instance=self.object)
        else:
            context['form'] = SaleOrderForm(instance=self.object)
            context['products'] = PRODUCT_FORMSET(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        products = context['products']
        with transaction.atomic():
            form.instance.um = self.request.user.pk
            if form.is_valid() and products.is_valid():
                self.object = form.save(commit=False)
                products.instance = self.object
                products.save()
                self.object.save()
                return super().form_valid(form)
            else:
                return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('PySaleOrder:detail', kwargs={'pk': self.object.pk})


# ========================================================================== #
class SaleOrderDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar las sale
    """
    model = PySaleOrder
    template_name = 'sale/saleorderdelete.html'
    success_url = reverse_lazy('PySaleOrder:list')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super(SaleOrderDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'ELiminar Orden de Venta'
        context['action_url'] = 'PySaleOrder:delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar la orden de compras <strong>' + self.object.name + '</strong>?</p>'
        context['cant_delete_message'] = '<p>La orden de compras <strong>' + self.object.name + '</strong>, no puede ser eliminada ya que posee un detalle que debe eliminar antes.</p>'
        context['detail'] = PySaleOrderDetail.objects.filter(sale_order_id=pk).exists()
        return context

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        success_url = self.get_success_url()
        detail = PySaleOrderDetail.objects.filter(sale_order_id=pk).exists()
        if not detail:
            self.object.delete()
        return HttpResponseRedirect(success_url)


# ========================================================================== #
def load_product(request):
    context = {}
    product_id = request.GET.get('product')
    product = PyProduct.objects.filter(pk=product_id)
    context['product'] = serializers.serialize('json', product)
    return JsonResponse(data=context, safe=False)


# ========================================================================== #
def load_tax(request):
    context = {}
    tax_id = request.GET.getlist('tax[]')
    print("Aqui voy {}".format(tax_id))
    tax = PyTax.objects.filter(pk__in=tax_id)
    context['tax'] = serializers.serialize('json', tax)
    return JsonResponse(data=context, safe=False)
