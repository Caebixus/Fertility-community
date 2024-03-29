from django.contrib import sitemaps
from django.urls import reverse


class CitiesViewSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return [
        'fertilityClinicPrague',
        'fertilityClinicBrno',

        'fertilityClinicBratislava',

        'fertilityClinicCopenhagen',

        'fertilityClinicRiga',

        'fertilityClinicBerlin',

        'fertilityClinicLisbon',

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

        'fertilityClinicsAmdavad',
        'fertilityClinicsBangalore',
        'fertilityClinicsBhopal',
        'fertilityClinicsBhubaneswar',
        'fertilityClinicsDehradun',
        'fertilityClinicsFaridabad',
        'fertilityClinicsHyderabad',
        'fertilityClinicsChandigarh',
        'fertilityClinicsChennai',
        'fertilityClinicsIndore',
        'fertilityClinicsJaipur',
        'fertilityClinicsJamshedpur',
        'fertilityClinicsKanpur',
        'fertilityClinicsKochi',
        'fertilityClinicsKolkata',
        'fertilityClinicsLucknow',
        'fertilityClinicsMumbai',
        'fertilityClinicsNagpur',
        'fertilityClinicsPatna',
        'fertilityClinicsRaipur',
        'fertilityClinicsTrivandrum',
        'fertilityClinicsLudhiana',
        'fertilityClinicsVisakhapatnam',
        'fertilityClinicsVijayawada',
        'fertilityClinicsNewDelhi',
        'fertilityClinicsVadodara',
        'fertilityClinicsGurugram',
        'fertilityClinicsRohtak',
        'fertilityClinicsJammu',
        'fertilityClinicsRanchi',
        'fertilityClinicsGwalior',
        'fertilityClinicsPune',
        'fertilityClinicsWarangal',
        'fertilityClinicsGachibowli',
        'fertilityClinicsMadhapur',
        'fertilityClinicsNoida',
        'fertilityClinicsMeerut',
        'fertilityClinicsHaldwani',

        'fertilityClinicsAthens',
        'fertilityClinicsThessaloniki',

        'fertilityClinicsNicosia',
        'fertilityClinicsGirne',

        'fertilityClinicsCancun',
        'fertilityClinicsMexicoCity',
        ]

    def location(self, item):
        return reverse(item)
