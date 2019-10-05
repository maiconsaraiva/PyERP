import os

# Django Library
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models import F

# Thirdparty Library
from apps.sale.models import PySaleOrder, PySaleOrderDetail


# ========================================================================== #
@receiver(post_save, sender=PySaleOrder)
def post_save_sale_order(sender, instance, created, **kwargs):
    sale_order = PySaleOrder.objects.get(pk=instance.pk)
    amount_untaxed = 0

    for product in PySaleOrderDetail.objects.filter(sale_order_id=instance.pk):
        amount_untaxed += (product.quantity * product.amount_untaxed) - product.discount

    # PySaleOrder.objects.filter(pk=instance.pk).update(description=124)
    # os._exit(1)
    instance.amount_untaxed = amount_untaxed  # amount_untaxed
    instance.description = amount_untaxed
    # sale_order.save()
    # print(amount_untaxed)


# ========================================================================== #
@receiver(post_delete, sender=PySaleOrderDetail)
def post_delete_sale_order(sender, instance, **kwargs):
    _sale_order = PySaleOrder.objects.get(pk=instance.sale_order_id.pk)
    _amount_untaxed = sender.objects.filter(sale_order_id=instance.sale_order_id.pk).aggregate(Sum('amount_total'))
    if _amount_untaxed['amount_total__sum']:
        _sale_order.amount_untaxed = _amount_untaxed['amount_total__sum']
    else:
        _sale_order.amount_untaxed = 0
    _sale_order.save()
