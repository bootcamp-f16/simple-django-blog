import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.test import TestCase

from .models import Post

# Create your tests here.
class PostModelTests(TestCase):
    def setUp(self):
        pass

    def test_string_representation(self):
        post = Post(title="This is my test title")
        self.assertEqual(str(post), post.title)

    def test_is_published_with_no_publish_date_set(self):
        post = Post(title="test")

        self.assertEqual(post.is_published(), False)

    def test_is_published_with_past_date_set(self):
        published_date = timezone.now() - datetime.timedelta(days=5)
        post = Post(title="Test", published_date=published_date)

        self.assertEqual(post.is_published(), True)

    def test_is_published_with_future_date(self):
        published_date = timezone.now() + datetime.timedelta(days=5)
        post = Post(title="Test", published_date=published_date)

        self.assertEqual(post.is_published(), False)

    def test_generate_slug_from_title_automatically(self):
        title = "This is a test"
        slug = slugify(title)
        post = Post(title=title)
        post.save()

        self.assertEqual(post.slug, slug)

    def test_slug_does_not_change_on_save_if_set(self):
        title = "This is a test"
        slug = slugify("something totally different")

        post = Post(title=title, slug=slug)

        post.save()

        self.assertNotEqual(post.slug, slugify(title))
        self.assertEqual(post.slug, slug)

    def test_get_absolute_url(self):
        title = "Testing my slug"
        slug = slugify(title)
        post = Post(title=title)
        post.save()

        self.assertEqual(reverse('blog:post', kwargs={'slug': slug}), post.get_absolute_url())