from django.urls import path

from . import views

urlpatterns = [
    path('fertility-clinics/usa', views.fertilityClinicUSA, name='fertilityClinicUSA'),
    path('fertility-clinics/uk', views.fertilityClinicUK, name='fertilityClinicUK'),
    path('fertility-clinics/spain', views.fertilityClinicSpain, name='fertilityClinicSpain'),
    path('fertility-clinics/india', views.fertilityClinicIndia, name='fertilityClinicIndia'),
    path('fertility-clinics/greece', views.fertilityClinicGreece, name='fertilityClinicGreece'),
    path('fertility-clinics/czech-republic', views.fertilityClinicCzech, name='fertilityClinicCzech'),
    path('fertility-clinics/cyprus', views.fertilityClinicCyprus, name='fertilityClinicCyprus'),
    path('fertility-clinics/mexico', views.fertilityClinicMexico, name='fertilityClinicMexico'),

    # --------------------------------------->>>>>>>> Redirects
    path('fertility-clinic-usa', views.fertilityClinicUSA1, name='fertilityClinicUSA1'),
    path('fertility-clinic-uk', views.fertilityClinicUK1, name='fertilityClinicUK1'),
    path('fertility-clinic-spain', views.fertilityClinicSpain1, name='fertilityClinicSpain1'),
    path('fertility-clinic-india', views.fertilityClinicIndia1, name='fertilityClinicIndia1'),
    path('fertility-clinic-greece', views.fertilityClinicGreece1, name='fertilityClinicGreece1'),
    path('fertility-clinic-czech-republic', views.fertilityClinicCzech1, name='fertilityClinicCzech1'),
    path('fertility-clinic-cyprus', views.fertilityClinicCyprus1, name='fertilityClinicCyprus1'),
]
