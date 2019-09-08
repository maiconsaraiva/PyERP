# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather


class PyPost(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.title)
