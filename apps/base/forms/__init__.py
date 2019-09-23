# -*- coding: utf-8 -*-
"""
Formularios para la app globales
"""
# Librerias Standard
import re

# Librerias Django
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import (
    EmailInput, ModelForm, PasswordInput, Select, TextInput)
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from dal import autocomplete
from tempus_dominus.widgets import DatePicker

# Librerias en carpetas locales
from ..models import PyCompany, PyCountry, PyUser


class PerfilForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    class Meta:
        model = PyUser
        fields = (
            'first_name',
            'last_name',
            # 'email_secundario',
            'celular',
            'fecha_nacimiento',
            'sexo',
        )
        labels = {
            'first_name': _('Name'),
            'last_name': _('Last Name'),
            # 'email_secundario': _('Secondary email'),
            'celular': _('Mobile Phone'),
            'fecha_nacimiento': _('Birthdate'),
            'sexo': _('Sex'),
        }
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            # 'email_secundario': TextInput(attrs={'class': 'form-control'}),
            'celular': TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': DatePicker(attrs={'class': 'form-control'}),
            'sexo': Select(attrs={'class': 'form-control select2'}),
        }

    def clean_telefono(self):
        """
        Validamos que el teléfono cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        telefono = diccionario_limpio.get('telefono')
        patron = re.compile('^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$')
        if telefono:
            if patron.match(telefono) is None:
                raise forms.ValidationError("El número de teléfono local debe\
                                                cumplir con la forma +58 (999)\
                                                999-99-99")
        return telefono

    def clean_celular(self):
        """
        Validamos que el celular cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        celular = diccionario_limpio.get('celular')
        patron = re.compile('^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$')
        if celular:
            if patron.match(celular) is None:
                raise forms.ValidationError(
                    "El número de teléfono celular debe cumplir con la forma +58 (999) 999-99-99")
        return celular


class PersonaChangeForm(UserChangeForm):
    """Para algo sera esto
    """
    class Meta(UserChangeForm.Meta):
        model = PyUser
        fields = (
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
            'first_name',
            'last_name',
        )


# ========================================================================== #
class PasswordRecoveryForm(ModelForm):
    """Para enviar el correo de recuperacion de la cuenta
    """
    class Meta():
        model = PyUser
        fields = (
            'email',
        )
        widgets = {
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': _('Email')}
            ),
        }


# ========================================================================== #
class PasswordSetForm(forms.Form):
    """Para enviar el correo de recuperacion de la cuenta
    """
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Password')}
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Retype password')}
        )
    )

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print('entre8888')
        if password1 != password2:
            raise forms.ValidationError(
                _('The two password fields didn\'t match.')
            )
        if password1 != password2:
            raise forms.ValidationError(
                _('The two password fields didn\'t match.')
            )


class PersonaCreationForm(UserCreationForm):
    """Con esta clase de formulario se renderiza la plantilla de registro de
    ususarios
    """
    class Meta(UserCreationForm.Meta):
        model = PyUser
        fields = (
            'email',
        )
        widgets = {
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': _('Email')}
            ),
        }


class AvatarForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """
    class Meta:
        model = PyUser
        fields = (
            'avatar',
        )


class InitForm(forms.ModelForm):
    """Fromulario para la inicializacion de PyERP
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Admin email')
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Admin Password')
            }
        )
    )

    class Meta:
        model = PyCompany
        fields = [
            'name',
            'country',
            'email',
            'password'
        ]
        labels = {
            'name': _('Company Name'),
            'country': _('Country'),
            'email': _('Admin user email'),
            'password': _('Password'),
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Company Name'),
                    'style': 'width: 100%',
                },
            ),
            'country': autocomplete.ModelSelect2(
                url='base:country-autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Select a country...'),
                    'style': 'width: 100%',
                },
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Admin user email'),
                    'style': 'width: 100%',
                },
            ),
        }
