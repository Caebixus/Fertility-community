from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsCities import views
from location import views

class CitiesViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return [
        ]

    def location(self, item):
        return reverse(item)
