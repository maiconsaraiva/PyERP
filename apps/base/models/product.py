# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather
from .product_category import PyProductCategory
from .product_webcategory import PyProductWebCategory

PRODUCT_CHOICE = (
    ("product", "Almacenable"),
    ('consu', 'Consumible'),
    ('service', 'Servicio')
)


class PyProduct(PyFather):
    name = models.CharField(_("Name"), max_length=80)
    code = models.CharField(_("Code"), max_length=80, blank=True)
    bar_code = models.CharField(_("Bar Code"), max_length=80, blank=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, default=1)
    cost = models.DecimalField(_("cost"), max_digits=10, decimal_places=2, default=0)
    category_id = models.ForeignKey(PyProductCategory, null=True, blank=True, on_delete=models.CASCADE)
    web_category_id = models.ForeignKey(PyProductWebCategory, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(_("description"), blank=True, null=True)
    img = models.ImageField(_("image"), default="default.png")

    web_active = models.BooleanField('Web', default=False)

    type = models.CharField(_("type"), choices=PRODUCT_CHOICE, max_length=64, default='consu')

    def get_absolute_url(self):
        return reverse('base:product-detail', kwargs={'pk': self.pk})

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return format(self.name)

    class Meta:
        ordering = ['created_on']
