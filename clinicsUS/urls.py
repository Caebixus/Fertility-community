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
    path('clinics/us/arizona/troche-fertility-glendale', views.tfg, name='tfg'),
    path('clinics/us/arizona/troche-fertility-mesa', views.tfm, name='tfm'),
    path('clinics/us/arizona/troche-fertility-scottsdale', views.tfc, name='tfc'),
    path('clinics/us/arizona/southwest-fertility-center', views.sfc, name='sfc'),
    path('clinics/us/arizona/advanced-fertility-care-scottsdale', views.afcs, name='afcs'),
    path('clinics/us/arizona/advanced-fertility-care-mesa', views.afcm, name='afcm'),
    path('clinics/us/arizona/arizona-associates-for-reproductive-health-scottsdale', views.aafrhs, name='aafrhs'),
    path('clinics/us/arizona/arizona-associates-for-reproductive-health-gilbert', views.aafrhg, name='aafrhg'),
    path('clinics/us/arizona/bloom-reproductive-institute-scottsdale', views.bris, name='bris'),
    path('clinics/us/arizona/bloom-reproductive-institute-gilbert', views.brig, name='brig'),
    path('clinics/us/arizona/boston-ivf-arizona-center-scottsdale', views.biacs, name='biacs'),
    path('clinics/us/arizona/boston-ivf-arizona-center-chandler', views.biacch, name='biacch'),
    path('clinics/us/arizona/boston-ivf-arizona-center-peoria', views.biacp, name='biacp'),
    path('clinics/us/arizona/boston-ivf-arizona-center-flagstaff', views.biacf, name='biacf'),
    path('clinics/us/arizona/ivf-phoenix', views.ip, name='ip'),
    path('clinics/us/arizona/fertility-treatment-center', views.ftc, name='ftc'),
    path('clinics/us/arizona/arizona-reproductive-institute-fertility-clinic', views.arifc, name='arifc'),
]
