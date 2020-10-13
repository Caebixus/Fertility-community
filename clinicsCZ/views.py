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

# PRAGUE
def pragamedica(request):
    listing = BasicClinic.objects.get(pk=36)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=36)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pragamedica.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pragamedica.html', context)

def fertilityportx(request):
    listing = BasicClinic.objects.get(pk=600)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=600)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/fertilityport-prague.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/fertilityport-prague.html', context)

def praguefertilitycentre(request):
    listing = BasicClinic.objects.get(pk=601)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=601)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/prague-fertility-centre.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/prague-fertility-centre.html', context)

def gynemfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=602)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=602)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/gynem-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/gynem-fertility-clinic.html', context)

def gennet(request):
    listing = BasicClinic.objects.get(pk=604)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=604)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/gennet.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/gennet.html', context)

def medicaltravelczechrep(request):
    listing = BasicClinic.objects.get(pk=605)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=605)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/medical-travel-czech-republic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/medical-travel-czech-republic.html', context)

def pronatalplusprague(request):
    listing = BasicClinic.objects.get(pk=606)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=606)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pronatal-plus-prague6.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-plus-prague6.html', context)

def pronatalsanatoriumprague(request):
    listing = BasicClinic.objects.get(pk=607)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=607)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pronatal-sanatorium-prague4.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-sanatorium-prague4.html', context)

def ivfcube(request):
    listing = BasicClinic.objects.get(pk=612)

    pragueclisting = BasicClinic.objects.all()
    pragueclisting = pragueclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=612)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/ivf-cube.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/ivf-cube.html', context)

# BRNO
def ivfzlinczechrep(request):
    listing = BasicClinic.objects.get(pk=603)

    brnolisting = BasicClinic.objects.all()
    brnolisting = brnolisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=603)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/ivf-zlin-czech-republic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'brnolisting': brnolisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Brno/ivf-zlin-czech-republic.html', context)

def reprofitbrno(request):
    listing = BasicClinic.objects.get(pk=613)

    brnolisting = BasicClinic.objects.all()
    brnolisting = brnolisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=613)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/reprofit-brno.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'brnolisting': brnolisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Brno/reprofit-brno.html', context)

def reprogenesis(request):
    listing = BasicClinic.objects.get(pk=615)

    brnolisting = BasicClinic.objects.all()
    brnolisting = brnolisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=615)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/reprogenesis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'brnolisting': brnolisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Brno/reprogenesis.html', context)

# KOLÍN
def pronatalkolin(request):
    listing = BasicClinic.objects.get(pk=608)

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=608)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Kolin/pronatal-kolin.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Kolin/pronatal-kolin.html', context)

# ČESKÉ BUDĚJOVICE
def pronatalreproceskebudejovice(request):
    listing = BasicClinic.objects.get(pk=609)

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=609)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Ceske-budejovice/pronatal-repro-ceske-budejovice.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Ceske-budejovice/pronatal-repro-ceske-budejovice.html', context)

# TEPLICE
def pronatalnordteplice(request):
    listing = BasicClinic.objects.get(pk=610)

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=610)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Teplice/pronatal-nord-teplice.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Teplice/pronatal-nord-teplice.html', context)

# KARLOVY VARY
def pronatalspakarlovyvary(request):
    listing = BasicClinic.objects.get(pk=611)

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=611)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Karlovy-vary/pronatal-spa-karlovy-vary.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Karlovy-vary/pronatal-spa-karlovy-vary.html', context)

# OSTRAVA
def reprofitostrava(request):
    listing = BasicClinic.objects.get(pk=614)

    czlisting = BasicClinic.objects.all()
    czlisting = czlisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=614)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Ostrava/reprofit-ostrava.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Ostrava/reprofit-ostrava.html', context)
