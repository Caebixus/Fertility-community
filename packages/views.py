from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_US_REGION
from location.currencies import gbpToEur, gbpToUsd, gbpToInr, usdToGbp, usdToEur, usdToInr, eurToGbp, eurToUsd, eurToInr, inrToGbp, inrToEur, inrToUsd
from .packageChoices import CATEGORY_PACKAGE
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from .models import Package
from datetime import datetime, timedelta
from django.utils import timezone


def packages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def ivfpackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def eggpackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def embryopackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))
