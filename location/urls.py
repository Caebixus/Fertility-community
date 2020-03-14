from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('locations', views.locations, name='locations'),
    path('locations/us-regions', views.locationsRegions, name='locationsRegions'),
    path('currencies', include('currencies.urls')),
]
