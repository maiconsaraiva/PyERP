
# Librerias Standard
import os

# Librerias Django
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

# Librerias en carpetas locales
from ..rename_image import RenameImage
from .currency import PyCurrency
from .father import PyFather

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "logo/{id}{ext}".format(id=instance.pk, ext=ext)


class PyCompany(PyFather):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40, blank=True)

    currency_id = models.ForeignKey(PyCurrency, null=True, blank=True, on_delete=models.CASCADE)

    postal_code = models.CharField(max_length=255, blank=True)

    social_facebook = models.CharField(max_length=255, blank=True)
    social_instagram = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)
    social_youtube = models.CharField(max_length=255, blank=True)

    slogan = models.CharField('Eslogan', max_length=250, blank=True)
    logo = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='logo/default_logo.png'
    )

    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:company-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)


@receiver(pre_save, sender=PyCompany)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.logo)
        instance.logo = 'logo/default_logo.png'


@receiver(post_save, sender=PyCompany)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.logo = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.logo or instance.logo is None:
        instance.logo = 'logo/default_logo.png'
        instance.save()
