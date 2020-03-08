from django.urls import path

from . import views

urlpatterns = [
    path('fertility-clinics-uk', views.fertilityClinicuk, name='fertilityClinicuk'),
]
