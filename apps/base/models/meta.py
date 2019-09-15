# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather

class PyMeta(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('base:meta-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.title)
