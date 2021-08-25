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

#ALICANTE   --------------------------------
def ivfspainalicante(request):
    listing = BasicClinic.objects.get(pk=617)

    allcliniclisting = BasicClinic.objects.all()

    alicantelisting = allcliniclisting.filter(is_published=True)
    alicantelisting = alicantelisting.filter(clinicRegion__iexact='Alicante')
    alicantelisting = alicantelisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'alicantelisting': alicantelisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Alicante/ivf-spain-alicante.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'alicantelisting': alicantelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Alicante/ivf-spain-alicante.html', context)

def ivialicante(request):
    listing = BasicClinic.objects.get(pk=619)

    allcliniclisting = BasicClinic.objects.all()

    alicantelisting = allcliniclisting.filter(is_published=True)
    alicantelisting = alicantelisting.filter(clinicRegion__iexact='Alicante')
    alicantelisting = alicantelisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'alicantelisting': alicantelisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Alicante/ivi-alicante.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'alicantelisting': alicantelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Alicante/ivi-alicante.html', context)

#BARCELONA   --------------------------------
def clinicadefertilidadbarcelonaivf(request):
    listing = BasicClinic.objects.get(pk=620)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/clinica-de-fertilidad-barcelona-ivf.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/clinica-de-fertilidad-barcelona-ivf.html', context)

def ferttyinternational(request):
    listing = BasicClinic.objects.get(pk=621)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/fertty-international.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fertty-international.html', context)

def fertilabbarcelona(request):
    listing = BasicClinic.objects.get(pk=622)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/fertilab-barcelona.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fertilab-barcelona.html', context)

def institutmarquesbarcelona(request):
    listing = BasicClinic.objects.get(pk=623)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/institut-marques-barcelona.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/institut-marques-barcelona.html', context)

def ivfforyou(request):
    listing = BasicClinic.objects.get(pk=624)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/ivf-for-you.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/ivf-for-you.html', context)

def gravida(request):
    listing = BasicClinic.objects.get(pk=625)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/gravida.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/gravida.html', context)

def ivibarcelona(request):
    listing = BasicClinic.objects.get(pk=626)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/ivi-barcelona.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/ivi-barcelona.html', context)

def fivmarbellabarcelona(request):
    listing = BasicClinic.objects.get(pk=627)

    allcliniclisting = BasicClinic.objects.all()

    barcelonalisting = allcliniclisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'barcelonalisting': barcelonalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Barcelona/fiv-marbella-barcelona.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fiv-marbella-barcelona.html', context)

#MADRID   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivfspainmadrid(request):
    listing = BasicClinic.objects.get(pk=628)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/ivf-spain-madrid.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/ivf-spain-madrid.html', context)

def fertilitymadrid(request):
    listing = BasicClinic.objects.get(pk=629)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/fertility-madrid.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fertility-madrid.html', context)

def evafertilityclinicmadrid(request):
    listing = BasicClinic.objects.get(pk=630)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/eva-fertility-clinic-madrid.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/eva-fertility-clinic-madrid.html', context)

def ivimadridaravaca(request):
    listing = BasicClinic.objects.get(pk=631)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/ivi-madrid-aravaca.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/ivi-madrid-aravaca.html', context)

def clinicatambre(request):
    listing = BasicClinic.objects.get(pk=632)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/clinica-tambre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/clinica-tambre.html', context)

def fertilityclinichru(request):
    listing = BasicClinic.objects.get(pk=633)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/fertility-clinic-hru.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fertility-clinic-hru.html', context)

def fivmarbellamadrid(request):
    listing = BasicClinic.objects.get(pk=634)

    allcliniclisting = BasicClinic.objects.all()

    madridlisting = allcliniclisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'madridlisting': madridlisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Madrid/fiv-marbella-madrid.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fiv-marbella-madrid.html', context)

#MALAGA   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivimalaga(request):
    listing = BasicClinic.objects.get(pk=635)

    allcliniclisting = BasicClinic.objects.all()

    malagalisting = allcliniclisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'malagalisting': malagalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Malaga/ivi-malaga.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/ivi-malaga.html', context)

def fivmarbellamalaga(request):
    listing = BasicClinic.objects.get(pk=636)

    allcliniclisting = BasicClinic.objects.all()

    malagalisting = allcliniclisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'malagalisting': malagalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Malaga/fiv-marbella-malaga.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/fiv-marbella-malaga.html', context)

def hcfertility(request):
    listing = BasicClinic.objects.get(pk=637)

    allcliniclisting = BasicClinic.objects.all()

    malagalisting = allcliniclisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'malagalisting': malagalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Malaga/hc-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/hc-fertility.html', context)

def clinicafertia(request):
    listing = BasicClinic.objects.get(pk=638)

    allcliniclisting = BasicClinic.objects.all()

    malagalisting = allcliniclisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'malagalisting': malagalisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Malaga/clinica-fertia.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/clinica-fertia.html', context)

#SEVILLE   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivisevilla(request):
    listing = BasicClinic.objects.get(pk=639)

    allcliniclisting = BasicClinic.objects.all()

    sevillelisting = allcliniclisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'sevillelisting': sevillelisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Seville/ivi-sevilla.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/ivi-sevilla.html', context)

def inebir(request):
    listing = BasicClinic.objects.get(pk=640)

    allcliniclisting = BasicClinic.objects.all()

    sevillelisting = allcliniclisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'sevillelisting': sevillelisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Seville/inebir.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/inebir.html', context)

def ginemedsevilla(request):
    listing = BasicClinic.objects.get(pk=641)

    allcliniclisting = BasicClinic.objects.all()

    sevillelisting = allcliniclisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'sevillelisting': sevillelisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Seville/ginemed-sevilla.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/ginemed-sevilla.html', context)

#VALENCIA   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ivivalencia(request):
    listing = BasicClinic.objects.get(pk=642)

    allcliniclisting = BasicClinic.objects.all()

    valencialisting = allcliniclisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'valencialisting': valencialisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Valencia/ivi-valencia.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/ivi-valencia.html', context)

def equipojuanacrespo(request):
    listing = BasicClinic.objects.get(pk=643)

    allcliniclisting = BasicClinic.objects.all()

    valencialisting = allcliniclisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'valencialisting': valencialisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Valencia/equipo-juana-crespo.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/equipo-juana-crespo.html', context)

def unidaddereproduccionasistidaimedvalencia(request):
    listing = BasicClinic.objects.get(pk=644)

    allcliniclisting = BasicClinic.objects.all()

    valencialisting = allcliniclisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'valencialisting': valencialisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Valencia/unidad-de-reproduccion-asistida-imed-valencia.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/unidad-de-reproduccion-asistida-imed-valencia.html', context)

def creavalencia(request):
    listing = BasicClinic.objects.get(pk=645)

    allcliniclisting = BasicClinic.objects.all()

    valencialisting = allcliniclisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'valencialisting': valencialisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Valencia/crea-valencia.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/crea-valencia.html', context)

def imerinstitutodemedicinareproductiva(request):
    listing = BasicClinic.objects.get(pk=646)

    allcliniclisting = BasicClinic.objects.all()

    valencialisting = allcliniclisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = allcliniclisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

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
            'valencialisting': valencialisting,
            'splisting': splisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/SP/Valencia/imer-instituto-de-medicina-reproductiva.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/imer-instituto-de-medicina-reproductiva.html', context)
