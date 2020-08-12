from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('ivf-cost', views.locationsStandardIVF, name='locations'),
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),

    path('ivf-cost/usa', views.locationsUSRegions, name='locationsUSRegions'),
    path('ivf-cost/uk', views.locationsUKRegions, name='locationsUKRegions'),
    path('ivf-cost/cz', views.locationsCZRegions, name='locationsCZRegions'),
    path('currencies', include('currencies.urls')),
]
