from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone
from owners.models import ownerProInterested, ProUser

# Create your views here.
def aberfercen(request):
    listing = BasicClinic.objects.get(pk=506)

    aberdeenclisting = BasicClinic.objects.all()
    aberdeenclisting = aberdeenclisting.filter(is_published=True)
    aberdeenclisting = aberdeenclisting.filter(clinicRegion__iexact='Aberdeen')
    aberdeenclisting = aberdeenclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=506)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'aberdeenclisting': aberdeenclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Aberdeen/aberdeen-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'aberdeenclisting': aberdeenclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Aberdeen/aberdeen-fertility-centre.html', context)

#BATH   --------------------------------
def carefertbath(request):
    listing = BasicClinic.objects.get(pk=507)

    bathlisting = BasicClinic.objects.all()
    bathlisting = bathlisting.filter(is_published=True)
    bathlisting = bathlisting.filter(clinicRegion__iexact='Bath')
    bathlisting = bathlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=507)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bathlisting': bathlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bath/care-fertility-bath.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bathlisting': bathlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bath/care-fertility-bath.html', context)

#BELFAST   --------------------------------

def belffert(request):
    listing = BasicClinic.objects.get(pk=508)

    belfastclisting = BasicClinic.objects.all()
    belfastclisting = belfastclisting.filter(is_published=True)
    belfastclisting = belfastclisting.filter(clinicRegion__iexact='Belfast')
    belfastclisting = belfastclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=508)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'belfastclisting': belfastclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Belfast/belfast-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'belfastclisting': belfastclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Belfast/belfast-fertility.html', context)

#BIRMINGHAM   --------------------------------

def carefertbirmingh(request):
    listing = BasicClinic.objects.get(pk=509)

    birminghamclisting = BasicClinic.objects.all()
    birminghamclisting = birminghamclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=509)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/care-fertility-birmingham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-birmingham.html', context)

def createfertbirmin(request):
    listing = BasicClinic.objects.get(pk=510)

    birminghamclisting = BasicClinic.objects.all()
    birminghamclisting = birminghamclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=510)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/create-fertility-birmingham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/create-fertility-birmingham.html', context)

def bmitheprioryhosp(request):
    listing = BasicClinic.objects.get(pk=511)

    birminghamclisting = BasicClinic.objects.all()
    birminghamclisting = birminghamclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=511)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/bmi-the-priory-hospital.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/bmi-the-priory-hospital.html', context)

def careferttamworth(request):
    listing = BasicClinic.objects.get(pk=512)

    birminghamclisting = BasicClinic.objects.all()
    birminghamclisting = birminghamclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=512)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/care-fertility-tamworth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-tamworth.html', context)

def stjudesfertclinic(request):
    listing = BasicClinic.objects.get(pk=513)

    birminghamclisting = BasicClinic.objects.all()
    birminghamclisting = birminghamclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=513)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/st-judes-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/st-judes-fertility-clinic.html', context)

#BOURNEMOUTH   --------------------------------

def completefertcentbourn(request):
    listing = BasicClinic.objects.get(pk=514)

    bournemouthclisting = BasicClinic.objects.all()
    bournemouthclisting = bournemouthclisting.filter(is_published=True)
    bournemouthclisting = bournemouthclisting.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclisting = bournemouthclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=514)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bournemouthclisting': bournemouthclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bournemouth/complete-fertility-centre-bournemouth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bournemouthclisting': bournemouthclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bournemouth/complete-fertility-centre-bournemouth.html', context)

def poundburyfertdorset(request):
    listing = BasicClinic.objects.get(pk=515)

    bournemouthclisting = BasicClinic.objects.all()
    bournemouthclisting = bournemouthclisting.filter(is_published=True)
    bournemouthclisting = bournemouthclisting.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclisting = bournemouthclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=515)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bournemouthclisting': bournemouthclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bournemouth/poundbury-fertility-dorset.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bournemouthclisting': bournemouthclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bournemouth/poundbury-fertility-dorset.html', context)

