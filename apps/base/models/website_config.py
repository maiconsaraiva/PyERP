# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather


class PyWebsiteConfig(PyFather):
    show_blog = models.BooleanField(_("Show Blog"), default=False)
    show_shop = models.BooleanField(_("Show Shop"), default=False)
    show_price = models.BooleanField(_("Show price"), default=True)
    show_chat = models.BooleanField(_("Show chat"), default=False)
    under_construction = models.BooleanField(_("Under Construction"), default=False)
    user_register = models.BooleanField(_("User Register"), default=True)


    @classmethod
    def create(cls, company):
        wbaseconfig = cls(company_id=company)
        wbaseconfig.save()
        return wbaseconfig

    class Meta:
        verbose_name = _("WebsiteConfig")
        verbose_name_plural = _("PyWebsiteConfig")
