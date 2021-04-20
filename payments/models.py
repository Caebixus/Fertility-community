from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from clinic.models import BasicClinic

# Create your models here.

class Customer(models.Model):
    customerClinic = models.OneToOneField(BasicClinic, on_delete=models.CASCADE) # Nebo ForeignKey když bude customer mít několik klinik a bude chtít u všech stejný Billing address?

    stripeid = models.CharField(max_length=255, null=True, blank=True)
    stripe_subscription_id = models.CharField(max_length=255, null=True, blank=True)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
