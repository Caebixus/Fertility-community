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

# PRAGUE
def pragamedica(request):
    listing = BasicClinic.objects.get(pk=36)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pragamedica.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pragamedica.html', context)

def fertilityportx(request):
    listing = BasicClinic.objects.get(pk=600)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/fertilityport-prague.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/fertilityport-prague.html', context)

def praguefertilitycentre(request):
    listing = BasicClinic.objects.get(pk=601)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/prague-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/prague-fertility-centre.html', context)

def gynemfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=602)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/gynem-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/gynem-fertility-clinic.html', context)

def gennet(request):
    listing = BasicClinic.objects.get(pk=604)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/gennet.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/gennet.html', context)

def medicaltravelczechrep(request):
    listing = BasicClinic.objects.get(pk=605)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/medical-travel-czech-republic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/medical-travel-czech-republic.html', context)

def pronatalplusprague(request):
    listing = BasicClinic.objects.get(pk=606)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pronatal-plus-prague6.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-plus-prague6.html', context)

def pronatalsanatoriumprague(request):
    listing = BasicClinic.objects.get(pk=607)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/pronatal-sanatorium-prague4.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/pronatal-sanatorium-prague4.html', context)

def ivfcube(request):
    listing = BasicClinic.objects.get(pk=612)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/ivf-cube.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/ivf-cube.html', context)

def medistella(request):
    listing = BasicClinic.objects.get(pk=705)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/medistella.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/medistella.html', context)

def europeivfprague(request):
    listing = BasicClinic.objects.get(pk=728)

    allcliniclisting = BasicClinic.objects.all()

    pragueclisting = allcliniclisting.filter(is_published=True)
    pragueclisting = pragueclisting.filter(clinicRegion__iexact='Prague')
    pragueclisting = pragueclisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'pragueclisting': pragueclisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Prague/europe-ivf-prague.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'pragueclisting': pragueclisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Prague/europe-ivf-prague.html', context)

# BRNO
def ivfzlinczechrep(request):
    listing = BasicClinic.objects.get(pk=603)

    allcliniclisting = BasicClinic.objects.all()

    brnolisting = allcliniclisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/ivf-zlin-czech-republic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'brnolisting': brnolisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Brno/ivf-zlin-czech-republic.html', context)

def reprofitbrno(request):
    listing = BasicClinic.objects.get(pk=613)

    allcliniclisting = BasicClinic.objects.all()

    brnolisting = allcliniclisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/reprofit-brno.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'brnolisting': brnolisting,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Brno/reprofit-brno.html', context)

def reprogenesis(request):
    listing = BasicClinic.objects.get(pk=615)

    allcliniclisting = BasicClinic.objects.all()

    brnolisting = allcliniclisting.filter(is_published=True)
    brnolisting = brnolisting.filter(clinicRegion__iexact='Brno')
    brnolisting = brnolisting.count()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'brnolisting': brnolisting,
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Brno/reprogenesis.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Kolin/pronatal-kolin.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Kolin/pronatal-kolin.html', context)

# ČESKÉ BUDĚJOVICE
def pronatalreproceskebudejovice(request):
    listing = BasicClinic.objects.get(pk=609)

    allcliniclisting = BasicClinic.objects.all()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Ceske-budejovice/pronatal-repro-ceske-budejovice.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Ceske-budejovice/pronatal-repro-ceske-budejovice.html', context)

# TEPLICE
def pronatalnordteplice(request):
    listing = BasicClinic.objects.get(pk=610)

    allcliniclisting = BasicClinic.objects.all()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Teplice/pronatal-nord-teplice.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Teplice/pronatal-nord-teplice.html', context)

# KARLOVY VARY
def pronatalspakarlovyvary(request):
    listing = BasicClinic.objects.get(pk=611)

    allcliniclisting = BasicClinic.objects.all()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Karlovy-vary/pronatal-spa-karlovy-vary.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Karlovy-vary/pronatal-spa-karlovy-vary.html', context)

# OSTRAVA
def reprofitostrava(request):
    listing = BasicClinic.objects.get(pk=614)

    allcliniclisting = BasicClinic.objects.all()

    czlisting = allcliniclisting.filter(is_published=True)
    czlisting = czlisting.filter(clinicState__iexact='Czech Republic')
    czlisting = czlisting.count()

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
        pass

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
            'czlisting': czlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CZ/Ostrava/reprofit-ostrava.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'czlisting': czlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CZ/Ostrava/reprofit-ostrava.html', context)
