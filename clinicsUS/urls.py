from django.urls import path

from . import views

urlpatterns = [
    path('clinics/us/california/western-fertility-institute', views.wfi, name='wfi'),
    path('clinics/us/california/california-ivf-fertility-center', views.cifc, name='cifc'),
    path('clinics/us/california/northern-california-fertility-medical-center', views.ncfmc, name='ncfmc'),
]
