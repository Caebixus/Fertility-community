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

    thessalonikilisting = BasicClinic.objects.all()
    thessalonikilisting = thessalonikilisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=687)

    author = GuestAuthor.objects.filter(guestauthor_id=687)
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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/newlife-ivf-clinic.html', context)

    else:
        pass

    context = {
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

    thessalonikilisting = BasicClinic.objects.all()
    thessalonikilisting = thessalonikilisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=688)

    author = GuestAuthor.objects.filter(guestauthor_id=688)
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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/embryoclinic.html', context)

    else:
        pass

    context = {
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

    thessalonikilisting = BasicClinic.objects.all()
    thessalonikilisting = thessalonikilisting.filter(is_published=True)
    thessalonikilisting = thessalonikilisting.filter(clinicCity__iexact='Thessaloniki')
    thessalonikilisting = thessalonikilisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=689)

    author = GuestAuthor.objects.filter(guestauthor_id=689)
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
            'thessalonikilisting': thessalonikilisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Thessaloniki/embryolab.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=690)

    author = GuestAuthor.objects.filter(guestauthor_id=690)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/serum-ivf-center.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=691)

    author = GuestAuthor.objects.filter(guestauthor_id=691)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/ivf-athens-center.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=692)

    author = GuestAuthor.objects.filter(guestauthor_id=692)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/embryoland-ivf-center-athens.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=693)

    author = GuestAuthor.objects.filter(guestauthor_id=693)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/embio-medical-center.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=694)

    author = GuestAuthor.objects.filter(guestauthor_id=694)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/mitosis-ivf-clinic.html', context)

    else:
        pass

    context = {
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

    athenslisting = BasicClinic.objects.all()
    athenslisting = athenslisting.filter(is_published=True)
    athenslisting = athenslisting.filter(clinicCity__iexact='Athens')
    athenslisting = athenslisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=695)

    author = GuestAuthor.objects.filter(guestauthor_id=695)
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
            'athenslisting': athenslisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Athens/eugonia-assisted-reproduction-unit.html', context)

    else:
        pass

    context = {
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

    chanialisting = BasicClinic.objects.all()
    chanialisting = chanialisting.filter(is_published=True)
    chanialisting = chanialisting.filter(clinicCity__iexact='Chania')
    chanialisting = chanialisting.count()

    grlisting = BasicClinic.objects.all()
    grlisting = grlisting.filter(is_published=True)
    grlisting = grlisting.filter(clinicState__iexact='Greece')
    grlisting = grlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=696)

    author = GuestAuthor.objects.filter(guestauthor_id=696)
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
            'chanialisting': chanialisting,
            'grlisting': grlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/GR/Chania/mediterranean-fertility-institute.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chanialisting': chanialisting,
        'grlisting': grlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/GR/Chania/mediterranean-fertility-institute.html', context)
