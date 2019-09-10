# __init__.py
""" Inicialización de las vistas de módulo sale
"""
# Librerias Django
from django.db.models import Q

# Librerias de terceros
from apps.base.models import PyProduct
from dal import autocomplete

# Librerias en carpetas locales
from ..models import PySaleOrderDetail
from .saleorderadd import SaleOrderAddView
from .saleorderdelete import SaleOrderDeleteView
from .saleorderdetailadd import SaleOrderDetailAddView
from .saleorderdetaildelete import SaleOrderDetailDeleteView
from .saleorderdetailedit import SaleOrderDetailEditView
from .saleorderedit import SaleOrderEditView
from .saleorderlist import SaleOrderListView


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
