from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
import clinic

from clinic.validators import validate_file_size

TAG_CHOICES = (
    ('IVF-Abroad', 'IVF-Abroad'),
    ('IVF Packages', 'IVF Packages'),
    ('IVF Costs', 'IVF Costs'),
    ('Educational', 'Educational'),
    ('Informational&Supportive', 'Informational&Supportive'),
    ('Research', 'Research'),
)


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
    tag = models.CharField(max_length=40, choices=TAG_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)
    blog_url = models.URLField()
    minute_read = models.IntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True, default=2022)

    def __str__(self):
        return self.title


class ModularBestClinics(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='author_modular_article')

    #relationship_country = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='relationship_with_best_country_article')
    #relationship_state = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='relationship_with_best_state_article')
    #relationship_city = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='relationship_with_best_city_article')

    country = models.CharField(max_length=100, blank=True, null=True)#aby se správně vyhledali kliniky
    state = models.CharField(max_length=100, blank=True, null=True)#aby se správně vyhledali kliniky ze regions
    city = models.CharField(max_length=100, blank=True, null=True)#aby se správně vyhledali kliniky

    description = models.CharField(max_length=150, blank=True, null=True)
    keywords = models.CharField(max_length=150, blank=True, null=True)

    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])

    link_fertility_clinics = models.CharField(max_length=150, blank=True, null=True)

    created_at = models.DateTimeField(default=now)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    modular_slug = models.SlugField(max_length=100, null=True)
    minute_read = models.IntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True, default=2022)
    active = models.BooleanField(default=False, blank=True, null=True)

    content = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.modular_slug:
            self.modular_slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ModularDetailView', kwargs={'modular_slug': self.modular_slug})

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

    google_reviews_section = models.ForeignKey("clinic.BasicClinic", on_delete=models.PROTECT, blank=True, null=True, related_name='best_clinic_article_city_reviews_section')
    pricing_section = models.ForeignKey("clinic.BasicClinic", on_delete=models.PROTECT, blank=True, null=True, related_name='best_clinic_article_city_pricing_section')
    distance_section = models.ForeignKey("clinic.BasicClinic", on_delete=models.PROTECT, blank=True, null=True, related_name='best_clinic_article_city_distance_section')
    accommodation_section = models.ForeignKey("clinic.BasicClinic", on_delete=models.PROTECT, blank=True, null=True, related_name='best_clinic_article_city_accommodation_section')
    packages_section = models.ForeignKey("clinic.BasicClinic", on_delete=models.PROTECT, blank=True, null=True, related_name='best_clinic_article_city_packages_section')

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


class SimpleBlog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries_simple_article')

    description = models.CharField(max_length=150)
    keywords = models.CharField(max_length=150, blank=True, null=True)

    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])
    tag = models.CharField(max_length=40, choices=TAG_CHOICES, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    simple_slug = models.SlugField(max_length=100, null=True)
    minute_read = models.IntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True, default=2022)
    active = models.BooleanField(default=False, blank=True, null=True)

    introduction = RichTextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.simple_slug:
            self.simple_slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('SimpleDetailView', kwargs={'simple_slug': self.simple_slug})

    def __str__(self):
        return self.title


class FAQBlog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True, related_name='entries_faq_article')

    description = models.CharField(max_length=150)
    keywords = models.CharField(max_length=150, blank=True, null=True)

    pic_blog = models.ImageField(upload_to='blogPhotos', blank=True, null=True, validators=[validate_file_size])

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=datetime.now, blank=True)

    slug = models.SlugField(max_length=100, null=True)
    minute_read = models.IntegerField(null=True, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True, default=2022)
    active = models.BooleanField(default=False, blank=True, null=True)

    content = RichTextField(blank=True, null=True)

    faq_simple_blog = models.ForeignKey(SimpleBlog, on_delete=models.PROTECT, blank=True, null=True, related_name='faq_simple_blog_reverse')
    faq_question = models.CharField(max_length=200, blank=True, null=True)
    faq_answer = RichTextField(blank=True, null=True)

    faq_old_blog = models.ForeignKey(Blog, on_delete=models.PROTECT, blank=True, null=True, related_name='faq_old_blog_reverse')
    faq_old_blog_question = models.CharField(max_length=200, blank=True, null=True)
    faq_old_blog_answer = RichTextField(blank=True, null=True)

    faq_bestclinicarticlecity = models.ForeignKey(BestClinicArticleCity, on_delete=models.PROTECT, blank=True, null=True, related_name='faq_bestclinicarticlecity_reverse')
    faq_bestclinicarticlecity_question = models.CharField(max_length=200, blank=True, null=True)
    faq_bestclinicarticlecity_answer = RichTextField(blank=True, null=True)

    faq_bestclinicarticlecountry = models.ForeignKey(BestClinicArticleCountry, on_delete=models.PROTECT, blank=True, null=True, related_name='faq_bestclinicarticlecountry_reverse')
    faq_bestclinicarticlecountry_question = models.CharField(max_length=200, blank=True, null=True)
    faq_bestclinicarticlecountry_answer = RichTextField(blank=True, null=True)

    faq_best_clinic_article_state = models.ForeignKey(ModularBestClinics, on_delete=models.PROTECT, blank=True, null=True, related_name='faq_modular_best_clinics_reverse')
    faq_best_clinic_article_state_question = models.CharField(max_length=200, blank=True, null=True)
    faq_best_clinic_article_state_answer = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FaqDetailView', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
