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

#Acapulco
def iregaacapulco(request):
    listing = BasicClinic.objects.get(pk=709)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/fertility-clinic-americas.html', context)

def advancedfertilitycenterfertilitycentercancun(request):
    listing = BasicClinic.objects.get(pk=711)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/advanced-fertility-center-fertility-center-cancun.html', context)

def newlifemexico(request):
    listing = BasicClinic.objects.get(pk=712)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Cancun/new-life-mexico.html', context)

def iregacancun(request):
    listing = BasicClinic.objects.get(pk=713)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Mexico-City/enlistalo-fertilidad-mexico-ciudad-de-mexico.html', context)

def citmermedicinareproductiva(request):
    listing = BasicClinic.objects.get(pk=716)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Nuevo-Vallarta/ivfvallarta.html', context)

def surrogacymexico(request):
    listing = BasicClinic.objects.get(pk=723)

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
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

    allcliniclisting = BasicClinic.objects.all()

    mxlisting = allcliniclisting.filter(is_published=True)
    mxlisting = mxlisting.filter(clinicState__iexact='Mexico')
    mxlisting = mxlisting.count()

    alllisting = allcliniclisting.filter(is_published=True)
    alllisting = alllisting.count()

    pkid = listing.id

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=pkid)

    author = GuestAuthor.objects.filter(guestauthor_id=pkid)
    guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)

    user_owner = User.objects.filter(basicclinic__pk=listing.pk)
    if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
        user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True).count()
        user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=pkid).filter(is_claimed=True, is_published=True)
    else:
        user_objects_count = 0
        user_objects = None

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'user_objects_count': user_objects_count,
            'user_objects': user_objects,
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
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'mxlisting': mxlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/MX/Puebla/irega-puebla.html', context)
