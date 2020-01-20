# Django Library
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather, PyPartner, PyProduct, PyTax, PyUom
from apps.base.views.sequence import get_next_value
from .invoice import PyInvoice

PAYMENT_TYPE = (
        (1, _('sale')),
        (2, _('purchase')),
    )


# ========================================================================== #
class PyPayment(PyFather):
    """Modelo de la orden de pago
    """
    name = models.CharField(_('Name'), max_length=80, editable=False)
    invoice_id = models.ForeignKey(
        PyInvoice,
        on_delete=models.PROTECT,
        verbose_name=_('Invoice')
    )
    amount_untaxed = models.DecimalField(
        _('Amount un'),
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_iva = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_other = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_exempt = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_total = models.DecimalField(
        _('Total'),
        max_digits=100,
        decimal_places=2,
        default=0
    )
    description = models.TextField(_('Description'), blank=True, null=True)
    state = models.ForeignKey(
        PyPaymentState,
        on_delete=models.PROTECT,
        verbose_name=_('State'),
        default=1
    )
    note = models.TextField(_('Note'), blank=True, null=True)
    date_confirm = models.DateTimeField(null=True)
    origin = models.CharField(_('Origin'), max_length=80, blank=True, null=True)

    class Meta:
        ordering = ['pk']
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')


    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = get_next_value(self._meta.object_name, 'INV')

        if not self.date_invoice or self.date_invoice == "":
            self.date_invoice = timezone.now
        super().save(*args, **kwargs)


# ========================================================================== #
class PyPaymentDetail(PyFather):
    """Modelo del detalle de la orden de pago
    """
    invoice_id = models.ForeignKey(
        PyPayment,
        on_delete=models.PROTECT
    )
    product_id = models.ForeignKey(
        PyProduct,
        on_delete=models.PROTECT,
        verbose_name=_('Product')
    )
    description = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(
        _('Quantity'),
        max_digits=100,
        decimal_places=2,
        default=0
    )
    uom_id = models.ForeignKey(
        PyUom,
        verbose_name=_('UOM'),
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    price = models.DecimalField(
        _('Price'),
        max_digits=100,
        decimal_places=2,
        default=0
    )
    tax_id = models.ManyToManyField(PyTax, verbose_name=_('Tax'), blank=True)
    amount_untaxed = models.DecimalField(
        _('Amount un'),
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_iva = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_other = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_tax_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    amount_exempt = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0
    )
    discount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    amount_total = models.DecimalField(
        _('Total'),
        max_digits=100,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ['pk']
        verbose_name = _('Payment detail')
        verbose_name_plural = _('Payment details')
