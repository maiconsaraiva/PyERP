"""Sub Vistas del módulo
"""
# Librerias Standard
import logging

# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _

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
    template_name = 'sale/saleorderform.html'
    success_url = 'sale:sale-order-edit'

    def get_context_data(self, **kwargs):
        context = super(SaleOrderAddView, self).get_context_data(**kwargs)
        context['title'] = _('Sale Order Add')
        context['action_url'] = 'sale:sale-order-add'
        context['back_url'] = 'sale:sale-order'
        context['breadcrumbs'] = [{'url': 'sale:sale-order', 'name': _('Sales')}]

        return context

    def form_valid(self, form):
        self.object = form.save()
        url = reverse_lazy(self.get_success_url(), kwargs={'pk': self.object.pk})

        return HttpResponseRedirect(url)
