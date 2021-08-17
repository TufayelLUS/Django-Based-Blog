from django.db import models
import django
from datetime import datetime

# Create your models here.


class BlogPost(models.Model):
    blog_slug = models.CharField(max_length=100, default='')
    blog_title = models.CharField(max_length=100)
    blog_text = models.TextField(max_length=1024280)
    blog_owner = models.CharField(max_length=15)
    post_time = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    blog_slug = models.CharField(max_length=100, default='')
    comment_owner = models.CharField(max_length=100)
    comment_text = models.TextField(max_length=1024280)
    comment_time = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.blog_slug
