# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

STATE = (
        ("draft", "Borrador"),
        ('posted', 'Validado'),
    )

# Tabla de Leads
class PyAccountMove(models.Model):
    code = models.CharField('Código', max_length=80)
    name = models.CharField('Nombre', max_length=80)
    state = models.CharField(
        choices=STATE, max_length=64, default='draft')

    def get_absolute_url(self):
        return reverse('account-move-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return + "[" + format(self.code) + "] " + format(self.name)
