# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyPartner(PyFather):
    name = models.CharField('Nombre', max_length=40)
    street = models.CharField('Calle', max_length=100, blank=True)
    street_2 = models.CharField('Calle 2', max_length=100, blank=True)
    city = models.CharField('Ciudad', max_length=50, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.EmailField('Correo', max_length=40, blank=True)
    customer = models.BooleanField('Es cliente', default=True)
    provider = models.BooleanField('Es proveedor', default=True)
    for_invoice = models.BooleanField('Para Facturar', default=True)
    note = models.TextField(blank=True, null=True)

    not_email = models.BooleanField('No Email', default=False)

    created_by = models.ForeignKey(
        'base.UserCustom', related_name='pypartner_created_by',
        on_delete=models.SET_NULL, null=True)

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def get_absolute_url(self):
        return reverse('base:partner-detail', kwargs={'pk': self.pk})

    def __str__(self):
        # %s%s' % (self.rut and ('[%s] ' % self.rut) or '', self.name)
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']
