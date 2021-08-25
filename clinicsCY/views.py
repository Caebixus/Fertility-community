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

#Nicosia
def cyprusivfcentre(request):
    listing = BasicClinic.objects.get(pk=697)

    allcliniclisting = BasicClinic.objects.all()

    nicosialisting = allcliniclisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/cyprus-ivf-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nicosialisting': nicosialisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Nicosia/cyprus-ivf-centre.html', context)

def britishcyprusivfhospital(request):
    listing = BasicClinic.objects.get(pk=698)

    allcliniclisting = BasicClinic.objects.all()

    nicosialisting = allcliniclisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/british-cyprus-ivf-hospital.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nicosialisting': nicosialisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Nicosia/british-cyprus-ivf-hospital.html', context)

def eurocareivf(request):
    listing = BasicClinic.objects.get(pk=699)

    allcliniclisting = BasicClinic.objects.all()

    nicosialisting = allcliniclisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/eurocareivf.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nicosialisting': nicosialisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Nicosia/eurocareivf.html', context)

def dogusfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=700)

    allcliniclisting = BasicClinic.objects.all()

    nicosialisting = allcliniclisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/dogus-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nicosialisting': nicosialisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Nicosia/dogus-fertility-clinic.html', context)

def pedieosivfcenter(request):
    listing = BasicClinic.objects.get(pk=701)

    allcliniclisting = BasicClinic.objects.all()

    nicosialisting = allcliniclisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/pedieos-ivf-center.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'nicosialisting': nicosialisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Nicosia/pedieos-ivf-center.html', context)

#Famagusta
def crownivfcyprus(request):
    listing = BasicClinic.objects.get(pk=702)

    allcliniclisting = BasicClinic.objects.all()

    famagustalisting = allcliniclisting.filter(is_published=True)
    famagustalisting = famagustalisting.filter(clinicCity__iexact='Famagusta')
    famagustalisting = famagustalisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'famagustalisting': famagustalisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Famagusta/crown-ivf-cyprus.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'famagustalisting': famagustalisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Famagusta/crown-ivf-cyprus.html', context)

#Girne
def dunyaivfcyprusfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=703)

    allcliniclisting = BasicClinic.objects.all()

    girnelisting = allcliniclisting.filter(is_published=True)
    girnelisting = girnelisting.filter(clinicCity__iexact='Girne')
    girnelisting = girnelisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'girnelisting': girnelisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Girne/dunya-ivf-cyprus-fertility-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'girnelisting': girnelisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Girne/dunya-ivf-cyprus-fertility-clinic.html', context)

def kyreniaivfcenter(request):
    listing = BasicClinic.objects.get(pk=704)

    allcliniclisting = BasicClinic.objects.all()

    girnelisting = allcliniclisting.filter(is_published=True)
    girnelisting = girnelisting.filter(clinicCity__iexact='Girne')
    girnelisting = girnelisting.count()

    cylisting = allcliniclisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

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
            'girnelisting': girnelisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Girne/kyrenia-ivf-center.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'girnelisting': girnelisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Girne/kyrenia-ivf-center.html', context)
