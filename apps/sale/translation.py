from modeltranslation.translator import register, TranslationOptions
from .models import PySaleOrderType


@register(PySaleOrderType)
class PySaleOrderTypeTranslationOptions(TranslationOptions):
    fields = ('name',)
