from datetime import datetime
from django.db import models
from django.utils.text import slugify
from clinic.validators import validate_file_size

class Author(models.Model):
    author_name = models.CharField(max_length=40)
    author_lastname = models.CharField(max_length=40)
    author_pic = models.ImageField(upload_to='authorPhotos', blank=True, null=True, validators=[validate_file_size])
    author_small_bio = models.CharField(max_length=250, blank=True, null=True)
    author_description = models.TextField()
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    additional_url = models.URLField(blank=True, null=True)
    author_page_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.author_name} {self.author_lastname}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries')
    description = models.TextField()
    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])
    TAG_CHOICES = (
        ('IVF-Abroad', 'IVF-Abroad'),
        ('IVF Packages', 'IVF Packages'),
        ('IVF Costs', 'IVF Costs'),
        ('Educational', 'Educational'),
        ('Informational&Supportive', 'Informational&Supportive'),
        ('Research', 'Research'),
        )
    tag = models.CharField(max_length=40, choices=TAG_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)
    blog_url = models.URLField()
    minute_read = models.IntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True, default=2022)

    def __str__(self):
        return self.title

class BestClinicArticleCountry(models.Model):
    title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=155, blank=True, null=True,)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries_best_clinic_article_country')
    description = models.TextField(max_length=1000, blank=True, null=True)
    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])

    year = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    slug = models.SlugField(max_length=100, null=True)

    minute_read = models.IntegerField(null=True, blank=True)
    best_article_country_noindex_sitemap_boolean = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BestClinicArticleState(models.Model):
    title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=155, blank=True, null=True,)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries_best_clinic_article_state')
    description = models.TextField(max_length=1000, blank=True, null=True)
    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])

    year = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    slug = models.SlugField(max_length=100, null=True)

    minute_read = models.IntegerField(null=True, blank=True)
    best_article_state_noindex_sitemap_boolean = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BestClinicArticleCity(models.Model):
    title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=155, blank=True, null=True,)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries_best_clinic_article_city')
    description = models.TextField(max_length=1000, blank=True, null=True)
    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])

    year = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    slug = models.SlugField(max_length=100, null=True)

    minute_read = models.IntegerField(null=True, blank=True)
    best_article_city_noindex_sitemap_boolean = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
