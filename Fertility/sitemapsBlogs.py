from django.contrib import sitemaps
from django.urls import reverse


class BlogsViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
        'blog:ivfabroadcosts',
        'blog:fertilityTreatmentAbroadWhatYouNeedToKnow',
        'blog:ivfabroadpackages',
        'blog:everythingYouNeedToKnowAboutNaturalIvf',
        'blog:whatismildminiivf',
        'blog:fertilitytreatmentshowamericanscomparewiththerestoftheworld',
        'blog:whydoesivffails',
        'blog:whatisicsitreatment',
        'blog:whydoesivfcostsomuch',
        'blog:whatisivfwitheggdonation',
        'blog:ivf_in_spain',
        'blog:ivf_in_greece',
        'blog:ivf_in_czech_republic',
        'blog:ivf_in_slovakia',
        'blog:ivf_in_prague',
        'blog:ivf_in_portugal',
        'blog:ivfmeditation',
        'blog:ivfstepbystep',

        'blog:bestivfclinicsinczech',
        'blog:bestivfclinicsinspain',
        'blog:bestivfclinicsingreece',
        'blog:bestivfclinicsinslovakia',
        'blog:bestivfclinicsinportugal',
        'blog:bestivfclinicsingermany',

        'blog:best_ivf_clinics_world',
        ]

    def location(self, item):
        return reverse(item)
