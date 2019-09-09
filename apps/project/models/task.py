# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather

# Librerias en carpetas locales
from .project import PyProject

TASK_STATE = (
        ("nuevo", "Nuevo"),
        ('trabajando', 'Trabajando'),
        ('finalizado', 'Finalizado')
    )


class PyTask(PyFather):
    name = models.CharField('Nombre', max_length=80)
    note = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(PyProject, null=True, blank=True, on_delete=models.CASCADE)

    state = models.CharField(
        choices=TASK_STATE, max_length=64, default='nuevo')

    def get_absolute_url(self):
        return reverse('project:task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
