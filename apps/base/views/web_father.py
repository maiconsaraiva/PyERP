from django.views.generic import ListView, DetailView
from ..models import PyWParameter, PyMeta

def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter

def _web_meta():
    cad = ''
    for meta in PyMeta.objects.all():
        cad += '<meta name="'+meta.title+'" content="'+meta.content+'">' + '\n'
    return cad


class FatherListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['meta'] = _web_meta()
        return context

    class Meta:
        abstract = True

class FatherDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['meta'] = _web_meta()
        return context

    class Meta:
        abstract = True