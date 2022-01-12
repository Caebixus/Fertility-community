from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views, views2, views3

urlpatterns = [
    path('ivf-cost', views.locationsStandardIVF, name='locations'),
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),
    path('iui-cost', views.locationsIUI, name='locationsIUI'),

    path('ivf-cost/usa', views2.locationsUSRegions, name='locationsUSRegions'),
    path('ivf-cost/uk', views2.locationsUKRegions, name='locationsUKRegions'),
    path('ivf-cost/cz', views2.locationsCZRegions, name='locationsCZRegions'),
    path('ivf-cost/sk', views2.locationsSKRegions, name='locationsSKRegions'),
    path('ivf-cost/spain', views2.locationsSPRegions, name='locationsSPRegions'),
    path('ivf-cost/denmark', views2.locationsDKRegions, name='locationsDKRegions'),
    path('ivf-cost/india', views2.locationsINRegions, name='locationsINRegions'),
    path('ivf-cost/greece', views2.locationsGRRegions, name='locationsGRRegions'),
    path('ivf-cost/cyprus', views2.locationsCYRegions, name='locationsCYRegions'),
    path('ivf-cost/germany', views2.locationsDERegions, name='locationsDERegions'),
    path('ivf-cost/latvia', views2.locationsLVRegions, name='locationsLVRegions'),
    path('ivf-cost/portugal', views2.locationsPTRegions, name='locationsPTRegions'),
    path('ivf-cost/mexico', views2.locationsMXRegions, name='locationsMXRegions'),
    path('currencies', include('currencies.urls')),

    path('ivf-cost/usa/texas', views3.locationsTexasRegions, name='locationsTexasRegions'),

    # --------------------------------------->>>>>>>> Redirects
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),
    path('iui-cost', views.locationsIUI, name='locationsIUI'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
