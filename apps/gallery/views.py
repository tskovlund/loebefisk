from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Post

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        """
        Return the last five published images (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class PostView(generic.DetailView):
    model = Post
    template_name = 'gallery/post.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())
