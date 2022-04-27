from django.urls import path

from . import views, views_best_ivf_clinics_countries, views_best_ivf_clinics_cities, views_best_ivf_clinics_world
from .views import AuthorDetailView
from .views_faq_blogs import FaqDetailView


urlpatterns = [
    #Authors
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='authorDetailView'),

    #FAQBlog
    path('blog/<slug:slug>/', FaqDetailView.as_view(), name='FaqDetailView'),

    #IVF Abroad
    path('blog/ivf-abroad-costs', views.ivfabroadcosts, name='ivfabroadcosts'),
    path('blog/fertility-treatment-abroad-what-you-need-to-know', views.fertilityTreatmentAbroadWhatYouNeedToKnow, name='fertilityTreatmentAbroadWhatYouNeedToKnow'),
    path('blog/ivf-in-spain', views.ivf_in_spain, name='ivf_in_spain'),
    path('blog/ivf-in-greece', views.ivf_in_greece, name='ivf_in_greece'),
    path('blog/ivf-in-czech-republic', views.ivf_in_czech_republic, name='ivf_in_czech_republic'),
    path('blog/ivf-in-slovakia', views.ivf_in_slovakia, name='ivf_in_slovakia'),
    path('blog/ivf-in-prague', views.ivf_in_prague, name='ivf_in_prague'),
    path('blog/ivf-in-portugal', views.ivf_in_portugal, name='ivf_in_portugal'),

    #Packages
    path('blog/ivf-abroad-packages', views.ivfabroadpackages, name='ivfabroadpackages'),

    #Educational
    path('blog/everything-you-need-to-know-about-natural-ivf', views.everythingYouNeedToKnowAboutNaturalIvf, name='everythingYouNeedToKnowAboutNaturalIvf'),
    path('blog/what-is-mild-mini-ivf', views.whatismildminiivf, name='whatismildminiivf'),
    path('blog/why-does-ivf-fails', views.whydoesivffails, name='whydoesivffails'),
    path('blog/what-is-icsi-treatment', views.whatisicsitreatment, name='whatisicsitreatment'),
    path('blog/why-does-ivf-cost-so-much-usa', views.whydoesivfcostsomuch, name='whydoesivfcostsomuch'),
    path('blog/ivf-with-egg-donation-process', views.whatisivfwitheggdonation, name='whatisivfwitheggdonation'),
    path('blog/ivf-and-meditation', views.ivfmeditation, name='ivfmeditation'),

    #Information & support
    path('blog/prague-ivf-reviews', views.pragueivfreviews, name='pragueivfreviews'),
    path('blog/ivf-step-by-step', views.ivfstepbystep, name='ivfstepbystep'),

    #Research
    path('blog/how-americans-ivf-compare-with-the-world', views.fertilitytreatmentshowamericanscomparewiththerestoftheworld, name='fertilitytreatmentshowamericanscomparewiththerestoftheworld'),

    #Best Clinics In World
    path('blog/best-ivf-clinics-world', views_best_ivf_clinics_world.best_ivf_clinics_world, name='best_ivf_clinics_world'),

    #Best Clinics In Countries
    path('blog/best-ivf-clinics-czech', views_best_ivf_clinics_countries.bestivfclinicsinczech, name='bestivfclinicsinczech'),
    path('blog/best-ivf-clinics-in-czech', views_best_ivf_clinics_countries.bestivfclinicsinczechbezin, name='bestivfclinicsinczechbezin'),
    path('blog/best-ivf-clinics-spain', views_best_ivf_clinics_countries.bestivfclinicsinspain, name='bestivfclinicsinspain'),
    path('blog/best-ivf-clinics-greece', views_best_ivf_clinics_countries.bestivfclinicsingreece, name='bestivfclinicsingreece'),
    path('blog/best-ivf-clinics-slovakia', views_best_ivf_clinics_countries.bestivfclinicsinslovakia, name='bestivfclinicsinslovakia'),
    path('blog/best-ivf-clinics-portugal', views_best_ivf_clinics_countries.bestivfclinicsinportugal, name='bestivfclinicsinportugal'),
    path('blog/best-ivf-clinics-germany', views_best_ivf_clinics_countries.bestivfclinicsingermany, name='bestivfclinicsingermany'),

    #Best Clinics In Cities
    path('blog/best-ivf-clinics-prague', views_best_ivf_clinics_cities.bestivfclinicsinprague, name='bestivfclinicsinprague'),
]
