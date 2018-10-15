from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import Http404

from .models import Post

class PostView(generic.DetailView):
    model = Post
    template_name = 'gallery/post.html'

class LatestView(PostView):
    def get_object(self):
        return Post.get_published_posts()[0]

class PreviousView(PostView):
    def get_object(self):
        posts = Post.get_published_posts()
        try:
            post = Post.objects.get(pk=self.kwargs['pk'])
            return posts[list(posts).index(post)+1]
        except Post.DoesNotExist:
            raise Http404("Post does not exist.")

class NextView(PostView):
    def get_object(self):
        posts = Post.get_published_posts()
        try:
            post = Post.objects.get(pk=self.kwargs['pk'])
            return posts[list(posts).index(post)-1]
        except Post.DoesNotExist:
            raise Http404("Post does not exist.")

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        """
        return the last five published images (not including those set to be
        published in the future).
        """
        return Post.get_published_posts()[:5]

class DetailView(PostView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.get_published_posts()
