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

#Acapulco
def iregaacapulco(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Cancun
def fertilityclinicamericas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

def advancedfertilitycenterfertilitycentercancun(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

def newlifemexico(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

def iregacancun(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Centro
def embryogengertilitycenterguasave(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Mexico City
def enlistalofertilidadmexicociudaddemexico(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

def citmermedicinareproductiva(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Cualican-rosales
def embryogenfertilitycenterculiacan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Hermosillo
def embryogenfertilitycenterhermosillo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Mazatlan
def embryogenfertilitycentermazatlan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Mexicali
def mexicofertilitycenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Nogales
def embryogenfertilitycenternogales(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Nuevo Vallarta
def ivfvallarta(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

def surrogacymexico(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))

#Puebla
def iregapuebla(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicMexico'))
