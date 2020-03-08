from django.urls import path

from . import views

urlpatterns = [
    path('fertility-clinics-london', views.fertilityClinicLondon, name='fertilityClinicLondon'),
    path('fertility-clinics-manchester', views.fertilityClinicManchester, name='fertilityClinicManchester'),
]
