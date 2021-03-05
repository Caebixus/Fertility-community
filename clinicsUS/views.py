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
from guestblogging.models import GuestBlog, GuestAuthor


# Create your views here.
def wfi(request):
    listing = BasicClinic.objects.get(pk=1)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=1)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/western-fertility-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/western-fertility-institute.html', context)

def cifc(request):
    listing = BasicClinic.objects.get(pk=2)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=2)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/california-ivf-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/california-ivf-fertility-center.html', context)

def ncfmcr(request):
    listing = BasicClinic.objects.get(pk=3)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=3)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/northern-california-fertility-medical-center-roseville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-roseville.html', context)

def ncfmcs(request):
    listing = BasicClinic.objects.get(pk=4)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=4)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

def liwla(request):
    listing = BasicClinic.objects.get(pk=5)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=5)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/la-ivf-west-los-angeles.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/la-ivf-west-los-angeles.html', context)

def lip(request):
    listing = BasicClinic.objects.get(pk=6)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=6)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/la-ivf-pasadena.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/la-ivf-pasadena.html', context)

def lich(request):
    listing = BasicClinic.objects.get(pk=7)

    callisting = BasicClinic.objects.all()
    callisting = callisting.filter(is_published=True)
    callisting = callisting.filter(clinicRegion__iexact='California')
    callisting = callisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=7)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'callisting': callisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/California/la-ivf-chino-hills.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'callisting': callisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/California/la-ivf-chino-hills.html', context)

# ALABAMA Views --------------------------------------------------------------------------------------------------------

def tcfrm(request):
    listing = BasicClinic.objects.get(pk=8)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=8)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/center-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/center-for-reproductive-medicine.html', context)

def af(request):
    listing = BasicClinic.objects.get(pk=9)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/alabama-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/alabama-fertility.html', context)

def aminstrepbir(request):
    listing = BasicClinic.objects.get(pk=648)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/american-institute-of-reproductive-medicine-birmingham.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/american-institute-of-reproductive-medicine-birmingham.html', context)

def aminstrephomeb(request):
    listing = BasicClinic.objects.get(pk=649)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/american-institute-of-reproductive-medicine-homewood.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/american-institute-of-reproductive-medicine-homewood.html', context)

def newlifemobile(request):
    listing = BasicClinic.objects.get(pk=650)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/newlife-mobile.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/newlife-mobile.html', context)

def newlifedothan(request):
    listing = BasicClinic.objects.get(pk=651)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/newlife-dothan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/newlife-dothan.html', context)

def fertinstofnorthal(request):
    listing = BasicClinic.objects.get(pk=652)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/fertility-institute-of-north-alabama.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/fertility-institute-of-north-alabama.html', context)

def huntsrepromed(request):
    listing = BasicClinic.objects.get(pk=653)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/huntsville-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/huntsville-reproductive-medicine.html', context)

def artfertproofal(request):
    listing = BasicClinic.objects.get(pk=654)

    alalisting = BasicClinic.objects.all()
    alalisting = alalisting.filter(is_published=True)
    alalisting = alalisting.filter(clinicRegion__iexact='Alabama')
    alalisting = alalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=9)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'alalisting': alalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Alabama/art-fertility-program-of-alabama.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'alalisting': alalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Alabama/art-fertility-program-of-alabama.html', context)

# ARIZONA Views --------------------------------------------------------------------------------------------------------

def tfc(request):
    listing = BasicClinic.objects.get(pk=10)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=10)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/troche-fertility-scottsdale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-scottsdale.html', context)

def tfg(request):
    listing = BasicClinic.objects.get(pk=11)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=11)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/troche-fertility-glendale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-glendale.html', context)

def tfm(request):
    listing = BasicClinic.objects.get(pk=12)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=12)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/troche-fertility-mesa.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-mesa.html', context)

def sfc(request):
    listing = BasicClinic.objects.get(pk=13)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=13)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/southwest-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/southwest-fertility-center.html', context)

def afcs(request):
    listing = BasicClinic.objects.get(pk=14)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=14)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/advanced-fertility-care-scottsdale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-scottsdale.html', context)

def afcm(request):
    listing = BasicClinic.objects.get(pk=15)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=15)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/advanced-fertility-care-mesa.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-mesa.html', context)

def aafrhs(request):
    listing = BasicClinic.objects.get(pk=16)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=16)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-scottsdale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-scottsdale.html', context)

def aafrhg(request):
    listing = BasicClinic.objects.get(pk=17)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=17)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-gilbert.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-gilbert.html', context)

def bris(request):
    listing = BasicClinic.objects.get(pk=18)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=18)

    author = GuestAuthor.objects.filter(guestauthor__id=18)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'guestblog': guestblog,
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-scottsdale.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-scottsdale.html', context)

def brig(request):
    listing = BasicClinic.objects.get(pk=19)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=19)

    author = GuestAuthor.objects.filter(guestauthor_id=19)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'guestblog': guestblog,
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-gilbert.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-gilbert.html', context)

def biacs(request):
    listing = BasicClinic.objects.get(pk=20)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=20)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-scottsdale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-scottsdale.html', context)

def biacch(request):
    listing = BasicClinic.objects.get(pk=21)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=21)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-chandler.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-chandler.html', context)

def biacp(request):
    listing = BasicClinic.objects.get(pk=22)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=22)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-peoria.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-peoria.html', context)

def biacf(request):
    listing = BasicClinic.objects.get(pk=23)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=23)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-flagstaff.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-flagstaff.html', context)

def ip(request):
    listing = BasicClinic.objects.get(pk=24)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=24)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/ivf-phoenix.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/ivf-phoenix.html', context)

def ftc(request):
    listing = BasicClinic.objects.get(pk=25)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=25)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/fertility-treatment-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/fertility-treatment-center.html', context)

def arifc(request):
    listing = BasicClinic.objects.get(pk=26)

    arilisting = BasicClinic.objects.all()
    arilisting = arilisting.filter(is_published=True)
    arilisting = arilisting.filter(clinicRegion__iexact='Arizona')
    arilisting = arilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=26)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arilisting': arilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arizona/arizona-reproductive-institute-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arilisting': arilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arizona/arizona-reproductive-institute-fertility-clinic.html', context)

# ARKANSAS Views --------------------------------------------------------------------------------------------------------

def afg(request):
    listing = BasicClinic.objects.get(pk=37)

    arklisting = BasicClinic.objects.all()
    arklisting = arklisting.filter(is_published=True)
    arklisting = arklisting.filter(clinicRegion__iexact='Arkansas')
    arklisting = arklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=37)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'arklisting': arklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Arkansas/arkansas-fertility-gynecology.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'arklisting': arklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Arkansas/arkansas-fertility-gynecology.html', context)

# COLORADO Views --------------------------------------------------------------------------------------------------------

def ccrmcmclt(request):
    listing = BasicClinic.objects.get(pk=38)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=38)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/ccrm-colorado-main-center-lone-tree.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-main-center-lone-tree.html', context)

def ccrmcdo(request):
    listing = BasicClinic.objects.get(pk=39)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=39)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/ccrm-colorado-denver-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-denver-office.html', context)

def ccrmclo(request):
    listing = BasicClinic.objects.get(pk=40)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=40)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/ccrm-colorado-louisville-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-louisville-office.html', context)

def ucarmd(request):
    listing = BasicClinic.objects.get(pk=41)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=41)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-denver.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-denver.html', context)

def ucarmcos(request):
    listing = BasicClinic.objects.get(pk=42)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=42)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-co-springs.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-co-springs.html', context)

def rmcrm(request):
    listing = BasicClinic.objects.get(pk=43)

    collisting = BasicClinic.objects.all()
    collisting = collisting.filter(is_published=True)
    collisting = collisting.filter(clinicRegion__iexact='Colorado')
    collisting = collisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=43)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'collisting': collisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Colorado/rocky-mountain-center-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'collisting': collisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Colorado/rocky-mountain-center-reproductive-medicine.html', context)

# CONNECTICUT Views --------------------------------------------------------------------------------------------------------

def carsf(request):
    listing = BasicClinic.objects.get(pk=44)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=44)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/cars-farmington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/cars-farmington.html', context)

def carsh(request):
    listing = BasicClinic.objects.get(pk=45)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=45)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/cars-hartford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/cars-hartford.html', context)

def carsnl(request):
    listing = BasicClinic.objects.get(pk=46)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=46)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/cars-new-london.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/cars-new-london.html', context)

def carsb(request):
    listing = BasicClinic.objects.get(pk=47)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=47)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/cars-branford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/cars-branford.html', context)

def gfg(request):
    listing = BasicClinic.objects.get(pk=48)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=48)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/greenwich-fertility-greenwich.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-greenwich.html', context)

def gfs(request):
    listing = BasicClinic.objects.get(pk=49)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=49)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/greenwich-fertility-stamford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-stamford.html', context)

def rmactn(request):
    listing = BasicClinic.objects.get(pk=50)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=50)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/rmact-norwalk.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/rmact-norwalk.html', context)

def rmacts(request):
    listing = BasicClinic.objects.get(pk=51)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=51)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/rmact-stamford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/rmact-stamford.html', context)

def rmactd(request):
    listing = BasicClinic.objects.get(pk=52)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=52)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/rmact-danbury.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/rmact-danbury.html', context)

def rmactt(request):
    listing = BasicClinic.objects.get(pk=53)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=53)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/rmact-trumbull.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/rmact-trumbull.html', context)

def paft(request):
    listing = BasicClinic.objects.get(pk=54)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=54)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/park-avenue-fertility-trumbull.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-trumbull.html', context)

def paff(request):
    listing = BasicClinic.objects.get(pk=55)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=55)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/park-avenue-fertility-fairfield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-fairfield.html', context)

def pafn(request):
    listing = BasicClinic.objects.get(pk=56)

    connlisting = BasicClinic.objects.all()
    connlisting = connlisting.filter(is_published=True)
    connlisting = connlisting.filter(clinicRegion__iexact='Connecticut')
    connlisting = connlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=56)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'connlisting': connlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Connecticut/park-avenue-fertility-norwalk.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'connlisting': connlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-norwalk.html', context)

# DELAWARE Views --------------------------------------------------------------------------------------------------------

def dirmn(request):
    listing = BasicClinic.objects.get(pk=57)

    dellisting = BasicClinic.objects.all()
    dellisting = dellisting.filter(is_published=True)
    dellisting = dellisting.filter(clinicRegion__iexact='Delaware')
    dellisting = dellisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=57)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'dellisting': dellisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Delaware/dirm-newark.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'dellisting': dellisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Delaware/dirm-newark.html', context)

def dirmm(request):
    listing = BasicClinic.objects.get(pk=58)

    dellisting = BasicClinic.objects.all()
    dellisting = dellisting.filter(is_published=True)
    dellisting = dellisting.filter(clinicRegion__iexact='Delaware')
    dellisting = dellisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=58)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'dellisting': dellisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Delaware/dirm-milford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'dellisting': dellisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Delaware/dirm-milford.html', context)

def radfn(request):
    listing = BasicClinic.objects.get(pk=59)

    dellisting = BasicClinic.objects.all()
    dellisting = dellisting.filter(is_published=True)
    dellisting = dellisting.filter(clinicRegion__iexact='Delaware')
    dellisting = dellisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=59)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'dellisting': dellisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Delaware/radfertility-newark.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'dellisting': dellisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Delaware/radfertility-newark.html', context)

def radfw(request):
    listing = BasicClinic.objects.get(pk=60)

    dellisting = BasicClinic.objects.all()
    dellisting = dellisting.filter(is_published=True)
    dellisting = dellisting.filter(clinicRegion__iexact='Delaware')
    dellisting = dellisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=60)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'dellisting': dellisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Delaware/radfertility-wilmington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'dellisting': dellisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Delaware/radfertility-wilmington.html', context)

def radfd(request):
    listing = BasicClinic.objects.get(pk=61)

    dellisting = BasicClinic.objects.all()
    dellisting = dellisting.filter(is_published=True)
    dellisting = dellisting.filter(clinicRegion__iexact='Delaware')
    dellisting = dellisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=61)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'dellisting': dellisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Delaware/radfertility-dover.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'dellisting': dellisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Delaware/radfertility-dover.html', context)

# FLORIDA Views --------------------------------------------------------------------------------------------------------

def bocaf(request):
    listing = BasicClinic.objects.get(pk=62)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=62)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/boca-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/boca-fertility.html', context)

def pbfcbr(request):
    listing = BasicClinic.objects.get(pk=63)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=63)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/pbfc-boca-raton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/pbfc-boca-raton.html', context)

def pbfcpbg(request):
    listing = BasicClinic.objects.get(pk=64)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=64)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/pbfc-palm-beach-gardens.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/pbfc-palm-beach-gardens.html', context)

def ffico(request):
    listing = BasicClinic.objects.get(pk=65)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=65)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ffi-clearwater-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ffi-clearwater-office.html', context)

def ffito(request):
    listing = BasicClinic.objects.get(pk=66)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=66)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ffi-tampa-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ffi-tampa-office.html', context)

def cfcg(request):
    listing = BasicClinic.objects.get(pk=67)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=67)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/conceptions-florida-coral-gables.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-coral-gables.html', context)

def cfm(request):
    listing = BasicClinic.objects.get(pk=68)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=68)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/conceptions-florida-miramar.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-miramar.html', context)