#BRIGHTON   --------------------------------

def brightfertasso(request):
    listing = BasicClinic.objects.get(pk=516)

    brightonclisting = BasicClinic.objects.all()
    brightonclisting = brightonclisting.filter(is_published=True)
    brightonclisting = brightonclisting.filter(clinicRegion__iexact='Brighton')
    brightonclisting = brightonclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=516)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'brightonclisting': brightonclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Brighton/brighton-fertility-associates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'brightonclisting': brightonclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Brighton/brighton-fertility-associates.html', context)

def agoragynandfertcentre(request):
    listing = BasicClinic.objects.get(pk=517)

    brightonclisting = BasicClinic.objects.all()
    brightonclisting = brightonclisting.filter(is_published=True)
    brightonclisting = brightonclisting.filter(clinicRegion__iexact='Brighton')
    brightonclisting = brightonclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=517)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'brightonclisting': brightonclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Brighton/agora-gynaecology-and-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'brightonclisting': brightonclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Brighton/agora-gynaecology-and-fertility-centre.html', context)

#BRISTOL   --------------------------------

def abcivfbristol(request):
    listing = BasicClinic.objects.get(pk=518)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=518)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/abc-ivf-bristol.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/abc-ivf-bristol.html', context)

def bristolcentreforrepromedicine(request):
    listing = BasicClinic.objects.get(pk=519)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=519)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine.html', context)

def crgwbristol(request):
    listing = BasicClinic.objects.get(pk=520)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=520)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/crgw-bristol.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/crgw-bristol.html', context)

def createfertbristol(request):
    listing = BasicClinic.objects.get(pk=521)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=521)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/create-fertility-bristol.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/create-fertility-bristol.html', context)

def bristolcenforrepromedspireclinic(request):
    listing = BasicClinic.objects.get(pk=522)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=522)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine-spire-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine-spire-clinic.html', context)

def londonwomensclinicbristol(request):
    listing = BasicClinic.objects.get(pk=523)

    bristolclisting = BasicClinic.objects.all()
    bristolclisting = bristolclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=523)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/london-womens-clinic-bristol.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/london-womens-clinic-bristol.html', context)

#CAMBRIDGE   --------------------------------

def bournhallcliniccambridge(request):
    listing = BasicClinic.objects.get(pk=524)

    cambridgeclisting = BasicClinic.objects.all()
    cambridgeclisting = cambridgeclisting.filter(is_published=True)
    cambridgeclisting = cambridgeclisting.filter(clinicRegion__iexact='Cambridge')
    cambridgeclisting = cambridgeclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=524)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'cambridgeclisting': cambridgeclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cambridge/bourn-hall-clinic-cambridge.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'cambridgeclisting': cambridgeclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cambridge/bourn-hall-clinic-cambridge.html', context)

def cambridgeivf(request):
    listing = BasicClinic.objects.get(pk=525)

    cambridgeclisting = BasicClinic.objects.all()
    cambridgeclisting = cambridgeclisting.filter(is_published=True)
    cambridgeclisting = cambridgeclisting.filter(clinicRegion__iexact='Cambridge')
    cambridgeclisting = cambridgeclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=525)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'cambridgeclisting': cambridgeclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cambridge/cambridge-ivf.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'cambridgeclisting': cambridgeclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cambridge/cambridge-ivf.html', context)

#CARDIFF   --------------------------------

def crgwcardiff(request):
    listing = BasicClinic.objects.get(pk=526)

    cardiffclisting = BasicClinic.objects.all()
    cardiffclisting = cardiffclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=526)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/crgw-cardiff.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'cardiffclisting': cardiffclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cardiff/crgw-cardiff.html', context)

