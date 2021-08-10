from django.db import models
from datetime import datetime

# Create your models here.


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_text = models.TextField(max_length=10000)
    blog_owner = models.CharField(max_length=15)
    post_time = models.DateField(default=datetime.today())

    def __str__(self):
        return self.blog_title
