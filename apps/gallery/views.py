from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404

from .models import Post

class PostView(generic.DetailView):
    model = Post
    template_name = 'gallery/post.html'

class LatestView(generic.View):
    def get_object(self):
        return Post.get_published_posts()[0]

    def get(self, request):
        return HttpResponseRedirect(self.get_object().get_absolute_url())

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        """
        return all published images (not including those set to be
        published in the future).
        """
        return Post.get_published_posts()

class DetailView(PostView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.get_published_posts()
