# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather

TYPE_CHOICE = (
    ("company", _("Company")),
    ("individual", _("Individual")),
    ("address", _("Address")),
    ("contact", _("Contact")),
)

class PyPartner(PyFather):
    name = models.CharField(_("Name"), max_length=40)
    street = models.CharField(_("Street"), max_length=100, blank=True)
    street_2 = models.CharField(_("Street Other"), max_length=100, blank=True)
    city = models.CharField(_("City"), max_length=50, blank=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    email = models.EmailField(_("Email"), max_length=40, blank=True)
    customer = models.BooleanField(_("Customer"), default=True)
    provider = models.BooleanField(_("Provider"), default=True)
    for_invoice = models.BooleanField(_("For Invoice"), default=True)
    note = models.TextField(blank=True, null=True)
    not_email = models.BooleanField(_("No Email"), default=False)
    parent_id = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.CASCADE)

    type = models.CharField(_("type"), choices=TYPE_CHOICE, max_length=64, default='company')

    def get_absolute_url(self):
        return reverse('base:partner-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
