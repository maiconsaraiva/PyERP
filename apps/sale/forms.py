"""Formularios del modulo sale
"""
# Django Library
from django import forms
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from .models import PySaleOrder, PySaleOrderDetail


# ========================================================================== #
class SaleOrderForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrder
        fields = [
            'date_order',
            'partner_id',
            'note'
        ]
        labels = {
            'partner_id': _('Client',),
            'note': _('Note'),
            'date_order': _('Date')
            # 'description': 'Descripción',
        }
        widgets = {
            'partner_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un cliente ...',
                    'style': 'width: 100%',
                },
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descripción del presupuesto ...',
                    'style': 'width: 100%',
                },
            ),
        }


# ========================================================================== #
class CustomSelect(forms.SelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        options = super(CustomSelect, self).create_option(name, value, label, selected, index, subindex=None, attrs=None)
        options['attrs']['data-content'] = """<span class='badge badge-primary'>{}</span>""".format(label)
        return options


class SaleOrderDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrderDetail
        exclude = ()
        fields = [
            'product_id',
            'description',
            'quantity',
            'uom_id',
            'price',
            'discount',
            'tax_id',
            'amount_total',
        ]
        widgets = {
            'product_id': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a product ...'),
                    # 'style': 'width: 180px',
                },
            ),
            # 'product_id': autocomplete.ModelSelect2(
            #     url='PyProduct:autocomplete',
            #     attrs={
            #         'class': 'form-control form-control-sm',
            #         'data-placeholder': _('Select a product ...'),
            #         'style': 'width: 180px',
            #     },
            # ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                    # 'style': 'width: 150px',
                },
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Product quantity ...'),
                    # 'style': 'width: 80px',
                },
            ),
            'uom_id': forms.Select(
                attrs={
                    'class': 'custom-select custom-select-sm',
                    'data-placeholder': _('Unit measurement ...'),
                    # 'style': 'width: 80px',
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm text-right',
                    'data-placeholder': 'Precio del producto ...',
                    # 'style': 'width: 80px',
                    'value': 0,
                },
            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm text-right',
                    'data-placeholder': 'Descuento ...',
                    # 'style': 'width: 80px',
                },
            ),
            'tax_id': CustomSelect(
                attrs={
                    'class': 'selectpicker',
                    'data-placeholder': _('Select taxes...'),
                    # 'style': 'width: 150px',
                },
            ),
            # 'tax_id': autocomplete.ModelSelect2Multiple(
            #     url='PyTax:autocomplete',
            #     attrs={
            #         'class': 'form-control  custom-select custom-select-sm',
            #         'data-placeholder': _('Select taxes...'),
            #         'style': 'width: 280px',
            #     },
            # ),
            'amount_total': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm text-right',
                    'data-placeholder': 'Total ...',
                    # 'style': 'width: 80px',
                    'readonly': True,
                },
            ),
        }


class BaseProductFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''

PRODUCT_FORMSET = inlineformset_factory(
    PySaleOrder, PySaleOrderDetail,
    form=SaleOrderDetailForm,
    formset=BaseProductFormSet,
    extra=1,
    can_delete=True
)
