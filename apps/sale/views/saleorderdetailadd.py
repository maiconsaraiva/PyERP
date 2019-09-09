"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Librerias en carpetas locales
from ..forms import SaleOrderDetailForm
from ..models import PySaleOrder, PySaleOrderDetail

LOGGER = logging.getLogger(__name__)


# ========================================================================== #
class SaleOrderDetailAddView(LoginRequiredMixin, CreateView):
    """Vista para agregar las sale
    """
    model = PySaleOrderDetail
    form_class = SaleOrderDetailForm
    template_name = 'saleordermodalform.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderDetailAddView, self).get_context_data(**kwargs)
        context['title'] = 'Agregar Producto a la Orden de Venta'
        context['action_url'] = reverse_lazy(
            'sale:sale-order-detail-add',
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
