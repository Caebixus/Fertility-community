from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.register, name='register'),
    path('signin', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create, name='create'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('claim', views.claimClinic, name='claim'),
    path('contactus', views.contactClinic, name='contactus'),
    path('upgrade2', views.upgrade2, name='upgrade2'),
    path('update/<int:listing_id>', views.update, name='update'),
    path('updateprice/<int:listing_id>', views.updatePricing, name='updatePricing'),
    path('updatepricepro/<int:listing_id>', views.updatePricingPro, name='updatePricingPro'),
    path('updatePro/<int:listing_id>', views.updatePro, name='updatePro'),
]
