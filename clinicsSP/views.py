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

#ALICANTE   --------------------------------
def ivfspainalicante(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ivialicante(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

#BARCELONA   --------------------------------
def clinicadefertilidadbarcelonaivf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ferttyinternational(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fertilabbarcelona(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def institutmarquesbarcelona(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ivfforyou(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def gravida(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ivibarcelona(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fivmarbellabarcelona(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

#MADRID   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivfspainmadrid(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fertilitymadrid(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def evafertilityclinicmadrid(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ivimadridaravaca(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def clinicatambre(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fertilityclinichru(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fivmarbellamadrid(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

#MALAGA   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivimalaga(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fivmarbellamalaga(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def hcfertility(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def clinicafertia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

#SEVILLE   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivisevilla(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def inebir(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def ginemedsevilla(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

#VALENCIA   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivivalencia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def equipojuanacrespo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def unidaddereproduccionasistidaimedvalencia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def creavalencia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def imerinstitutodemedicinareproductiva(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))
