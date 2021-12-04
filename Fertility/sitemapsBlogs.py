from django.contrib import sitemaps
from django.urls import reverse
from base import views
from blog import views

class BlogsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
        'ivfabroadcosts',
        'fertilityTreatmentAbroadWhatYouNeedToKnow',
        'ivfabroadpackages',
        'everythingYouNeedToKnowAboutNaturalIvf',
        'whatismildminiivf',
        'fertilitytreatmentshowamericanscomparewiththerestoftheworld',
        'whydoesivffails',
        'whatisicsitreatment',
        'whydoesivfcostsomuch',
        'whatisivfwitheggdonation',

        'bestivfclinicsinprague',
        'bestivfclinicsinczech',
        'bestivfclinicsinspain',
        'bestivfclinicsingreece',
        ]

    def location(self, item):
        return reverse(item)
