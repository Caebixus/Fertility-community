from datetime import datetime
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.db import models
from ckeditor.fields import RichTextField
from .packageChoices import CATEGORY_PACKAGE
from clinic.validators import validate_file_size


class Package(models.Model):
    packageclinic = models.ForeignKey(BasicClinic, on_delete=models.CASCADE)

    package_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    package_pic_delete = models.BooleanField(default=False, blank=True, null=True)
    packagetitle = models.CharField(max_length=30, blank=True, null = True)
    packagecategory = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null=True, default=CATEGORY_PACKAGE[0][0])
    packagedesc = RichTextField(blank=True, null=True, max_length=800)
    packagecost = models.FloatField(blank=True, null=True)

    package_list_date = models.DateTimeField(default=datetime.now, blank=True)
    package_update_date = models.DateTimeField(default=datetime.now, blank=True)

    package_end_list_date = models.DateTimeField(blank=True, null=True)

    package_url = models.URLField(null=True, blank=True, max_length=500)
    package_phone = models.CharField(max_length=25, null=True, blank=True)

    is_package_active = models.BooleanField(default=False, null=True, blank=True)

    TYPE = (
        ('30 Days', '30 Days'),
        ('90 Days', '90 Days'),
        )

    package_limit_days = models.CharField(max_length=40, choices=TYPE, null = True, default='30 Days')

    def __str__(self):
        return str(self.packagetitle)




#
##
###
####
#####
######
#######
######## DEPRECIATED TEST MODELS
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
