from django.urls import path

from . import views

urlpatterns = [
    path('clinics/us/california/western-fertility-institute', views.wfi, name='wfi'),
]
