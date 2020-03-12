from django.urls import path

from . import views

urlpatterns = [
    path('locations/regions/fertility-clinics-california', views.fertilityClinicsCalifornia, name='fertilityClinicsCalifornia'),
]
