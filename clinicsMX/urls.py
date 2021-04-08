from django.urls import path

from . import views

urlpatterns = [
    #Acapulco
    path('clinics/mx/acapulco/irega-acapulco', views.iregaacapulco, name='iregaacapulco'),

    #Cancun
    path('clinics/mx/cancun/fertility-clinic-americas', views.fertilityclinicamericas, name='fertilityclinicamericas'),
    path('clinics/mx/cancun/advanced-fertility-center-fertility-center-cancun', views.advancedfertilitycenterfertilitycentercancun, name='advancedfertilitycenterfertilitycentercancun'),
    path('clinics/mx/cancun/new-life-mexico', views.newlifemexico, name='newlifemexico'),
    path('clinics/mx/cancun/irega-cancun', views.iregacancun, name='iregacancun'),

    #Centro
    path('clinics/mx/centro/embryogen-fertility-center-guasave', views.embryogengertilitycenterguasave, name='embryogengertilitycenterguasave'),

    #Mexico City
    path('clinics/mx/mexico-city/enlistalo-fertilidad-mexico-ciudad-de-mexico', views.enlistalofertilidadmexicociudaddemexico, name='enlistalofertilidadmexicociudaddemexico'),
    path('clinics/mx/mexico-city/citmer-medicina-reproductiva', views.citmermedicinareproductiva, name='citmermedicinareproductiva'),

    #Cualican rosales
    path('clinics/mx/cualican-rosales/embryogen-fertility-center-culiacan', views.embryogenfertilitycenterculiacan, name='embryogenfertilitycenterculiacan'),

    #Hermosillo
    path('clinics/mx/hermosillo/embryogen-fertility-center-hermosillo', views.embryogenfertilitycenterhermosillo, name='embryogenfertilitycenterhermosillo'),

    #Mazatlan
    path('clinics/mx/mazatlan/embryogen-fertility-center-mazatlan', views.embryogenfertilitycentermazatlan, name='embryogenfertilitycentermazatlan'),

    #Mexicali
    path('clinics/mx/mexicali/mexico-fertility-center', views.mexicofertilitycenter, name='mexicofertilitycenter'),

    #Nogales
    path('clinics/mx/nogales/embryogen-fertility-center-nogales', views.embryogenfertilitycenternogales, name='embryogenfertilitycenternogales'),

    #Nuevo Vallarta
    path('clinics/mx/nuevo-vallarta/ivfvallarta', views.ivfvallarta, name='ivfvallarta'),
    path('clinics/mx/nuevo-vallarta/surrogacymexico', views.surrogacymexico, name='surrogacymexico'),

    #Puebla
    path('clinics/mx/puebla/irega-puebla', views.iregapuebla, name='iregapuebla'),
    ]
