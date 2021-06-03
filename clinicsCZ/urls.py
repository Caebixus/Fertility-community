from django.urls import path

from . import views

urlpatterns = [
    #PRAGUE
    path('clinics/cz/prague/pragamedica', views.pragamedica, name='pragamedica'),
    path('clinics/cz/prague/fertilityport-prague', views.fertilityportx, name='fertilityportx'),
    path('clinics/cz/prague/prague-fertility-centre', views.praguefertilitycentre, name='praguefertilitycentre'),
    path('clinics/cz/prague/gynem-fertility-clinic', views.gynemfertilityclinic, name='gynemfertilityclinic'),
    path('clinics/cz/prague/gennet', views.gennet, name='gennet'),
    path('clinics/cz/prague/medical-travel-czech-republic', views.medicaltravelczechrep, name='medicaltravelczechrep'),
    path('clinics/cz/prague/pronatal-plus-prague6', views.pronatalplusprague, name='pronatalplusprague'),
    path('clinics/cz/prague/pronatal-sanatorium-prague4', views.pronatalsanatoriumprague, name='pronatalsanatoriumprague'),
    path('clinics/cz/prague/ivf-cube', views.ivfcube, name='ivfcube'),
    path('clinics/cz/prague/medistella', views.medistella, name='medistella'),
    path('clinics/cz/prague/europe-ivf-prague', views.europeivfprague, name='europeivfprague'),
    #BRNO
    path('clinics/cz/brno/ivf-zlin-czech-republic', views.ivfzlinczechrep, name='ivfzlinczechrep'),
    path('clinics/cz/brno/reprofit-brno', views.reprofitbrno, name='reprofitbrno'),
    path('clinics/cz/brno/reprogenesis', views.reprogenesis, name='reprogenesis'),
    #KOLIN
    path('clinics/cz/kolin/pronatal-kolin', views.pronatalkolin, name='pronatalkolin'),
    #ČESKÉ BUDĚJOVICE
    path('clinics/cz/ceske-budejovice/pronatal-repro-ceske-budejovice', views.pronatalreproceskebudejovice, name='pronatalreproceskebudejovice'),
    #TEPLICE
    path('clinics/cz/teplice/pronatal-nord-teplice', views.pronatalnordteplice, name='pronatalnordteplice'),
    #TEPLICE
    path('clinics/cz/karlovy-vary/pronatal-spa-karlovy-vary', views.pronatalspakarlovyvary, name='pronatalspakarlovyvary'),
    #OSTRAVA
    path('clinics/cz/ostrava/reprofit-ostrava', views.reprofitostrava, name='reprofitostrava'),
    ]
