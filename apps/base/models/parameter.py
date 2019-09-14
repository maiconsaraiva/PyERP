# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyParameter(PyFather):
    name = models.CharField('Nombre', max_length=40)
    value = models.CharField('Nombre', max_length=40)


    def get_absolute_url(self):
        return reverse('base:parameter-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return format(self.name)
