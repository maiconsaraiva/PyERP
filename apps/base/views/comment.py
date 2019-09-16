# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyComment

COMMENT_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Comment"), 'field': 'comment'},
]

COMMENT_SHORT = ['name', 'comment']


class CommentListView(LoginRequiredMixin, ListView):
    model = PyComment
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        context['title'] = 'Comments'
        context['detail_url'] = 'base:comment-detail'
        context['add_url'] = 'base:comment-add'
        context['fields'] = COMMENT_FIELDS
        return context


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = PyComment
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['update_url'] = 'base:comment-update'
        context['delete_url'] = 'base:comment-delete'
        context['fields'] = COMMENT_FIELDS
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = PyComment
    fields = COMMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Comment'
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['back_url'] = reverse('base:comments')
        return context


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = PyComment
    fields = COMMENT_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(CommentUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:comments', 'name': 'Comments'}]
        context['back_url'] = reverse('base:comment-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeleteComment(self, pk):
    comment = PyFaq.objects.get(id=pk)
    comment.delete()
    return redirect(reverse('base:comments'))
