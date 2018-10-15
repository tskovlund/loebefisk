from django.test import TestCase
from django.urls import reverse

from .models import Post

class Test(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(title='Post1',author='Author1',image='post1.jpg')
        self.post2 = Post.objects.create(title='Post2',author='Author2',image='post2.jpg')

    def test_latest_view_redirects(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('gallery:post', kwargs={'pk':self.post2.pk}))