def londonwomenscliniccardiff(request):
    listing = BasicClinic.objects.get(pk=527)

    cardiffclisting = BasicClinic.objects.all()
    cardiffclisting = cardiffclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=527)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/london-womens-clinic-cardiff.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'cardiffclisting': cardiffclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cardiff/london-womens-clinic-cardiff.html', context)

def walesfertilityinstitutecardiff(request):
    listing = BasicClinic.objects.get(pk=528)

    cardiffclisting = BasicClinic.objects.all()
    cardiffclisting = cardiffclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=528)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/wales-fertility-institute-cardiff.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'cardiffclisting': cardiffclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cardiff/wales-fertility-institute-cardiff.html', context)

#COLCHESTER   --------------------------------

def bournhallcliniccolchester(request):
    listing = BasicClinic.objects.get(pk=529)

    colchesterclisting = BasicClinic.objects.all()
    colchesterclisting = colchesterclisting.filter(is_published=True)
    colchesterclisting = colchesterclisting.filter(clinicRegion__iexact='Colchester')
    colchesterclisting = colchesterclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=529)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'colchesterclisting': colchesterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Colchester/bourn-hall-clinic-colchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'colchesterclisting': colchesterclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Colchester/bourn-hall-clinic-colchester.html', context)

#DERBY   --------------------------------

def nurturefertburtsatclinic(request):
    listing = BasicClinic.objects.get(pk=530)

    derbyclisting = BasicClinic.objects.all()
    derbyclisting = derbyclisting.filter(is_published=True)
    derbyclisting = derbyclisting.filter(clinicRegion__iexact='Derby')
    derbyclisting = derbyclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=530)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'derbyclisting': derbyclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Derby/nurture-fertility-burton-satellite-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'derbyclisting': derbyclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Derby/nurture-fertility-burton-satellite-clinic.html', context)

#EXETER   --------------------------------

def fertilityexeter(request):
    listing = BasicClinic.objects.get(pk=531)

    exeterclisting = BasicClinic.objects.all()
    exeterclisting = exeterclisting.filter(is_published=True)
    exeterclisting = exeterclisting.filter(clinicRegion__iexact='Exeter')
    exeterclisting = exeterclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=531)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'exeterclisting': exeterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Exeter/fertility-exeter.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'exeterclisting': exeterclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Exeter/fertility-exeter.html', context)

#GLASGOW   --------------------------------

def gcrmfertilityglasgow(request):
    listing = BasicClinic.objects.get(pk=532)

    glasgowclisting = BasicClinic.objects.all()
    glasgowclisting = glasgowclisting.filter(is_published=True)
    glasgowclisting = glasgowclisting.filter(clinicRegion__iexact='Glasgow')
    glasgowclisting = glasgowclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=532)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'glasgowclisting': glasgowclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Glasgow/gcrm-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'glasgowclisting': glasgowclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Glasgow/gcrm-fertility.html', context)

def semovoglasgow(request):
    listing = BasicClinic.objects.get(pk=533)

    glasgowclisting = BasicClinic.objects.all()
    glasgowclisting = glasgowclisting.filter(is_published=True)
    glasgowclisting = glasgowclisting.filter(clinicRegion__iexact='Glasgow')
    glasgowclisting = glasgowclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=533)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'glasgowclisting': glasgowclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Glasgow/semovo-glasgow.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'glasgowclisting': glasgowclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Glasgow/semovo-glasgow.html', context)

#KINGSTON UPON HULL   --------------------------------

def hullivfunit(request):
    listing = BasicClinic.objects.get(pk=534)

    kingstonuponhillwclisting = BasicClinic.objects.all()
    kingstonuponhillwclisting = kingstonuponhillwclisting.filter(is_published=True)
    kingstonuponhillwclisting = kingstonuponhillwclisting.filter(clinicRegion__iexact='Hull')
    kingstonuponhillwclisting = kingstonuponhillwclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=534)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'kingstonuponhillwclisting': kingstonuponhillwclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Kingstonuponhill/hull-ivf-unit.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'kingstonuponhillwclisting': kingstonuponhillwclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Kingstonuponhill/hull-ivf-unit.html', context)

