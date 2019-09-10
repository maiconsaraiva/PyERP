"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView

# Librerias en carpetas locales
from ..models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)


# ========================================================================== #
class SaleOrderDetailDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar los productos de la sale order
    """
    model = PySaleOrderDetail
    template_name = 'sale/saleorderdelete.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super(SaleOrderDetailDeleteView, self).get_context_data(**kwargs)
        context['title'] = _('Remove Product from the Sales Order')
        context['action_url'] = 'sale:sale-order-detail-delete'
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
