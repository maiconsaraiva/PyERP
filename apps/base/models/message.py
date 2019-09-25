# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather
from ..models import PyUser

class PyMessage(PyFather):
    message = models.TextField(_("Note"))
    user_id = models.ForeignKey(PyUser, null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('base:message-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
