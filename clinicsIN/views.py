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

#Bengalore
def kiraninfertilitycenterbengaluru(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def mannatfertilitycentre(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Gachibowli
def hyderabadwomenfertilitycentregachibowli(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Gurugram
def indiaivfclinicgurgaon(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Gwalior
def indiaivfclinicgwalior(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Haldwani
def indiaivfclinichaldwani(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))


#Hyderabad
def oasisfertilityhyderabadbanjarahills(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def oasisfertilityhyderabadsecunderabad(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def oasisfertilityhyderabaddilsukhnagar(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def oasisfertilityhyderabadgachibowli(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def oasisfertilityhyderabmiyapur(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def kiraninfertilitycenterhyderabad(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def kiraninfertilitycenterkothapet(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def hegdefertilitymalakpet(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Chennai
def oasisfertchennai(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def kiraninfertilitycenterchennai(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Jammu
def indiaivfclinicjammu(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Madhapur
def hegdehospitalmadhapur(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Meerut
def indiaivfclinicmeerut(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#New Delhi
def indiaivfclinicnewdelhi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def selectivfnewdelhi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def indiraivfcentredelhi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Noida
def indiaivfclinicnoida(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Pune
def oasisfertilitypune(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Ranchi
def oasisfertilityranchi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def indiaivfclinicranchi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Rohtak
def indiaivfclinicrohtak(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Vadodara
def oasisfertilityvadodara(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Vijayawada
def oasisfertilityvijayawada(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Visakhapatnam
def oasisfertilityvisakhapatnam(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

#Warangal
def oasisfertilitywarangal(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))
