"""Formularios del modulo sale
"""
# Django Library
from django import forms
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete
from tempus_dominus.widgets import DatePicker, DateTimePicker, TimePicker

# Localfolder Library
from ..models import PyAccountMove, PyAccountMoveDetail


# ========================================================================== #
class AccountMoveForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyAccountMove
        fields = [
            'journal_id',
            'date_move',
            'company_move',
            'reference'
        ]
        labels = {
            'journal_id': _('Journal',),
            'date_move': _('Date'),
            'company_move': _('Company'),
            'reference': 'Reference',
        }
        widgets = {
            'journal_id': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a journal ...'),
                },
            ),
            'date_move': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                    'icons': {
                        'time': 'far fa-clock'
                    }
                },
                attrs={
                    # 'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                    # 'style': 'width: 150px',
                },
            ),
            'reference': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                    # 'style': 'width: 150px',
                },
            ),
        }


# ========================================================================== #
class CustomSelect(forms.SelectMultiple):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        options = super(CustomSelect, self).create_option(name, value, label, selected, index, subindex=None, attrs=None)
        options['attrs']['data-content'] = """<span class='badge badge-primary'>{}</span>""".format(label)
        return options


class AccountMoveDetailForm(forms.ModelForm):
    """Formulario para agregar y/o editar ordenes de compra
    """
    class Meta:
        model = PyAccountMoveDetail
        exclude = ()
        fields = [
            'account_plan_id',
            'reference_company',
            'tags',
            'debit',
            'credit',
            'date_due'
        ]
        widgets = {
            'account_plan_id': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select an account ...'),
                    # 'style': 'width: 180px',
                },
            ),
            'reference_company': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a company ...'),
                    # 'style': 'width: 180px',
                },
            ),
            'tags': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                    # 'style': 'width: 150px',
                },
            ),
            'debit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Debit'),
                    # 'style': 'width: 80px',
                },
            ),
            'credit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Credit'),
                    # 'style': 'width: 80px',
                },
            ),
            'date_due': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                    'icons': {
                        'time': 'far fa-clock'
                    }
                },
                attrs={
                    # 'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
        }


class BaseAccountMoveFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = ''

ACCOUNTING_NOTES = inlineformset_factory(
    PyAccountMove, PyAccountMoveDetail,
    form=AccountMoveDetailForm,
    formset=BaseAccountMoveFormSet,
    extra=1,
    can_delete=True
)
