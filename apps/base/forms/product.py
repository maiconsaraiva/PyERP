# -*- coding: utf-8 -*-
"""
Formularios
"""
# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models.product import PyProduct


class ProductForm(forms.ModelForm):
    """Fromulario para los productos
    """

    class Meta:
        model = PyProduct
        fields = [
            'name',
            'uom_id',
            'category_id',
            'tax',
            'web_category_id',
            'brand_id',
            'code',
            'bar_code',
            'price',
            'cost',
            'type',
            'web_active',
            'pos_active',
            'youtube_video',
            'img',
            'description',
            'features',
        ]
        widgets = {
            'tax': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'data-placeholder': _('Select taxes...'),
                    'style': 'padding: 0 .75rem',
                },
            ),
        }
