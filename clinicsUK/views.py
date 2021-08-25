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

#ABERDEEN   --------------------------------
def aberfercen(request):
    listing = BasicClinic.objects.get(pk=506)

    allcliniclisting = BasicClinic.objects.all()

    aberdeenclisting = allcliniclisting.filter(is_published=True)
    aberdeenclisting = aberdeenclisting.filter(clinicRegion__iexact='Aberdeen')
    aberdeenclisting = aberdeenclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'aberdeenclisting': aberdeenclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Aberdeen/aberdeen-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    bathlisting = allcliniclisting.filter(is_published=True)
    bathlisting = bathlisting.filter(clinicRegion__iexact='Bath')
    bathlisting = bathlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bathlisting': bathlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bath/care-fertility-bath.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    belfastclisting = allcliniclisting.filter(is_published=True)
    belfastclisting = belfastclisting.filter(clinicRegion__iexact='Belfast')
    belfastclisting = belfastclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'belfastclisting': belfastclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Belfast/belfast-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    birminghamclisting = allcliniclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/care-fertility-birmingham.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-birmingham.html', context)

def createfertbirmin(request):
    listing = BasicClinic.objects.get(pk=510)

    allcliniclisting = BasicClinic.objects.all()

    birminghamclisting = allcliniclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/create-fertility-birmingham.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/create-fertility-birmingham.html', context)

def bmitheprioryhosp(request):
    listing = BasicClinic.objects.get(pk=511)

    allcliniclisting = BasicClinic.objects.all()

    birminghamclisting = allcliniclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/bmi-the-priory-hospital.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/bmi-the-priory-hospital.html', context)

def careferttamworth(request):
    listing = BasicClinic.objects.get(pk=512)

    allcliniclisting = BasicClinic.objects.all()

    birminghamclisting = allcliniclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/care-fertility-tamworth.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'birminghamclisting': birminghamclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-tamworth.html', context)

def stjudesfertclinic(request):
    listing = BasicClinic.objects.get(pk=513)

    allcliniclisting = BasicClinic.objects.all()

    birminghamclisting = allcliniclisting.filter(is_published=True)
    birminghamclisting = birminghamclisting.filter(clinicRegion__iexact='Birmingham')
    birminghamclisting = birminghamclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'birminghamclisting': birminghamclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Birmingham/st-judes-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    bournemouthclisting = allcliniclisting.filter(is_published=True)
    bournemouthclisting = bournemouthclisting.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclisting = bournemouthclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bournemouthclisting': bournemouthclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bournemouth/complete-fertility-centre-bournemouth.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bournemouthclisting': bournemouthclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bournemouth/complete-fertility-centre-bournemouth.html', context)

def poundburyfertdorset(request):
    listing = BasicClinic.objects.get(pk=515)

    allcliniclisting = BasicClinic.objects.all()

    bournemouthclisting = allcliniclisting.filter(is_published=True)
    bournemouthclisting = bournemouthclisting.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclisting = bournemouthclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bournemouthclisting': bournemouthclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bournemouth/poundbury-fertility-dorset.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    brightonclisting = allcliniclisting.filter(is_published=True)
    brightonclisting = brightonclisting.filter(clinicRegion__iexact='Brighton')
    brightonclisting = brightonclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'brightonclisting': brightonclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Brighton/brighton-fertility-associates.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'brightonclisting': brightonclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Brighton/brighton-fertility-associates.html', context)

def agoragynandfertcentre(request):
    listing = BasicClinic.objects.get(pk=517)

    allcliniclisting = BasicClinic.objects.all()

    brightonclisting = allcliniclisting.filter(is_published=True)
    brightonclisting = brightonclisting.filter(clinicRegion__iexact='Brighton')
    brightonclisting = brightonclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'brightonclisting': brightonclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Brighton/agora-gynaecology-and-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/abc-ivf-bristol.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/abc-ivf-bristol.html', context)

def bristolcentreforrepromedicine(request):
    listing = BasicClinic.objects.get(pk=519)

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine.html', context)

def crgwbristol(request):
    listing = BasicClinic.objects.get(pk=520)

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/crgw-bristol.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/crgw-bristol.html', context)

