from django.contrib import admin
from blog_apps.models import Post
from blog_apps.models import Commentary

# Register your models here.

admin.site.register(Post)
admin.site.register(Commentary)