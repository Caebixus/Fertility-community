from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone

# PRAGUE
def pragamedica(request):
    listing = BasicClinic.objects.get(pk=36)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/pragamedica.html', context)

def fertilityportx(request):
    listing = BasicClinic.objects.get(pk=600)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/fertilityport-prague.html', context)

def praguefertilitycentre(request):
    listing = BasicClinic.objects.get(pk=601)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/prague-fertility-centre.html', context)

def gynemfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=602)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/gynem-fertility-clinic.html', context)

def gennet(request):
    listing = BasicClinic.objects.get(pk=604)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/gennet.html', context)

def medicaltravelczechrep(request):
    listing = BasicClinic.objects.get(pk=605)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/medical-travel-czech-republic.html', context)

def pronatalplusprague(request):
    listing = BasicClinic.objects.get(pk=606)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-plus-prague6.html', context)

def pronatalsanatoriumprague(request):
    listing = BasicClinic.objects.get(pk=607)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-sanatorium-prague4.html', context)

def ivfcube(request):
    listing = BasicClinic.objects.get(pk=612)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Prague/ivf-cube.html', context)

# BRNO
def ivfzlinczechrep(request):
    listing = BasicClinic.objects.get(pk=603)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Brno/ivf-zlin-czech-republic.html', context)

def reprofitbrno(request):
    listing = BasicClinic.objects.get(pk=613)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Brno/reprofit-brno.html', context)

def reprogenesis(request):
    listing = BasicClinic.objects.get(pk=615)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Brno/reprogenesis.html', context)

# KOLÍN
def pronatalkolin(request):
    listing = BasicClinic.objects.get(pk=608)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Kolin/pronatal-kolin.html', context)

# ČESKÉ BUDĚJOVICE
def pronatalreproceskebudejovice(request):
    listing = BasicClinic.objects.get(pk=609)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Ceske-budejovice/pronatal-repro-ceske-budejovice.html', context)

# TEPLICE
def pronatalnordteplice(request):
    listing = BasicClinic.objects.get(pk=610)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Teplice/pronatal-nord-teplice.html', context)

# KARLOVY VARY
def pronatalspakarlovyvary(request):
    listing = BasicClinic.objects.get(pk=611)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Karlovy-vary/pronatal-spa-karlovy-vary.html', context)

# OSTRAVA
def reprofitostrava(request):
    listing = BasicClinic.objects.get(pk=614)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/CZ/Ostrava/reprofit-ostrava.html', context)
