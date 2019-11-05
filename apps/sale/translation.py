from modeltranslation.translator import register, TranslationOptions
from .models import PySaleOrderState


@register(PySaleOrderState)
class PySaleOrderStateTranslationOptions(TranslationOptions):
    fields = ('name',)
