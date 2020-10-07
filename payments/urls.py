from django.urls import path
from . import views

urlpatterns = [
    path('success-subscription', views.successpay, name='successpay'),
    path('payments/<int:listing_id>', views.payments, name='payments'),
    path('billing-info/<int:listing_id>', views.billinginfo, name='billinginfo'),
    path('billing-info-premium/<int:listing_id>', views.billinginfo1, name='billinginfo1'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('checkout-premium/<int:pk>', views.checkout1, name='checkout1'),
    path('checkout-random/<int:pk>', views.checkout2, name='checkout2'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
    ]
