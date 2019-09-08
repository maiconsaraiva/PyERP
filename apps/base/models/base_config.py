# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .company import PyCompany


class BaseConfig(models.Model):

    online = models.BooleanField('Online', default=False)
    main_company_id = models.ForeignKey(PyCompany, on_delete='cascade', null=True, blank=True)
    open_menu = models.BooleanField('Menu Abierto', default=True)
    load_data = models.BooleanField('Data Cargada', default=False)

    def get_absolute_url(self):
        return reverse('base:base-config', kwargs={'pk': self.pk})

    def dload_data(self):
        self.load_data = True
