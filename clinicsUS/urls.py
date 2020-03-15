from django.urls import path

from . import views

urlpatterns = [
    path('clinics/us/california/western-fertility-institute', views.wfi, name='wfi'),
    path('clinics/us/california/california-ivf-fertility-center', views.cifc, name='cifc'),
    path('clinics/us/california/northern-california-fertility-medical-center-roseville', views.ncfmcr, name='ncfmcr'),
    path('clinics/us/california/northern-california-fertility-medical-center-sacramento', views.ncfmcs, name='ncfmcs'),
    path('clinics/us/california/la-ivf-west-los-angeles', views.liwla, name='liwla'),
    path('clinics/us/california/la-ivf-pasadena', views.lip, name='lip'),
    path('clinics/us/california/la-ivf-chino-hills', views.lich, name='lich'),
    path('clinics/us/alabama/center-for-reproductive-medicine', views.tcfrm, name='tcfrm'),
    path('clinics/us/alabama/alabama-fertility', views.af, name='af'),
]
