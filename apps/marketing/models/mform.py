# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather

# Librerias en carpetas locales
from .campaign import PyCampaign


class PyMform(PyFather):
    name = models.CharField('Nombre', max_length=255)
    campaign_id = models.ForeignKey(PyCampaign, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('mform-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
