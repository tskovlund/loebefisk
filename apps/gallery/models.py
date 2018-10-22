from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce.models import HTMLField

class Post(models.Model):
    """
    A post with a title, an author, a published date and an image.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    image = models.ImageField(null=True, blank=True, upload_to='images/%Y/%m/%d/')
    text = HTMLField(blank=True) 

    def __str__(self):
        return self.title + ' by ' + self.author
    
    @classmethod
    def get_published_posts(cls):
        """
        Return a QuerySet of all published posts.
        """
        return cls.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

    def get_absolute_url(self):
        """
        Return the absolute url of this post.
        """
        return reverse('gallery:post', kwargs={'pk': self.pk})

    def get_previous(self):
        """
        Return the post published right before this post. If no such post
        exists, None is returned.
        """
        try:
            return Post.get_published_posts().filter(pub_date__lt=self.pub_date).order_by('-pub_date')[0]
        except IndexError:
            return None

    def get_next(self):
        """
        Return the post published right after this post. If no such post
        exists, None is returned.
        """
        try:
            return Post.get_published_posts().filter(pub_date__gt=self.pub_date).order_by('pub_date')[0]
        except IndexError:
            return None

    def is_first(self):
        posts = Post.get_published_posts()
        return posts[0] == self

    def is_last(self):
        posts = Post.get_published_posts()
        return posts[len(posts)-1] == self
