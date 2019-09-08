# Librerias Django
from django import template

# Librerias de terceros
from apps.home.models import WebsiteConfig

register = template.Library()

@register.filter
def web_chat(obj):
    try:
        return WebsiteConfig.objects.get(pk=1).show_chat
    except WebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_show_shop(obj):
    try:
        return WebsiteConfig.objects.get(pk=1).show_shop
    except WebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_under_construction(obj):
    try:
        return WebsiteConfig.objects.get(pk=1).under_construction
    except WebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_blog(obj):
    try:
        return WebsiteConfig.objects.get(pk=1).show_blog
    except WebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_price(obj):
    try:
        return WebsiteConfig.objects.get(pk=1).show_price
    except WebsiteConfig.DoesNotExist:
        return None
