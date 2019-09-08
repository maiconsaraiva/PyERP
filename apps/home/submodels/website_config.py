# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather


class WebsiteConfig(PyFather):
    show_blog = models.BooleanField(_("Show Blog"), default=False)
    show_shop = models.BooleanField(_("Show Shop"), default=False)
    show_price = models.BooleanField(_("Show price"), default=True)
    show_chat = models.BooleanField(_("Show chat"), default=False)
    under_construction = models.BooleanField(_("Under Construction"), default=False)


    def get_absolute_url(self):
        return reverse('base:website-config', kwargs={'pk': self.pk})
