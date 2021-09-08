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

# PRAGUE
def pragamedica(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def fertilityportx(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def praguefertilitycentre(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def gynemfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def gennet(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def medicaltravelczechrep(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def pronatalplusprague(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def pronatalsanatoriumprague(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def ivfcube(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def medistella(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def europeivfprague(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# BRNO
def ivfzlinczechrep(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def reprofitbrno(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def reprogenesis(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# KOLÍN
def pronatalkolin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# ČESKÉ BUDĚJOVICE
def pronatalreproceskebudejovice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# TEPLICE
def pronatalnordteplice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# KARLOVY VARY
def pronatalspakarlovyvary(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

# OSTRAVA
def reprofitostrava(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))
