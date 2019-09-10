"""Sub Vistas del módulo
"""
# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PySaleOrder

SALE_FIELDS = [
    {'string': _('Name'), 'field': 'name'},
    {'string': _('Client'), 'field': 'partner_id'},
    {'string': _('Estatus'), 'field': 'state'},
]

LEAD_FIELDS_SHORT = ['name', 'partner_id', 'state']


# ========================================================================== #
class SaleOrderListView(LoginRequiredMixin, ListView):
    """Lista de las ordenes de venta
    """
    model = PySaleOrder
    template_name = 'sale/saleorderlist.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        """Definición de variables de contexto
        """
        context = super(SaleOrderListView, self).get_context_data(**kwargs)
        context['title'] = _('Sales Orders')
        context['detail_url'] = 'base:sale:sale-order-detail'
        context['add_url'] = 'sale:sale-order-add'
        context['edit_url'] = 'sale:sale-order-edit'
        context['delete_url'] = 'sale:sale-order-delete'
        context['fields'] = SALE_FIELDS
        return context
