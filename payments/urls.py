from django.urls import path
from . import views

urlpatterns = [
    path('success-subscription', views.successpay, name='successpay'),
    path('billing-info/<int:listing_id>', views.billinginfo, name='billinginfo'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
    ]
