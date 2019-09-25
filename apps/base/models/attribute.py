# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models.variant import PyVariant
from .father import PyFather


class PyAttribute(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    variant_id = models.ForeignKey(PyVariant, null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('base:attribute-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("PyAttribute")
