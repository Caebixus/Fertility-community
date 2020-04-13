from django.urls import path

from . import views

urlpatterns = [
    path('locations/fertility-clinics-prague', views.fertilityClinicPrague, name='fertilityClinicPrague'),
    path('locations/fertility-clinics-brno', views.fertilityClinicBrno, name='fertilityClinicBrno'),
]
