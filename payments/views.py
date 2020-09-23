from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from .models import Customer
from packages.models import Packages
from owners.models import ownerProInterested, ProUser
from django.utils import timezone
from datetime import datetime
from django.core.mail import send_mail
from owners.decorators import allowed_users
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY
stripePublickKey = settings.STRIPE_PUBLIC_KEY

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def billinginfo(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    stripe_customer = stripe.Customer.create(name=instance.clinicName, email=instance.contact_email)

    customer = Customer()
    customerClinic = instance.pk
    customer.stripeid = stripe_customer.id
    customer.save()

    session = stripe.checkout.Session.create(
      payment_method_types=['card'],
      line_items=[{
        'price': 'plan_HJuupx4J7RzP6K',
        'quantity': 1,
      }],
      customer='customer.id',
      mode='subscription',
      billing_address_collection='required',
      success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id={CHECKOUT_SESSION_ID}',
      cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )

    context = {
        'instance': instance,
        'session_id': session.id,
        'stripe_public_key': stripePublickKey,
    }

    return render(request, 'owners/payments/billinginfo.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def monthly(request):
    return render(request, 'owners/payments/billinginfo.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def successpay(request):
    return render(request, 'owners/payments/successpay.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def checkout(request):
    return render(request, 'owners/payments/successpay.html')

@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_Ab0RoJj4Mhh4JKzF7GQxEs3dFv8qNObT'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)
