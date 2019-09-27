# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyMessage(PyFather):
    message = models.TextField(_("Note"))
    user_id = models.ForeignKey('base.PyUser', null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('base:message-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("PyMessage")