def createfertbristol(request):
    listing = BasicClinic.objects.get(pk=521)

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/create-fertility-bristol.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/create-fertility-bristol.html', context)

def bristolcenforrepromedspireclinic(request):
    listing = BasicClinic.objects.get(pk=522)

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine-spire-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bristolclisting': bristolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine-spire-clinic.html', context)

def londonwomensclinicbristol(request):
    listing = BasicClinic.objects.get(pk=523)

    allcliniclisting = BasicClinic.objects.all()

    bristolclisting = allcliniclisting.filter(is_published=True)
    bristolclisting = bristolclisting.filter(clinicRegion__iexact='Bristol')
    bristolclisting = bristolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'bristolclisting': bristolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Bristol/london-womens-clinic-bristol.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    cambridgeclisting = allcliniclisting.filter(is_published=True)
    cambridgeclisting = cambridgeclisting.filter(clinicRegion__iexact='Cambridge')
    cambridgeclisting = cambridgeclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'cambridgeclisting': cambridgeclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cambridge/bourn-hall-clinic-cambridge.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'cambridgeclisting': cambridgeclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cambridge/bourn-hall-clinic-cambridge.html', context)

def cambridgeivf(request):
    listing = BasicClinic.objects.get(pk=525)

    allcliniclisting = BasicClinic.objects.all()

    cambridgeclisting = allcliniclisting.filter(is_published=True)
    cambridgeclisting = cambridgeclisting.filter(clinicRegion__iexact='Cambridge')
    cambridgeclisting = cambridgeclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'cambridgeclisting': cambridgeclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cambridge/cambridge-ivf.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    cardiffclisting = allcliniclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/crgw-cardiff.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'cardiffclisting': cardiffclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cardiff/crgw-cardiff.html', context)

def londonwomenscliniccardiff(request):
    listing = BasicClinic.objects.get(pk=527)

    allcliniclisting = BasicClinic.objects.all()

    cardiffclisting = allcliniclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/london-womens-clinic-cardiff.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'cardiffclisting': cardiffclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Cardiff/london-womens-clinic-cardiff.html', context)

def walesfertilityinstitutecardiff(request):
    listing = BasicClinic.objects.get(pk=528)

    allcliniclisting = BasicClinic.objects.all()

    cardiffclisting = allcliniclisting.filter(is_published=True)
    cardiffclisting = cardiffclisting.filter(clinicRegion__iexact='Cardiff')
    cardiffclisting = cardiffclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'cardiffclisting': cardiffclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Cardiff/wales-fertility-institute-cardiff.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    colchesterclisting = allcliniclisting.filter(is_published=True)
    colchesterclisting = colchesterclisting.filter(clinicRegion__iexact='Colchester')
    colchesterclisting = colchesterclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'colchesterclisting': colchesterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Colchester/bourn-hall-clinic-colchester.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    derbyclisting = allcliniclisting.filter(is_published=True)
    derbyclisting = derbyclisting.filter(clinicRegion__iexact='Derby')
    derbyclisting = derbyclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'derbyclisting': derbyclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Derby/nurture-fertility-burton-satellite-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    exeterclisting = allcliniclisting.filter(is_published=True)
    exeterclisting = exeterclisting.filter(clinicRegion__iexact='Exeter')
    exeterclisting = exeterclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'exeterclisting': exeterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Exeter/fertility-exeter.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    glasgowclisting = allcliniclisting.filter(is_published=True)
    glasgowclisting = glasgowclisting.filter(clinicRegion__iexact='Glasgow')
    glasgowclisting = glasgowclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'glasgowclisting': glasgowclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Glasgow/gcrm-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'glasgowclisting': glasgowclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Glasgow/gcrm-fertility.html', context)

