from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post


class PostListView(ListView):
    template_name = 'blogging/list.html'
    context_object_name = 'posts'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class PostDetailView(DetailView):
    template_name = 'blogging/detail.html'
    context_object_name = 'post'
    queryset = Post.objects.exclude(published_date__exact=None)

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get('pk')
        try:
            post = queryset.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        return post