#CHELMSFORD   --------------------------------

def simplyfertilitychelm(request):
    listing = BasicClinic.objects.get(pk=535)

    chelmsfordclisting = BasicClinic.objects.all()
    chelmsfordclisting = chelmsfordclisting.filter(is_published=True)
    chelmsfordclisting = chelmsfordclisting.filter(clinicRegion__iexact='Chelmsford')
    chelmsfordclisting = chelmsfordclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=535)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'chelmsfordclisting': chelmsfordclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Chelmsford/simply-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Chelmsford/simply-fertility.html', context)

def bournhallclinicwockford(request):
    listing = BasicClinic.objects.get(pk=536)

    chelmsfordclisting = BasicClinic.objects.all()
    chelmsfordclisting = chelmsfordclisting.filter(is_published=True)
    chelmsfordclisting = chelmsfordclisting.filter(clinicRegion__iexact='Chelmsford')
    chelmsfordclisting = chelmsfordclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=536)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'chelmsfordclisting': chelmsfordclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Chelmsford/bourn-hall-clinic-wickford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Chelmsford/bourn-hall-clinic-wickford.html', context)

def carefertilitychester(request):
    listing = BasicClinic.objects.get(pk=537)

    chelmsfordclisting = BasicClinic.objects.all()
    chelmsfordclisting = chelmsfordclisting.filter(is_published=True)
    chelmsfordclisting = chelmsfordclisting.filter(clinicRegion__iexact='Chelmsford')
    chelmsfordclisting = chelmsfordclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=537)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'chelmsfordclisting': chelmsfordclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/care-fertility-chester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/care-fertility-chester.html', context)

#LEEDS   --------------------------------

def leedsfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=538)

    leedsclisting = BasicClinic.objects.all()
    leedsclisting = leedsclisting.filter(is_published=True)
    leedsclisting = leedsclisting.filter(clinicRegion__iexact='Leeds')
    leedsclisting = leedsclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=538)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'leedsclisting': leedsclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leeds/leeds-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'leedsclisting': leedsclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Leeds/leeds-fertility-clinic.html', context)

def semovoleeds(request):
    listing = BasicClinic.objects.get(pk=539)

    leedsclisting = BasicClinic.objects.all()
    leedsclisting = leedsclisting.filter(is_published=True)
    leedsclisting = leedsclisting.filter(clinicRegion__iexact='Leeds')
    leedsclisting = leedsclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=539)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'leedsclisting': leedsclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leeds/semovo-leeds.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'leedsclisting': leedsclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Leeds/semovo-leeds.html', context)

#LEICESTER   --------------------------------

def xyfertility(request):
    listing = BasicClinic.objects.get(pk=540)

    leicesterclisting = BasicClinic.objects.all()
    leicesterclisting = leicesterclisting.filter(is_published=True)
    leicesterclisting = leicesterclisting.filter(clinicRegion__iexact='Leicester')
    leicesterclisting = leicesterclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=540)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'leicesterclisting': leicesterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leicester/xy-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'leicesterclisting': leicesterclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Leicester/xy-fertility.html', context)

#LIVERPOOL   --------------------------------

def carefertilityliverpool(request):
    listing = BasicClinic.objects.get(pk=541)

    liverpoolclisting = BasicClinic.objects.all()
    liverpoolclisting = liverpoolclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=541)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/care-fertility-liverpool.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/care-fertility-liverpool.html', context)

def thehewittfertilitycentreliverpool(request):
    listing = BasicClinic.objects.get(pk=542)

    liverpoolclisting = BasicClinic.objects.all()
    liverpoolclisting = liverpoolclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=542)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/the-hewitt-fertility-centre-liverpool.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/the-hewitt-fertility-centre-liverpool.html', context)

