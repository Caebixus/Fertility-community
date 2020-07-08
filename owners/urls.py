from django.urls import path
from django.contrib.auth.forms import PasswordChangeForm

from . import views

urlpatterns = [
    path('signup', views.register, name='register'),
    path('signin', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('settings', views.settings, name='settings'),
    path('payments', views.payments, name='payments'),
    path('banners', views.banners, name='banners'),
    path('create1', views.create1, name='create1'),
    path('create', views.create, name='create'),
    path('packages', views.packages, name='packages'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('claim', views.claimClinic, name='claim'),
    path('change-password', views.change_password, name='change-password'),
    path('contactus', views.contactClinic, name='contactus'),
    path('upgrade2', views.upgrade2, name='upgrade2'),
    path('update/<int:listing_id>', views.update, name='update'),
    path('updateprice/<int:listing_id>', views.updatePricing, name='updatePricing'),
    path('updatepricepro/<int:listing_id>', views.updatePricingPro, name='updatePricingPro'),
    path('updatepro/<int:listing_id>', views.updateproclinic, name='updateproclinic'),
]
