from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Post

class GalleryTest(TestCase):
    def setUp(self):
        self.published_posts = []
        self.published_posts.append(Post.objects.create(title='Post1',author='Author1',image='post1.jpg'))
        self.published_posts.append(Post.objects.create(title='Post2',author='Author2',image='post2.jpg'))
        
        self.unpublished_posts = []
        self.unpublished_posts.append(Post.objects.create(
            title='UPost1',
            author='UAuthor1',
            image='upost1.jpg',
            pub_date=timezone.now()+datetime.timedelta(30),
        ))

    # MODELS
 
    # Post
    def test_published_posts_len(self):
        published_posts = Post.get_published_posts()
        self.assertEqual(len(published_posts), len(self.published_posts))

    def test_published_posts_first_element(self):
        published_posts_list = list(Post.get_published_posts())
        self.assertEqual(published_posts_list[-1], self.published_posts[0])

    def test_get_absolute_url(self):
        post_url = self.published_posts[0].get_absolute_url()
        self.assertEqual(post_url, '/1/')

    def test_get_previous(self):
        self.assertEqual(self.published_posts[0],
                self.published_posts[1].get_previous())

    def test_get_previous_first_none(self):
        self.assertIsNone(self.published_posts[0].get_previous())

    def test_get_next(self):
        self.assertEqual(self.published_posts[1],
                self.published_posts[0].get_next())

    def test_get_next_last_none(self):
        self.assertIsNone(self.published_posts[-1].get_next())

    def test_is_first_positive(self):
        self.assertTrue(self.published_posts[-1].is_first())

    def test_is_first_negative(self):
        self.assertFalse(self.published_posts[0].is_first())

    def test_is_last_positive(self):
        self.assertTrue(self.published_posts[0].is_last())

    def test_is_last_negative(self):
        self.assertFalse(self.published_posts[-1].is_last())


    # VIEWS

    # LatestView
    def test_latest_view_redirects(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('gallery:post',
            kwargs={'pk':self.published_posts[-1].pk}))

    # IndexView
    def test_posts_view(self):
        response = self.client.get('/posts/')
        for p in self.published_posts:
            self.assertContains(response,p.pk) 
        for p in self.unpublished_posts:
            self.assertNotContains(response,p.pk)

    # DetailView
    def test_detail_view_positive(self):
        pk = self.published_posts[0].pk
        response = self.client.get('/%d/'%pk)
        self.assertContains(response, pk)

    def test_detail_view_negative(self):
        pk1 = self.published_posts[0].pk
        title2 = self.published_posts[1].title  
        response = self.client.get('/%d/'%pk1)
        self.assertNotContains(response, title2)

    def test_detail_404(self):
        latest_pk = self.published_posts[-1].pk
        response = self.client.get('/%d/'%(latest_pk+1))
        self.assertEqual(response.status_code, 404)
