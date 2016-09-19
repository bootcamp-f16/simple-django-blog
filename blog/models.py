from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    published_date = models.DateTimeField(null=True, blank=True)

    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_published(self):
        return self.published_date is not None and self.published_date < timezone.now()

    is_published.boolean = True
    is_published.short_description = 'Published?'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})