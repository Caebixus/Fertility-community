from django.contrib import sitemaps
from django.urls import reverse
from clinic.models import BasicClinic

class ClinicsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return BasicClinic.objects.filter(is_published=True)
