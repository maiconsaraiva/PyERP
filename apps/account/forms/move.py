"""Formularios del modulo sale
"""
# Django Library
from django import forms
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete
from taggit.forms import TagWidget
from tempus_dominus.widgets import DatePicker

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
            'journal_id': autocomplete.ModelSelect2(
                url='PyJournal:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a journal')
                },
            ),
            'date_move': DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                    'icons': {}
                },
                attrs={
                    # 'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'company_move': autocomplete.ModelSelect2(
                url='PyCompany:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a company'),
                    'disabled': 'true'
                },
            ),
            'reference': forms.TextInput(
                attrs={
                    'class': 'form-control',
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
            'account_plan_id': autocomplete.ModelSelect2(
                url='PyAccountPlan:autocomplete',
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select an account'),
                },
            ),
            'reference_company': autocomplete.ModelSelect2(
                url='PyCompany:autocomplete',
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Select a company'),
                },
            ),
            'tags': TagWidget(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': _('----------'),
                },
            ),
            'debit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Debit'),
                },
            ),
            'credit': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'data-placeholder': _('Credit'),
                },
            ),
            'date_due': DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                    'icons': {}
                },
                attrs={
                    'class': 'form-control form-control-sm',
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
    extra=0,
    can_delete=True
)
