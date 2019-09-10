"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView

# Librerias en carpetas locales
from ..forms import SaleOrderForm
from ..models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)


SALE_DETAIL_FIELDS = [
    {'string': 'Producto', 'field': 'product', 'align': ''},
    {'string': 'Descripcion', 'field': 'description', 'align': ''},
    {'string': 'Cantidad', 'field': 'quantity', 'align': ''},
    {'string': 'Precio', 'field': 'amount_untaxed', 'align': 'text-right'},
    {'string': 'Descuento', 'field': 'discount', 'align': 'text-right'},
    {'string': 'Sub Total', 'field': 'amount_total', 'align': 'text-right'},
]


# ========================================================================== #
class SaleOrderEditView(LoginRequiredMixin, UpdateView):
    """Vista para editarar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'sale/saleorderform.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        _pk = self.kwargs.get(self.pk_url_kwarg)
        context = super(SaleOrderEditView, self).get_context_data(**kwargs)
        context['title'] = _('Sale Order Edit')
        context['action_url'] = 'sale:sale-order-edit'
        context['back_url'] = 'sale:sale-order'
        context['print_url'] = 'sale:sale-order-pdf'
        context['product_add_url'] = 'sale:sale-order-detail-add'
        context['product_edit_url'] = 'sale:sale-order-detail-edit'
        context['product_delete_url'] = 'sale:sale-order-detail-delete'
        context['breadcrumbs'] = [{'url': 'sale:sale-order', 'name': _('Sales')}]
        context['fields'] = SALE_DETAIL_FIELDS
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
