from django.contrib import sitemaps
from django.urls import reverse
from base import views
from searchLocationsRegionsUS import views
from location import views

class RegionsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.7
    protocol = "https"

    def items(self):
        return [
        'fertilityClinicsAlabama',
        'fertilityClinicsAlaska',
        'fertilityClinicsArizona',
        'fertilityClinicsArkansas',
        'fertilityClinicsCalifornia',
        'fertilityClinicsColorado',
        'fertilityClinicsConnecticut',
        'fertilityClinicsDelaware',
        'fertilityClinicsGeorgia',
        'fertilityClinicsHawaii',
        'fertilityClinicsIdaho',
        'fertilityClinicsIllinois',
        'fertilityClinicsIndiana',
        'fertilityClinicsIowa',
        'fertilityClinicsKansas',
        'fertilityClinicsKentucky',
        'fertilityClinicsLouisiana',
        'fertilityClinicsMaine',
        'fertilityClinicsMaryland',
        'fertilityClinicsMassachusetts',
        'fertilityClinicsMichigan',
        'fertilityClinicsMinnesota',
        'fertilityClinicsMississippi',
        'fertilityClinicsMissouri',
        'fertilityClinicsNebraska',
        'fertilityClinicsNewHampshire',
        'fertilityClinicsNewJersey',
        'fertilityClinicsNewMexico',
        'fertilityClinicsNewYork',
        'fertilityClinicsNorthCarolina',
        'fertilityClinicsOhio',
        'fertilityClinicsOklahoma',
        'fertilityClinicsOregon',
        'fertilityClinicsPennsylvania',
        'fertilityClinicsRhodeIsland',
        'fertilityClinicsSouthCarolina',
        'fertilityClinicsSouthDakota',
        'fertilityClinicsTennessee',
        'fertilityClinicsTexas',
        'fertilityClinicsUtah',
        'fertilityClinicsVermont',
        'fertilityClinicsVirginia',
        'fertilityClinicsWashington',
        'fertilityClinicsWestVirginia',
        'fertilityClinicsWisconsin',
        'fertilityClinicsWyoming',
        'fertilityClinicsDistrictOfColumbia',
        ]

    def location(self, item):
        return reverse(item)
