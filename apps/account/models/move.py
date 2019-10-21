# Standard Library
from datetime import datetime

# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager

# Thirdparty Library
from apps.base.models import PyCompany, PyFather


# Localfolder Library
from .journal import PyJournal
from .plan import PyAccountPlan

ACCOUNT_MOVE_STATE = (
        (0, _('No asentado')),
        (1, _('Validado')),
        (2, _('cancel')),
        (3, _('confirmed'))
    )


# ========================================================================== #
class PyAccountMove(PyFather):
    code = models.CharField(_('Code'), max_length=80)
    name = models.CharField(_('Name'), max_length=80)
    state = models.CharField(
        choices=ACCOUNT_MOVE_STATE, max_length=64, default='draft')
    journal = models.ForeignKey(PyJournal, on_delete=models.PROTECT)
    date_move = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    reference_company = models.ForeignKey(PyCompany, on_delete=models.PROTECT)
    amount_total = models.DecimalField(
        _('Total'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    debit = models.DecimalField(
        _('debit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        _('credit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def get_absolute_url(self):
        return reverse('PyAccountMove:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)

    class Meta:
        verbose_name = _("Account Move")
        verbose_name_plural = _("Account Moves")


# ========================================================================== #
class PyAccountMoveDetail(PyFather):
    """Modelo del detalle de la orden de pago
    """
    account_plan_id = models.ForeignKey(
        PyAccountPlan,
        on_delete=models.PROTECT
    )
    reference_company = models.ForeignKey(
        PyCompany,
        on_delete=models.PROTECT,
        verbose_name=_('Product')
    )
    tags = TaggableManager(blank=True)
    debit = models.DecimalField(
        _('debit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    credit = models.DecimalField(
        _('credit'),
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ['pk']
        verbose_name = _('Invoice detail')
        verbose_name_plural = _('Invoice details')
