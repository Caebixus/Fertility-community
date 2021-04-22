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

    author = GuestAuthor.objects.filter(guestauthor_id=709)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Acapulco/irega-acapulco.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=710)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/fertility-clinic-americas.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=711)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/advanced-fertility-center-fertility-center-cancun.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=712)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/new-life-mexico.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=713)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Cancun/irega-cancun.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=714)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Centro/embryogen-fertility-center-guasave.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=715)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexico-City/enlistalo-fertilidad-mexico-ciudad-de-mexico.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=716)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexico-City/citmer-medicina-reproductiva.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=717)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Culiacan-rosales/embryogen-fertility-center-culiacan.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=718)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Hermosillo/embryogen-fertility-center-hermosillo.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=719)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mazatlan/embryogen-fertility-center-mazatlan.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=720)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Mexicali/mexico-fertility-center.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=721)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nogales/embryogen-fertility-center-nogales.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=722)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nuevo-Vallarta/ivfvallarta.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=723)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Nuevo-Vallarta/surrogacymexico.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
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

    author = GuestAuthor.objects.filter(guestauthor_id=724)
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
            'mxlisting': mxlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/MX/Puebla/irega-puebla.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Puebla/irega-puebla.html', context)
