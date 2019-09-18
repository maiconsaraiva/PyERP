# Librerias Django
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather

ALPHANUMERIC = RegexValidator(
    r'^[0-9a-z]*$',
    _('Only lowercase alphanumeric characters are allowed.')
)


class PyWParameter(PyFather):
    name = models.CharField(
        _('Name'),
        max_length=100,
        validators=[ALPHANUMERIC],
        unique=True
        )
    value = models.CharField(_('Value'), max_length=255)


    def get_absolute_url(self):
        return reverse('base:wparameter-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return format(self.name)
