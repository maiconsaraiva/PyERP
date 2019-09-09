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
from ..forms import SaleOrderForm
from ..models import PySaleOrder

LOGGER = logging.getLogger(__name__)


# ========================================================================== #
class SaleOrderAddView(LoginRequiredMixin, CreateView):
    """Vista para agregar las sale
    """
    model = PySaleOrder
    form_class = SaleOrderForm
    template_name = 'saleorderform.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderAddView, self).get_context_data(**kwargs)
        context['title'] = 'Agregar Orden de Venta'
        context['action_url'] = 'sale:sale-order-add'
        context['back_url'] = 'sale:sale-order'

        return context

    def form_valid(self, form):
        self.object = form.save()
        url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})

        return HttpResponseRedirect(url)
