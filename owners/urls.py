from django.urls import path
from . import views, views_worlds_best_clinic, views_best_articles, views_packages, views_update_pricing_basicclinic


urlpatterns = [
    path('signup', views.register, name='register'),
    path('signin', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('not-active-user', views.notActiveUser, name='notActiveUser'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('settings', views.settings, name='settings'),
    path('banners', views.banners, name='banners'),
    path('create1', views.create1, name='create1'),
    path('create', views.create, name='create'),
    path('howtousefertilitycommunity', views.howtousefertilitycommunity, name='howtousefertilitycommunity'),
    path('fc-traffic/<int:listing_id>', views.fctrafficreport, name='fctrafficreport'),

    #views_packages
    path('packages/<int:listing_id>', views_packages.packages, name='packages'),
    path('packages/create-package/<int:listing_id>', views_packages.createpackage, name='createpackage'),
    path('clinic-packages/<int:listing_id>', views_packages.clinicpackagesettings, name='clinicpackagesettings'),
    path('packages/update-package/<int:package_id>', views_packages.updatepropackage, name='updatepropackage'),
    path('packages/prolong-package/<int:package_id>', views_packages.prolongpropackage, name='prolongpropackage'),
    path('packages/delete-package/<int:package_id>', views_packages.deletepropackage, name='deletepropackage'),

    path('upgrade/<int:listing_id>', views.upgrade, name='upgrade'),
    path('claim', views.claimClinic, name='claim'),
    path('change-password', views.change_password, name='change-password'),
    path('contactus', views.contactClinic, name='contactus'),
    path('upgrade2', views.upgrade2, name='upgrade2'),

    path('update/<int:listing_id>', views_update_pricing_basicclinic.update, name='update'),
    path('updateprice/<int:listing_id>', views_update_pricing_basicclinic.updatePricing, name='updatePricing'),
    path('updatepricepro/<int:listing_id>', views_update_pricing_basicclinic.updatePricingPro, name='updatePricingPro'),
    path('updatepro/<int:listing_id>', views_update_pricing_basicclinic.updateproclinic, name='updateproclinic'),

    path('live-chat-settings/<int:listing_id>', views.livechatsettings, name='livechatsettings'),
    path('live-chat-settings2/<int:listing_id>', views.livechatsettings2, name='livechatsettings2'),

    path('reviews-settings/<int:listing_id>', views.reviewssettings, name='reviewssettings'),

    #views_best_articles
    path('best-clinic-articles/<int:listing_id>', views_best_articles.bestclinicarticles, name='bestclinicarticles'),
    path('best-clinic-articles-city/<int:listing_id>', views_best_articles.bestclinicarticlescity, name='bestclinicarticlescity'),
    path('best-clinic-articles-state/<int:listing_id>', views_best_articles.bestclinicarticlesstate, name='bestclinicarticlesstate'),
    path('best-clinic-articles-country/<int:listing_id>', views_best_articles.bestclinicarticlescountry, name='bestclinicarticlescountry'),

    path('activate-user', views.activateUser, name='activateUser'),

    #views_worlds_best_clinic
    path('best-world-clinic-settings/', views_worlds_best_clinic.bestclinicworldsettings, name='bestclinicworldsettings'),
    path('best-world-clinic-settings-update/<int:bestclinicworldsettingsupdate_id>', views_worlds_best_clinic.bestclinicworldsettingsupdate, name='bestclinicworldsettingsupdate'),
]
