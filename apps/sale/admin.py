# Django Library
from django.contrib import admin



# Localfolder Library
from .models import PySaleOrder, PySaleOrderDetail

# Register your models here.


class PySaleOrderDetailInline(admin.TabularInline):
    model = PySaleOrderDetail
    extra = 1
    fields = [
            # 'sale_order_id',
            'product',
            'description',
            'quantity',
            # 'measure_unit',
            # 'product_tax',
            'amount_untaxed',
            'discount',
            # 'amount_total',
        ]


class PySaleOrderAdmin(admin.ModelAdmin):
    fields = ['partner_id']
    inlines = [PySaleOrderDetailInline]


admin.site.register(PySaleOrder, PySaleOrderAdmin)
