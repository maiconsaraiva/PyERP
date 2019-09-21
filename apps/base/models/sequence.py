# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PySequence(PyFather):
    name = models.CharField(_("Name"), max_length=100)
    prefix = models.CharField(_("Prefix"), max_length=40)
    padding = models.DecimalField(_("Padding"), max_digits=10, decimal_places=2, default=1)
    increment = models.DecimalField(_("Increment"), max_digits=10, decimal_places=2, default=1)
    next_number = models.DecimalField(_("Next Number"), max_digits=10, decimal_places=2, default=1)
    model = models.CharField(_("Model"), max_length=100)

    def get_absolute_url(self):
        return reverse('base:sequence-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
