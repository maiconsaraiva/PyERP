# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather

CRON_CHOICE = (
    ("minutes", "Almacenable"),
    ('hours', 'Horas'),
    ('work_day', 'Días laborales'),
    ('weeks', 'Semanas'),
    ('month', 'Meses'),
)


class PyCron(PyFather):
    name = models.CharField('Nombre', max_length=40)
    active = models.BooleanField('Activo', default=False)
    interval_type = models.CharField(
        choices=CRON_CHOICE, max_length=64, default='hours')
    model_name = models.CharField('Modelo', max_length=40)
    function = models.CharField('Método', max_length=40)
    number_call = models.IntegerField('Número de llamadas', default=-1)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def get_absolute_url(self):
        return reverse('base:cron-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_on']
