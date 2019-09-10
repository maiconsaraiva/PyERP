"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..forms import SaleOrderDetailForm
from ..models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)


# ========================================================================== #
class SaleOrderDetailEditView(LoginRequiredMixin, UpdateView):
    """Vista para editarar los productos de los sale
    """
    model = PySaleOrderDetail
    form_class = SaleOrderDetailForm
    template_name = 'sale/saleordermodalform.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderDetailEditView, self).get_context_data(**kwargs)
        context['title'] = _('Edit Product of the Sales Order')
        context['action_url'] = reverse_lazy(
            'sale:sale-order-detail-edit',
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
