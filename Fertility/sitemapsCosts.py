from django.contrib import sitemaps
from django.urls import reverse
from base import views
from location import views

class CostsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
        'locations',
        
        'locationsUSRegions',
        'locationsUKRegions',
        'locationsCZRegions',
        'locationsSPRegions',
        'locationsINRegions',
        'locationsGRRegions',

        'locationsTexasRegions',
        ]

    def location(self, item):
        return reverse(item)
