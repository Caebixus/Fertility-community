from django.urls import path

from . import views

urlpatterns = [
    path('clinics/us/california/the-center-for-fertility-and-gynecology', views.tcffag, name='tcffag'),
]
