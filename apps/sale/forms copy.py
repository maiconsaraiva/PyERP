"""Formularios del modulo sale
"""
# Django Library
from django import forms
from django.forms.models import inlineformset_factory

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from .models import PySaleOrder, PySaleOrderDetail



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


# ========================================================================== #
class SaleOrderForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrder
        fields = [
            'partner_id',
            'description',
        ]
        labels = {
            'partner_id': 'Cliente',
            'description': 'Descripción',
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
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': 'Descripción del presupuesto ...',
                    'style': 'width: 100%',
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('product'),
                Field('description'),
                Field('quantity'),
                Field('amount_untaxed'),
                Field('discount'),
                Fieldset(
                    'Add product',
                    Formset('product')
                ),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )


# ========================================================================== #
class SaleOrderDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PySaleOrderDetail
        exclude = ()
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
            'sale_order': forms.HiddenInput(),
            # 'product': autocomplete.ModelSelect2(
            #     url='PySaleOrder:product-autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un producto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
            'product': forms.Select(
                attrs={
                    'class': 'form-control select2',
                    'data-placeholder': 'Seleccione un producto ...',
                    'style': 'width: 100%',
                },
            ),
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
            # 'product_tax': autocomplete.ModelSelect2(
            #     url='PyTax:autocomplete',
            #     attrs={
            #         'class': 'form-control',
            #         'data-placeholder': 'Seleccione un Impuesto ...',
            #         'style': 'width: 100%',
            #     },
            # ),
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


PRODUCT_FORMSET = inlineformset_factory(
    PySaleOrder, PySaleOrderDetail,
    form=SaleOrderDetailForm,
    # fields=['product', 'description'],
    extra=1,
    can_delete=True
)