def semovoliverpool(request):
    listing = BasicClinic.objects.get(pk=543)

    liverpoolclisting = BasicClinic.objects.all()
    liverpoolclisting = liverpoolclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=543)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/semovo-liverpool.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/semovo-liverpool.html', context)

def centreforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=544)

    liverpoolclisting = BasicClinic.objects.all()
    liverpoolclisting = liverpoolclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=544)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/centre-for-reproductive-health.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/centre-for-reproductive-health.html', context)

#LONDON   --------------------------------

def londonwomensclinicbrentwood(request):
    listing = BasicClinic.objects.get(pk=545)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=545)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-brentwood.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-brentwood.html', context)

def londonwomensclinicharrow(request):
    listing = BasicClinic.objects.get(pk=546)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=546)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-harrow.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harrow.html', context)

def abcivfharleystreet(request):
    listing = BasicClinic.objects.get(pk=547)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=547)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/abc-ivf-harley-street.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/abc-ivf-harley-street.html', context)

def abcivfwimbledon(request):
    listing = BasicClinic.objects.get(pk=548)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=548)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/abc-ivf-wimbledon.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/abc-ivf-wimbledon.html', context)

def assistedreproandgynaecologycentre(request):
    listing = BasicClinic.objects.get(pk=549)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=549)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/assisted-reproduction-and-gynaecology-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/assisted-reproduction-and-gynaecology-centre.html', context)

def cityfertility(request):
    listing = BasicClinic.objects.get(pk=550)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=550)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/city-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/city-fertility.html', context)

def createfertistpauls(request):
    listing = BasicClinic.objects.get(pk=551)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=551)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-st-pauls.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/create-fertility-st-pauls.html', context)

def fertilityplusfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=552)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=552)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/fertility-plus-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/fertility-plus-fertility-clinic.html', context)

def londonwomensclinicharleystreet(request):
    listing = BasicClinic.objects.get(pk=553)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=553)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-harley-street.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harley-street.html', context)

def poundburyfertilitylondon(request):
    listing = BasicClinic.objects.get(pk=554)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=554)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/poundbury-fertility-london.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/poundbury-fertility-london.html', context)

def semovolondon(request):
    listing = BasicClinic.objects.get(pk=555)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=555)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/semovo-london.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/semovo-london.html', context)

def londonwomenscliniclondonbridge(request):
    listing = BasicClinic.objects.get(pk=556)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=556)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-london-bridge.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-london-bridge.html', context)

def thamesvalleyfertility(request):
    listing = BasicClinic.objects.get(pk=557)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=557)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/thames-valley-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/thames-valley-fertility.html', context)

def ivflondonelstree(request):
    listing = BasicClinic.objects.get(pk=558)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=558)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/ivf-london-elstree.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/ivf-london-elstree.html', context)

def hertsandessexfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=559)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=559)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/herts-and-essex-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/herts-and-essex-fertility-centre.html', context)

def bostonplace(request):
    listing = BasicClinic.objects.get(pk=560)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=560)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/boston-place.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/boston-place.html', context)

def carefertilitylondon(request):
    listing = BasicClinic.objects.get(pk=561)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=561)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/care-fertility-london.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/care-fertility-london.html', context)

def conceptfertility(request):
    listing = BasicClinic.objects.get(pk=562)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=562)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/concept-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/concept-fertility.html', context)

def createfertilitywimbledon(request):
    listing = BasicClinic.objects.get(pk=563)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=563)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-wimbledon.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/create-fertility-wimbledon.html', context)

def evewell(request):
    listing = BasicClinic.objects.get(pk=564)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=564)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/evewell.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/evewell.html', context)

def thefertilitygynaecologyacademy(request):
    listing = BasicClinic.objects.get(pk=565)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=565)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/the-fertility-gynaecology-academy.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/the-fertility-gynaecology-academy.html', context)

def harleystreetfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=566)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=566)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/harley-street-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/harley-street-fertility-clinic.html', context)

def homertonfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=567)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=567)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/homerton-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/homerton-fertility-centre.html', context)

def ivilondon(request):
    listing = BasicClinic.objects.get(pk=568)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=568)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/ivi-london.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/ivi-london.html', context)

def kingsfertility(request):
    listing = BasicClinic.objects.get(pk=569)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=569)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/kings-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/kings-fertility.html', context)

def listerfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=570)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=570)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/lister-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/lister-fertility-clinic.html', context)

def createfertilityhertfordshire(request):
    listing = BasicClinic.objects.get(pk=571)

    londonlisting = BasicClinic.objects.all()
    londonlisting = londonlisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=571)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-hertfordshire.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/create-fertility-hertfordshire.html', context)

#MANCHESTER   --------------------------------

def manchesterfertility(request):
    listing = BasicClinic.objects.get(pk=572)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=572)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/manchester-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/manchester-fertility.html', context)

def semovomanchestersouth(request):
    listing = BasicClinic.objects.get(pk=573)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=573)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/semovo-manchester-south.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-south.html', context)

def thehewittfertilitycentreknutsford(request):
    listing = BasicClinic.objects.get(pk=574)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=574)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/the-hewitt-fertility-centre-knutsford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/the-hewitt-fertility-centre-knutsford.html', context)

def aurorareprohealthaltrincham(request):
    listing = BasicClinic.objects.get(pk=575)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=575)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/aurora-reproductive-healthcare-altrincham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/aurora-reproductive-healthcare-altrincham.html', context)

def abcivfmanchester(request):
    listing = BasicClinic.objects.get(pk=576)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=576)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/abc-ivf-manchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/abc-ivf-manchester.html', context)

def createfertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=577)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=577)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/create-fertility-manchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/create-fertility-manchester.html', context)

def semovomanchestercitycentre(request):
    listing = BasicClinic.objects.get(pk=578)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=578)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/semovo-manchester-city-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-city-centre.html', context)

def fertilityfusion(request):
    listing = BasicClinic.objects.get(pk=579)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=579)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/fertility-fusion.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/fertility-fusion.html', context)

def carefertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=580)

    manchesterlisting = BasicClinic.objects.all()
    manchesterlisting = manchesterlisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=580)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/care-fertility-manchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/care-fertility-manchester.html', context)

#MIDDLESBROUGH   --------------------------------

def londonwomensclinicdarlington(request):
    listing = BasicClinic.objects.get(pk=581)

    middlesbroughlisting = BasicClinic.objects.all()
    middlesbroughlisting = middlesbroughlisting.filter(is_published=True)
    middlesbroughlisting = middlesbroughlisting.filter(clinicRegion__iexact='Middlesbrough')
    middlesbroughlisting = middlesbroughlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=581)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'middlesbroughlisting': middlesbroughlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Middlesbrough/london-womens-clinic-darlington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'middlesbroughlisting': middlesbroughlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Middlesbrough/london-womens-clinic-darlington.html', context)

#NEWCASTLE   --------------------------------

def newcastlefertilitycentre(request):
    listing = BasicClinic.objects.get(pk=582)

    newcastlelisting = BasicClinic.objects.all()
    newcastlelisting = newcastlelisting.filter(is_published=True)
    newcastlelisting = newcastlelisting.filter(clinicRegion__iexact='Newcastle')
    newcastlelisting = newcastlelisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=582)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcastlelisting': newcastlelisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Newcastle/newcastle-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcastlelisting': newcastlelisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Newcastle/newcastle-fertility-centre.html', context)

#NORWICH   --------------------------------

def bournhallclinicnorwich(request):
    listing = BasicClinic.objects.get(pk=583)

    norwichlisting = BasicClinic.objects.all()
    norwichlisting = norwichlisting.filter(is_published=True)
    norwichlisting = norwichlisting.filter(clinicRegion__iexact='Norwich')
    norwichlisting = norwichlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=583)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'norwichlisting': norwichlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Norwich/bourn-hall-clinic-norwich.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'norwichlisting': norwichlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Norwich/bourn-hall-clinic-norwich.html', context)

