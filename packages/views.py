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
from .models import Package
from datetime import datetime, timedelta
from django.utils import timezone

def packages(request):
    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
    count = listing.count()

    prolisting = prolisting.order_by('package_end_list_date')
    ppqlisting = ppqlisting.order_by('package_end_list_date')

    order_data = list(ppqlisting) + list(prolisting)

    paginator = Paginator(order_data, 25)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listing': listing,
        'count': count,
        'order_data': paginationing,
        'paginationing': paginationing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'values': request.GET,
    }

    return render(request, 'packages/packages.html', context)

def ivfpackages(request):
    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='IVF packages')
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='IVF packages')
    count = listing.count()

    prolisting = prolisting.order_by('package_end_list_date')
    ppqlisting = ppqlisting.order_by('package_end_list_date')

    order_data = list(ppqlisting) + list(prolisting)

    paginator = Paginator(order_data, 25)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listing': listing,
        'count': count,
        'order_data': paginationing,
        'paginationing': paginationing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'values': request.GET,
    }

    return render(request, 'packages/ivf-packages.html', context)

def eggpackages(request):
    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='Egg Donation')
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='Egg Donation')
    count = listing.count()

    prolisting = prolisting.order_by('package_end_list_date')
    ppqlisting = ppqlisting.order_by('package_end_list_date')

    order_data = list(ppqlisting) + list(prolisting)

    paginator = Paginator(order_data, 25)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listing': listing,
        'count': count,
        'order_data': paginationing,
        'paginationing': paginationing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'values': request.GET,
    }

    return render(request, 'packages/ivf-with-donor-eggs-packages.html', context)



def embryopackages(request):
    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='Embryo Donation')
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False).filter(packagecategory='Embryo Donation')
    count = listing.count()

    prolisting = prolisting.order_by('package_end_list_date')
    ppqlisting = ppqlisting.order_by('package_end_list_date')

    order_data = list(ppqlisting) + list(prolisting)

    paginator = Paginator(order_data, 25)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listing': listing,
        'count': count,
        'order_data': paginationing,
        'paginationing': paginationing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'values': request.GET,
    }
    return render(request, 'packages/ivf-with-donor-embryo-packages.html', context)


# Locations US ------------------------

def ivfpackagesus(request):
    return render(request, 'packages/packages.html')

def embryopackagesus(request):
    return render(request, 'packages/packages.html')

def eggpackagesus(request):
    return render(request, 'packages/packages.html')

# Locations UK ------------------------

def ivfpackagesuk(request):
    return render(request, 'packages/packages.html')

def embryopackagesuk(request):
    return render(request, 'packages/packages.html')

def eggpackagesuk(request):
    return render(request, 'packages/packages.html')

# Locations ES ------------------------

def ivfpackagessp(request):
    return render(request, 'packages/packages.html')

def embryopackagessp(request):
    return render(request, 'packages/packages.html')

def eggpackagessp(request):
    return render(request, 'packages/packages.html')

# Locations CZ ------------------------

def ivfpackagescz(request):
    return render(request, 'packages/packages.html')

def embryopackagescz(request):
    return render(request, 'packages/packages.html')

def eggpackagescz(request):
    return render(request, 'packages/packages.html')

# Locations GR ------------------------

def ivfpackagesgr(request):
    return render(request, 'packages/packages.html')

def embryopackagesgr(request):
    return render(request, 'packages/packages.html')

def eggpackagesgr(request):
    return render(request, 'packages/packages.html')

# Locations IN ------------------------

def ivfpackagesin(request):
    return render(request, 'packages/packages.html')

def embryopackagesin(request):
    return render(request, 'packages/packages.html')

def eggpackagesin(request):
    return render(request, 'packages/packages.html')
