from django.db import models
from django.contrib.auth.models import User
from clinic.validators import validate_file_size
from datetime import datetime
from django.urls import reverse

from blog.models import Blog, BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity


class Coaches(models.Model):
    coach_user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_profile_photo = models.ImageField(upload_to='fertility_coach', validators=[validate_file_size])
    coach_profile_photo_delete = models.BooleanField(default=False, blank=True, null=True)

    coach_category = models.CharField(max_length=256, blank=True, null=True)

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
    coach_social_website = models.URLField(blank=True, null=True)

    job_gynecologist = models.BooleanField(default=False)
    job_obstetrician = models.BooleanField(default=False)
    job_reproductive_immunologist = models.BooleanField(default=False)
    job_reproductive_surgeon = models.BooleanField(default=False)
    job_andrologist = models.BooleanField(default=False)
    job_reproductive_endocrinologist = models.BooleanField(default=False)
    job_fertility_specialist = models.BooleanField(default=False)
    job_fertility_coach = models.BooleanField(default=False)

    coach_preferred_client_country = models.CharField(max_length=256, blank=True, null=True)
    coach_preferred_client_city = models.CharField(max_length=256, blank=True, null=True)

    coach_preferred_languages = models.CharField(max_length=256, blank=True, null=True)

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
        return reverse('coaches:fertility-coach-detail', kwargs={'pk': self.id, 'slug': self.coach_username})

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


class SnippetNew(models.Model):
    snippet_owner = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='type_of_jobs')
    snippet_blog_relationship = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='snippet_blog_conn')
    text = models.TextField(blank=True, null=True)

    STATUS = (
        ('wait for review', 'wait for review'),
        ('is published', 'is published'),
        ('is not approved', 'is not approved'),
        )
    status = models.CharField(max_length=40, choices=STATUS, null=True, default='wait for review')