#NOTTINGHAM   --------------------------------

def nurturefertilitynottingham(request):
    listing = BasicClinic.objects.get(pk=584)

    nottinghamlisting = BasicClinic.objects.all()
    nottinghamlisting = nottinghamlisting.filter(is_published=True)
    nottinghamlisting = nottinghamlisting.filter(clinicRegion__iexact='Nottingham')
    nottinghamlisting = nottinghamlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=584)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nottinghamlisting': nottinghamlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Nottingham/nurture-fertility-nottingham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nottinghamlisting': nottinghamlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Nottingham/nurture-fertility-nottingham.html', context)

def carefertilitynottingham(request):
    listing = BasicClinic.objects.get(pk=585)

    nottinghamlisting = BasicClinic.objects.all()
    nottinghamlisting = nottinghamlisting.filter(is_published=True)
    nottinghamlisting = nottinghamlisting.filter(clinicRegion__iexact='Nottingham')
    nottinghamlisting = nottinghamlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=585)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nottinghamlisting': nottinghamlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Nottingham/care-fertility-nottingham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nottinghamlisting': nottinghamlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Nottingham/care-fertility-nottingham.html', context)

#OXFORD   --------------------------------

def createfertilityoxford(request):
    listing = BasicClinic.objects.get(pk=586)

    oxfordlisting = BasicClinic.objects.all()
    oxfordlisting = oxfordlisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=586)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/create-fertility-oxford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oxfordlisting': oxfordlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Oxford/create-fertility-oxford.html', context)

def oxfordfertility(request):
    listing = BasicClinic.objects.get(pk=587)

    oxfordlisting = BasicClinic.objects.all()
    oxfordlisting = oxfordlisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=587)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/oxford-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oxfordlisting': oxfordlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Oxford/oxford-fertility.html', context)

def abcivfoxford(request):
    listing = BasicClinic.objects.get(pk=588)

    oxfordlisting = BasicClinic.objects.all()
    oxfordlisting = oxfordlisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=588)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/abc-ivf-oxford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oxfordlisting': oxfordlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Oxford/abc-ivf-oxford.html', context)

#PETERBOROUGH   --------------------------------

def bournhallclinicpeterborough(request):
    listing = BasicClinic.objects.get(pk=589)

    peterboroughlisting = BasicClinic.objects.all()
    peterboroughlisting = peterboroughlisting.filter(is_published=True)
    peterboroughlisting = peterboroughlisting.filter(clinicRegion__iexact='Peterborough')
    peterboroughlisting = peterboroughlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=589)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'peterboroughlisting': peterboroughlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Peterborough/bourn-hall-clinic-peterborough.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'peterboroughlisting': peterboroughlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Peterborough/bourn-hall-clinic-peterborough.html', context)

#PLYMOUTH   --------------------------------

def crgwplymouth(request):
    listing = BasicClinic.objects.get(pk=590)

    plymouthlisting = BasicClinic.objects.all()
    plymouthlisting = plymouthlisting.filter(is_published=True)
    plymouthlisting = plymouthlisting.filter(clinicRegion__iexact='Plymouth')
    plymouthlisting = plymouthlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=590)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'plymouthlisting': plymouthlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Plymouth/crgw-plymouth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'plymouthlisting': plymouthlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Plymouth/crgw-plymouth.html', context)

#PORTSMOUTH   --------------------------------

def completefertilitycentreportsmouth(request):
    listing = BasicClinic.objects.get(pk=591)

    portsmouthlisting = BasicClinic.objects.all()
    portsmouthlisting = portsmouthlisting.filter(is_published=True)
    portsmouthlisting = portsmouthlisting.filter(clinicRegion__iexact='Portsmouth')
    portsmouthlisting = portsmouthlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=591)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'portsmouthlisting': portsmouthlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Portsmouth/complete-fertility-centre-portsmouth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'portsmouthlisting': portsmouthlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Portsmouth/complete-fertility-centre-portsmouth.html', context)

