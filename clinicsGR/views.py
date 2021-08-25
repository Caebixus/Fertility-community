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

#Thessaloniki
def newlifeivfclinic(request):
    listing = BasicClinic.objects.get(pk=687)

    allcliniclisting = BasicClinic.objects.all()

    thessalonikilisting = allcliniclisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/newlife-ivf-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'thessalonikilisting': thessalonikilisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Thessaloniki/newlife-ivf-clinic.html', context)

def embryoclinic(request):
    listing = BasicClinic.objects.get(pk=688)

    allcliniclisting = BasicClinic.objects.all()

    thessalonikilisting = allcliniclisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/embryoclinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'thessalonikilisting': thessalonikilisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Thessaloniki/embryoclinic.html', context)

def embryolab(request):
    listing = BasicClinic.objects.get(pk=689)

    allcliniclisting = BasicClinic.objects.all()

    thessalonikilisting = allcliniclisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/embryolab.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'thessalonikilisting': thessalonikilisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Thessaloniki/embryolab.html', context)


#Athens
def serumivfcenter(request):
    listing = BasicClinic.objects.get(pk=690)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/serum-ivf-center.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/serum-ivf-center.html', context)

def ivfathenscenter(request):
    listing = BasicClinic.objects.get(pk=691)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/ivf-athens-center.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/ivf-athens-center.html', context)

def embryolandivfcenterathens(request):
    listing = BasicClinic.objects.get(pk=692)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/embryoland-ivf-center-athens.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/embryoland-ivf-center-athens.html', context)

def embiomedicalcenter(request):
    listing = BasicClinic.objects.get(pk=693)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/embio-medical-center.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/embio-medical-center.html', context)

def mitosisivfclinic(request):
    listing = BasicClinic.objects.get(pk=694)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/mitosis-ivf-clinic.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/mitosis-ivf-clinic.html', context)

def eugoniaassistedreproductionunit(request):
    listing = BasicClinic.objects.get(pk=695)

    allcliniclisting = BasicClinic.objects.all()

    athenslisting = allcliniclisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/eugonia-assisted-reproduction-unit.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'athenslisting': athenslisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Athens/eugonia-assisted-reproduction-unit.html', context)

#Chania
def mediterraneanfertilityinstitute(request):
    listing = BasicClinic.objects.get(pk=696)

    allcliniclisting = BasicClinic.objects.all()

    chanialisting = allcliniclisting.filter(is_published=True)
    chanialisting = chanialisting.filter(clinicCity__iexact='Chania')
    chanialisting = chanialisting.count()

    grlisting = allcliniclisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

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
            'chanialisting': chanialisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Chania/mediterranean-fertility-institute.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chanialisting': chanialisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Chania/mediterranean-fertility-institute.html', context)
