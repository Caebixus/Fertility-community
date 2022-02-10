from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views, views2, views3
from .views_country import views_cz, views_sk, views_cy, views_sp, views_gr, views_mx, views_lv, views_pt, views_de, views_dk, views_in, views_uk, views_us

urlpatterns = [
    path('ivf-cost', views2.locationsStandardIVF, name='locations'),
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),
    path('iui-cost', views.locationsIUI, name='locationsIUI'),

    path('ivf-cost/usa', views_us.locationsUSRegions, name='locationsUSRegions'),
    path('ivf-cost/uk', views_uk.locationsUKRegions, name='locationsUKRegions'),
    path('ivf-cost/cz', views_cz.locationsCZRegions, name='locationsCZRegions'),
    path('ivf-cost/sk', views_sk.locationsSKRegions, name='locationsSKRegions'),
    path('ivf-cost/spain', views_sp.locationsSPRegions, name='locationsSPRegions'),
    path('ivf-cost/denmark', views_dk.locationsDKRegions, name='locationsDKRegions'),
    path('ivf-cost/india', views_in.locationsINRegions, name='locationsINRegions'),
    path('ivf-cost/greece', views_gr.locationsGRRegions, name='locationsGRRegions'),
    path('ivf-cost/cyprus', views_cy.locationsCYRegions, name='locationsCYRegions'),
    path('ivf-cost/germany', views_de.locationsDERegions, name='locationsDERegions'),
    path('ivf-cost/latvia', views_lv.locationsLVRegions, name='locationsLVRegions'),
    path('ivf-cost/portugal', views_pt.locationsPTRegions, name='locationsPTRegions'),
    path('ivf-cost/mexico', views_mx.locationsMXRegions, name='locationsMXRegions'),
    path('currencies', include('currencies.urls')),

    path('ivf-cost/usa/texas', views3.locationsTexasRegions, name='locationsTexasRegions'),

    # --------------------------------------->>>>>>>> Redirects
    path('egg-donation-cost', views.locationsIVFwithEggDonation, name='locationsIVFwithEggDonation'),
    path('embryo-donation-cost', views.locationsIVFwithEmbryoDonation, name='locationsIVFwithEmbryoDonation'),
    path('iui-cost', views.locationsIUI, name='locationsIUI'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
