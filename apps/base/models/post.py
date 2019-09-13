# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)

class PyPost(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    keywords = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('base:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.title)
