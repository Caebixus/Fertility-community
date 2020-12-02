from django.urls import path

from . import views

urlpatterns = [
    #Nicosia
    path('clinics/cy/nicosia/cyprus-ivf-centre', views.cyprusivfcentre, name='cyprusivfcentre'),
    path('clinics/cy/nicosia/british-cyprus-ivf-hospital', views.britishcyprusivfhospital, name='britishcyprusivfhospital'),
    path('clinics/cy/nicosia/eurocareivf', views.eurocareivf, name='eurocareivf'),
    path('clinics/cy/nicosia/dogus-fertility-clinic', views.dogusfertilityclinic, name='dogusfertilityclinic'),
    path('clinics/cy/nicosia/pedieos-ivf-center', views.pedieosivfcenter, name='pedieosivfcenter'),

    #Famagusta
    path('clinics/cy/famagusta/crown-ivf-cyprus', views.crownivfcyprus, name='crownivfcyprus'),

    #Girne
    path('clinics/cy/girne/dunya-ivf-cyprus-fertility-clinic', views.dunyaivfcyprusfertilityclinic, name='dunyaivfcyprusfertilityclinic'),
    path('clinics/cy/girne/kyrenia-ivf-center', views.kyreniaivfcenter, name='kyreniaivfcenter'),
    ]
