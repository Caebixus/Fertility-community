from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Author(models.Model):
    author_name = models.CharField(max_length=40)
    author_lastname = models.CharField(max_length=40)
    author_pic = models.ImageField(upload_to='authorPhotos', blank=True, null=True)
    author_small_bio = models.CharField(max_length=250, blank=True, null=True)
    author_description = models.TextField()
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    additional_url = models.URLField(blank=True, null=True)
    author_page_url = models.URLField(blank=True, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries')
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
