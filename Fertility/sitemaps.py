from django.contrib import sitemaps
from django.urls import reverse

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
        'coach:coach_search',
        ]

    def location(self, item):
        return reverse(item)
