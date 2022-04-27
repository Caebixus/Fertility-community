from django.contrib import sitemaps
from blog.models import FAQBlog

class FaqBlogsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return FAQBlog.objects.filter(active=True)

    def location(self, item):
        return item.get_absolute_url()