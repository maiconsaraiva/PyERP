# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather
from .product_category_uom import PyProductCategoryUOM

TYPE_CHOICE = (
    ("bigger", "Bigger"),
    ('reference', 'Reference'),
    ('smaller', 'Smaller'),
)


class PyUom(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    ratio = models.DecimalField(_("Ratio"), max_digits=10, decimal_places=2, default=1)
    rouding = models.DecimalField(_("Ratio"), max_digits=10, decimal_places=2, default=0.01)
    type = models.CharField(_("type"), choices=TYPE_CHOICE, max_length=64, default='consu')
    category_id = models.ForeignKey(PyProductCategoryUOM, null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('base:uom-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
