from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.db import models
from ckeditor.fields import RichTextField
from .choices import CATEGORY_PACKAGE
from django.db.models import Q

# Create your models here.

class Packages(models.Model):

    packageOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    packageClinic = models.ForeignKey(BasicClinic, on_delete=models.CASCADE, blank=True, null = True, related_name='packageClinic')
    packageClinics = models.ManyToManyField(BasicClinic, blank=True, related_name='packageClinics')

    packagestitle = models.CharField(max_length=30, blank=True, null = True)
    packagescategory = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    packagesdesc = RichTextField(blank=True, null=True, max_length=400)
    packagescost = models.FloatField(blank=True, null=True)
    # Možná přidat i queryemail model field?

    packageslimitnumber = models.PositiveIntegerField(null=True, blank=True, default='0')

    def __str__(self):
        return str(self.packagestitle)