def semovoglasgow(request):
    listing = BasicClinic.objects.get(pk=533)

    allcliniclisting = BasicClinic.objects.all()

    glasgowclisting = allcliniclisting.filter(is_published=True)
    glasgowclisting = glasgowclisting.filter(clinicRegion__iexact='Glasgow')
    glasgowclisting = glasgowclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'glasgowclisting': glasgowclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Glasgow/semovo-glasgow.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    kingstonuponhillwclisting = allcliniclisting.filter(is_published=True)
    kingstonuponhillwclisting = kingstonuponhillwclisting.filter(clinicRegion__iexact='Hull')
    kingstonuponhillwclisting = kingstonuponhillwclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'kingstonuponhillwclisting': kingstonuponhillwclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Kingstonuponhull/hull-ivf-unit.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'kingstonuponhillwclisting': kingstonuponhillwclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Kingstonuponhull/hull-ivf-unit.html', context)

#CHELMSFORD   --------------------------------

def simplyfertilitychelm(request):
    listing = BasicClinic.objects.get(pk=535)

    allcliniclisting = BasicClinic.objects.all()

    chelmsfordclisting = allcliniclisting.filter(is_published=True)
    chelmsfordclisting = chelmsfordclisting.filter(clinicRegion__iexact='Chelmsford')
    chelmsfordclisting = chelmsfordclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'chelmsfordclisting': chelmsfordclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Chelmsford/simply-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Chelmsford/simply-fertility.html', context)

def bournhallclinicwockford(request):
    listing = BasicClinic.objects.get(pk=536)

    allcliniclisting = BasicClinic.objects.all()

    chelmsfordclisting = allcliniclisting.filter(is_published=True)
    chelmsfordclisting = chelmsfordclisting.filter(clinicRegion__iexact='Chelmsford')
    chelmsfordclisting = chelmsfordclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'chelmsfordclisting': chelmsfordclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Chelmsford/bourn-hall-clinic-wickford.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Chelmsford/bourn-hall-clinic-wickford.html', context)

#LEEDS   --------------------------------

def leedsfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=538)

    allcliniclisting = BasicClinic.objects.all()

    leedsclisting = allcliniclisting.filter(is_published=True)
    leedsclisting = leedsclisting.filter(clinicRegion__iexact='Leeds')
    leedsclisting = leedsclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'leedsclisting': leedsclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leeds/leeds-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'leedsclisting': leedsclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Leeds/leeds-fertility-clinic.html', context)

def semovoleeds(request):
    listing = BasicClinic.objects.get(pk=539)

    allcliniclisting = BasicClinic.objects.all()

    leedsclisting = allcliniclisting.filter(is_published=True)
    leedsclisting = leedsclisting.filter(clinicRegion__iexact='Leeds')
    leedsclisting = leedsclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'leedsclisting': leedsclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leeds/semovo-leeds.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    leicesterclisting = allcliniclisting.filter(is_published=True)
    leicesterclisting = leicesterclisting.filter(clinicRegion__iexact='Leicester')
    leicesterclisting = leicesterclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'leicesterclisting': leicesterclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Leicester/xy-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'leicesterclisting': leicesterclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Leicester/xy-fertility.html', context)

#LIVERPOOL   --------------------------------

def carefertilitychester(request):
    listing = BasicClinic.objects.get(pk=537)

    allcliniclisting = BasicClinic.objects.all()

    liverpoolclisting = allcliniclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/care-fertility-chester.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chelmsfordclisting': chelmsfordclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/care-fertility-chester.html', context)


def carefertilityliverpool(request):
    listing = BasicClinic.objects.get(pk=541)

    allcliniclisting = BasicClinic.objects.all()

    liverpoolclisting = allcliniclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/care-fertility-liverpool.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/care-fertility-liverpool.html', context)

def thehewittfertilitycentreliverpool(request):
    listing = BasicClinic.objects.get(pk=542)

    allcliniclisting = BasicClinic.objects.all()

    liverpoolclisting = allcliniclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/the-hewitt-fertility-centre-liverpool.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/the-hewitt-fertility-centre-liverpool.html', context)

def semovoliverpool(request):
    listing = BasicClinic.objects.get(pk=543)

    allcliniclisting = BasicClinic.objects.all()

    liverpoolclisting = allcliniclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/semovo-liverpool.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'liverpoolclisting': liverpoolclisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Liverpool/semovo-liverpool.html', context)

def centreforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=544)

    allcliniclisting = BasicClinic.objects.all()

    liverpoolclisting = allcliniclisting.filter(is_published=True)
    liverpoolclisting = liverpoolclisting.filter(clinicRegion__iexact='Liverpool')
    liverpoolclisting = liverpoolclisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'liverpoolclisting': liverpoolclisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Liverpool/centre-for-reproductive-health.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-brentwood.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-brentwood.html', context)

def londonwomensclinicharrow(request):
    listing = BasicClinic.objects.get(pk=546)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-harrow.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harrow.html', context)

def abcivfharleystreet(request):
    listing = BasicClinic.objects.get(pk=547)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/abc-ivf-harley-street.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/abc-ivf-harley-street.html', context)

def abcivfwimbledon(request):
    listing = BasicClinic.objects.get(pk=548)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/abc-ivf-wimbledon.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/abc-ivf-wimbledon.html', context)

def assistedreproandgynaecologycentre(request):
    listing = BasicClinic.objects.get(pk=549)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/assisted-reproduction-and-gynaecology-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/assisted-reproduction-and-gynaecology-centre.html', context)

def cityfertility(request):
    listing = BasicClinic.objects.get(pk=550)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/city-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/city-fertility.html', context)

def createfertistpauls(request):
    listing = BasicClinic.objects.get(pk=551)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-st-pauls.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/create-fertility-st-pauls.html', context)

def fertilityplusfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=552)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/fertility-plus-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/fertility-plus-fertility-clinic.html', context)

def londonwomensclinicharleystreet(request):
    listing = BasicClinic.objects.get(pk=553)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-harley-street.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harley-street.html', context)

def poundburyfertilitylondon(request):
    listing = BasicClinic.objects.get(pk=554)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/poundbury-fertility-london.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/poundbury-fertility-london.html', context)

def semovolondon(request):
    listing = BasicClinic.objects.get(pk=555)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/semovo-london.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/semovo-london.html', context)

def londonwomenscliniclondonbridge(request):
    listing = BasicClinic.objects.get(pk=556)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/london-womens-clinic-london-bridge.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-london-bridge.html', context)

def thamesvalleyfertility(request):
    listing = BasicClinic.objects.get(pk=557)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/thames-valley-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/thames-valley-fertility.html', context)

def ivflondonelstree(request):
    listing = BasicClinic.objects.get(pk=558)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/ivf-london-elstree.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/ivf-london-elstree.html', context)

def hertsandessexfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=559)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/herts-and-essex-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/herts-and-essex-fertility-centre.html', context)

def bostonplace(request):
    listing = BasicClinic.objects.get(pk=560)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/boston-place.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/boston-place.html', context)

def carefertilitylondon(request):
    listing = BasicClinic.objects.get(pk=561)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/care-fertility-london.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/care-fertility-london.html', context)

def conceptfertility(request):
    listing = BasicClinic.objects.get(pk=562)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/concept-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/concept-fertility.html', context)

def createfertilitywimbledon(request):
    listing = BasicClinic.objects.get(pk=563)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-wimbledon.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/create-fertility-wimbledon.html', context)

def evewell(request):
    listing = BasicClinic.objects.get(pk=564)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/evewell.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/evewell.html', context)

def thefertilitygynaecologyacademy(request):
    listing = BasicClinic.objects.get(pk=565)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/the-fertility-gynaecology-academy.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/the-fertility-gynaecology-academy.html', context)

def harleystreetfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=566)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/harley-street-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/harley-street-fertility-clinic.html', context)

def homertonfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=567)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/homerton-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/homerton-fertility-centre.html', context)

def ivilondon(request):
    listing = BasicClinic.objects.get(pk=568)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/ivi-london.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/ivi-london.html', context)

def kingsfertility(request):
    listing = BasicClinic.objects.get(pk=569)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/kings-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/kings-fertility.html', context)

def listerfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=570)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/lister-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'londonlisting': londonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/London/lister-fertility-clinic.html', context)

def createfertilityhertfordshire(request):
    listing = BasicClinic.objects.get(pk=571)

    allcliniclisting = BasicClinic.objects.all()

    londonlisting = allcliniclisting.filter(is_published=True)
    londonlisting = londonlisting.filter(clinicRegion__iexact='London')
    londonlisting = londonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'londonlisting': londonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/London/create-fertility-hertfordshire.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/manchester-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/manchester-fertility.html', context)

