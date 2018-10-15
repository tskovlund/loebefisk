from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    image = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return self.title + ' by ' + self.author
    
    @classmethod
    def get_published_posts(cls):
        return cls.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

    def is_first(self):
        posts = Post.get_published_posts()
        return posts[0] == self

    def is_last(self):
        posts = Post.get_published_posts()
        return posts[len(posts)-1] == self