def jcrmj(request):
    listing = BasicClinic.objects.get(pk=69)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=68)

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=69)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/jcrm-jacksonville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/jcrm-jacksonville.html', context)

def jcrmg(request):
    listing = BasicClinic.objects.get(pk=70)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=70)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/jcrm-gainesville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/jcrm-gainesville.html', context)

def jcrmpc(request):
    listing = BasicClinic.objects.get(pk=71)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=71)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/jcrm-panama-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/jcrm-panama-city.html', context)

def jcrmo(request):
    listing = BasicClinic.objects.get(pk=72)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=72)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/jcrm-orlando.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/jcrm-orlando.html', context)

def rmanlm(request):
    listing = BasicClinic.objects.get(pk=73)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=73)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/rma-network-lake-mary.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/rma-network-lake-mary.html', context)

def ivffwfc(request):
    listing = BasicClinic.objects.get(pk=74)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=74)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-wellington-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-wellington-fertility-center.html', context)

def ivffcgfc(request):
    listing = BasicClinic.objects.get(pk=75)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=75)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-coral-gables-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-coral-gables-fertility-center.html', context)

def ivfppfc(request):
    listing = BasicClinic.objects.get(pk=76)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=76)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-pembroke-pines-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-pembroke-pines-fertility-center.html', context)

def ivffmfc(request):
    listing = BasicClinic.objects.get(pk=77)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=77)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-margate-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-margate-fertility-center.html', context)

def ivfbrfc(request):
    listing = BasicClinic.objects.get(pk=78)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=78)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-boca-raton-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-boca-raton-fertility-center.html', context)

def ivffjpbgfc(request):
    listing = BasicClinic.objects.get(pk=79)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=79)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-jupiter-palm-beach-gardens-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-jupiter-palm-beach-gardens-fertility-center.html', context)

def ivffplfc(request):
    listing = BasicClinic.objects.get(pk=80)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=80)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-florida-port-lucie-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-port-lucie-fertility-clinic.html', context)

def vfc(request):
    listing = BasicClinic.objects.get(pk=81)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=81)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/viera-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/viera-fertility-center.html', context)

def fivfcm(request):
    listing = BasicClinic.objects.get(pk=82)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=82)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/fivfcm-miami.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami.html', context)

def fivfcmb(request):
    listing = BasicClinic.objects.get(pk=83)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=83)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/fivfcm-miami-beach.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami-beach.html', context)

def fg(request):
    listing = BasicClinic.objects.get(pk=84)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=84)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/fertility-genetics.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/fertility-genetics.html', context)

def ivfmdm(request):
    listing = BasicClinic.objects.get(pk=85)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=85)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-miami.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-miami.html', context)

def ivfmdcc(request):
    listing = BasicClinic.objects.get(pk=86)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=86)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-cooper-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-cooper-city.html', context)

def ivfmdbr(request):
    listing = BasicClinic.objects.get(pk=87)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=87)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-boca-raton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-boca-raton.html', context)

def ivfmdj(request):
    listing = BasicClinic.objects.get(pk=88)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=88)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-jupiter.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-jupiter.html', context)

def ivfmdn(request):
    listing = BasicClinic.objects.get(pk=89)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=89)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-naples.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-naples.html', context)

def ivfmdv(request):
    listing = BasicClinic.objects.get(pk=90)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=90)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivfmd-viera.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivfmd-viera.html', context)

def sgftw(request):
    listing = BasicClinic.objects.get(pk=91)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=91)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/sgf-tampa-westshore.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/sgf-tampa-westshore.html', context)

def sgfb(request):
    listing = BasicClinic.objects.get(pk=92)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=92)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/sgf-brandon.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/sgf-brandon.html', context)

def sgfwc(request):
    listing = BasicClinic.objects.get(pk=93)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=93)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/sgf-wesley-chapel.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/sgf-wesley-chapel.html', context)

def rmgnto(request):
    listing = BasicClinic.objects.get(pk=94)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=94)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/rmg-north-tampa-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/rmg-north-tampa-office.html', context)

def rmgsto(request):
    listing = BasicClinic.objects.get(pk=95)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=95)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/rmg-south-tampa-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/rmg-south-tampa-office.html', context)

def rmgco(request):
    listing = BasicClinic.objects.get(pk=96)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=96)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/rmg-clearwater-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/rmg-clearwater-office.html', context)

def rmgbo(request):
    listing = BasicClinic.objects.get(pk=97)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=97)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/rmg-brandon-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/rmg-brandon-office.html', context)

def fifrst(request):
    listing = BasicClinic.objects.get(pk=98)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=98)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/florida-institute-for-reproductive-sciences-technologies.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/florida-institute-for-reproductive-sciences-technologies.html', context)

def arswp(request):
    listing = BasicClinic.objects.get(pk=99)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=99)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/advanced-reproductive-specialists-winter-park.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/advanced-reproductive-specialists-winter-park.html', context)

def ivfowp(request):
    listing = BasicClinic.objects.get(pk=100)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=100)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/ivf-orlando-winter-park.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/ivf-orlando-winter-park.html', context)

def fcare(request):
    listing = BasicClinic.objects.get(pk=101)

    flolisting = BasicClinic.objects.all()
    flolisting = flolisting.filter(is_published=True)
    flolisting = flolisting.filter(clinicRegion__iexact='Florida')
    flolisting = flolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=101)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'flolisting': flolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Florida/fertility-center-assisted-reproduction-endocrinology.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'flolisting': flolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Florida/fertility-center-assisted-reproduction-endocrinology.html', context)

# GEORGIA Views --------------------------------------------------------------------------------------------------------

def afa(request):
    listing = BasicClinic.objects.get(pk=102)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=102)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/aspire-fertility-atlanta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/aspire-fertility-atlanta.html', context)

def acrmap(request):
    listing = BasicClinic.objects.get(pk=103)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=103)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/acrm-atlanta-perimetr.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-perimetr.html', context)

def acrmab(request):
    listing = BasicClinic.objects.get(pk=104)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=104)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/acrm-atlanta-buckhead.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-buckhead.html', context)

def acrmjc(request):
    listing = BasicClinic.objects.get(pk=105)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=105)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/acrm-johns-creek.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/acrm-johns-creek.html', context)

def acrmm(request):
    listing = BasicClinic.objects.get(pk=106)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=106)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/acrm-marietta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/acrm-marietta.html', context)

def mfs(request):
    listing = BasicClinic.objects.get(pk=107)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=107)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/massey-fertility-services.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/massey-fertility-services.html', context)

def sfi(request):
    listing = BasicClinic.objects.get(pk=108)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=108)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/servy-fertility-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/servy-fertility-institute.html', context)

def sgfan(request):
    listing = BasicClinic.objects.get(pk=109)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=109)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/sgf-atlanta-northside.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/sgf-atlanta-northside.html', context)

def sgfa(request):
    listing = BasicClinic.objects.get(pk=110)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=110)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/sgf-alpharetta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/sgf-alpharetta.html', context)

def sgfbp(request):
    listing = BasicClinic.objects.get(pk=111)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=111)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/sgf-buckhead-piedmont.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/sgf-buckhead-piedmont.html', context)

def sgfm(request):
    listing = BasicClinic.objects.get(pk=112)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=112)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/sgf-marietta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/sgf-marietta.html', context)

def rbamo(request):
    listing = BasicClinic.objects.get(pk=113)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=113)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–main-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–main-office.html', context)

def rbam(request):
    listing = BasicClinic.objects.get(pk=114)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=114)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–marietta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–marietta.html', context)

def rbaf(request):
    listing = BasicClinic.objects.get(pk=115)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=115)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–fayetteville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–fayetteville.html', context)

def rbal(request):
    listing = BasicClinic.objects.get(pk=116)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=116)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–lawrenceville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–lawrenceville.html', context)

def rbac(request):
    listing = BasicClinic.objects.get(pk=117)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=117)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cumming.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cumming.html', context)

def rbaph(request):
    listing = BasicClinic.objects.get(pk=118)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=118)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–piedmont-hospital.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–piedmont-hospital.html', context)

def rbacar(request):
    listing = BasicClinic.objects.get(pk=119)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=119)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cartersville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cartersville.html', context)

def cnyferticentatlanta(request):
    listing = BasicClinic.objects.get(pk=504)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=504)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/cny-fertility-center-atlanta.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/cny-fertility-center-atlanta.html', context)

def coastalfertispecsavannah(request):
    listing = BasicClinic.objects.get(pk=505)

    georlisting = BasicClinic.objects.all()
    georlisting = georlisting.filter(is_published=True)
    georlisting = georlisting.filter(clinicRegion__iexact='Georgia')
    georlisting = georlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=505)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'georlisting': georlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Georgia/coastal-fertility-specialists-savannah.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'georlisting': georlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Georgia/coastal-fertility-specialists-savannah.html', context)

# HAWAII Views --------------------------------------------------------------------------------------------------------

def arch(request):
    listing = BasicClinic.objects.get(pk=120)

    hawlisting = BasicClinic.objects.all()
    hawlisting = hawlisting.filter(is_published=True)
    hawlisting = hawlisting.filter(clinicRegion__iexact='Hawaii')
    hawlisting = hawlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=120)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'hawlisting': hawlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Hawaii/advanced-reproductive-center-hawaii.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'hawlisting': hawlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Hawaii/advanced-reproductive-center-hawaii.html', context)

def armghh(request):
    listing = BasicClinic.objects.get(pk=121)

    hawlisting = BasicClinic.objects.all()
    hawlisting = hawlisting.filter(is_published=True)
    hawlisting = hawlisting.filter(clinicRegion__iexact='Hawaii')
    hawlisting = hawlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=121)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'hawlisting': hawlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Hawaii/armgh-honolulu.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'hawlisting': hawlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Hawaii/armgh-honolulu.html', context)

def armghk(request):
    listing = BasicClinic.objects.get(pk=122)

    hawlisting = BasicClinic.objects.all()
    hawlisting = hawlisting.filter(is_published=True)
    hawlisting = hawlisting.filter(clinicRegion__iexact='Hawaii')
    hawlisting = hawlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=122)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'hawlisting': hawlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Hawaii/armgh-kailua.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'hawlisting': hawlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Hawaii/armgh-kailua.html', context)

def pivfi(request):
    listing = BasicClinic.objects.get(pk=123)

    hawlisting = BasicClinic.objects.all()
    hawlisting = hawlisting.filter(is_published=True)
    hawlisting = hawlisting.filter(clinicRegion__iexact='Hawaii')
    hawlisting = hawlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=123)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'hawlisting': hawlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Hawaii/pacific-in-vitro-fertilization-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'hawlisting': hawlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Hawaii/pacific-in-vitro-fertilization-institute.html', context)

# IOWA Views --------------------------------------------------------------------------------------------------------

def mif(request):
    listing = BasicClinic.objects.get(pk=124)

    iowalisting = BasicClinic.objects.all()
    iowalisting = iowalisting.filter(is_published=True)
    iowalisting = iowalisting.filter(clinicRegion__iexact='Iowa')
    iowalisting = iowalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=124)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'iowalisting': iowalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Iowa/mid-iowa-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'iowalisting': iowalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Iowa/mid-iowa-fertility.html', context)

# IDAHO Views --------------------------------------------------------------------------------------------------------

def icrm(request):
    listing = BasicClinic.objects.get(pk=125)

    Idaholisting = BasicClinic.objects.all()
    Idaholisting = Idaholisting.filter(is_published=True)
    Idaholisting = Idaholisting.filter(clinicRegion__iexact='Idaho')
    Idaholisting = Idaholisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=125)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Idaholisting': Idaholisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Idaho/idaho-center-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Idaholisting': Idaholisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Idaho/idaho-center-reproductive-medicine.html', context)

def reprocarecenteridahofalls(request):
    listing = BasicClinic.objects.get(pk=503)

    Idaholisting = BasicClinic.objects.all()
    Idaholisting = Idaholisting.filter(is_published=True)
    Idaholisting = Idaholisting.filter(clinicRegion__iexact='Idaho')
    Idaholisting = Idaholisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=503)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Idaholisting': Idaholisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Idaho/reproductive-care-center-idaho-falls.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Idaholisting': Idaholisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Idaho/reproductive-care-center-idaho-falls.html', context)

# ILLINOIS Views --------------------------------------------------------------------------------------------------------

def crc(request):
    listing = BasicClinic.objects.get(pk=126)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=126)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/center-reproductive-care.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/center-reproductive-care.html', context)

def fcibgc(request):
    listing = BasicClinic.objects.get(pk=127)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=127)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-buffalo-grove-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-buffalo-grove-clinic.html', context)

def fcicnc(request):
    listing = BasicClinic.objects.get(pk=128)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=128)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-chicago-north-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-chicago-north-clinic.html', context)

def fcigc(request):
    listing = BasicClinic.objects.get(pk=129)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=129)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-glenview-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-glenview-clinic.html', context)

def fcihpc(request):
    listing = BasicClinic.objects.get(pk=130)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=130)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-highland-park-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-highland-park-clinic.html', context)

def fcihc(request):
    listing = BasicClinic.objects.get(pk=131)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=131)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-hinsdale-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-hinsdale-clinic.html', context)

