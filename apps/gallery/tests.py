from django.test import TestCase
from django.urls import reverse

from .models import Post

class Test(TestCase):
    def test_latest_view_redirects(self):
        post = Post.objects.create(title='Hej',author='Jeppe',image='foo.jpg')
        response = self.client.get('/')
        self.assertRedirects(response, reverse('gallery:post', kwargs={'pk':
            post.pk}))
