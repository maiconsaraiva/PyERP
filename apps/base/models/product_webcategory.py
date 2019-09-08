# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .father import PyFather


class PyProductWebCategory(PyFather):
    name = models.CharField(max_length=40)

    parent_id = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '%s%s' % (self.parent_id and ('[%s] ' % self.parent_id) or '', self.name)

    def get_absolute_url(self):
        return reverse('base:product-webcategory-detail', kwargs={'pk': self.pk})
