from django.urls import path

from . import views

urlpatterns = [
    path('fertility-clinic-usa', views.fertilityClinicUSA, name='fertilityClinicUSA'),
    path('fertility-clinic-uk', views.fertilityClinicUK, name='fertilityClinicUK'),
    path('fertility-clinic-spain', views.fertilityClinicSpain, name='fertilityClinicSpain'),
    path('fertility-clinic-india', views.fertilityClinicIndia, name='fertilityClinicIndia'),
    path('fertility-clinic-greece', views.fertilityClinicGreece, name='fertilityClinicGreece'),
    path('fertility-clinic-czech-republic', views.fertilityClinicCzech, name='fertilityClinicCzech'),
]
