import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from django.utils.text import slugify
from clinic.models import BasicClinic

clinic = BasicClinic.objects.all()

for clinics in clinic:
    clinics.slug = slugify(clinics.clinicName, allow_unicode=True)
    clinics.save()