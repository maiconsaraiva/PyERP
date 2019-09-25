# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather
from ..models import PyPartner

TYPE_CHOICE = (
    ("received", "Received"),
    ('sent', 'sent')
)


class PyEmail(PyFather):
    title = models.CharField(_("Title"), max_length=255)
    content = models.TextField(_("Content"))
    partner_id = models.ForeignKey(PyPartner, null=True, blank=True, on_delete=models.PROTECT)
    type = models.CharField(_("type"), choices=TYPE_CHOICE, max_length=64)

    def get_absolute_url(self):
        return reverse('base:email-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
