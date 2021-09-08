from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages, Package
from django.utils import timezone
from owners.models import ownerProInterested, ProUser
from datetime import datetime, timedelta
from guestblogging.models import GuestBlog, GuestAuthor

from searchLocationsCountries import views

#Nicosia
def cyprusivfcentre(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def britishcyprusivfhospital(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def eurocareivf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def dogusfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def pedieosivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

#Famagusta
def crownivfcyprus(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

#Girne
def dunyaivfcyprusfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def kyreniaivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))
