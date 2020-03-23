from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsRegionsUS import views
from location import views
from clinicsUS import views

class ClinicsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"

    def items(self):
        return [
        'wfi',
        'cifc',
        'ncfmcr',
        'ncfmcs',
        'liwla',
        'lip',
        'lich',
        'tcfrm',
        'af',
        'tfc',
        'tfg',
        'tfm',
        'sfc',
        'afcs',
        'afcm',
        'aafrhs',
        'aafrhg',
        'bris',
        'brig',
        'biacs',
        'biacch',
        'biacp',
        'biacf',
        'ip',
        'ftc',
        'arifc',
        'irmsco',
        'irmsewo',
        'irmsho',
        'irmshbo',
        'irmsnjo',
        'irmslo',
        'irmsobo',
        'cfnyc',
        'ccrmnyfc',
        ]

    def location(self, item):
        return reverse(item)