#SALISBURY   --------------------------------

def salisburyfertcentre(request):
    listing = BasicClinic.objects.get(pk=592)

    salisburylisting = BasicClinic.objects.all()
    salisburylisting = salisburylisting.filter(is_published=True)
    salisburylisting = salisburylisting.filter(clinicRegion__iexact='Salisbury')
    salisburylisting = salisburylisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=592)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'salisburylisting': salisburylisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Salisbury/salisbury-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'salisburylisting': salisburylisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Salisbury/salisbury-fertility-centre.html', context)

#SHEFFIELD   --------------------------------

def nurturefertilitychesterfield(request):
    listing = BasicClinic.objects.get(pk=593)

    sheffieldlisting = BasicClinic.objects.all()
    sheffieldlisting = sheffieldlisting.filter(is_published=True)
    sheffieldlisting = sheffieldlisting.filter(clinicRegion__iexact='Sheffield')
    sheffieldlisting = sheffieldlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=593)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'sheffieldlisting': sheffieldlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Sheffield/nurture-fertility-chesterfield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'sheffieldlisting': sheffieldlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Sheffield/nurture-fertility-chesterfield.html', context)

def carefertilitysheffield(request):
    listing = BasicClinic.objects.get(pk=594)

    sheffieldlisting = BasicClinic.objects.all()
    sheffieldlisting = sheffieldlisting.filter(is_published=True)
    sheffieldlisting = sheffieldlisting.filter(clinicRegion__iexact='Sheffield')
    sheffieldlisting = sheffieldlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=594)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'sheffieldlisting': sheffieldlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Sheffield/care-fertility-sheffield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'sheffieldlisting': sheffieldlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Sheffield/care-fertility-sheffield.html', context)

#SOUTHAMPTON   --------------------------------

def completefertilitycentresouthampton(request):
    listing = BasicClinic.objects.get(pk=595)

    southamptonlisting = BasicClinic.objects.all()
    southamptonlisting = southamptonlisting.filter(is_published=True)
    southamptonlisting = southamptonlisting.filter(clinicRegion__iexact='Southampton')
    southamptonlisting = southamptonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=595)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southamptonlisting': southamptonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Southampton/complete-fertility-centre-southampton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southamptonlisting': southamptonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Southampton/complete-fertility-centre-southampton.html', context)

def wessexfertility(request):
    listing = BasicClinic.objects.get(pk=596)

    southamptonlisting = BasicClinic.objects.all()
    southamptonlisting = southamptonlisting.filter(is_published=True)
    southamptonlisting = southamptonlisting.filter(clinicRegion__iexact='Southampton')
    southamptonlisting = southamptonlisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=596)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southamptonlisting': southamptonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Southampton/wessex-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southamptonlisting': southamptonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Southampton/wessex-fertility.html', context)

#SWANSEA   --------------------------------

def walesfertilityinstituteneath(request):
    listing = BasicClinic.objects.get(pk=597)

    swansealisting = BasicClinic.objects.all()
    swansealisting = swansealisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=597)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/wales-fertility-institute-neath.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/wales-fertility-institute-neath.html', context)

def crgwswansea(request):
    listing = BasicClinic.objects.get(pk=598)

    swansealisting = BasicClinic.objects.all()
    swansealisting = swansealisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=598)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/crgw-swansea.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/crgw-swansea.html', context)

def londonwomensclinicswansea(request):
    listing = BasicClinic.objects.get(pk=599)

    swansealisting = BasicClinic.objects.all()
    swansealisting = swansealisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = BasicClinic.objects.all()
    uklisting = uklisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=599)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/london-womens-clinic-swansea.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/london-womens-clinic-swansea.html', context)