def fcihec(request):
    listing = BasicClinic.objects.get(pk=132)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=132)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-hoffman-estates-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-hoffman-estates-clinic.html', context)

def fcilc(request):
    listing = BasicClinic.objects.get(pk=133)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=133)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-lindenhurst-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-lindenhurst-clinic.html', context)

def fcitpc(request):
    listing = BasicClinic.objects.get(pk=134)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=134)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-tinley-park-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-tinley-park-clinic.html', context)

def fciwc(request):
    listing = BasicClinic.objects.get(pk=135)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=135)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/fci-warrenville-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/fci-warrenville-clinic.html', context)

def ihrc(request):
    listing = BasicClinic.objects.get(pk=136)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=136)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/ihr-chicago.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/ihr-chicago.html', context)

def ihro(request):
    listing = BasicClinic.objects.get(pk=137)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=137)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/ihr-oakbrook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/ihr-oakbrook.html', context)

def vfica(request):
    listing = BasicClinic.objects.get(pk=138)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=138)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-aurora.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-aurora.html', context)

def vficwp(request):
    listing = BasicClinic.objects.get(pk=139)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=139)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-wicker-park.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-wicker-park.html', context)

def vficwlil(request):
    listing = BasicClinic.objects.get(pk=140)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=140)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-west-loop-ivf-lab.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-west-loop-ivf-lab.html', context)

def vficg(request):
    listing = BasicClinic.objects.get(pk=141)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=141)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-glenview.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-glenview.html', context)

def vfiche(request):
    listing = BasicClinic.objects.get(pk=142)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=142)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-hoffman-estates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-hoffman-estates.html', context)

def dfis(request):
    listing = BasicClinic.objects.get(pk=143)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=143)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/davies-fertility-ivf-specialists.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/davies-fertility-ivf-specialists.html', context)

def hcr(request):
    listing = BasicClinic.objects.get(pk=144)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=144)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/hinsdale-center-reproduction.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/hinsdale-center-reproduction.html', context)

def ifsah(request):
    listing = BasicClinic.objects.get(pk=145)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=145)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/invia-fertility-specialists-arlington-heights.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-arlington-heights.html', context)

def ifscl(request):
    listing = BasicClinic.objects.get(pk=146)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=146)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/invia-fertility-specialists-crystal-lake.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-crystal-lake.html', context)

def ifshe(request):
    listing = BasicClinic.objects.get(pk=147)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=147)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/invia-fertility-specialists-hoffman-estates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-hoffman-estates.html', context)

def ifsn(request):
    listing = BasicClinic.objects.get(pk=148)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=148)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/invia-fertility-specialists-northbrook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-northbrook.html', context)

def ivf1(request):
    listing = BasicClinic.objects.get(pk=149)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=149)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/ivf1.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/ivf1.html', context)

def rmib(request):
    listing = BasicClinic.objects.get(pk=150)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=150)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-bloomingdale.html', context)

    else:
        pass


    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-bloomingdale.html', context)

def rmic(request):
    listing = BasicClinic.objects.get(pk=151)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=151)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-chicago.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-chicago.html', context)

def rmiel(request):
    listing = BasicClinic.objects.get(pk=152)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=152)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-elmhurst.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-elmhurst.html', context)

def rmiev(request):
    listing = BasicClinic.objects.get(pk=153)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=153)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-evanston.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-evanston.html', context)

def rminb(request):
    listing = BasicClinic.objects.get(pk=154)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=154)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-northbrook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-northbrook.html', context)

def rmiob(request):
    listing = BasicClinic.objects.get(pk=155)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=155)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-oak-brook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-brook.html', context)

def rmiol(request):
    listing = BasicClinic.objects.get(pk=156)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=156)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/rmi-oak-lawn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-lawn.html', context)

def civfops(request):
    listing = BasicClinic.objects.get(pk=157)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=157)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/chicago-ivf-orland-park–southwest.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-orland-park–southwest.html', context)

def civfscn(request):
    listing = BasicClinic.objects.get(pk=158)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=158)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/chicago-ivf-stcharles–northwest.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-stcharles–northwest.html', context)

def civfnw(request):
    listing = BasicClinic.objects.get(pk=159)

    Illinoislisting = BasicClinic.objects.all()
    Illinoislisting = Illinoislisting.filter(is_published=True)
    Illinoislisting = Illinoislisting.filter(clinicRegion__iexact='Illinois')
    Illinoislisting = Illinoislisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=159)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Illinoislisting': Illinoislisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Illinois/chicago-ivf-naperville–west.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Illinoislisting': Illinoislisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-naperville–west.html', context)

# INDIANA Views --------------------------------------------------------------------------------------------------------

def ihrval(request):
    listing = BasicClinic.objects.get(pk=161)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=161)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/ihr-valparaiso.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/ihr-valparaiso.html', context)

def mfcar(request):
    listing = BasicClinic.objects.get(pk=162)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=162)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/midwest-fertility-carmel.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-carmel.html', context)

def mffortwayne(request):
    listing = BasicClinic.objects.get(pk=165)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=165)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/midwest-fertility-fort-wayne.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-fort-wayne.html', context)

def civfval(request):
    listing = BasicClinic.objects.get(pk=163)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=163)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/chicago-ivf-valparaiso.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-valparaiso.html', context)

def civfmun(request):
    listing = BasicClinic.objects.get(pk=164)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=164)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/chicago-ivf-munster.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-munster.html', context)

def prhmun(request):
    listing = BasicClinic.objects.get(pk=166)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=166)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/partners-reproductive-health-munster.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/partners-reproductive-health-munster.html', context)

def fbeg(request):
    listing = BasicClinic.objects.get(pk=167)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=167)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/family-beginnings.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/family-beginnings.html', context)

def ifinst(request):
    listing = BasicClinic.objects.get(pk=168)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=168)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/indiana-fertility-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/indiana-fertility-institute.html', context)

def rcimo(request):
    listing = BasicClinic.objects.get(pk=169)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=169)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/reproductive-care-indiana-main-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-main-office.html', context)

def rcith(request):
    listing = BasicClinic.objects.get(pk=170)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=170)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/reproductive-care-indiana-terre-haute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-terre-haute.html', context)

def rcilaf(request):
    listing = BasicClinic.objects.get(pk=171)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=171)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/reproductive-care-indiana-lafayette.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-lafayette.html', context)

def rcibmc(request):
    listing = BasicClinic.objects.get(pk=172)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=172)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-mc.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-mc.html', context)

def rcibws(request):
    listing = BasicClinic.objects.get(pk=173)

    Indianalisting = BasicClinic.objects.all()
    Indianalisting = Indianalisting.filter(is_published=True)
    Indianalisting = Indianalisting.filter(clinicRegion__iexact='Indiana')
    Indianalisting = Indianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=173)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Indianalisting': Indianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-ws.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Indianalisting': Indianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-ws.html', context)

# KANSAS Views --------------------------------------------------------------------------------------------------------

def midrepc(request):
    listing = BasicClinic.objects.get(pk=174)

    Kansaslisting = BasicClinic.objects.all()
    Kansaslisting = Kansaslisting.filter(is_published=True)
    Kansaslisting = Kansaslisting.filter(clinicRegion__iexact='Kansas')
    Kansaslisting = Kansaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=174)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'Kansaslisting': Kansaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Kansas/midwest-reproductive-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'Kansaslisting': Kansaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Kansas/midwest-reproductive-center.html', context)

# KENTUCKY Views --------------------------------------------------------------------------------------------------------

def ferendas(request):
    listing = BasicClinic.objects.get(pk=175)

    kentuckylisting = BasicClinic.objects.all()
    kentuckylisting = kentuckylisting.filter(is_published=True)
    kentuckylisting = kentuckylisting.filter(clinicRegion__iexact='Kentucky')
    kentuckylisting = kentuckylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=175)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'kentuckylisting': kentuckylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Kentucky/fertility-endocrine-associates.html', context)

    else:
        pass


    context = {
        'listing': listing,
        'package': package,
        'kentuckylisting': kentuckylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Kentucky/fertility-endocrine-associates.html', context)

def ifrhealthflo(request):
    listing = BasicClinic.objects.get(pk=501)

    kentuckylisting = BasicClinic.objects.all()
    kentuckylisting = kentuckylisting.filter(is_published=True)
    kentuckylisting = kentuckylisting.filter(clinicRegion__iexact='Kentucky')
    kentuckylisting = kentuckylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=501)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'kentuckylisting': kentuckylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-florence.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'kentuckylisting': kentuckylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-florence.html', context)

def ifrhealthlou(request):
    listing = BasicClinic.objects.get(pk=502)

    kentuckylisting = BasicClinic.objects.all()
    kentuckylisting = kentuckylisting.filter(is_published=True)
    kentuckylisting = kentuckylisting.filter(clinicRegion__iexact='Kentucky')
    kentuckylisting = kentuckylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=502)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'kentuckylisting': kentuckylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-louisville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'kentuckylisting': kentuckylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-louisville.html', context)

# LOUISIANA Views --------------------------------------------------------------------------------------------------------

def feanla(request):
    listing = BasicClinic.objects.get(pk=176)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=176)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fertility-answers-lafayette.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lafayette.html', context)

def feanbaro(request):
    listing = BasicClinic.objects.get(pk=177)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=177)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fertility-answers-baton-rouge.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-baton-rouge.html', context)

def feanco(request):
    listing = BasicClinic.objects.get(pk=178)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=178)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fertility-answers-covington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-covington.html', context)

def feanlach(request):
    listing = BasicClinic.objects.get(pk=179)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=179)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fertility-answers-lake-charles.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lake-charles.html', context)

def fiman(request):
    listing = BasicClinic.objects.get(pk=180)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=180)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fi-mandeville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fi-mandeville.html', context)

def fimet(request):
    listing = BasicClinic.objects.get(pk=181)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=181)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fi-metairie.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fi-metairie.html', context)

def fibaro(request):
    listing = BasicClinic.objects.get(pk=182)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=182)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/fi-baton-rouge.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/fi-baton-rouge.html', context)

def audfer(request):
    listing = BasicClinic.objects.get(pk=183)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=183)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/audubon-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/audubon-fertility.html', context)

def arkferrepmed(request):
    listing = BasicClinic.objects.get(pk=184)

    louisianalisting = BasicClinic.objects.all()
    louisianalisting = louisianalisting.filter(is_published=True)
    louisianalisting = louisianalisting.filter(clinicRegion__iexact='Louisiana')
    louisianalisting = louisianalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=184)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'louisianalisting': louisianalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Louisiana/arklatex-fertility-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'louisianalisting': louisianalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Louisiana/arklatex-fertility-reproductive-medicine.html', context)

# MAINE Views --------------------------------------------------------------------------------------------------------

def fcnebc(request):
    listing = BasicClinic.objects.get(pk=186)

    mainelisting = BasicClinic.objects.all()
    mainelisting = mainelisting.filter(is_published=True)
    mainelisting = mainelisting.filter(clinicRegion__iexact='Maine')
    mainelisting = mainelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=186)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mainelisting': mainelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Maine/fcne-bangor-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mainelisting': mainelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Maine/fcne-bangor-center.html', context)

def bivfbfc(request):
    listing = BasicClinic.objects.get(pk=187)

    mainelisting = BasicClinic.objects.all()
    mainelisting = mainelisting.filter(is_published=True)
    mainelisting = mainelisting.filter(clinicRegion__iexact='Maine')
    mainelisting = mainelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=187)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mainelisting': mainelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Maine/boston-ivf-bangor-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mainelisting': mainelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-bangor-fertility-center.html', context)

def bivfpfc(request):
    listing = BasicClinic.objects.get(pk=188)

    mainelisting = BasicClinic.objects.all()
    mainelisting = mainelisting.filter(is_published=True)
    mainelisting = mainelisting.filter(clinicRegion__iexact='Maine')
    mainelisting = mainelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=188)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mainelisting': mainelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Maine/boston-ivf-portland-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mainelisting': mainelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-portland-fertility-center.html', context)

# MARYLAND Views --------------------------------------------------------------------------------------------------------

# MASSACHUSETTS Views --------------------------------------------------------------------------------------------------------

def masghfc(request):
    listing = BasicClinic.objects.get(pk=185)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=185)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/massachusetts-general-hospital-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/massachusetts-general-hospital-fertility-center.html', context)

def ccrmbmc(request):
    listing = BasicClinic.objects.get(pk=189)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=189)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/ccrm-boston-main-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-boston-main-center.html', context)

def ccrmmo(request):
    listing = BasicClinic.objects.get(pk=190)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=190)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/ccrm-metrowest-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-metrowest-office.html', context)

def ccrmsso(request):
    listing = BasicClinic.objects.get(pk=191)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=191)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/ccrm-south-shore-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-south-shore-office.html', context)

def bivfmfc(request):
    listing = BasicClinic.objects.get(pk=192)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=192)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-tufts-medical-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-tufts-medical-fertility-center.html', context)

def bivfdbfc(request):
    listing = BasicClinic.objects.get(pk=193)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=193)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-downtown-boston-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-downtown-boston-fertility-center.html', context)

def bivflfc(request):
    listing = BasicClinic.objects.get(pk=194)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=194)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-lexington-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-lexington-fertility-center.html', context)

def bivfqfc(request):
    listing = BasicClinic.objects.get(pk=195)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=195)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-quincy-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-quincy-fertility-center.html', context)

