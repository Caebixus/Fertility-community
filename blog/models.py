from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True)
    TAG_CHOICES = (
        ('IVF-Abroad', 'IVF-Abroad'),
        )
    tag = models.CharField(max_length=40, choices=TAG_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    blog_url = models.URLField()
    minute_read = models.IntegerField(null=True, blank=True)

class Author(models.Model):
    author = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=40)
    author_lastname = models.CharField(max_length=40)
    author_pic = models.ImageField(upload_to='authorPhotos', blank=True, null=True)
    author_small_bio = models.CharField(max_length=250)
    author_description = models.TextField()
    linkedin_url = models.URLField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    additional_url = models.URLField()
    author_page_url = models.URLField()
