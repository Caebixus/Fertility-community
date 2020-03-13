from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fertility/sperm-donor-basics.html', views.businessinsiderbacklink, name='businessinsiderbacklink'),
    path('infertility-male3.html', views.backlink2, name='backlink2'),
    path('robots.txt', views.robots, name='robots.txt'),
    path('about', views.about, name='about'),
    path('contact', views.contactWebsite, name='contact'),
    path('team', views.team, name='team'),
    path('travel-calculator', views.travelCalculator, name='travelCalculator'),
    path('cookies', views.cookies, name='cookies'),
    path('privacy', views.privacy, name='privacy'),
    path('ivf-country-difference', views.ivf_country_difference, name='ivf-country-difference'),
]
