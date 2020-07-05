from django.contrib import sitemaps
from django.urls import reverse
from base import views
from agenciesCZ import views

class AgenciesViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
        'pragamedica',
        ]

    def location(self, item):
        return reverse(item)
