from django.urls import path

from . import views

urlpatterns = [
    path('locations/fertility-clinics-prague', views.fertilityClinicsPrague, name='fertilityClinicsPrague'),
    path('locations/fertility-clinics-brno', views.fertilityClinicsBrno, name='fertilityClinicsBrno'),
]
