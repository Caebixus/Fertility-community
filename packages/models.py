from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.db import models
from ckeditor.fields import RichTextField
from .choices import CATEGORY_PACKAGE
from django.db.models import Q
from django.utils import timezone


class Package(models.Model):
    packageclinic = models.ForeignKey(BasicClinic, on_delete=models.CASCADE)

    packagetitle = models.CharField(max_length=30, blank=True, null = True)
    packagecategory = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    packagedesc = RichTextField(blank=True, null=True, max_length=800)
    packagecost = models.FloatField(blank=True, null=True)

    package_list_date = models.DateTimeField(default=datetime.now, blank=True)
    package_update_date = models.DateTimeField(default=datetime.now, blank=True)

    package_end_list_date = models.DateTimeField(blank=True, null=True)

    package_url = models.URLField(null=True, blank=True)
    package_phone = models.CharField(max_length=15, null=True, blank=True)

    TYPE = (
        ('30 Days', '30 Days'),
        ('90 Days', '90 Days'),
        )

    package_limit_days = models.CharField(max_length=40, choices=TYPE, null = True, default='30 Days')

    def __str__(self):
        return str(self.packagetitle)










# DEPRECIATED TEST MODELS
class Packages(models.Model):

    packageOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    packageClinic = models.ForeignKey(BasicClinic, on_delete=models.CASCADE, blank=True, null = True, related_name='packageClinic')

    packagestitle = models.CharField(max_length=30, blank=True, null = True)
    packagescategory = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    packagesdesc = RichTextField(blank=True, null=True, max_length=800)
    packagescost = models.FloatField(blank=True, null=True)

    package_list_date = models.DateTimeField(default=datetime.now, blank=True)
    package_update_date = models.DateTimeField(default=datetime.now, blank=True)
    # Možná přidat i queryemail model field?

    packageslimitnumber = models.PositiveIntegerField(null=True, blank=True, default='0')

    def __str__(self):
        return str(self.packagestitle)

class TruePackages(BasicClinic):
    Truepackagetitle = models.CharField(max_length=30, blank=True, null = True)


    def __str__(self):
        return str(self.Truepackagetitle)


class FinalPackages(BasicClinic):
    finalpackagetitle = models.CharField(max_length=30, blank=True, null = True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.finalpackagetitle)
