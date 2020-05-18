from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class contactClinic(models.Model):
    ### Basic information
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    contactTitle = models.CharField(max_length=40)
    contactMessage = models.TextField(max_length=800, blank=True)

    def __str__(self):
        return str(self.clinicOwner)

class claimClinic(models.Model):
    ### Basic information
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    claimTitle = models.CharField(max_length=40)
    claimMessage = models.TextField(max_length=800, blank=True)
    claimUrl = models.URLField(max_length=800, blank=True)

    def __str__(self):
        return str(self.clinicOwner)

class contactWebsite(models.Model):
    ### Basic information
    contactTitle = models.CharField(max_length=40)
    contactMessage = models.TextField(max_length=800, blank=True)
    contact_email = models.EmailField(max_length=60, blank=True)
    anti_spam_challenge = models.TextField(max_length=10, blank=True)

    def __str__(self):
        return str(self.contactTitle)
