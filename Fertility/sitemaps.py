from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsRegionsUS import views
from location import views

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = "https"

    def items(self):
        return [
        'index',
        'blog1',
        'blog',
        'packagesearch',
        'about',
        ]

    def location(self, item):
        return reverse(item)
