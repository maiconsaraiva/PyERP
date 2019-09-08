# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyCountry(PyFather):
    name = models.CharField(_("Name"), max_length=40)

    def __str__(self):
        return format(self.name)

    def get_absolute_url(self):
        return reverse('base:country-detail', kwargs={'pk': self.pk})
