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

#Thessaloniki
def newlifeivfclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryoclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryolab(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

#Athens
def serumivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def ivfathenscenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryolandivfcenterathens(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embiomedicalcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def mitosisivfclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def eugoniaassistedreproductionunit(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

#Chania
def mediterraneanfertilityinstitute(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))
