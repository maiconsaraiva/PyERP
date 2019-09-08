# Librerias Django
from django import template

# Librerias de terceros
from apps.home.models import PyWebsiteConfig

register = template.Library()

@register.filter
def web_chat(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_chat
    except PyWebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_show_shop(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_shop
    except PyWebsiteConfig.DoesNotExist:
        return None



@register.filter
def web_under_construction(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).under_construction
    except PyWebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_blog(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_blog
    except PyWebsiteConfig.DoesNotExist:
        return None


@register.filter
def web_show_price(obj):
    try:
        return PyWebsiteConfig.objects.get(pk=1).show_price
    except PyWebsiteConfig.DoesNotExist:
        return None
