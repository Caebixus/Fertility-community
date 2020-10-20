from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views, views2

urlpatterns = [
    path('ivf-cost', views.locationsStandardIVF, name='locations'),
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),
    path('iui-cost', views.locationsIUI, name='locationsIUI'),

    path('ivf-cost/usa', views.locationsUSRegions, name='locationsUSRegions'),
    path('ivf-cost/uk', views.locationsUKRegions, name='locationsUKRegions'),
    path('ivf-cost/cz', views.locationsCZRegions, name='locationsCZRegions'),
    path('ivf-cost/spain', views.locationsSPRegions, name='locationsSPRegions'),
    path('currencies', include('currencies.urls')),

    path('ivf-cost/usa/texas', views2.locationsTexasRegions, name='locationsTexasRegions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
