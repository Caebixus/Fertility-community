from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('ivf-cost', views.locations, name='locations'),
    path('ivf-cost/usa', views.locationsUSRegions, name='locationsUSRegions'),
    path('ivf-cost/uk', views.locationsUKRegions, name='locationsUKRegions'),
    path('currencies', include('currencies.urls')),
]
