"""Signals para el calculo de las ordenes de compra
"""

# Django Library
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

# Thirdparty Library
from apps.sale.models import PySaleOrder, PySaleOrderDetail


# ========================================================================== #
@receiver(post_delete, sender=PySaleOrder)
@receiver(post_save, sender=PySaleOrder)
def calc_sale_order(sender, instance, created, **kwargs):
    amount_untaxed = 0
    amount_exempt = 0
    amount_tax_iva = 0
    amount_tax_other = 0
    amount_tax_total = 0
    amount_total = 0

    for product in PySaleOrderDetail.objects.filter(sale_order_id=instance.pk):
        amount_untaxed += product.amount_untaxed
        amount_tax_iva += product.amount_tax_iva
        amount_tax_other += product.amount_tax_other
        amount_tax_total += product.amount_tax_total
        amount_exempt += product.amount_exempt
        amount_total += product.amount_total

    instance.amount_untaxed = amount_untaxed
    instance.amount_tax_iva = amount_tax_iva
    instance.amount_tax_other = amount_tax_other
    instance.amount_tax_total = amount_tax_total
    instance.amount_exempt = amount_exempt
    instance.amount_total = amount_total


# ========================================================================== #
@receiver(pre_save, sender=PySaleOrderDetail)
def calc_sale_order_detail(sender, instance, **kwargs):
    amount_untaxed = 0
    amount_exempt = 0
    amount_tax_iva = 0
    amount_tax_other = 0

    amount_untaxed = (instance.quantity * instance.price) - instance.discount
    if instance.tax_id.all().exists():
        for tax in instance.tax_id.all():
            if tax.pk == 1:
                amount_tax_iva = (amount_untaxed * tax.amount)/100
            else:
                amount_tax_other += (amount_untaxed * tax.amount)/100
    else:
        amount_exempt = amount_untaxed

    instance.amount_untaxed = amount_untaxed
    instance.amount_tax_iva = amount_tax_iva
    instance.amount_tax_other = amount_tax_other
    instance.amount_tax_total = amount_tax_iva + amount_tax_other
    instance.amount_exempt = amount_exempt
    instance.amount_total = amount_untaxed + amount_tax_iva + amount_tax_other
