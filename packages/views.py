from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION
from .choices import CATEGORY_PACKAGE
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from .models import Packages


def packages(request):
    listing = Packages.objects.all()

    context = {
        'listing': listing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'values': request.GET,
    }

    return render(request, 'packages/packages.html', context)

def searchpackages(request):
    if 'States' in request.GET:
        states = request.GET['States']

        if states == 'US':
            pro_queryset_list = Packages.objects.all()
            pro_queryset_list = pro_queryset_list.filter(packageClinic__clinicState='United States')

            context = {
                'listing': pro_queryset_list,
                'values': request.GET,
                }


            return render(request, 'packages/searching.html', context)

    context = {
        'listing': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'my_total_count': my_total_count,
        'values': request.GET,
        }

    return render(request, 'packages/searching.html', context)
