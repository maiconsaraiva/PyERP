"""Sub Vistas del módulo
"""
# Standard Library
import logging

# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.db import transaction

# Thirdparty Library
from apps.base.models import PyProduct
from apps.base.views.web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView)
from dal import autocomplete

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
            context['producto'] = PRODUCT_FORMSET(self.request.POST)
        else:
            context['producto'] = PRODUCT_FORMSET()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        producto = context['producto']
        with transaction.atomic():
            form.instance.uc = self.request.user.pk
            self.object = form.save()
            if producto.is_valid():
                producto.instance = self.object
                producto.save()
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
        context = super(SaleOrderEditView, self).get_context_data(**kwargs)
        context['title'] = _('Sale Order Edit')
        context['action_url'] = 'PySaleOrder:update'
        # context['back_url'] = 'PySaleOrder:list'
        context['print_url'] = 'PySaleOrder:sale-order-pdf'
        context['product_add_url'] = 'PySaleOrder:sale-order-detail-add'
        context['product_edit_url'] = 'PySaleOrder:sale-order-detail-edit'
        context['product_delete_url'] = 'PySaleOrder:sale-order-detail-delete'
        context['breadcrumbs'] = [{'url': 'PySaleOrder:sale-order', 'name': _('Sales')}]
        if self.request.POST:
            context['producto'] = PRODUCT_FORMSET(self.request.POST, instance=self.object)
        else:
            context['producto'] = PRODUCT_FORMSET(instance=self.object)
        return context
        context['fields'] = OBJECT_FORM_FIELDS
        context['object_list'] = PySaleOrderDetail.objects.filter(
            sale_order=_pk
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
        self.object = form.save()
        url = reverse_lazy(
            self.get_success_url(),
            kwargs={'pk': self.object.pk}
        )
        return HttpResponseRedirect(url)


# ========================================================================== #
class SaleOrderDeleteView(DeleteView):
    """Vista para eliminar las sale
    """
    model = PySaleOrder
    template_name = 'sale/saleorderdelete.html'
    success_url = reverse_lazy('PySaleOrder:sale-order')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super(SaleOrderDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'ELiminar Orden de Venta'
        context['action_url'] = 'PySaleOrder:sale-order-delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar la orden de compras <strong>' + self.object.name + '</strong>?</p>'
        context['cant_delete_message'] = '<p>La orden de compras <strong>' + self.object.name + '</strong>, no puede ser eliminada ya que posee un detalle que debe eliminar antes.</p>'
        context['detail'] = PySaleOrderDetail.objects.filter(sale_order=pk).exists()
        return context

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        success_url = self.get_success_url()
        detail = PySaleOrderDetail.objects.filter(sale_order=pk).exists()
        if not detail:
            self.object.delete()
        return HttpResponseRedirect(success_url)


# ========================================================================== #
class SaleOrderDetailAddView(CreateView):
    """Vista para agregar las sale
    """
    model = PySaleOrderDetail
    form_class = SaleOrderDetailForm
    template_name = 'sale/saleordermodalform.html'
    success_url = 'PySaleOrder:update'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderDetailAddView, self).get_context_data(**kwargs)
        context['title'] = _('Add Product to the Sales Order')
        context['action_url'] = reverse_lazy(
            'PySaleOrder:sale-order-detail-add',
            kwargs={'saleorder_pk': self.kwargs['saleorder_pk']}
        )
        context['sale_order_pk'] = self.kwargs['saleorder_pk']
        return context

    def get_initial(self):
        initial = super(SaleOrderDetailAddView, self).get_initial()
        initial.update({'sale_order': self.kwargs['saleorder_pk']})
        return initial

    def form_valid(self, form):
        """To Do:
            1.-Validar que la "order sale" este habilitada para poderle
            agregar más productos.
            2.- Otras validaciones concernientes a los calculos y la
            aplicación de impuestos y esas cosas.
        """
        _sale_order_pk = self.kwargs['saleorder_pk']
        self.object = form.save(commit=False)
        self.object.sale_order_id = _sale_order_pk
        self.object.amount_total = (
            self.object.amount_untaxed * self.object.quantity
        ) - self.object.discount
        self.object.save()
        url = reverse_lazy(
            self.get_success_url(),
            kwargs={'pk': _sale_order_pk}
        )
        return HttpResponseRedirect(url)


# ========================================================================== #
class SaleOrderDetailDeleteView(DeleteView):
    """Vista para eliminar los productos de la sale order
    """
    model = PySaleOrderDetail
    template_name = 'sale/saleorderdelete.html'
    success_url = 'PySaleOrder:update'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super(SaleOrderDetailDeleteView, self).get_context_data(**kwargs)
        context['title'] = _('Remove Product from the Sales Order')
        context['action_url'] = 'PySaleOrder:sale-order-detail-delete'
        context['delete_message'] = '<p>¿Está seguro de eliminar el producto <strong>' + self.object.product.name + '</strong> de la orden de compras?</p>'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        url = reverse_lazy(
            self.get_success_url(),
            kwargs={'pk': self.object.sale_order.pk}
        )
        print(url)
        self.object.delete()
        return HttpResponseRedirect(url)


# ========================================================================== #
class SaleOrderDetailEditView(UpdateView):
    """Vista para editarar los productos de los sale
    """
    model = PySaleOrderDetail
    form_class = SaleOrderDetailForm
    template_name = 'sale/saleordermodalform.html'
    success_url = 'PySaleOrder:update'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderDetailEditView, self).get_context_data(**kwargs)
        context['title'] = _('Edit Product of the Sales Order')
        context['action_url'] = reverse_lazy(
            'PySaleOrder:sale-order-detail-edit',
            kwargs={'pk': self.kwargs['pk']}
        )
        return context

    def form_valid(self, form):
        """To Do:
            1.- Validar que la "order sale" este habilitada para poderle
            hacer modificaciones a los productos.
            2.- Otras validaciones concernientes a los calculos y la
            aplicación de impuestos y esas cosas.
        """
        self.object = form.save(commit=False)
        self.object.amount_total = (
            self.object.amount_untaxed * self.object.quantity
        ) - self.object.discount
        self.object.save()
        url = reverse_lazy(
            self.get_success_url(),
            kwargs={'pk': self.object.sale_order.pk}
        )
        return HttpResponseRedirect(url)


# ========================================================================== #
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
        return queryset
