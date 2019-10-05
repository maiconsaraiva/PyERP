"""Sub Vistas del módulo
"""
# Standard Library
import logging

# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView

# Thirdparty Library
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)

# Localfolder Library
from .forms import PRODUCT_FORMSET, SaleOrderDetailForm, SaleOrderForm
from .models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)

OBJECT_LIST_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Partner'), 'field': 'partner_id'},
    {'string': ('Date'), 'field': 'date_order'},
    # {'string': 'Precio', 'field': 'amount_untaxed', 'align': 'text-right'},
    # {'string': 'Descuento', 'field': 'discount', 'align': 'text-right'},
    {'string': _('Status'), 'field': 'state'},
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
    extra_context = {'fields': OBJECT_LIST_FIELDS}


# ========================================================================== #
class SaleOrderAddView(FatherCreateView):
    """Vista para agregar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'sale/saleorderform.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Sale Order Add')
        context['action_url'] = 'PySaleOrder:sale-order-add'
        # context['back_url'] = 'PySaleOrder:list'
        context['breadcrumbs'] = [{'url': 'PySaleOrder:sale-order', 'name': _('Sales')}]
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

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.uc = self.request.user.pk
    #     self.object.company_id = self.request.user.active_company_id
    #     self.object.save()
    #     url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})
    #     return HttpResponseRedirect(url)


# ========================================================================== #
class SaleOrderEditView(FatherUpdateView):
    """Vista para editarar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'sale/saleorderform.html'

    def get_context_data(self, **kwargs):
        _pk = self.kwargs.get(self.pk_url_kwarg)
        context = super().get_context_data(**kwargs)
        context['title'] = _('Sale Order Edit')
        context['action_url'] = 'PySaleOrder:update'
        # context['back_url'] = 'PySaleOrder:list'
        context['print_url'] = 'PySaleOrder:sale-order-pdf'
        context['product_add_url'] = 'PySaleOrder:sale-order-detail-add'
        context['product_edit_url'] = 'PySaleOrder:sale-order-detail-edit'
        context['product_delete_url'] = 'PySaleOrder:sale-order-detail-delete'
        context['breadcrumbs'] = [{'url': 'PySaleOrder:sale-order', 'name': _('Sales')}]
        if self.request.POST:
            context['form'] = SaleOrderForm(self.request.POST, instance=self.object)
            context['products'] = PRODUCT_FORMSET(self.request.POST, instance=self.object)
        else:
            context['form'] = SaleOrderForm(instance=self.object)
            context['products'] = PRODUCT_FORMSET(instance=self.object)
        return context
        context['fields'] = OBJECT_FORM_FIELDS
        context['object_list'] = PySaleOrderDetail.objects.filter(
            sale_order_id=_pk
        ).only(
            "product",
            "description",
            "quantity",
            "amount_untaxed",
            "discount",
            "amount_total"
        )
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
class SaleOrderDeleteView(DeleteView):
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
