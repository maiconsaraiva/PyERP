"""Sub Vista logout modaldel módulo erp
"""
# Librerias Django
from django.views.generic import TemplateView


# ========================================================================== #
class LogOutModalView(TemplateView):
    """Lista de las ordenes de venta
    """
    template_name = 'usercusto/logoutmodal.html'
