from django.urls import path

from . import views

urlpatterns = [
    path('locations/fertility-clinics-prague', views.fertilityClinicPrague, name='fertilityClinicPrague'),
]
