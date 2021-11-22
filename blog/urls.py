from django.urls import path, include
from django.conf import settings

from . import views, views_best_ivf_clinics_countries, views_best_ivf_clinics_cities

urlpatterns = [
    #Authors
    path('authors/lisa-holliman', views.authorlisaholliman, name='authorlisaholliman'),

    #Blogs
    path('blog/ivf-abroad-costs', views.ivfabroadcosts, name='ivfabroadcosts'),
    path('blog/fertility-treatment-abroad-what-you-need-to-know', views.fertilityTreatmentAbroadWhatYouNeedToKnow, name='fertilityTreatmentAbroadWhatYouNeedToKnow'),

    #Packages
    path('blog/ivf-abroad-packages', views.ivfabroadpackages, name='ivfabroadpackages'),

    #Educational
    path('blog/everything-you-need-to-know-about-natural-ivf', views.everythingYouNeedToKnowAboutNaturalIvf, name='everythingYouNeedToKnowAboutNaturalIvf'),
    path('blog/what-is-mild-mini-ivf', views.whatismildminiivf, name='whatismildminiivf'),

    #Research
    path('blog/how-americans-ivf-compare-with-the-world', views.fertilitytreatmentshowamericanscomparewiththerestoftheworld, name='fertilitytreatmentshowamericanscomparewiththerestoftheworld'),


    #Best Clinics In Countries
    path('blog/best-ivf-clinics-czech', views_best_ivf_clinics_countries.bestivfclinicsinczech, name='bestivfclinicsinczech'),
    path('blog/best-ivf-clinics-in-czech', views_best_ivf_clinics_countries.bestivfclinicsinczechbezin, name='bestivfclinicsinczechbezin'),
    path('blog/best-ivf-clinics-spain', views_best_ivf_clinics_countries.bestivfclinicsinspain, name='bestivfclinicsinspain'),

    #Best Clinics In Cities
    path('blog/best-ivf-clinics-prague', views_best_ivf_clinics_cities.bestivfclinicsinprague, name='bestivfclinicsinprague'),
]
