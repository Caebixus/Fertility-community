from django.contrib import sitemaps
from coaches.models import Coaches

class CoachesViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Coaches.objects.filter(coach_is_published=True)

    def location(self, item):
        return item.get_absolute_coach_url()