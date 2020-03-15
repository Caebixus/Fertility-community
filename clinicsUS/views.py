from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.utils import timezone

# Create your views here.
def wfi(request):
    listing = BasicClinic.objects.get(pk=1)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/western-fertility-institute.html', context)

def cifc(request):
    listing = BasicClinic.objects.get(pk=2)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/california-ivf-fertility-center.html', context)

def ncfmcr(request):
    listing = BasicClinic.objects.get(pk=3)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-roseville.html', context)

def ncfmcs(request):
    listing = BasicClinic.objects.get(pk=4)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

def liwla(request):
    listing = BasicClinic.objects.get(pk=5)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-west-los-angeles.html', context)

def lip(request):
    listing = BasicClinic.objects.get(pk=7)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-pasadena.html', context)

def lich(request):
    listing = BasicClinic.objects.get(pk=8)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-chino-hills.html', context)

def tcfrm(request):
    listing = BasicClinic.objects.get(pk=9)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Alabama/center-for-reproductive-medicine.html', context)

def af(request):
    listing = BasicClinic.objects.get(pk=10)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Alabama/alabama-fertility.html', context)

def tfc(request):
    listing = BasicClinic.objects.get(pk=11)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-scottsdale.html', context)

def tfg(request):
    listing = BasicClinic.objects.get(pk=12)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-glendale.html', context)

def tfm(request):
    listing = BasicClinic.objects.get(pk=13)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-mesa.html', context)

def sfc(request):
    listing = BasicClinic.objects.get(pk=14)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/southwest-fertility-center.html', context)

def afcs(request):
    listing = BasicClinic.objects.get(pk=15)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-scottsdale.html', context)

def afcm(request):
    listing = BasicClinic.objects.get(pk=16)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-mesa.html', context)

def aafrhs(request):
    listing = BasicClinic.objects.get(pk=17)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-scottsdale.html', context)

def aafrhg(request):
    listing = BasicClinic.objects.get(pk=18)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-gilbert.html', context)

def bris(request):
    listing = BasicClinic.objects.get(pk=19)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-scottsdale.html', context)

def brig(request):
    listing = BasicClinic.objects.get(pk=20)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-gilbert.html', context)

def biacs(request):
    listing = BasicClinic.objects.get(pk=21)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-scottsdale.html', context)

def biacch(request):
    listing = BasicClinic.objects.get(pk=22)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-chandler.html', context)

def biacp(request):
    listing = BasicClinic.objects.get(pk=23)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-peoria.html', context)

def biacf(request):
    listing = BasicClinic.objects.get(pk=24)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-flagstaff.html', context)

def ip(request):
    listing = BasicClinic.objects.get(pk=25)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/ivf-phoenix.html', context)

def ftc(request):
    listing = BasicClinic.objects.get(pk=26)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/fertility-treatment-center.html', context)

def arifc(request):
    listing = BasicClinic.objects.get(pk=27)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-reproductive-institute-fertility-clinic.html', context)
