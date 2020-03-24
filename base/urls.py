from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fertility/sperm-donor-basics.html', views.businessinsiderbacklink, name='businessinsiderbacklink'),
    path('infertility-male3.html', views.backlink2, name='backlink2'),
    path('intrauterine-insemination-iui/2020189726-increaseyourchances-org.html', views.backlink3, name='backlink3'),
    path('robots.txt', views.robots, name='robots.txt'),
    path('about', views.about, name='about'),
    path('contact', views.contactWebsite, name='contact'),
    path('team', views.team, name='team'),
    path('travel-calculator', views.travelCalculator, name='travelCalculator'),
    path('cookies', views.cookies, name='cookies'),
    path('privacy', views.privacy, name='privacy'),
]
