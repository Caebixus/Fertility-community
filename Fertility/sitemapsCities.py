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
        'fertilityClinicPrague',
        'fertilityClinicBrno',

        'fertilityClinicsAberdeen',
        'fertilityClinicsBath',
        'fertilityClinicsBelfast',
        'fertilityClinicsBirmingham',
        'fertilityClinicsBournemouth',
        'fertilityClinicsBrightonHove',
        'fertilityClinicsBristol',
        'fertilityClinicsCambridge',
        'fertilityClinicsCardiff',
        'fertilityClinicsColchester',
        'fertilityClinicsDerby',
        'fertilityClinicsExeter',
        'fertilityClinicsGlasgow',
        'fertilityClinicsHull',
        'fertilityClinicsChelmsford',
        'fertilityClinicsLeeds',
        'fertilityClinicsLeicester',
        'fertilityClinicsLiverpool',
        'fertilityClinicsLondon',
        'fertilityClinicsManchester',
        'fertilityClinicsMiddlesbrough',
        'fertilityClinicsNewcastle',
        'fertilityClinicsNorwich',
        'fertilityClinicsNottingham',
        'fertilityClinicsOxford',
        'fertilityClinicsPeterborough',
        'fertilityClinicsPlymouth',
        'fertilityClinicsPortsmouth',
        'fertilityClinicsSalisbury',
        'fertilityClinicsSheffield',
        'fertilityClinicsSouthampton',
        'fertilityClinicsSwansea',

        'fertilityClinicsAlicante',
        'fertilityClinicsBarcelona',
        'fertilityClinicsMadrid',
        'fertilityClinicsMalaga',
        'fertilityClinicsSeville',
        'fertilityClinicsValencia',
        ]

    def location(self, item):
        return reverse(item)
