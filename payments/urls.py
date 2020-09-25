from django.urls import path
from . import views

urlpatterns = [
    path('success-subscription', views.successpay, name='successpay'),
    path('payments/<int:listing_id>', views.payments, name='payments'),
    path('billing-info/<int:listing_id>', views.billinginfo, name='billinginfo'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
    ]
