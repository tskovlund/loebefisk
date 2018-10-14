from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return self.title + ' by ' + self.author
