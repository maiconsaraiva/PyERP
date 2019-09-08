# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..submodels.post import PyPost

POST_FIELDS = [
            {'string': 'Título', 'field': 'title'},
            {'string': 'Creado en', 'field': 'created_on'},
        ]

POST_FIELDS_SHORT = ['title','content']

class PostListView(ListView):
    model = PyPost
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = 'Entradas'
        context['detail_url'] = 'base:post-detail'
        context['add_url'] = 'base:post-add'
        context['fields'] = POST_FIELDS
        return context

class PostDetailView(DetailView):
    model = PyPost
    template_name = 'base/detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:post', 'name': 'Entradas'}]
        context['update_url'] = 'base:post-update'
        context['delete_url'] = 'base:post-delete'
        context['fields'] = POST_FIELDS
        return context

class PostCreateView(CreateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Post'
        context['breadcrumbs'] = [{'url': 'base:post', 'name': 'Entrada'}]
        context['back_url'] = reverse('base:post')
        return context

class PostUpdateView(UpdateView):
    model = PyPost
    fields = POST_FIELDS_SHORT
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        context['breadcrumbs'] = [{'url': 'base:post', 'name': 'Entrada'}]
        context['back_url'] = reverse('base:post-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeletePost(self, pk):
    post = PyPost.objects.get(id=pk)
    post.delete()
    return redirect(reverse('post'))