def semovomanchestersouth(request):
    listing = BasicClinic.objects.get(pk=573)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/semovo-manchester-south.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-south.html', context)

def thehewittfertilitycentreknutsford(request):
    listing = BasicClinic.objects.get(pk=574)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/the-hewitt-fertility-centre-knutsford.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/the-hewitt-fertility-centre-knutsford.html', context)

def aurorareprohealthaltrincham(request):
    listing = BasicClinic.objects.get(pk=575)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/aurora-reproductive-healthcare-altrincham.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/aurora-reproductive-healthcare-altrincham.html', context)

def abcivfmanchester(request):
    listing = BasicClinic.objects.get(pk=576)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/abc-ivf-manchester.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/abc-ivf-manchester.html', context)

def createfertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=577)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/create-fertility-manchester.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/create-fertility-manchester.html', context)

def semovomanchestercitycentre(request):
    listing = BasicClinic.objects.get(pk=578)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/semovo-manchester-city-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-city-centre.html', context)

def fertilityfusion(request):
    listing = BasicClinic.objects.get(pk=579)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/fertility-fusion.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'manchesterlisting': manchesterlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Manchester/fertility-fusion.html', context)

def carefertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=580)

    allcliniclisting = BasicClinic.objects.all()

    manchesterlisting = allcliniclisting.filter(is_published=True)
    manchesterlisting = manchesterlisting.filter(clinicRegion__iexact='Manchester')
    manchesterlisting = manchesterlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'manchesterlisting': manchesterlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Manchester/care-fertility-manchester.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    middlesbroughlisting = allcliniclisting.filter(is_published=True)
    middlesbroughlisting = middlesbroughlisting.filter(clinicRegion__iexact='Middlesbrough')
    middlesbroughlisting = middlesbroughlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'middlesbroughlisting': middlesbroughlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Middlesbrough/london-womens-clinic-darlington.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    newcastlelisting = allcliniclisting.filter(is_published=True)
    newcastlelisting = newcastlelisting.filter(clinicRegion__iexact='Newcastle')
    newcastlelisting = newcastlelisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'newcastlelisting': newcastlelisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Newcastle/newcastle-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    norwichlisting = allcliniclisting.filter(is_published=True)
    norwichlisting = norwichlisting.filter(clinicRegion__iexact='Norwich')
    norwichlisting = norwichlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'norwichlisting': norwichlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Norwich/bourn-hall-clinic-norwich.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    nottinghamlisting = allcliniclisting.filter(is_published=True)
    nottinghamlisting = nottinghamlisting.filter(clinicRegion__iexact='Nottingham')
    nottinghamlisting = nottinghamlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'nottinghamlisting': nottinghamlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Nottingham/nurture-fertility-nottingham.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nottinghamlisting': nottinghamlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Nottingham/nurture-fertility-nottingham.html', context)

def carefertilitynottingham(request):
    listing = BasicClinic.objects.get(pk=585)

    allcliniclisting = BasicClinic.objects.all()

    nottinghamlisting = allcliniclisting.filter(is_published=True)
    nottinghamlisting = nottinghamlisting.filter(clinicRegion__iexact='Nottingham')
    nottinghamlisting = nottinghamlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'nottinghamlisting': nottinghamlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Nottingham/care-fertility-nottingham.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    oxfordlisting = allcliniclisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/create-fertility-oxford.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'oxfordlisting': oxfordlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Oxford/create-fertility-oxford.html', context)

def oxfordfertility(request):
    listing = BasicClinic.objects.get(pk=587)

    allcliniclisting = BasicClinic.objects.all()

    oxfordlisting = allcliniclisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/oxford-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'oxfordlisting': oxfordlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Oxford/oxford-fertility.html', context)

