from modeltranslation.translator import register, TranslationOptions
from .models import PyPurchaseOrderState


@register(PyPurchaseOrderState)
class PyPurchaseOrderStateTranslationOptions(TranslationOptions):
    fields = ('name',)
