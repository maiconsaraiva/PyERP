from apps.home.models import WebsiteConfig
# Librerias Django
from django import template
register = template.Library()

@register.filter
def web_chat(obj):
    return WebsiteConfig.objects.get(pk=1).show_chat


@register.filter
def web_show_shop(obj):
    return WebsiteConfig.objects.get(pk=1).show_shop


@register.filter
def web_under_construction(obj):
    return WebsiteConfig.objects.get(pk=1).under_construction

@register.filter
def web_show_blog(obj):
    return WebsiteConfig.objects.get(pk=1).show_blog


@register.filter
def web_show_price(obj):
    return WebsiteConfig.objects.get(pk=1).show_price