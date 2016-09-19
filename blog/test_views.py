from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Post

# Create your tests here.
class BlogViewTests(TestCase):
    def setUp(self):
        self.index_url = reverse('blog:index')

    def test_views_index(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('blog/index.html', [template.name for template in response.templates])