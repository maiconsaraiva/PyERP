from modeltranslation.translator import register, TranslationOptions
from .models import PyInvoiceType


@register(PyInvoiceType)
class PyInvoiceTypeTranslationOptions(TranslationOptions):
    fields = ('name',)
