from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.test import TestCase

from .models import Post

# Create your tests here.
class BlogViewTests(TestCase):
    def setUp(self):
        self.index_url = reverse('blog:index')
        self.post_title = "Post title"
        self.post = Post(title=slugify(self.post_title))
        self.post.save()

    def test_views_index(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('posts' in response.context)
        self.assertIn('blog/index.html', [template.name for template in response.templates])

    def test_views_post(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.post, response.context['post'])
        self.assertIn('blog/post.html', [template.name for template in response.templates])