def bivfwfc(request):
    listing = BasicClinic.objects.get(pk=196)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=196)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-waltham-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-waltham-fertility-center.html', context)

def bivfsfc(request):
    listing = BasicClinic.objects.get(pk=197)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=197)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/boston-ivf-stoneham-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-stoneham-fertility-center.html', context)

def fcnelc(request):
    listing = BasicClinic.objects.get(pk=198)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=198)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-leominster-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-leominster-center.html', context)

def fcnerc(request):
    listing = BasicClinic.objects.get(pk=199)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=199)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-reading-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-reading-center.html', context)

def fcnedc(request):
    listing = BasicClinic.objects.get(pk=200)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=200)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-danvers-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-danvers-center.html', context)

def fcnebce(request):
    listing = BasicClinic.objects.get(pk=201)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=201)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-braintree-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-braintree-center.html', context)

def fcnebcen(request):
    listing = BasicClinic.objects.get(pk=202)

    massachusettslisting = BasicClinic.objects.all()
    massachusettslisting = massachusettslisting.filter(is_published=True)
    massachusettslisting = massachusettslisting.filter(clinicRegion__iexact='Massachusetts')
    massachusettslisting = massachusettslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=202)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'massachusettslisting': massachusettslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-boston-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'massachusettslisting': massachusettslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-boston-center.html', context)

# MICHIGAN Views --------------------------------------------------------------------------------------------------------

def ivfmfcaafc(request):
    listing = BasicClinic.objects.get(pk=203)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=203)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-ann-arbor-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-ann-arbor-fertility-center.html', context)

def ivfmfcbhfc(request):
    listing = BasicClinic.objects.get(pk=204)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=204)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-bloomfield-hills-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-bloomfield-hills-fertility-center.html', context)

def ivfmfcchebfc(request):
    listing = BasicClinic.objects.get(pk=205)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=205)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-cheboygan-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-cheboygan-fertility-center.html', context)

def ivfmfcdfc(request):
    listing = BasicClinic.objects.get(pk=206)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=206)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-dearborn-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-dearborn-fertility-center.html', context)

def ivfmfcelfc(request):
    listing = BasicClinic.objects.get(pk=207)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=207)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-east-lansing-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-east-lansing-fertility-center.html', context)

def ivfmfcmfc(request):
    listing = BasicClinic.objects.get(pk=208)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=208)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-macomb-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-macomb-fertility-center.html', context)

def ivfmfcpfc(request):
    listing = BasicClinic.objects.get(pk=209)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=209)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-petoskey-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-petoskey-fertility-center.html', context)

def ivfmfcsfc(request):
    listing = BasicClinic.objects.get(pk=210)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=210)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-saginaw-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-saginaw-fertility-center.html', context)

def ivfmfctfc(request):
    listing = BasicClinic.objects.get(pk=211)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=211)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-toledo-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-toledo-fertility-center.html', context)

def gcffb(request):
    listing = BasicClinic.objects.get(pk=212)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=212)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/gago-center-for-fertility-brighton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-brighton.html', context)

def ggcffl(request):
    listing = BasicClinic.objects.get(pk=213)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=213)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/gago-center-for-fertility-lansing.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-lansing.html', context)

def ggcffaa(request):
    listing = BasicClinic.objects.get(pk=214)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=214)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/gago-center-for-fertility-ann-arbor.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-ann-arbor.html', context)

def tfcgr(request):
    listing = BasicClinic.objects.get(pk=215)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=215)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/the-fertility-center-grand-rapids.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-grand-rapids.html', context)

def tfcm(request):
    listing = BasicClinic.objects.get(pk=216)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=216)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/the-fertility-center-mason.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-mason.html', context)

def tfck(request):
    listing = BasicClinic.objects.get(pk=217)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=217)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/the-fertility-center-kalamazoo.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-kalamazoo.html', context)

def tfctc(request):
    listing = BasicClinic.objects.get(pk=218)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=218)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/the-fertility-center-traverse-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-traverse-city.html', context)

def ivfmrh(request):
    listing = BasicClinic.objects.get(pk=219)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=219)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-rochester-hills.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-rochester-hills.html', context)

def ivfmf(request):
    listing = BasicClinic.objects.get(pk=220)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=220)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-flint.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-flint.html', context)

def ivfmd(request):
    listing = BasicClinic.objects.get(pk=221)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=221)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/ivf-michigan-dearborn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-dearborn.html', context)

def rmaom(request):
    listing = BasicClinic.objects.get(pk=222)

    michiganlisting = BasicClinic.objects.all()
    michiganlisting = michiganlisting.filter(is_published=True)
    michiganlisting = michiganlisting.filter(clinicRegion__iexact='Michigan')
    michiganlisting = michiganlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=222)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'michiganlisting': michiganlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Michigan/reproductive-medicine-associates-of-michigan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'michiganlisting': michiganlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Michigan/reproductive-medicine-associates-of-michigan.html', context)

# MINNESOTA Views --------------------------------------------------------------------------------------------------------

def cccrmmin(request):
    listing = BasicClinic.objects.get(pk=223)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=223)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/ccrm-minneapolis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/ccrm-minneapolis.html', context)

def midcfrh(request):
    listing = BasicClinic.objects.get(pk=224)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=224)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/midwest-center-for-reproductive-health.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/midwest-center-for-reproductive-health.html', context)

def cenfrmmin(request):
    listing = BasicClinic.objects.get(pk=225)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=225)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-minneapolis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-minneapolis.html', context)

def cenfrmstp(request):
    listing = BasicClinic.objects.get(pk=226)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=226)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-paul.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-paul.html', context)

def cenfrmwesog(request):
    listing = BasicClinic.objects.get(pk=227)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=227)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-western-ob-gyn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-western-ob-gyn.html', context)

def cenfremstluobgyna(request):
    listing = BasicClinic.objects.get(pk=228)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=228)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-lukes-obstetrics-gynecology-associates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-lukes-obstetrics-gynecology-associates.html', context)

def repmeinaswoo(request):
    listing = BasicClinic.objects.get(pk=229)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=229)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-woodbury.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-woodbury.html', context)

def repmeinasedi(request):
    listing = BasicClinic.objects.get(pk=230)

    minnesotalisting = BasicClinic.objects.all()
    minnesotalisting = minnesotalisting.filter(is_published=True)
    minnesotalisting = minnesotalisting.filter(clinicRegion__iexact='Minnesota')
    minnesotalisting = minnesotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=230)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'minnesotalisting': minnesotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-edina.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'minnesotalisting': minnesotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-edina.html', context)

# MISSISSIPPI Views --------------------------------------------------------------------------------------------------------

def cenfrmmfc(request):
    listing = BasicClinic.objects.get(pk=231)

    mississippilisting = BasicClinic.objects.all()
    mississippilisting = mississippilisting.filter(is_published=True)
    mississippilisting = mississippilisting.filter(clinicRegion__iexact='Mississippi')
    mississippilisting = mississippilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=231)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mississippilisting': mississippilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Mississippi/center-for-reproductive-medicine-mississippi-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mississippilisting': mississippilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Mississippi/center-for-reproductive-medicine-mississippi-fertility-clinic.html', context)

def missrepmed(request):
    listing = BasicClinic.objects.get(pk=232)

    mississippilisting = BasicClinic.objects.all()
    mississippilisting = mississippilisting.filter(is_published=True)
    mississippilisting = mississippilisting.filter(clinicRegion__iexact='Mississippi')
    mississippilisting = mississippilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=232)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'mississippilisting': mississippilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Mississippi/mississippi-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'mississippilisting': mississippilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Mississippi/mississippi-reproductive-medicine.html', context)

# MISSOURI Views --------------------------------------------------------------------------------------------------------

def vfichisl(request):
    listing = BasicClinic.objects.get(pk=233)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=233)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-saint-louis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-saint-louis.html', context)

def vfichiofa(request):
    listing = BasicClinic.objects.get(pk=234)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=234)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-ofallon.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-ofallon.html', context)

def infeceofstlo(request):
    listing = BasicClinic.objects.get(pk=235)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=235)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/infertility-center-of-st-louis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/infertility-center-of-st-louis.html', context)

def mcrmferstlo(request):
    listing = BasicClinic.objects.get(pk=236)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=236)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/mcrm-fertility-st-louis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-st-louis.html', context)

def mcrmferspring(request):
    listing = BasicClinic.objects.get(pk=237)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=237)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/mcrm-fertility-springfield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-springfield.html', context)

def missofer(request):
    listing = BasicClinic.objects.get(pk=238)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=238)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/missouri-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/missouri-fertility.html', context)

def shiforrepmestlofecl(request):
    listing = BasicClinic.objects.get(pk=239)

    missourilisting = BasicClinic.objects.all()
    missourilisting = missourilisting.filter(is_published=True)
    missourilisting = missourilisting.filter(clinicRegion__iexact='Missouri')
    missourilisting = missourilisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=239)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'missourilisting': missourilisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Missouri/sher-institutes-for-reproductive-medicine-st-louis-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'missourilisting': missourilisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Missouri/sher-institutes-for-reproductive-medicine-st-louis-fertility-clinic.html', context)

# NEBRASKA Views --------------------------------------------------------------------------------------------------------

def hearceforrepme(request):
    listing = BasicClinic.objects.get(pk=240)

    nebraskalisting = BasicClinic.objects.all()
    nebraskalisting = nebraskalisting.filter(is_published=True)
    nebraskalisting = nebraskalisting.filter(clinicRegion__iexact='Nebraska')
    nebraskalisting = nebraskalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=240)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nebraskalisting': nebraskalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Nebraska/heartland-center-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nebraskalisting': nebraskalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Nebraska/heartland-center-for-reproductive-medicine.html', context)

# NEVADA Views --------------------------------------------------------------------------------------------------------

def greevalferpartners(request):
    listing = BasicClinic.objects.get(pk=241)

    nevadalisting = BasicClinic.objects.all()
    nevadalisting = nevadalisting.filter(is_published=True)
    nevadalisting = nevadalisting.filter(clinicRegion__iexact='Nevada')
    nevadalisting = nevadalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=241)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nevadalisting': nevadalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Nevada/green-valley-fertility-partners.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nevadalisting': nevadalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Nevada/green-valley-fertility-partners.html', context)

def theferceoflasvegas(request):
    listing = BasicClinic.objects.get(pk=242)

    nevadalisting = BasicClinic.objects.all()
    nevadalisting = nevadalisting.filter(is_published=True)
    nevadalisting = nevadalisting.filter(clinicRegion__iexact='Nevada')
    nevadalisting = nevadalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=242)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nevadalisting': nevadalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Nevada/the-fertility-center-of-las-vegas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nevadalisting': nevadalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Nevada/the-fertility-center-of-las-vegas.html', context)

def sherinsfrepmedlasvegfecl(request):
    listing = BasicClinic.objects.get(pk=243)

    nevadalisting = BasicClinic.objects.all()
    nevadalisting = nevadalisting.filter(is_published=True)
    nevadalisting = nevadalisting.filter(clinicRegion__iexact='Nevada')
    nevadalisting = nevadalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=243)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nevadalisting': nevadalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Nevada/sher-institutes-for-reproductive-medicine-las-vegas-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nevadalisting': nevadalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Nevada/sher-institutes-for-reproductive-medicine-las-vegas-fertility-clinic.html', context)

def redrofercen(request):
    listing = BasicClinic.objects.get(pk=244)

    nevadalisting = BasicClinic.objects.all()
    nevadalisting = nevadalisting.filter(is_published=True)
    nevadalisting = nevadalisting.filter(clinicRegion__iexact='Nevada')
    nevadalisting = nevadalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=244)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'nevadalisting': nevadalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Nevada/red-rock-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'nevadalisting': nevadalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Nevada/red-rock-fertility-center.html', context)

# NEW JERSEY Views --------------------------------------------------------------------------------------------------------

def irmsco(request):
    listing = BasicClinic.objects.get(pk=27)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=27)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-clark-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-clark-office.html', context)

def irmsewo(request):
    listing = BasicClinic.objects.get(pk=28)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=28)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-east-windsor-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-east-windsor-office.html', context)

def irmsho(request):
    listing = BasicClinic.objects.get(pk=29)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=29)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-hackensack-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hackensack-office.html', context)

def irmshbo(request):
    listing = BasicClinic.objects.get(pk=30)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=30)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-hoboken-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hoboken-office.html', context)

def irmsnjo(request):
    listing = BasicClinic.objects.get(pk=31)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=31)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-jersey-city-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-jersey-city-office.html', context)

def irmslo(request):
    listing = BasicClinic.objects.get(pk=32)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=32)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-livingston-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-livingston-office.html', context)

def irmsobo(request):
    listing = BasicClinic.objects.get(pk=33)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=33)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/irms-old-bridge-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/irms-old-bridge-office.html', context)

def Cenfoarepmedicinefer(request):
    listing = BasicClinic.objects.get(pk=245)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=245)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/center-for-advanced-reproductive-medicine-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/center-for-advanced-reproductive-medicine-fertility.html', context)

def rmanetbasrid(request):
    listing = BasicClinic.objects.get(pk=246)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=246)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-basking-ridge.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-basking-ridge.html', context)

def rmaneteaton(request):
    listing = BasicClinic.objects.get(pk=247)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=247)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-eatontown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-eatontown.html', context)

