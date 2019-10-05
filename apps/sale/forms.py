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
            'partner_id',
        ]
        labels = {
            'partner_id': 'Cliente',
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
            # 'description': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Descripción del presupuesto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
        }


# ========================================================================== #
class SaleOrderDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrderDetail
        exclude = ()
        fields = [
            # 'sale_order_id',
            'product_id',
            'description',
            'quantity',
            # 'measure_unit',
            # 'product_tax',
            'amount_untaxed',
            'discount',
            # 'amount_total',
        ]
        widgets = {
            'sale_order': forms.HiddenInput(),
            'product': autocomplete.ModelSelect2(
                url='PyProduct:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un producto ...',
                    'style': 'width: 100%',
                },
            ),
            # 'product_id': forms.Select(
            #     attrs={
            #         'class': 'form-control select2',
            #         'data-placeholder': 'Seleccione un producto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Cantidad del producto ...',
                    'style': 'width: 100%',
                },
            ),
            # 'measure_unit': autocomplete.ModelSelect2(
            #     url='measure-unit-autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un unidad ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            'tax_id': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'data-placeholder': _('Select taxes...'),
                },
            ),
            'amount_untaxed': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Precio del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descuento ...',
                    'style': 'width: 100%',
                },
            ),
            # 'amount_total': NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Sub total ...',
            #         'style': 'width: 100%',
            #     },
            # ),
        }


class BaseProductFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''


PRODUCT_FORMSET = inlineformset_factory(
    PySaleOrder, PySaleOrderDetail,
    # form=SaleOrderDetailForm,
    fields=[
        'sale_order_id',
        'product_id',
        'description',
        'quantity',
        'uom_id',
        'amount_untaxed',
        'tax_id',
        'discount',
        'amount_total',
    ],
    widgets={
        'product_id': autocomplete.ModelSelect2(
            url='PyProduct:autocomplete',
            attrs={
                'class': 'form-control',
                'data-placeholder': 'Seleccione un producto ...',
                'style': 'width: 80%',
            },
        ),
        # 'product_id': forms.Select(
        #     attrs={
        #         'class': 'form-control custom-select',
        #         'data-placeholder': 'Seleccione un producto ...',
        #         'style': 'width: 100%',
        #     },
        # ),
        'description': forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Descripción del producto ...',
                'style': 'width: 100%',
            },
        ),
        'quantity': forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-placeholder': 'Cantidad del producto ...',
                'style': 'width: 100%',
            },
        ),
        'uom_id': forms.Select(
            attrs={
                'class': 'custom-select custom-select-sm',
                'data-placeholder': 'Cantidad del producto ...',
                'style': 'width: 100%',
            },
        ),
        'amount_untaxed': forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-placeholder': 'Precio del producto ...',
                'style': 'width: 100%',
            },
        ),
        # 'tax_id': autocomplete.ModelSelect2Multiple(
        #     url='PyTax:autocomplete',
        #     attrs={
        #         'class': 'form-control  custom-select custom-select-sm',
        #         'data-placeholder': _('Select taxes...'),
        #         'style': 'padding: 0 .75rem; width: 100%',
        #     },
        # ),
        'tax_id': autocomplete.ModelSelect2Multiple(
                url='PyTax:autocomplete',
                attrs={
                    'class': 'form-control  custom-select custom-select-sm',
                    'data-placeholder': _('Select taxes...'),
                    'style': 'padding: 0 .75rem; width: 100%',
                },
            ),
        'discount': forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-placeholder': 'Descuento ...',
                'style': 'width: 100%',
            },
        ),
        'amount_total': forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm',
                'data-placeholder': 'Total ...',
                'style': 'width: 100%',
            },
        ),
    },
    formset=BaseProductFormSet,
    extra=1,
    can_delete=True
)
