# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .father import PyFather

POSITION_CHOICE = (
    ("before", "Antes de la Cantidad"),
    ('after', 'Después de la Cantidad'),
)


class PyCurrency(PyFather):
    name = models.CharField('Nombre', max_length=3)
    alias = models.CharField('Alias', max_length=40)
    symbol = models.CharField('Símbolo', max_length=1)
    position = models.CharField(
        choices=POSITION_CHOICE, max_length=64, default='after')

    def get_absolute_url(self):
        return reverse('base:currency-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