def rmanetenglewood(request):
    listing = BasicClinic.objects.get(pk=248)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=248)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-englewood.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-englewood.html', context)

def rmanetfreehold(request):
    listing = BasicClinic.objects.get(pk=249)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=249)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-freehold.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-freehold.html', context)

def rmanetmarlton(request):
    listing = BasicClinic.objects.get(pk=250)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=250)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-marlton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-marlton.html', context)

def rmanetmorristown(request):
    listing = BasicClinic.objects.get(pk=251)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=251)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-morristown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-morristown.html', context)

def rmanetprinceston(request):
    listing = BasicClinic.objects.get(pk=252)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=252)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-princeton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-princeton.html', context)

def rmanetsomerset(request):
    listing = BasicClinic.objects.get(pk=253)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=253)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-somerset.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-somerset.html', context)

def rmanetspringfield(request):
    listing = BasicClinic.objects.get(pk=254)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=254)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-springfield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-springfield.html', context)

def rmanetwestorang(request):
    listing = BasicClinic.objects.get(pk=255)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=255)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/rma-network-west-orange.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-west-orange.html', context)

def unirepproassohasbhei(request):
    listing = BasicClinic.objects.get(pk=256)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=256)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hasbrouck-heights.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hasbrouck-heights.html', context)

def unirepproassohoboken(request):
    listing = BasicClinic.objects.get(pk=257)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=257)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hoboken.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hoboken.html', context)

def unirepproassowayne(request):
    listing = BasicClinic.objects.get(pk=258)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=258)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-wayne.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-wayne.html', context)

def princetonivf(request):
    listing = BasicClinic.objects.get(pk=259)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=259)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/princeton-ivf.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/princeton-ivf.html', context)

def delawvallinsoffergenmarlton(request):
    listing = BasicClinic.objects.get(pk=260)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=260)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-marlton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-marlton.html', context)

def delawvallinsoffergenvineland(request):
    listing = BasicClinic.objects.get(pk=261)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=261)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-vineland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-vineland.html', context)

def delawvallinsoffergenprinceton(request):
    listing = BasicClinic.objects.get(pk=262)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=262)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-princeton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-princeton.html', context)

def southjefecemarlton(request):
    listing = BasicClinic.objects.get(pk=263)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=263)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-marlton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-marlton.html', context)

def southjefeceburlington(request):
    listing = BasicClinic.objects.get(pk=264)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=264)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-burlington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-burlington.html', context)

def southjefecesewell(request):
    listing = BasicClinic.objects.get(pk=265)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=265)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-sewell.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-sewell.html', context)

def southjefecetownship(request):
    listing = BasicClinic.objects.get(pk=266)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=266)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-egg-harbor-township.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-egg-harbor-township.html', context)

def diamondinsmilburn(request):
    listing = BasicClinic.objects.get(pk=267)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=267)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/diamond-institute-millburn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-millburn.html', context)

def diamondinsdover(request):
    listing = BasicClinic.objects.get(pk=269)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=269)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/diamond-institute-dover.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-dover.html', context)

def diamondinsmtlaurel(request):
    listing = BasicClinic.objects.get(pk=270)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=270)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/cooper-institute-mt-laurel.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-mt-laurel.html', context)

def diamondinsmtmelrosepark(request):
    listing = BasicClinic.objects.get(pk=271)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=271)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/cooper-institute-melrose-park.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-melrose-park.html', context)

def fertilinstofnewjernewyork(request):
    listing = BasicClinic.objects.get(pk=272)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=272)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/fertility-institute-of-new-jersey-new-york.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }


    return render(request, 'clinics/US/New-Jersey/fertility-institute-of-new-jersey-new-york.html', context)

def damienfertpartshrewsbury(request):
    listing = BasicClinic.objects.get(pk=273)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=273)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-shrewsbury.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-shrewsbury.html', context)

def damienfertpartnewjerseycity(request):
    listing = BasicClinic.objects.get(pk=274)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=274)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-jersey-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-jersey-city.html', context)

def damienfertpartnewark(request):
    listing = BasicClinic.objects.get(pk=275)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=275)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-newark.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-newark.html', context)

def islandrepsernewjer(request):
    listing = BasicClinic.objects.get(pk=276)

    newjerseylisting = BasicClinic.objects.all()
    newjerseylisting = newjerseylisting.filter(is_published=True)
    newjerseylisting = newjerseylisting.filter(clinicRegion__iexact='New Jersey')
    newjerseylisting = newjerseylisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=276)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newjerseylisting': newjerseylisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Jersey/island-reproductive-services-new-jersey.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newjerseylisting': newjerseylisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Jersey/island-reproductive-services-new-jersey.html', context)

# NEW MEXICO Views --------------------------------------------------------------------------------------------------------

def ferticentofnewmexico(request):
    listing = BasicClinic.objects.get(pk=277)

    newmexicolisting = BasicClinic.objects.all()
    newmexicolisting = newmexicolisting.filter(is_published=True)
    newmexicolisting = newmexicolisting.filter(clinicRegion__iexact='New Mexico')
    newmexicolisting = newmexicolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=277)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newmexicolisting': newmexicolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-Mexico/fertility-center-of-new-mexico.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newmexicolisting': newmexicolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-Mexico/fertility-center-of-new-mexico.html', context)

# NEW YORK Views --------------------------------------------------------------------------------------------------------

def diamondinsgoshen(request):
    listing = BasicClinic.objects.get(pk=268)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=268)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/diamond-institute-goshen.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/diamond-institute-goshen.html', context)

def cfnyc(request):
    listing = BasicClinic.objects.get(pk=34)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=34)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/chelsea-fertility-nyc.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/chelsea-fertility-nyc.html', context)

def ccrmnyfc(request):
    listing = BasicClinic.objects.get(pk=35)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=35)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/ccrm-new-york-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/ccrm-new-york-fertility-clinic.html', context)

def sherinsforrepmednewyorkferclinic(request):
    listing = BasicClinic.objects.get(pk=278)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=278)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/sher-institutes-for-reproductive-medicine-new-york-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/sher-institutes-for-reproductive-medicine-new-york-fertility-clinic.html', context)

def greenwfertuck(request):
    listing = BasicClinic.objects.get(pk=279)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=279)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/greenwich-fertility-tuckahoe.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/greenwich-fertility-tuckahoe.html', context)

def rmactnorwalk(request):
    listing = BasicClinic.objects.get(pk=280)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=280)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/rmact-norwalk.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/rmact-norwalk.html', context)

def extendfert(request):
    listing = BasicClinic.objects.get(pk=281)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=281)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/extend-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/extend-fertility.html', context)

def geneferrepromedibaypark(request):
    listing = BasicClinic.objects.get(pk=282)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=282)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-bay-parkway.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-bay-parkway.html', context)

def geneferrepromediparkslope(request):
    listing = BasicClinic.objects.get(pk=283)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=283)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-park-slope.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-park-slope.html', context)

def geneferrepromediforesthills(request):
    listing = BasicClinic.objects.get(pk=284)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=284)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-forest-hills.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-forest-hills.html', context)

def geneferrepromedistatenisland(request):
    listing = BasicClinic.objects.get(pk=285)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=285)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-staten-island.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-staten-island.html', context)

def geneferrepromedilongisland(request):
    listing = BasicClinic.objects.get(pk=286)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=286)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-long-island.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-long-island.html', context)

def buffinferivfas(request):
    listing = BasicClinic.objects.get(pk=287)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=287)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/buffalo-infertility-and-ivf-associates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/buffalo-infertility-and-ivf-associates.html', context)

def hudsvallfert(request):
    listing = BasicClinic.objects.get(pk=288)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=288)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/hudson-valley-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/hudson-valley-fertility.html', context)

def bostonivfalbany(request):
    listing = BasicClinic.objects.get(pk=289)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=289)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/boston-ivf–albany.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/boston-ivf–albany.html', context)

def bostonivfsyracusy(request):
    listing = BasicClinic.objects.get(pk=290)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=290)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/boston-ivf-syracuse.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/boston-ivf-syracuse.html', context)

def longislivfmelville(request):
    listing = BasicClinic.objects.get(pk=291)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=291)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-melville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-melville.html', context)

def longislivfeastpatchogue(request):
    listing = BasicClinic.objects.get(pk=292)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=292)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-east-patchogue.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-east-patchogue.html', context)

def longislivfgardencity(request):
    listing = BasicClinic.objects.get(pk=293)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=293)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-garden-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-garden-city.html', context)

def longislivfwestislip(request):
    listing = BasicClinic.objects.get(pk=294)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=294)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-west-islip.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-west-islip.html', context)

def longislivflakesuccess(request):
    listing = BasicClinic.objects.get(pk=295)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=295)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-lake-success.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-lake-success.html', context)

def longislivfstonybrooks(request):
    listing = BasicClinic.objects.get(pk=296)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=296)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/long-island-ivf-stony-brook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-stony-brook.html', context)

def nyulangonerepspenewyorkmineola(request):
    listing = BasicClinic.objects.get(pk=297)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=297)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-mineola.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-mineola.html', context)

def nyulangonerepspenewyorkbrooklyn(request):
    listing = BasicClinic.objects.get(pk=298)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=298)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-brooklyn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-brooklyn.html', context)

def kindboynewyorkmedical(request):
    listing = BasicClinic.objects.get(pk=299)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=299)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/kindbody-of-new-york-medical.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/kindbody-of-new-york-medical.html', context)

def kofifertgroupstatenisland(request):
    listing = BasicClinic.objects.get(pk=300)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=300)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/kofinas-fertility-group-staten-island.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-staten-island.html', context)

def kofifertgroupupperwestside(request):
    listing = BasicClinic.objects.get(pk=301)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=301)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/kofinas-fertility-group-upper-west-side.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-upper-west-side.html', context)

def kofifertgrouplowermanhattan(request):
    listing = BasicClinic.objects.get(pk=302)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=302)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/kofinas-fertility-group-lower-manhattan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-lower-manhattan.html', context)

def sgfmanhattan(request):
    listing = BasicClinic.objects.get(pk=303)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=303)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/sgf-manhattan.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/sgf-manhattan.html', context)

def newaymedical(request):
    listing = BasicClinic.objects.get(pk=304)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=304)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/neway-medical.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/neway-medical.html', context)

def repromedassocnewyorkeastside(request):
    listing = BasicClinic.objects.get(pk=305)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=305)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-eastside.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-eastside.html', context)

def repromedassocnewyorkwestside(request):
    listing = BasicClinic.objects.get(pk=306)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=306)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westside.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westside.html', context)

def repromedassocnewyorkdowntown(request):
    listing = BasicClinic.objects.get(pk=307)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=307)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-downtown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-downtown.html', context)

def repromedassocnewyorkbrooklyn(request):
    listing = BasicClinic.objects.get(pk=308)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=308)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-brooklyn.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-brooklyn.html', context)

def repromedassocnewyorkwestchester(request):
    listing = BasicClinic.objects.get(pk=309)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=309)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westchester.html', context)

def repromedassocnewyorkmountsinai(request):
    listing = BasicClinic.objects.get(pk=310)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=310)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-mount-sinai.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-mount-sinai.html', context)

def islandreproservicesstatenisland(request):
    listing = BasicClinic.objects.get(pk=311)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=311)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/island-reproductive-services-staten-island.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/island-reproductive-services-staten-island.html', context)

def cnyfercensyracuse(request):
    listing = BasicClinic.objects.get(pk=312)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=312)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/cny-fertility-center-syracuse.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-syracuse.html', context)

def cnyfercenalbany(request):
    listing = BasicClinic.objects.get(pk=313)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=313)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/cny-fertility-center-albany.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-albany.html', context)

def cnyfercenrochester(request):
    listing = BasicClinic.objects.get(pk=314)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=314)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/cny-fertility-center-rochester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-rochester.html', context)

def cnyfercenbuffalo(request):
    listing = BasicClinic.objects.get(pk=315)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=315)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/cny-fertility-center-buffalo.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-buffalo.html', context)

def nyulangonefertilitycenter(request):
    listing = BasicClinic.objects.get(pk=707)

    newyorklisting = BasicClinic.objects.all()
    newyorklisting = newyorklisting.filter(is_published=True)
    newyorklisting = newyorklisting.filter(clinicRegion__iexact='New York')
    newyorklisting = newyorklisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=315)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newyorklisting': newyorklisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/New-York/nyu-langone-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newyorklisting': newyorklisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-fertility-center.html', context)

# NORTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def northcarcenfrepmedic(request):
    listing = BasicClinic.objects.get(pk=316)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=316)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/north-carolina-center-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/north-carolina-center-for-reproductive-medicine.html', context)

def reproendoassoofcharlotte(request):
    listing = BasicClinic.objects.get(pk=317)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=317)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte.html', context)

def reproendoassoofcharlottelakenorman(request):
    listing = BasicClinic.objects.get(pk=318)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=318)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte-lake-norman.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte-lake-norman.html', context)

def atlanticreprmedspec(request):
    listing = BasicClinic.objects.get(pk=319)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=319)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/atlantic-reproductive-medicine-specialists.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/atlantic-reproductive-medicine-specialists.html', context)

def carolinaconcerale(request):
    listing = BasicClinic.objects.get(pk=320)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=320)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolina-conceptions-raleigh.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-raleigh.html', context)

