"""Sub Vistas del módulo
"""
# Librerias Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Librerias en carpetas locales
from ..models import PySaleOrder

SALE_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Cliente', 'field': 'partner_id'},
    {'string': 'Estado', 'field': 'state'},
]

LEAD_FIELDS_SHORT = ['name', 'partner_id', 'state']


# ========================================================================== #
class SaleOrderListView(LoginRequiredMixin, ListView):
    """Lista de las ordenes de venta
    """
    model = PySaleOrder
    template_name = 'saleorderlist.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        """Definición de variables de contexto
        """
        context = super(SaleOrderListView, self).get_context_data(**kwargs)
        context['title'] = 'Orden de Venta'
        context['detail_url'] = 'base:sale:sale-order-detail'
        context['add_url'] = 'base:sale:sale-order-add'
        context['edit_url'] = 'sale:sale-order-edit'
        context['delete_url'] = 'base:sale:sale-order-delete'
        context['fields'] = SALE_FIELDS
        return context
