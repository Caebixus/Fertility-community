from django.contrib import sitemaps
from clinic.models import BasicClinic

class ClinicsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return BasicClinic.objects.filter(is_published=True)

    def location(self, item):
        return item.get_absolute_url()