def carolinaconcewilmington(request):
    listing = BasicClinic.objects.get(pk=321)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=321)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolina-conceptions-wilmington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-wilmington.html', context)

def carolinaconcehampstead(request):
    listing = BasicClinic.objects.get(pk=322)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=322)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolina-conceptions-hampstead.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-hampstead.html', context)

def carolinaconcegreenville(request):
    listing = BasicClinic.objects.get(pk=323)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=323)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolina-conceptions-greenville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-greenville.html', context)

def carolfertinstgreens(request):
    listing = BasicClinic.objects.get(pk=324)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=324)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-greensboro.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-greensboro.html', context)

def carolfertinstwinstonsalem(request):
    listing = BasicClinic.objects.get(pk=325)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=325)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-winston-salem.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-winston-salem.html', context)

def carolfertinstcharlotte(request):
    listing = BasicClinic.objects.get(pk=326)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=326)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-charlotte.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-charlotte.html', context)

def piedmoreproendogroupashe(request):
    listing = BasicClinic.objects.get(pk=327)

    newcarolinalisting = BasicClinic.objects.all()
    newcarolinalisting = newcarolinalisting.filter(is_published=True)
    newcarolinalisting = newcarolinalisting.filter(clinicRegion__iexact='New Carolina')
    newcarolinalisting = newcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=327)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newcarolinalisting': newcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Carolina/piedmont-reproductive-endocrinology-group-asheville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newcarolinalisting': newcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Carolina/piedmont-reproductive-endocrinology-group-asheville.html', context)

# NORTH DAKOTA Views --------------------------------------------------------------------------------------------------------

def midwecenforreprohealfargo(request):
    listing = BasicClinic.objects.get(pk=328)

    newdakotalisting = BasicClinic.objects.all()
    newdakotalisting = newdakotalisting.filter(is_published=True)
    newdakotalisting = newdakotalisting.filter(clinicRegion__iexact='New Dakota')
    newdakotalisting = newdakotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=328)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newdakotalisting': newdakotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-fargo.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newdakotalisting': newdakotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-fargo.html', context)

def midwecenforreprohealminot(request):
    listing = BasicClinic.objects.get(pk=329)

    newdakotalisting = BasicClinic.objects.all()
    newdakotalisting = newdakotalisting.filter(is_published=True)
    newdakotalisting = newdakotalisting.filter(clinicRegion__iexact='New Dakota')
    newdakotalisting = newdakotalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=329)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'newdakotalisting': newdakotalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-minot.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'newdakotalisting': newdakotalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-minot.html', context)

# OHIO Views --------------------------------------------------------------------------------------------------------

def ivfmichiganohio(request):
    listing = BasicClinic.objects.get(pk=330)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=330)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/ivf-michigan-ohio.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/ivf-michigan-ohio.html', context)

def northeasternohiofertcen(request):
    listing = BasicClinic.objects.get(pk=331)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=331)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/northeastern-ohio-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/northeastern-ohio-fertility-center.html', context)

def reprogyninferakron(request):
    listing = BasicClinic.objects.get(pk=332)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=332)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-akron.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-akron.html', context)

def reprogyninfercolumbus(request):
    listing = BasicClinic.objects.get(pk=333)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=333)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-columbus.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-columbus.html', context)

def reprogyninfercleveland(request):
    listing = BasicClinic.objects.get(pk=334)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=334)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-cleveland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-cleveland.html', context)

def reprogyninferyoungstown(request):
    listing = BasicClinic.objects.get(pk=335)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=335)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-youngstown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-youngstown.html', context)

def reprogyninfercanton(request):
    listing = BasicClinic.objects.get(pk=336)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=336)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-canton.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-canton.html', context)

def springcreekfertility(request):
    listing = BasicClinic.objects.get(pk=337)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=337)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/springcreek-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/springcreek-fertility.html', context)

def instituteforhealthcincinnati(request):
    listing = BasicClinic.objects.get(pk=338)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=338)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-cincinnati.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-cincinnati.html', context)

def instituteforhealthwestche(request):
    listing = BasicClinic.objects.get(pk=339)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=339)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-west-chester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-west-chester.html', context)

def ohioreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=340)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=340)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/ohio-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/ohio-reproductive-medicine.html', context)

def fertilitywellnessinstohio(request):
    listing = BasicClinic.objects.get(pk=341)

    ohiolisting = BasicClinic.objects.all()
    ohiolisting = ohiolisting.filter(is_published=True)
    ohiolisting = ohiolisting.filter(clinicRegion__iexact='Ohio')
    ohiolisting = ohiolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=341)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'ohiolisting': ohiolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Ohio/fertility-wellness-institute-of-ohio.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'ohiolisting': ohiolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Ohio/fertility-wellness-institute-of-ohio.html', context)

# OKLAHOMA Views --------------------------------------------------------------------------------------------------------

def ouphysiciansrepromedicine(request):
    listing = BasicClinic.objects.get(pk=342)

    oklahomalisting = BasicClinic.objects.all()
    oklahomalisting = oklahomalisting.filter(is_published=True)
    oklahomalisting = oklahomalisting.filter(clinicRegion__iexact='Oklahoma')
    oklahomalisting = oklahomalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=342)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oklahomalisting': oklahomalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Oklahoma/ou-physicians-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oklahomalisting': oklahomalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Oklahoma/ou-physicians-reproductive-medicine.html', context)

def tulsafertcenter(request):
    listing = BasicClinic.objects.get(pk=343)

    oklahomalisting = BasicClinic.objects.all()
    oklahomalisting = oklahomalisting.filter(is_published=True)
    oklahomalisting = oklahomalisting.filter(clinicRegion__iexact='Oklahoma')
    oklahomalisting = oklahomalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=343)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oklahomalisting': oklahomalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Oklahoma/tulsa-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oklahomalisting': oklahomalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Oklahoma/tulsa-fertility-center.html', context)

# OREGON Views --------------------------------------------------------------------------------------------------------

def ormfertilityclidownportland(request):
    listing = BasicClinic.objects.get(pk=344)

    oregonlisting = BasicClinic.objects.all()
    oregonlisting = oregonlisting.filter(is_published=True)
    oregonlisting = oregonlisting.filter(clinicRegion__iexact='Oregon')
    oregonlisting = oregonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=344)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oregonlisting': oregonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Oregon/orm-fertility-clinic-downtown-portland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oregonlisting': oregonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-downtown-portland.html', context)

def ormfertilitycliwestsideportland(request):
    listing = BasicClinic.objects.get(pk=345)

    oregonlisting = BasicClinic.objects.all()
    oregonlisting = oregonlisting.filter(is_published=True)
    oregonlisting = oregonlisting.filter(clinicRegion__iexact='Oregon')
    oregonlisting = oregonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=345)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oregonlisting': oregonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Oregon/orm-fertility-clinic-westside-portland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oregonlisting': oregonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-westside-portland.html', context)

def ormfertilityclisouthportland(request):
    listing = BasicClinic.objects.get(pk=346)

    oregonlisting = BasicClinic.objects.all()
    oregonlisting = oregonlisting.filter(is_published=True)
    oregonlisting = oregonlisting.filter(clinicRegion__iexact='Oregon')
    oregonlisting = oregonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=346)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'oregonlisting': oregonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Oregon/orm-fertility-clinic-southside-portland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'oregonlisting': oregonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-southside-portland.html', context)

# PENNSYLVANIA Views --------------------------------------------------------------------------------------------------------

def sincerarepromedabington(request):
    listing = BasicClinic.objects.get(pk=347)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=347)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-abington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-abington.html', context)

def sincerarepromedbethlehem(request):
    listing = BasicClinic.objects.get(pk=348)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=348)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-bethlehem.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-bethlehem.html', context)

def sincerarepromedfortwashington(request):
    listing = BasicClinic.objects.get(pk=349)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=349)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-fort-washington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-fort-washington.html', context)

def sincerarepromedkingofprussia(request):
    listing = BasicClinic.objects.get(pk=350)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=350)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-king-of-prussia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-king-of-prussia.html', context)

def sincerarepromedlancaster(request):
    listing = BasicClinic.objects.get(pk=351)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=351)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lancaster.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lancaster.html', context)

def sincerarepromedlanghorne(request):
    listing = BasicClinic.objects.get(pk=352)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=352)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-langhorne.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-langhorne.html', context)

def sincerarepromedlansdale(request):
    listing = BasicClinic.objects.get(pk=353)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=353)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lansdale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lansdale.html', context)

def sincerarepromedwestchester(request):
    listing = BasicClinic.objects.get(pk=354)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=354)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-west-chester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-west-chester.html', context)

def rmanetwork(request):
    listing = BasicClinic.objects.get(pk=355)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=355)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/rma-network-allentown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/rma-network-allentown.html', context)

def familyfertilitycenterbethlehem(request):
    listing = BasicClinic.objects.get(pk=356)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=356)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/family-fertility-center-bethlehem.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-bethlehem.html', context)

def familyfertilitycenterclarkssummit(request):
    listing = BasicClinic.objects.get(pk=357)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=357)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/family-fertility-center-clarks-summit.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-clarks-summit.html', context)

def mainlinefertilityrepromedicinebrynmawr(request):
    listing = BasicClinic.objects.get(pk=358)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=358)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-bryn-mawr.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-bryn-mawr.html', context)

def mainlinefertilityrepromedicinepaoli(request):
    listing = BasicClinic.objects.get(pk=359)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=359)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-paoli.html', context)

    else:
        pass


    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-paoli.html', context)

def mainlinefertilityrepromedicinephiladelphia(request):
    listing = BasicClinic.objects.get(pk=360)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=360)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-philadelphia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-philadelphia.html', context)

def mainlinefertilityrepromedicinewestchester(request):
    listing = BasicClinic.objects.get(pk=361)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=361)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-west-chester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-west-chester.html', context)

def mainlinefertilityrepromedicinehavertown(request):
    listing = BasicClinic.objects.get(pk=362)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=362)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-havertown.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-havertown.html', context)

def mainlinefertilityrepromedicinereading(request):
    listing = BasicClinic.objects.get(pk=363)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=363)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-reading.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-reading.html', context)

def shadygrovefertilityphiladelphia(request):
    listing = BasicClinic.objects.get(pk=364)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=364)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-philadelphia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-philadelphia.html', context)

def shadygrovefertilitychesterbrook(request):
    listing = BasicClinic.objects.get(pk=365)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=365)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-chesterbrook.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-chesterbrook.html', context)

def shadygrovefertilitymechanicsburg(request):
    listing = BasicClinic.objects.get(pk=366)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=366)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-mechanicsburg.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-mechanicsburg.html', context)

def shadygrovefertilitylancaster(request):
    listing = BasicClinic.objects.get(pk=367)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=367)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-lancaster.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-lancaster.html', context)

def shadygrovefertilitywarrington(request):
    listing = BasicClinic.objects.get(pk=368)

    pennsylvanialisting = BasicClinic.objects.all()
    pennsylvanialisting = pennsylvanialisting.filter(is_published=True)
    pennsylvanialisting = pennsylvanialisting.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvanialisting = pennsylvanialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=368)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'pennsylvanialisting': pennsylvanialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-warrington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'pennsylvanialisting': pennsylvanialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-warrington.html', context)

# PUERTO RICO Views --------------------------------------------------------------------------------------------------------

def puertoricofertilitycenter(request):
    listing = BasicClinic.objects.get(pk=369)

    puertoricolisting = BasicClinic.objects.all()
    puertoricolisting = puertoricolisting.filter(is_published=True)
    puertoricolisting = puertoricolisting.filter(clinicRegion__iexact='Puerto Rico')
    puertoricolisting = puertoricolisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=369)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'puertoricolisting': puertoricolisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Puerto-Rico/puerto-rico-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'puertoricolisting': puertoricolisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Puerto-Rico/puerto-rico-fertility-center.html', context)

# SOUTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def piedmontreproendogroupgreenville(request):
    listing = BasicClinic.objects.get(pk=370)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=370)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-greenville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-greenville.html', context)


def piedmontreproendogroupspartanburg(request):
    listing = BasicClinic.objects.get(pk=371)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=371)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-spartanburg.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-spartanburg.html', context)

def piedmontreproendogroupcolumbia(request):
    listing = BasicClinic.objects.get(pk=372)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=372)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-columbia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-columbia.html', context)

def coastalfertspecimountpleasant(request):
    listing = BasicClinic.objects.get(pk=373)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=373)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-mount-pleasant.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-mount-pleasant.html', context)

def coastalfertspecinorthcharleston(request):
    listing = BasicClinic.objects.get(pk=374)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=374)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-north-charleston.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-north-charleston.html', context)

def coastalfertspecilexington(request):
    listing = BasicClinic.objects.get(pk=375)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=375)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-lexington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-lexington.html', context)

def coastalfertspecimyrtlebeach(request):
    listing = BasicClinic.objects.get(pk=376)

    southcarolinalisting = BasicClinic.objects.all()
    southcarolinalisting = southcarolinalisting.filter(is_published=True)
    southcarolinalisting = southcarolinalisting.filter(clinicRegion__iexact='South Carolina')
    southcarolinalisting = southcarolinalisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=376)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'southcarolinalisting': southcarolinalisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-myrtle-beach.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'southcarolinalisting': southcarolinalisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-myrtle-beach.html', context)

