from django.urls import path

from . import views

urlpatterns = [
    #Alicante
    path('clinics/sp/alicante/ivf-spain-alicante', views.ivfspainalicante, name='ivfspainalicante'),
    path('clinics/sp/alicante/ivi-alicante', views.ivialicante, name='ivialicante'),
    #Barcelona
    path('clinics/sp/barcelona/clinica-de-fertilidad-barcelona-ivf', views.clinicadefertilidadbarcelonaivf, name='clinicadefertilidadbarcelonaivf'),
    path('clinics/sp/barcelona/fertilab-barcelona', views.fertilabbarcelona, name='fertilabbarcelona'),
    path('clinics/sp/barcelona/institut-marques-barcelona', views.institutmarquesbarcelona, name='institutmarquesbarcelona'),
    path('clinics/sp/barcelona/ivf-for-you', views.ivfforyou, name='ivfforyou'),
    path('clinics/sp/barcelona/gravida', views.gravida, name='gravida'),
    path('clinics/sp/barcelona/fertty-international', views.ferttyinternational, name='ferttyinternational'),
    path('clinics/sp/barcelona/ivi-barcelona', views.ivibarcelona, name='ivibarcelona'),
    path('clinics/sp/barcelona/fiv-marbella-barcelona', views.fivmarbellabarcelona, name='fivmarbellabarcelona'),
    #Madrid
    path('clinics/sp/madrid/ivf-spain-madrid', views.ivfspainmadrid, name='ivfspainmadrid'),
    path('clinics/sp/madrid/fertility-madrid', views.fertilitymadrid, name='fertilitymadrid'),
    path('clinics/sp/madrid/eva-fertility-clinic-madrid', views.evafertilityclinicmadrid, name='evafertilityclinicmadrid'),
    path('clinics/sp/madrid/ivi-madrid-aravaca', views.ivimadridaravaca, name='ivimadridaravaca'),
    path('clinics/sp/madrid/clinica-tambre', views.clinicatambre, name='clinicatambre'),
    path('clinics/sp/madrid/fertility-clinic-hru', views.fertilityclinichru, name='fertilityclinichru'),
    path('clinics/sp/madrid/fiv-marbella-madrid', views.fivmarbellamadrid, name='fivmarbellamadrid'),
    #Malaga
    path('clinics/sp/malaga/ivi-malaga', views.ivimalaga, name='ivimalaga'),
    path('clinics/sp/malaga/fiv-marbella-malaga', views.fivmarbellamalaga, name='fivmarbellamalaga'),
    path('clinics/sp/malaga/hc-fertility', views.hcfertility, name='hcfertility'),
    path('clinics/sp/malaga/clinica-fertia', views.clinicafertia, name='clinicafertia'),
    #Seville
    path('clinics/sp/seville/ivi-sevilla', views.ivisevilla, name='ivisevilla'),
    path('clinics/sp/seville/inebir', views.inebir, name='inebir'),
    path('clinics/sp/seville/ginemed-sevilla', views.ginemedsevilla, name='ginemedsevilla'),
    #Valencia
    path('clinics/sp/valencia/ivi-valencia', views.ivivalencia, name='ivivalencia'),
    path('clinics/sp/valencia/equipo-juana-crespo', views.equipojuanacrespo, name='equipojuanacrespo'),
    path('clinics/sp/valencia/unidad-de-reproduccion-asistida-imed-valencia', views.unidaddereproduccionasistidaimedvalencia, name='unidaddereproduccionasistidaimedvalencia'),
    path('clinics/sp/valencia/crea-valencia', views.creavalencia, name='creavalencia'),
    path('clinics/sp/valencia/imer-instituto-de-medicina-reproductiva', views.imerinstitutodemedicinareproductiva, name='imerinstitutodemedicinareproductiva'),
    ]
