# Thirdparty Library
from modeltranslation.translator import TranslationOptions, register

# Localfolder Library
from .models import PyInvoiceType


@register(PyInvoiceType)
class PyInvoiceTypeTranslationOptions(TranslationOptions):
    fields = ('name',)