# TENNESSEE Views --------------------------------------------------------------------------------------------------------

def tenrepromedchattaivffertclin(request):
    listing = BasicClinic.objects.get(pk=377)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=377)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/tennessee-reproductive-medicine-chattanooga-ivf-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/tennessee-reproductive-medicine-chattanooga-ivf-fertility-clinic.html', context)

def myfertilitycenterchatt(request):
    listing = BasicClinic.objects.get(pk=378)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=378)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/my-fertility-center-chattanooga.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/my-fertility-center-chattanooga.html', context)

def myfertilitycenterknoxville(request):
    listing = BasicClinic.objects.get(pk=379)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=379)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/my-fertility-center-knoxville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/my-fertility-center-knoxville.html', context)

def tennesseefertiinstitute(request):
    listing = BasicClinic.objects.get(pk=380)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=380)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/tennessee-fertility-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/tennessee-fertility-institute.html', context)

def fertiassoofmemphis(request):
    listing = BasicClinic.objects.get(pk=381)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=381)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/fertility-associates-of-memphis.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/fertility-associates-of-memphis.html', context)

def nashvillefertnashville(request):
    listing = BasicClinic.objects.get(pk=382)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=382)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/nashville-fertility-nashville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-nashville.html', context)

def nashvillefertmurfreesboro(request):
    listing = BasicClinic.objects.get(pk=383)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=383)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/nashville-fertility-murfreesboro.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-murfreesboro.html', context)

def nashvillefertfranklin(request):
    listing = BasicClinic.objects.get(pk=384)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=384)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/nashville-fertility-franklin.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-franklin.html', context)

def centerforreprohealthnash(request):
    listing = BasicClinic.objects.get(pk=385)

    tennesseelisting = BasicClinic.objects.all()
    tennesseelisting = tennesseelisting.filter(is_published=True)
    tennesseelisting = tennesseelisting.filter(clinicRegion__iexact='Tennessee')
    tennesseelisting = tennesseelisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=385)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'tennesseelisting': tennesseelisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Tennessee/the-center-for-reproductive-health-nashville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'tennesseelisting': tennesseelisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Tennessee/the-center-for-reproductive-health-nashville.html', context)

# TEXAS Views --------------------------------------------------------------------------------------------------------

def sherinsforrepmedicinedallas(request):
    listing = BasicClinic.objects.get(pk=386)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=386)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/sher-institutes-for-reproductive-medicine-dallas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/sher-institutes-for-reproductive-medicine-dallas.html', context)

def ccrmdallasfortworth(request):
    listing = BasicClinic.objects.get(pk=387)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=387)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ccrm-dallas-fort-worth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ccrm-dallas-fort-worth.html', context)

def ccrmhoustonmaincenter(request):
    listing = BasicClinic.objects.get(pk=388)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=388)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ccrm-houston-main-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-main-center.html', context)

def ccrmhoustonmedicalcenter(request):
    listing = BasicClinic.objects.get(pk=389)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=389)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ccrm-houston-medical-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-medical-center.html', context)

def ccrmhoustonsugarland(request):
    listing = BasicClinic.objects.get(pk=390)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=390)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ccrm-houston-sugar-land.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-sugar-land.html', context)

def aspirefertaustinfertilitycenter(request):
    listing = BasicClinic.objects.get(pk=391)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=391)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-austin-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-austin-fertility-center.html', context)

def aspirefertbeecavefertcenter(request):
    listing = BasicClinic.objects.get(pk=392)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=392)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-bee-cave-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-bee-cave-fertility-center.html', context)

def aspirefertadison(request):
    listing = BasicClinic.objects.get(pk=393)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=393)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-adison.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-adison.html', context)

def aspirefertclearlake(request):
    listing = BasicClinic.objects.get(pk=394)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=394)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-clear-lake-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-clear-lake-fertility-center.html', context)

def aspirefertfanninfece(request):
    listing = BasicClinic.objects.get(pk=395)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=395)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-fannin-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-fannin-fertility-center.html', context)

def aspirefertkatyfertce(request):
    listing = BasicClinic.objects.get(pk=396)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=396)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-katy-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-katy-fertility-center.html', context)

def aspirefertmainstreet(request):
    listing = BasicClinic.objects.get(pk=397)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=397)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-main-street-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-main-street-fertility-center.html', context)

def aspirefertsugarlandfertcen(request):
    listing = BasicClinic.objects.get(pk=398)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=398)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-sugar-land-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-sugar-land-fertility-center.html', context)

def aspirefertwillowbrookfertcent(request):
    listing = BasicClinic.objects.get(pk=399)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=399)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-willowbrook-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-willowbrook-fertility-center.html', context)

def aspirefertsanantoniofertcenter(request):
    listing = BasicClinic.objects.get(pk=400)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=400)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-san-antonio-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-san-antonio-fertility-center.html', context)

def aspirefertsatellitecliniclocation(request):
    listing = BasicClinic.objects.get(pk=401)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=401)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/aspire-fertility-satellite-clinic-location.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-satellite-clinic-location.html', context)

def ivfmdcenterarlington(request):
    listing = BasicClinic.objects.get(pk=402)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=402)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ivfmd-center-arlington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ivfmd-center-arlington.html', context)

def ivfmdcenterirving(request):
    listing = BasicClinic.objects.get(pk=403)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=403)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ivfmd-center-irving.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ivfmd-center-irving.html', context)

def austinfertrepmedwestlake(request):
    listing = BasicClinic.objects.get(pk=404)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=404)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-westlake.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-westlake.html', context)

def austinfertrepmedsouthlocation(request):
    listing = BasicClinic.objects.get(pk=405)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=405)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-south-location.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-south-location.html', context)

def austinfertrepmedroundrock(request):
    listing = BasicClinic.objects.get(pk=406)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=406)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-round-rock.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-round-rock.html', context)

def texasfertilitycentercentralaustin(request):
    listing = BasicClinic.objects.get(pk=407)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=407)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-central-austin.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-central-austin.html', context)

def texasfertilitycenterroundrock(request):
    listing = BasicClinic.objects.get(pk=408)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=408)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-round-rock.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-round-rock.html', context)

def texasfertilitycentersouthaustin(request):
    listing = BasicClinic.objects.get(pk=409)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=409)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-south-austin.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-south-austin.html', context)

def texasfertilitycenternewbraunfels(request):
    listing = BasicClinic.objects.get(pk=410)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=410)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-new-braunfels.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-new-braunfels.html', context)

def texasfertilitycentersanantonio(request):
    listing = BasicClinic.objects.get(pk=411)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=411)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-san-antonio.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-san-antonio.html', context)

def texasfertilitycentercorpuschristi(request):
    listing = BasicClinic.objects.get(pk=412)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=412)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-fertility-center-corpus-christi.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-corpus-christi.html', context)

def centerforassistedreprobedford(request):
    listing = BasicClinic.objects.get(pk=413)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=413)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-bedford.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-bedford.html', context)

def centerforassistedreprofortworth(request):
    listing = BasicClinic.objects.get(pk=414)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=414)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-fort-worth.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-fort-worth.html', context)

def dallasfortworthfertilityassociates(request):
    listing = BasicClinic.objects.get(pk=415)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=415)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-dallas-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-dallas-fertility-center.html', context)

def dallasfortworthfertilityassociatessouthlake(request):
    listing = BasicClinic.objects.get(pk=416)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=416)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-southlake-fertility-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-southlake-fertility-center.html', context)

def dallasfortworthfertilityassociatesmedicalcity(request):
    listing = BasicClinic.objects.get(pk=417)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=417)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-medical-city-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-medical-city-office.html', context)

def fertilitycenterofdallas(request):
    listing = BasicClinic.objects.get(pk=418)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=418)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-center-of-dallas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-dallas.html', context)

def repromedfertilitycenterdallas(request):
    listing = BasicClinic.objects.get(pk=419)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=419)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-dallas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-dallas.html', context)

def repromedfertilitycentergrapevine(request):
    listing = BasicClinic.objects.get(pk=420)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=420)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-grapevine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-grapevine.html', context)

def repromedfertilitycentermckinney(request):
    listing = BasicClinic.objects.get(pk=421)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=421)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney.html', context)

def repromedfertilitycenterrockwall(request):
    listing = BasicClinic.objects.get(pk=422)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=422)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-rockwall.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-rockwall.html', context)

def repromedfertilitycentertyler(request):
    listing = BasicClinic.objects.get(pk=423)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=423)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-tyler.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-tyler.html', context)

def repromedfertilitycentermckinneysurgicalcenter(request):
    listing = BasicClinic.objects.get(pk=424)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=424)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney-surgical-center.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney-surgical-center.html', context)

def sherfertilityclinicdallas(request):
    listing = BasicClinic.objects.get(pk=425)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=425)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/sher-fertility-clinic-dallas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/sher-fertility-clinic-dallas.html', context)

def texascenterforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=426)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=426)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/texas-center-for-reproductive-health.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/texas-center-for-reproductive-health.html', context)

def fortworthfertility(request):
    listing = BasicClinic.objects.get(pk=427)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=427)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fort-worth-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fort-worth-fertility.html', context)

def dallasivffriscofertilityclinic(request):
    listing = BasicClinic.objects.get(pk=428)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=428)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-ivf-frisco-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-frisco-fertility-clinic.html', context)


def dallasivfdallasfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=429)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=429)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-ivf-dallas-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-dallas-fertility-clinic.html', context)

def dallasivfmckinleyfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=430)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=430)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-ivf-mckinney-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-mckinney-fertility-clinic.html', context)

def dallasivfplanofertilityclinic(request):
    listing = BasicClinic.objects.get(pk=431)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=431)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-ivf-plano-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-plano-fertility-clinic.html', context)

def dallasivftylerfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=432)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=432)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/dallas-ivf-tyler-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-tyler-fertility-clinic.html', context)

def fertilityspecialistsoftexasfrisco(request):
    listing = BasicClinic.objects.get(pk=433)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=433)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-frisco.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-frisco.html', context)

def fertilityspecialistsoftexasdallas(request):
    listing = BasicClinic.objects.get(pk=434)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=434)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-dallas.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-dallas.html', context)

def fertilityspecialistsoftexasrockwall(request):
    listing = BasicClinic.objects.get(pk=435)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=435)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-rockwall.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-rockwall.html', context)

def fertilityspecialistsoftexassouthlake(request):
    listing = BasicClinic.objects.get(pk=436)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=436)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-southlake.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-southlake.html', context)

def advancedfertilitycenteroftexasmemorialcity(request):
    listing = BasicClinic.objects.get(pk=437)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=437)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-memorial-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-memorial-city.html', context)

def advancedfertilitycenteroftexasspring(request):
    listing = BasicClinic.objects.get(pk=438)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=438)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-spring.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-spring.html', context)

def advancedfertilitycenteroftexascollegestation(request):
    listing = BasicClinic.objects.get(pk=439)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=439)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-college-station.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-college-station.html', context)

def centerofreproductivemedicinehouston(request):
    listing = BasicClinic.objects.get(pk=440)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=440)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-houston.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-houston.html', context)

def centerofreproductivemedicinememorialcity(request):
    listing = BasicClinic.objects.get(pk=441)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=441)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-memorial-city.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-memorial-city.html', context)

def centerofreproductivemedicineclearlake(request):
    listing = BasicClinic.objects.get(pk=442)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=442)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-clear-lake.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-clear-lake.html', context)

def centerofreproductivemedicinebeaumont(request):
    listing = BasicClinic.objects.get(pk=443)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=443)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-beaumont.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-beaumont.html', context)

def houstonfertilityinstitutehoustonoffice(request):
    listing = BasicClinic.objects.get(pk=444)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=444)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-houston-office-ivf-lab.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-houston-office-ivf-lab.html', context)

def houstonfertilityinstitutemedicalcentermemorialhermann(request):
    listing = BasicClinic.objects.get(pk=445)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=445)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–memorial-hermann.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–memorial-hermann.html', context)

def houstonfertilityinstitutemedicalcenterwomanshospital(request):
    listing = BasicClinic.objects.get(pk=446)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=446)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–womans-hospital.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–womans-hospital.html', context)

def houstonfertilityinstitutemedicalcenterkatyoffice(request):
    listing = BasicClinic.objects.get(pk=447)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=447)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-katy-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-katy-office.html', context)

def houstonfertilityinstitutemedicalcentersugarland(request):
    listing = BasicClinic.objects.get(pk=448)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=448)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-sugar-land-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-sugar-land-office.html', context)

def houstonfertilityinstitutemedicalcenterclearlakeoffice(request):
    listing = BasicClinic.objects.get(pk=449)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=449)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-clear-lake-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-clear-lake-office.html', context)

def houstonfertilityinstitutemedicalcentermemorialcityoffice(request):
    listing = BasicClinic.objects.get(pk=450)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=450)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-memorial-city-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-memorial-city-office.html', context)

def houstonfertilityinstitutemedicalcenterwillowbrookoffice(request):
    listing = BasicClinic.objects.get(pk=451)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=451)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-willowbrook-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-willowbrook-office.html', context)

def houstonfertilityinstitutemedicalcenterwoodlandsoffice(request):
    listing = BasicClinic.objects.get(pk=452)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=452)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-woodlands-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-woodlands-office.html', context)

