"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)


# ========================================================================== #
class SaleOrderDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar las sale
    """
    model = PySaleOrder
    template_name = 'sale/saleorderdelete.html'
    success_url = reverse_lazy('sale:sale-order')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        self.object = self.get_object()
        context = super(SaleOrderDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'ELiminar Orden de Venta'
        context['action_url'] = 'sale:sale-order-delete'
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
