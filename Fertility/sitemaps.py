from django.contrib import sitemaps
from django.urls import reverse
from base import views

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return ['index', 'about', 'ivf-country-difference', 'team', 'travelCalculator', 'contact', 'search']

    def location(self, item):
        return reverse(item)
