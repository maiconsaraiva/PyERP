# -*- coding: utf-8 -*-
"""
Vistas de la aplicación globales
"""
# Librerias Django
from django.shortcuts import redirect, render

# Librerias en carpetas locales
from ..forms import AvatarForm
from ..models import UserCustom
from .activate import ActivateView
from .activatelanguage import ActivateLanguageView
from .passwordchange import cambio_clave
from .passwordreset import PasswordRecoveryView
from .profile import ProfileView
from .signup import SignUpView
from .avatar import AvatarUpdateView
from .logoutmodal import LogOutModalView


ChangePasswordView = cambio_clave


# ========================================================================== #
def error_404(request, exception):
    """Gestion de errores html 404
    """

    data = {}
    return render(request, '404.html', data)


# ========================================================================== #
def error_500(request):
    """Gestion de errores html 500
    """

    data = {}
    return render(request, '500.html', data)
