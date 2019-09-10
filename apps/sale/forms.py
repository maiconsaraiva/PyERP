"""Formularios del modulo sale
"""
# Librerias Django
from django.forms import HiddenInput, ModelForm, NumberInput, TextInput

# Librerias de terceros
from dal import autocomplete

# Librerias en carpetas locales
from .models import PySaleOrder, PySaleOrderDetail


# ========================================================================== #
class SaleOrderForm(ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrder
        fields = [
            'name',
            'partner_id',
            'description',
        ]
        labels = {
            'name': 'Nombre',
            'partner_id': 'Cliente',
            'description': 'Descripción',
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Nobre del presupuesto ...',
                    'style': 'width: 100%',
                },
            ),
            'partner_id': autocomplete.ModelSelect2(
                url='base:partners-autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un cliente ...',
                    'style': 'width: 100%',
                },
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descripción del presupuesto ...',
                    'style': 'width: 100%',
                },
            ),
        }


# ========================================================================== #
class SaleOrderDetailForm(ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrderDetail
        fields = [
            'sale_order',
            'product',
            'description',
            'quantity',
            # 'measure_unit',
            # 'product_tax',
            'amount_untaxed',
            'discount',
            # 'amount_total',
        ]
        labels = {
            'product': 'Producto',
            'description': 'Descripción',
            'quantity': 'Cantidad',
            # 'measure_unit': 'Unidad',
            # 'product_tax': 'Impuesto',
            'amount_untaxed': 'Precio',
            'discount': 'Descuento',
            # 'amount_total': 'Sub total',
        }
        widgets = {
            'sale_order': HiddenInput(),
            'product': autocomplete.ModelSelect2(
                url='sale:product-autocomplete',
                forward=('sale_order',),
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Seleccione un producto ...',
                    'style': 'width: 100%',
                },
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'quantity': NumberInput(
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
            # 'product_tax': autocomplete.ModelSelect2(
            #     url='product-tax-autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un Impuesto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            'amount_untaxed': NumberInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Precio del producto ...',
                    'style': 'width: 100%',
                },
            ),
            'discount': NumberInput(
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
