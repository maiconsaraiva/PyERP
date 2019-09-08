# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather


class PyWebPaymentMethod(PyFather):
    name = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('web-payment-method-detail', kwargs={'pk': self.pk})

    def __repr__(self):
        return self.name
