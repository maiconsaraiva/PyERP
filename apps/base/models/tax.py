# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyTax(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('base:tax-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
