from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'published_date', 'is_published', )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)