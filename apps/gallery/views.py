from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404

import random

from .models import Post

class PostView(generic.DetailView):
    """
    A view for a single post.
    """
    model = Post
    template_name = 'gallery/post.html'

class LatestView(generic.View):
    """
    A view that shows the most recently published post.
    """
    def get_object(self):
        """
        Return the most recently published post.
        """
        return Post.get_published_posts()[0]

    def get(self, request):
        """
        Redirect to the url of the most recently published post.
        """
        return HttpResponseRedirect(self.get_object().get_absolute_url())

class RandomView(generic.View):
    """
    A view that shows the most recently published post.
    """
    def get_random_object(self):
        """
        Return the most recently published post.
        """
        published_posts = Post.get_published_posts()
        r = random.randint(0, len(published_posts)-1)
        return Post.get_published_posts()[r]

    def get(self, request):
        """
        Redirect to the url of the most recently published post.
        """
        return HttpResponseRedirect(self.get_random_object().get_absolute_url())

class PostsView(generic.ListView):
    """
    A view that shows all published posts. 
    """
    template_name = 'gallery/posts.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        """
        Return all published posts (not including those set to be
        published in the future).
        """
        return Post.get_published_posts()

class DetailView(PostView):
    def get_queryset(self):
        """
        Return all posts, excluding any posts that aren't published yet.
        """
        return Post.get_published_posts()
