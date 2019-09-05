# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

ACCOUNT_PLAN_TYPE = (
        ("activo", "Activo"),
        ('pasivo', 'Pasivo'),
        ('patrimonio_capital', 'Patrimonio'),
        ('ingresos', 'Ingresos'),
        ('costos', 'Costos'),
        ('gastos', 'Gastos'),
    )

# Tabla de Leads
class PyAccountPlan(models.Model):
    code = models.CharField('Código', max_length=80)
    name = models.CharField('Nombre', max_length=80)
    type = models.CharField(
        choices=ACCOUNT_PLAN_TYPE, max_length=64, default='activo')
    reconcile = models.BooleanField('Conciliación', default=False)

    def get_absolute_url(self):
        return reverse('accountplan-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return + "[" + format(self.code) + "] " + format(self.name)
