from django.contrib import admin
from home.models import BlogPost, BlogComment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogComment)
