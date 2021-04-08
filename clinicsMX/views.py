from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages, Package
from django.utils import timezone
from owners.models import ownerProInterested, ProUser
from datetime import datetime, timedelta

#Acapulco
def iregaacapulco(request):
    listing = BasicClinic.objects.get(pk=709)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=709)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Acapulco/irega-acapulco.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Acapulco/irega-acapulco.html', context)

#Cancun
def fertilityclinicamericas(request):
    listing = BasicClinic.objects.get(pk=710)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=710)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/fertility-clinic-americas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/fertility-clinic-americas.html', context)

def advancedfertilitycenterfertilitycentercancun(request):
    listing = BasicClinic.objects.get(pk=711)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=711)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/advanced-fertility-center-fertility-center-cancun.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/advanced-fertility-center-fertility-center-cancun.html', context)

def newlifemexico(request):
    listing = BasicClinic.objects.get(pk=712)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=712)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/new-life-mexico.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/new-life-mexico.html', context)

def iregacancun(request):
    listing = BasicClinic.objects.get(pk=713)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=713)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/irega-cancun.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/irega-cancun.html', context)

#Centro
def embryogengertilitycenterguasave(request):
    listing = BasicClinic.objects.get(pk=714)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=714)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Centro/embryogen-fertility-center-guasave.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Centro/embryogen-fertility-center-guasave.html', context)

#Mexico City
def enlistalofertilidadmexicociudaddemexico(request):
    listing = BasicClinic.objects.get(pk=715)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=715)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexico-City/enlistalo-fertilidad-mexico-ciudad-de-mexico.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Mexico-City/enlistalo-fertilidad-mexico-ciudad-de-mexico.html', context)

def citmermedicinareproductiva(request):
    listing = BasicClinic.objects.get(pk=716)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=716)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexico-City/citmer-medicina-reproductiva.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Mexico-City/citmer-medicina-reproductiva.html', context)

#Cualican-rosales
def embryogenfertilitycenterculiacan(request):
    listing = BasicClinic.objects.get(pk=717)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=717)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Culiacan-rosales/embryogen-fertility-center-culiacan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Culiacan-rosales/embryogen-fertility-center-culiacan.html', context)

#Hermosillo
def embryogenfertilitycenterhermosillo(request):
    listing = BasicClinic.objects.get(pk=718)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=718)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Hermosillo/embryogen-fertility-center-hermosillo.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Hermosillo/embryogen-fertility-center-hermosillo.html', context)

#Mazatlan
def embryogenfertilitycentermazatlan(request):
    listing = BasicClinic.objects.get(pk=719)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=719)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mazatlan/embryogen-fertility-center-mazatlan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Mazatlan/embryogen-fertility-center-mazatlan.html', context)

#Mexicali
def mexicofertilitycenter(request):
    listing = BasicClinic.objects.get(pk=720)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=720)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexicali/mexico-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Mexicali/mexico-fertility-center.html', context)

#Nogales
def embryogenfertilitycenternogales(request):
    listing = BasicClinic.objects.get(pk=721)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=721)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nogales/embryogen-fertility-center-nogales.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Nogales/embryogen-fertility-center-nogales.html', context)

#Nuevo Vallarta
def ivfvallarta(request):
    listing = BasicClinic.objects.get(pk=722)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=722)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nuevo-Vallarta/ivfvallarta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Nuevo-Vallarta/ivfvallarta.html', context)

def surrogacymexico(request):
    listing = BasicClinic.objects.get(pk=723)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=723)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nuevo-Vallarta/surrogacymexico.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Nuevo-Vallarta/surrogacymexico.html', context)

#Puebla
def iregapuebla(request):
    listing = BasicClinic.objects.get(pk=724)

    mxlisting = BasicClinic.objects.all()
    mxlisting = mxlisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=724)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Puebla/irega-puebla.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Puebla/irega-puebla.html', context)
