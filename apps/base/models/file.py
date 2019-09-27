# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyFile(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    note = models.TextField(_("Note"))
    user_id = models.ForeignKey(
        'base.PyUser',
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('base:file-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")
