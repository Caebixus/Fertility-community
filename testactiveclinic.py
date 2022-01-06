import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta

from clinic.models import BasicClinic


last_month = timezone.now() - timedelta(days=30)
last_3_months = timezone.now() - timedelta(days=90)
last_6_months = timezone.now() - timedelta(days=180)
clinics = BasicClinic.objects.filter(is_published=True, is_claimed=True)
for clinic in clinics:
    if clinic.clinicOwner.last_login > last_month:
        clinic.active_30 = True
        clinic.save()
    else:
        clinic.active_30 = False
        clinic.save()
    if clinic.clinicOwner.last_login > last_3_months:
        clinic.active_90 = True
        clinic.save()
    else:
        clinic.active_90 = False
        clinic.save()
    if clinic.clinicOwner.last_login > last_6_months:
        clinic.active_180 = True
        clinic.save()
    else:
        clinic.active_180 = False
        clinic.save()