def abcivfoxford(request):
    listing = BasicClinic.objects.get(pk=588)

    allcliniclisting = BasicClinic.objects.all()

    oxfordlisting = allcliniclisting.filter(is_published=True)
    oxfordlisting = oxfordlisting.filter(clinicRegion__iexact='Oxford')
    oxfordlisting = oxfordlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'oxfordlisting': oxfordlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Oxford/abc-ivf-oxford.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    peterboroughlisting = allcliniclisting.filter(is_published=True)
    peterboroughlisting = peterboroughlisting.filter(clinicRegion__iexact='Peterborough')
    peterboroughlisting = peterboroughlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'peterboroughlisting': peterboroughlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Peterborough/bourn-hall-clinic-peterborough.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    plymouthlisting = allcliniclisting.filter(is_published=True)
    plymouthlisting = plymouthlisting.filter(clinicRegion__iexact='Plymouth')
    plymouthlisting = plymouthlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'plymouthlisting': plymouthlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Plymouth/crgw-plymouth.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    portsmouthlisting = allcliniclisting.filter(is_published=True)
    portsmouthlisting = portsmouthlisting.filter(clinicRegion__iexact='Portsmouth')
    portsmouthlisting = portsmouthlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'portsmouthlisting': portsmouthlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Portsmouth/complete-fertility-centre-portsmouth.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    salisburylisting = allcliniclisting.filter(is_published=True)
    salisburylisting = salisburylisting.filter(clinicRegion__iexact='Salisbury')
    salisburylisting = salisburylisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'salisburylisting': salisburylisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Salisbury/salisbury-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    sheffieldlisting = allcliniclisting.filter(is_published=True)
    sheffieldlisting = sheffieldlisting.filter(clinicRegion__iexact='Sheffield')
    sheffieldlisting = sheffieldlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'sheffieldlisting': sheffieldlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Sheffield/nurture-fertility-chesterfield.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'sheffieldlisting': sheffieldlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Sheffield/nurture-fertility-chesterfield.html', context)

def carefertilitysheffield(request):
    listing = BasicClinic.objects.get(pk=594)

    allcliniclisting = BasicClinic.objects.all()

    sheffieldlisting = allcliniclisting.filter(is_published=True)
    sheffieldlisting = sheffieldlisting.filter(clinicRegion__iexact='Sheffield')
    sheffieldlisting = sheffieldlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'sheffieldlisting': sheffieldlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Sheffield/care-fertility-sheffield.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    southamptonlisting = allcliniclisting.filter(is_published=True)
    southamptonlisting = southamptonlisting.filter(clinicRegion__iexact='Southampton')
    southamptonlisting = southamptonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'southamptonlisting': southamptonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Southampton/complete-fertility-centre-southampton.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'southamptonlisting': southamptonlisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Southampton/complete-fertility-centre-southampton.html', context)

def wessexfertility(request):
    listing = BasicClinic.objects.get(pk=596)

    allcliniclisting = BasicClinic.objects.all()

    southamptonlisting = allcliniclisting.filter(is_published=True)
    southamptonlisting = southamptonlisting.filter(clinicRegion__iexact='Southampton')
    southamptonlisting = southamptonlisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'southamptonlisting': southamptonlisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Southampton/wessex-fertility.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
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

    allcliniclisting = BasicClinic.objects.all()

    swansealisting = allcliniclisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/wales-fertility-institute-neath.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/wales-fertility-institute-neath.html', context)

def crgwswansea(request):
    listing = BasicClinic.objects.get(pk=598)

    allcliniclisting = BasicClinic.objects.all()

    swansealisting = allcliniclisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/crgw-swansea.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/crgw-swansea.html', context)

def londonwomensclinicswansea(request):
    listing = BasicClinic.objects.get(pk=599)

    allcliniclisting = BasicClinic.objects.all()

    swansealisting = allcliniclisting.filter(is_published=True)
    swansealisting = swansealisting.filter(clinicRegion__iexact='Swansea')
    swansealisting = swansealisting.count()

    uklisting = allcliniclisting.filter(is_published=True)
    uklisting = uklisting.filter(clinicState__iexact='United Kingdom')
    uklisting = uklisting.count()

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
            'swansealisting': swansealisting,
            'uklisting': uklisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/UK/Swansea/london-womens-clinic-swansea.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'swansealisting': swansealisting,
        'uklisting': uklisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/UK/Swansea/london-womens-clinic-swansea.html', context)
