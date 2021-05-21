from django.urls import path

from . import views, views2

urlpatterns = [
    #Package main search page
    path('packages', views2.packagesearch, name='packagesearch'),

    # --------------------------------------->>>>>>>> Redirects
    path('packages/search', views2.packages2, name='packages2'),
    path('packages', views.packages1, name='packages1'),
    path('packages/ivf-packages', views.ivfpackages, name='ivfpackages'),
    path('packages/ivf-with-donor-eggs-packages', views.eggpackages, name='eggpackages'),
    path('packages/ivf-with-donor-embryo-packages', views.embryopackages, name='embryopackages'),

    #Location US
    #path('packages/ivf-packages/united-states', views.ivfpackagesus, name='ivfpackagesus'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/united-states', views.embryopackagesus, name='embryopackagesus'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/united-states', views.eggpackagesus, name='eggpackagesus'), #obecná stránka - landing page!

    #Location UK
    #path('packages/ivf-packages/united-kingdom', views.ivfpackagesuk, name='ivfpackagesuk'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/united-kingdom', views.embryopackagesuk, name='embryopackagesuk'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/united-kingdom', views.eggpackagesuk, name='eggpackagesuk'), #obecná stránka - landing page!

    #Location SP
    #path('packages/ivf-packages/spain', views.ivfpackagessp, name='ivfpackagessp'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/spain', views.embryopackagessp, name='embryopackagessp'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/spain', views.eggpackagessp, name='eggpackagessp'), #obecná stránka - landing page!

    #Location CZ
    #path('packages/ivf-packages/czech-republic', views.ivfpackagescz, name='ivfpackagescz'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/czech-republic', views.embryopackagescz, name='embryopackagescz'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/czech-republic', views.eggpackagescz, name='eggpackagescz'), #obecná stránka - landing page!

    #Location GR
    #path('packages/ivf-packages/greece', views.ivfpackagesgr, name='ivfpackagesgr'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/greece', views.embryopackagesgr, name='embryopackagesgr'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/greece', views.eggpackagesgr, name='eggpackagesgr'), #obecná stránka - landing page!

    #Location IN
    #path('packages/ivf-packages/india', views.ivfpackagesin, name='ivfpackagesin'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-embryo-packages/india', views.embryopackagesin, name='embryopackagesin'), #obecná stránka - landing page!
    #path('packages/ivf-with-donor-eggs-packages/india', views.eggpackagesin, name='eggpackagesin'), #obecná stránka - landing page!
]
