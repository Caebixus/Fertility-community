from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsCountries import views
from location import views

class CountriesViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return [
        'fertilityClinicUSA',
        'fertilityClinicUK',
        'fertilityClinicSpain',
        'fertilityClinicIndia',
        'fertilityClinicGreece',
        'fertilityClinicCzech',
        ]

    def location(self, item):
        return reverse(item)
