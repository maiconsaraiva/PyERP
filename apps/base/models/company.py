# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .currency import PyCurrency
from .father import PyFather


class PyCompany(PyFather):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    giro = models.CharField(max_length=80, blank=True)

    currency_id = models.ForeignKey(PyCurrency, null=True, blank=True, on_delete=models.CASCADE)

    social_facebook = models.CharField(max_length=255, blank=True)
    social_instagram = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)

    slogan = models.CharField('Eslogan', max_length=250, blank=True)

    def get_absolute_url(self):
        return reverse('base:company-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
