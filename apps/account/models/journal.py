# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from apps.base.models import PyFather

JOURNAL_TYPE = (
        ("sale", _("Sale")),
        ("purchase", _("Purchase")),
        ("cash", _("Cash")),
        ("bank", _("bank")),
        ("miscellaneous", _("Miscellaneous")),
    )


# ========================================================================== #
class PyJournal(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    type = models.CharField(
        choices=JOURNAL_TYPE,
        max_length=13,
        default='Sale'
    )
    short_code = models.CharField(max_length=6, default='Sale')
    default_credit_account = models.IntegerField(
        _("Default Credit Account"),
        null=True,
        blank=True
    )
    default_debit_account = models.IntegerField(
        _("Default Debit Account"),
        null=True,
        blank=True
    )

    def __str__(self):
        return "{}".format(self.name)