def houstonfertilityinstitutemedicalcenterbeaumontoffice(request):
    listing = BasicClinic.objects.get(pk=453)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=453)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-beaumont-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-beaumont-office.html', context)

def houstonfertilityinstitutemedicalcentercypresstoffice(request):
    listing = BasicClinic.objects.get(pk=454)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=454)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-cypress-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-cypress-office.html', context)

def houstonfertilityinstitutemedicalcenterkingwoodoffice(request):
    listing = BasicClinic.objects.get(pk=455)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=455)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-kingwood-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-kingwood-office.html', context)

def houstonfertilityinstitutemedicalcenterpearlandoffice(request):
    listing = BasicClinic.objects.get(pk=456)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=456)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/houston-fertility-institute-pearland-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-pearland-office.html', context)

def odessaivf(request):
    listing = BasicClinic.objects.get(pk=457)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=457)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/odessa-ivf.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/odessa-ivf.html', context)

def ivfplano(request):
    listing = BasicClinic.objects.get(pk=458)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=458)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/ivf-plano.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/ivf-plano.html', context)

def fertilityceofsanantsanantoffice(request):
    listing = BasicClinic.objects.get(pk=459)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=459)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-san-antonio-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-san-antonio-office.html', context)

def fertilityceofsanantstoneoakoffice(request):
    listing = BasicClinic.objects.get(pk=460)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=460)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-stone-oak-office.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-stone-oak-office.html', context)

def hartivffertilityclinicwoodlands(request):
    listing = BasicClinic.objects.get(pk=461)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=461)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-woodlands.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-woodlands.html', context)

def hartivffertilityclinickingwood(request):
    listing = BasicClinic.objects.get(pk=462)

    texaslisting = BasicClinic.objects.all()
    texaslisting = texaslisting.filter(is_published=True)
    texaslisting = texaslisting.filter(clinicRegion__iexact='Texas')
    texaslisting = texaslisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=462)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'texaslisting': texaslisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-kingwood.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'texaslisting': texaslisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-kingwood.html', context)

# UTAH Views --------------------------------------------------------------------------------------------------------

def utahfertilitycenterogden(request):
    listing = BasicClinic.objects.get(pk=463)

    utahlisting = BasicClinic.objects.all()
    utahlisting = utahlisting.filter(is_published=True)
    utahlisting = utahlisting.filter(clinicRegion__iexact='Utah')
    utahlisting = utahlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=463)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'utahlisting': utahlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Utah/utah-fertility-center-ogden.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'utahlisting': utahlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Utah/utah-fertility-center-ogden.html', context)

def conceptionsfertility(request):
    listing = BasicClinic.objects.get(pk=464)

    utahlisting = BasicClinic.objects.all()
    utahlisting = utahlisting.filter(is_published=True)
    utahlisting = utahlisting.filter(clinicRegion__iexact='Utah')
    utahlisting = utahlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=464)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'utahlisting': utahlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Utah/conceptions-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'utahlisting': utahlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Utah/conceptions-fertility.html', context)

def reproductivecarecenterclearfield(request):
    listing = BasicClinic.objects.get(pk=465)

    utahlisting = BasicClinic.objects.all()
    utahlisting = utahlisting.filter(is_published=True)
    utahlisting = utahlisting.filter(clinicRegion__iexact='Utah')
    utahlisting = utahlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=465)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'utahlisting': utahlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Utah/reproductive-care-center-clearfield.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'utahlisting': utahlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-clearfield.html', context)

def reproductivecarecentersandy(request):
    listing = BasicClinic.objects.get(pk=466)

    utahlisting = BasicClinic.objects.all()
    utahlisting = utahlisting.filter(is_published=True)
    utahlisting = utahlisting.filter(clinicRegion__iexact='Utah')
    utahlisting = utahlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=466)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'utahlisting': utahlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Utah/reproductive-care-center-sandy.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'utahlisting': utahlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-sandy.html', context)

def reproductivecarecenterpleasantgrove(request):
    listing = BasicClinic.objects.get(pk=467)

    utahlisting = BasicClinic.objects.all()
    utahlisting = utahlisting.filter(is_published=True)
    utahlisting = utahlisting.filter(clinicRegion__iexact='Utah')
    utahlisting = utahlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=467)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'utahlisting': utahlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Utah/reproductive-care-center-pleasant-grove.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'utahlisting': utahlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-pleasant-grove.html', context)

# VERMONT Views --------------------------------------------------------------------------------------------------------

def northeasternreproductivemedicinecolchester(request):
    listing = BasicClinic.objects.get(pk=468)

    vermontlisting = BasicClinic.objects.all()
    vermontlisting = vermontlisting.filter(is_published=True)
    vermontlisting = vermontlisting.filter(clinicRegion__iexact='Vermont')
    vermontlisting = vermontlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=468)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'vermontlisting': vermontlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Vermont/northeastern-reproductive-medicine-colchester.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'vermontlisting': vermontlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Vermont/northeastern-reproductive-medicine-colchester.html', context)

# VIRGINIA Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociatesarlington(request):
    listing = BasicClinic.objects.get(pk=469)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=469)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/columbia-fertility-associates-arlington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/columbia-fertility-associates-arlington.html', context)

def ccrmmaincenter(request):
    listing = BasicClinic.objects.get(pk=470)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=470)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/ccrm-fertility-northern-virginia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/ccrm-fertility-northern-virginia.html', context)

def ccrmcolumbia(request):
    listing = BasicClinic.objects.get(pk=471)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=471)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/ccrm-columbia.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/ccrm-columbia.html', context)

def washingtonfertilitycenterannandale(request):
    listing = BasicClinic.objects.get(pk=472)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=472)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/washington-fertility-center-annandale.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-annandale.html', context)

def washingtonfertilitycenterfredericksburg(request):
    listing = BasicClinic.objects.get(pk=473)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=473)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/washington-fertility-center-fredericksburg.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-fredericksburg.html', context)

def washingtonfertilitycenterreston(request):
    listing = BasicClinic.objects.get(pk=474)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=474)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/washington-fertility-center-reston.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-reston.html', context)

def dominionfertilityarlington(request):
    listing = BasicClinic.objects.get(pk=475)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=475)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/dominion-fertility-arlington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/dominion-fertility-arlington.html', context)

def dominionfertilityfairfax(request):
    listing = BasicClinic.objects.get(pk=476)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=476)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/dominion-fertility-fairfax.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/dominion-fertility-fairfax.html', context)

def reproductivemedicineandsurgerycenterofvirginiacharlottesville(request):
    listing = BasicClinic.objects.get(pk=477)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=477)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-charlottesville.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-charlottesville.html', context)

def reproductivemedicineandsurgerycenterofvirginialynchburg(request):
    listing = BasicClinic.objects.get(pk=478)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=478)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-lynchburg.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-lynchburg.html', context)

def geneticsivfinstitute(request):
    listing = BasicClinic.objects.get(pk=479)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=479)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/genetics-ivf-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/genetics-ivf-institute.html', context)

def virginiacenterforreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=480)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=480)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/virginia-center-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/virginia-center-for-reproductive-medicine.html', context)

def thenewhopecenterforreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=481)

    virginialisting = BasicClinic.objects.all()
    virginialisting = virginialisting.filter(is_published=True)
    virginialisting = virginialisting.filter(clinicRegion__iexact='Virginia')
    virginialisting = virginialisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=481)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'virginialisting': virginialisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Virginia/the-new-hope-center-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'virginialisting': virginialisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Virginia/the-new-hope-center-for-reproductive-medicine.html', context)

# WASHINGTON Views --------------------------------------------------------------------------------------------------------

def orgfertilityclinicbellevue(request):
    listing = BasicClinic.objects.get(pk=482)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=482)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/orm-fertility-clinic-bellevue.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/orm-fertility-clinic-bellevue.html', context)

def dominionfertilitywashington(request):
    listing = BasicClinic.objects.get(pk=483)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=483)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/dominion-fertility-washington.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/dominion-fertility-washington.html', context)

def bellevuefertilityclinic(request):
    listing = BasicClinic.objects.get(pk=484)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=484)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/bellevue-fertility-clinic.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/bellevue-fertility-clinic.html', context)

def pomafertility(request):
    listing = BasicClinic.objects.get(pk=485)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=485)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/poma-fertility.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/poma-fertility.html', context)


def pacificnwfertilityseattle(request):
    listing = BasicClinic.objects.get(pk=486)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=486)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/pacific-nw-fertility-seattle.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/pacific-nw-fertility-seattle.html', context)

def pacificnwfertilitybellevue(request):
    listing = BasicClinic.objects.get(pk=487)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=487)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/pacific-nw-fertility-bellevue.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/pacific-nw-fertility-bellevue.html', context)

def seattlereproductivemedicineseattle(request):
    listing = BasicClinic.objects.get(pk=488)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=488)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-seattle.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-seattle.html', context)

def seattlereproductivemedicinebellevue(request):
    listing = BasicClinic.objects.get(pk=489)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=489)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-bellevue.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-bellevue.html', context)

def seattlereproductivemedicinetacoma(request):
    listing = BasicClinic.objects.get(pk=490)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=490)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-tacoma.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-tacoma.html', context)

def seattlereproductivemedicinekirkland(request):
    listing = BasicClinic.objects.get(pk=491)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=491)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-kirkland.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-kirkland.html', context)

def seattlereproductivemedicineeverett(request):
    listing = BasicClinic.objects.get(pk=492)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=492)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-everett.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-everett.html', context)

def seattlereproductivemedicinespokane(request):
    listing = BasicClinic.objects.get(pk=493)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=493)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-spokane.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-spokane.html', context)

def soundfertilitycare(request):
    listing = BasicClinic.objects.get(pk=494)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=494)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/sound-fertility-care.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/sound-fertility-care.html', context)

def thecenterforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=495)

    washingtonlisting = BasicClinic.objects.all()
    washingtonlisting = washingtonlisting.filter(is_published=True)
    washingtonlisting = washingtonlisting.filter(clinicRegion__iexact='Washington')
    washingtonlisting = washingtonlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=495)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtonlisting': washingtonlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington/the-center-for-reproductive-health.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtonlisting': washingtonlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington/the-center-for-reproductive-health.html', context)

# WISCONSIN Views --------------------------------------------------------------------------------------------------------

def viosfertilityinstitutechicagomilwaukee(request):
    listing = BasicClinic.objects.get(pk=496)

    wisconsinlisting = BasicClinic.objects.all()
    wisconsinlisting = wisconsinlisting.filter(is_published=True)
    wisconsinlisting = wisconsinlisting.filter(clinicRegion__iexact='Wisconsin')
    wisconsinlisting = wisconsinlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=496)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'wisconsinlisting': wisconsinlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-milwaukee.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'wisconsinlisting': wisconsinlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-milwaukee.html', context)

def viosfertilityinstitutechicagolakecountry(request):
    listing = BasicClinic.objects.get(pk=497)

    wisconsinlisting = BasicClinic.objects.all()
    wisconsinlisting = wisconsinlisting.filter(is_published=True)
    wisconsinlisting = wisconsinlisting.filter(clinicRegion__iexact='Wisconsin')
    wisconsinlisting = wisconsinlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=497)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'wisconsinlisting': wisconsinlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-lake-country.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'wisconsinlisting': wisconsinlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-lake-country.html', context)

def wisconsinfertilityinstitute(request):
    listing = BasicClinic.objects.get(pk=498)

    wisconsinlisting = BasicClinic.objects.all()
    wisconsinlisting = wisconsinlisting.filter(is_published=True)
    wisconsinlisting = wisconsinlisting.filter(clinicRegion__iexact='Wisconsin')
    wisconsinlisting = wisconsinlisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=498)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'wisconsinlisting': wisconsinlisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Wisconsin/wisconsin-fertility-institute.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'wisconsinlisting': wisconsinlisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Wisconsin/wisconsin-fertility-institute.html', context)

# WASHINGTON-DC Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociateswashingtondc(request):
    listing = BasicClinic.objects.get(pk=499)

    washingtondclisting = BasicClinic.objects.all()
    washingtondclisting = washingtondclisting.filter(is_published=True)
    washingtondclisting = washingtondclisting.filter(clinicRegion__iexact='Wisconsin')
    washingtondclisting = washingtondclisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=499)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtondclisting': washingtondclisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington-DC/columbia-fertility-associates-washington-dc.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtondclisting': washingtondclisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington-DC/columbia-fertility-associates-washington-dc.html', context)

def gwmedicalfacultyassociates(request):
    listing = BasicClinic.objects.get(pk=500)

    washingtondclisting = BasicClinic.objects.all()
    washingtondclisting = washingtondclisting.filter(is_published=True)
    washingtondclisting = washingtondclisting.filter(clinicRegion__iexact='Wisconsin')
    washingtondclisting = washingtondclisting.count()

    uslisting = BasicClinic.objects.all()
    uslisting = uslisting.filter(is_published=True)
    uslisting = uslisting.filter(clinicState__iexact='United States')
    uslisting = uslisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=500)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            'washingtondclisting': washingtondclisting,
            'uslisting': uslisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/US/Washington-DC/gw-medical-faculty-associates.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        'washingtondclisting': washingtondclisting,
        'uslisting': uslisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/US/Washington-DC/gw-medical-faculty-associates.html', context)
