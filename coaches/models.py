from django.db import models
from django.contrib.auth.models import User
from clinic.validators import validate_file_size
from datetime import datetime
from django.urls import reverse

from blog.models import Blog, BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity, FAQBlog, SimpleBlog


class Coaches(models.Model):
    coach_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    coach_profile_photo = models.ImageField(upload_to='fertility_coach', validators=[validate_file_size], blank=True, null=True)
    coach_profile_photo_delete = models.BooleanField(default=False, blank=True, null=True)

    blog_review = models.ManyToManyField(Blog, related_name='blog_reviewed_by', blank=True)
    blog_best_country_review = models.ManyToManyField(BestClinicArticleCountry, related_name='country_reviewed_by', blank=True)
    blog_best_city_review = models.ManyToManyField(BestClinicArticleCity, related_name='city_reviewed_by', blank=True)
    blog_best_state_review = models.ManyToManyField(BestClinicArticleState, related_name='state_reviewed_by', blank=True)
    blog_faq_review = models.ManyToManyField(FAQBlog, related_name='blog_faq_reviewed_by', blank=True)

    coach_full_name = models.CharField(max_length=40)
    coach_username = models.SlugField(max_length=25, help_text='Use as slug in URL')
    coach_bio = models.TextField(blank=True, null=True)

    coach_contact_email = models.EmailField(max_length=256, blank=True, null=True)
    coach_phone = models.CharField(max_length=100, blank=True, null=True)

    coach_social_instagram = models.URLField(blank=True, null=True)
    coach_social_facebook = models.URLField(blank=True, null=True)
    coach_social_linkedin = models.URLField(blank=True, null=True)
    coach_social_pinterest = models.URLField(blank=True, null=True)
    coach_social_twitter = models.URLField(blank=True, null=True)
    coach_social_youtube = models.URLField(blank=True, null=True)
    coach_social_website = models.URLField(blank=True, null=True)

    coach_preferred_client_country = models.CharField(max_length=256, blank=True, null=True)
    coach_preferred_client_city = models.CharField(max_length=256, blank=True, null=True)

    #PREMIUM
    coach_education = models.TextField(blank=True, null=True)
    coach_specialization = models.TextField(blank=True, null=True)
    coach_certification = models.TextField(blank=True, null=True)
    coach_other = models.TextField(blank=True, null=True)

    #INTERN
    coach_is_published = models.BooleanField(default=False)
    coach_is_not_approved = models.BooleanField(default=False)
    coach_is_premium = models.BooleanField(default=False)

    coach_created = models.DateTimeField(default=datetime.now, blank=True)
    coach_updated = models.DateTimeField(default=datetime.now, blank=True)
    coach_subscription_update = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_coach_url(self):
        return reverse('coach:coach-detail', kwargs={'pk': self.id, 'slug': self.coach_username})

    def __str__(self):
        return self.coach_full_name


class TypeJobs(models.Model):
    coaches_relationship = models.ManyToManyField('Coaches', related_name='jobs', blank=True)
    type_of_job = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.type_of_job

class PreferredLanguage(models.Model):
    coaches_relationship = models.ManyToManyField('Coaches', related_name='languages', blank=True)
    preferred_language = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.preferred_language


class PreferredCountry(models.Model):
    coaches_relationship = models.ManyToManyField('Coaches', related_name='countries', blank=True)
    preferred_country = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.preferred_country


class Snippet(models.Model):
    owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='snippet_owner')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_blog')
    text = models.TextField(blank=True, null=True)
    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')

    def __str__(self):
        return self.blog.title


class SnippetCity(models.Model):
    owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='snippet_city_owner')
    blog = models.ForeignKey(BestClinicArticleCity, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_city_blog')
    text = models.TextField(blank=True, null=True)
    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')

    def __str__(self):
        return self.blog.title


class SnippetState(models.Model):
    owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='snippet_state_owner')
    blog = models.ForeignKey(BestClinicArticleState, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_state_blog')
    text = models.TextField(blank=True, null=True)
    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')

    def __str__(self):
        return self.blog.title


class SnippetCountry(models.Model):
    owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='snippet_country_owner')
    blog = models.ForeignKey(BestClinicArticleCountry, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_country_blog')
    text = models.TextField(blank=True, null=True)
    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')

    def __str__(self):
        return self.blog.title


class SnippetSimpleBlog(models.Model):
    owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='snippet_simple_blog_owner')
    blog = models.ForeignKey(SimpleBlog, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_simple_blog')
    text = models.TextField(blank=True, null=True)
    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')

    def __str__(self):
        return self.blog.title