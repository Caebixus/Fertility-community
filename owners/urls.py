from django.urls import path
from django.contrib.auth.forms import PasswordChangeForm

from . import views

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

    path('packages/<int:listing_id>', views.packages, name='packages'),
    path('packages/create-package/<int:listing_id>', views.createpackage, name='createpackage'),
    path('clinic-packages/<int:listing_id>', views.clinicpackagesettings, name='clinicpackagesettings'),
    path('packages/update-package/<int:package_id>', views.updatepropackage, name='updatepropackage'),
    path('packages/prolong-package/<int:package_id>', views.prolongpropackage, name='prolongpropackage'),
    path('packages/delete-package/<int:package_id>', views.deletepropackage, name='deletepropackage'),

    path('upgrade/<int:listing_id>', views.upgrade, name='upgrade'),
    path('claim', views.claimClinic, name='claim'),
    path('change-password', views.change_password, name='change-password'),
    path('contactus', views.contactClinic, name='contactus'),
    path('upgrade2', views.upgrade2, name='upgrade2'),

    path('update/<int:listing_id>', views.update, name='update'),
    path('updateprice/<int:listing_id>', views.updatePricing, name='updatePricing'),
    path('updatepricepro/<int:listing_id>', views.updatePricingPro, name='updatePricingPro'),
    path('updatepro/<int:listing_id>', views.updateproclinic, name='updateproclinic'),

    path('live-chat-settings/<int:listing_id>', views.livechatsettings, name='livechatsettings'),
    path('live-chat-settings2/<int:listing_id>', views.livechatsettings2, name='livechatsettings2'),

    path('reviews-settings/<int:listing_id>', views.reviewssettings, name='reviewssettings'),

    path('best-clinic-articles/<int:listing_id>', views.bestclinicarticles, name='bestclinicarticles'),
    path('best-clinic-articles-city/<int:listing_id>', views.bestclinicarticlescity, name='bestclinicarticlescity'),
    path('best-clinic-articles-state/<int:listing_id>', views.bestclinicarticlesstate, name='bestclinicarticlesstate'),
    path('best-clinic-articles-country/<int:listing_id>', views.bestclinicarticlescountry, name='bestclinicarticlescountry'),

    path('activate-user', views.activateUser, name='activateUser'),

]
