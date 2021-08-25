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

#Bengalore
def kiraninfertilitycenterbengaluru(request):
    listing = BasicClinic.objects.get(pk=655)

    allcliniclisting = BasicClinic.objects.all()

    bengaloralisting = allcliniclisting.filter(is_published=True)
    bengaloralisting = bengaloralisting.filter(clinicCity__iexact='Bangalore')
    bengaloralisting = bengaloralisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'bengaloralisting': bengaloralisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Bangalore/kiran-infertility-center-bangalore.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bengaloralisting': bengaloralisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Bangalore/kiran-infertility-center-bangalore.html', context)

def mannatfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=656)

    allcliniclisting = BasicClinic.objects.all()

    bengaloralisting = allcliniclisting.filter(is_published=True)
    bengaloralisting = bengaloralisting.filter(clinicCity__iexact='Bengalore')
    bengaloralisting = bengaloralisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'bengaloralisting': bengaloralisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Bangalore/mannat-fertility-centre.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'bengaloralisting': bengaloralisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Bangalore/mannat-fertility-centre.html', context)

#Gachibowli
def hyderabadwomenfertilitycentregachibowli(request):
    listing = BasicClinic.objects.get(pk=657)

    allcliniclisting = BasicClinic.objects.all()

    gachibowlisting = allcliniclisting.filter(is_published=True)
    gachibowlisting = gachibowlisting.filter(clinicCity__iexact='Gachibowli')
    gachibowlisting = gachibowlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'gachibowlisting': gachibowlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Gachibowli/hyderabad-women-fertility-centre-gachibowli.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'gachibowlisting': gachibowlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Gachibowli/hyderabad-women-fertility-centre-gachibowli.html', context)

#Gurugram
def indiaivfclinicgurgaon(request):
    listing = BasicClinic.objects.get(pk=658)

    allcliniclisting = BasicClinic.objects.all()

    gurugramlisting = allcliniclisting.filter(is_published=True)
    gurugramlisting = gurugramlisting.filter(clinicCity__iexact='Gurugram')
    gurugramlisting = gurugramlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'gurugramlisting': gurugramlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Gurugram/india-ivf-clinic-gurgaon.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'gurugramlisting': gurugramlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Gurugram/india-ivf-clinic-gurgaon.html', context)

#Gwalior
def indiaivfclinicgwalior(request):
    listing = BasicClinic.objects.get(pk=659)

    allcliniclisting = BasicClinic.objects.all()

    gwaliorlisting = allcliniclisting.filter(is_published=True)
    gwaliorlisting = gwaliorlisting.filter(clinicCity__iexact='Gwalior')
    gwaliorlisting = gwaliorlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'gwaliorlisting': gwaliorlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Gwalior/india-ivf-clinic-gwalior.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'gwaliorlisting': gwaliorlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Gwalior/india-ivf-clinic-gwalior.html', context)

#Haldwani
def indiaivfclinichaldwani(request):
    listing = BasicClinic.objects.get(pk=660)

    allcliniclisting = BasicClinic.objects.all()

    haldwanilisting = allcliniclisting.filter(is_published=True)
    haldwanilisting = haldwanilisting.filter(clinicCity__iexact='Haldwani')
    haldwanilisting = haldwanilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'haldwanilisting': haldwanilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Haldwani/india-ivf-clinic-haldwani.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'haldwanilisting': haldwanilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Haldwani/india-ivf-clinic-haldwani.html', context)


#Hyderabad
def oasisfertilityhyderabadbanjarahills(request):
    listing = BasicClinic.objects.get(pk=661)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-banjara-hills.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-banjara-hills.html', context)

def oasisfertilityhyderabadsecunderabad(request):
    listing = BasicClinic.objects.get(pk=662)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-secunderabad.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-secunderabad.html', context)

def oasisfertilityhyderabaddilsukhnagar(request):
    listing = BasicClinic.objects.get(pk=663)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-dilsukhnagar.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-dilsukhnagar.html', context)

def oasisfertilityhyderabadgachibowli(request):
    listing = BasicClinic.objects.get(pk=664)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-gachibowli.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-gachibowli.html', context)

def oasisfertilityhyderabmiyapur(request):
    listing = BasicClinic.objects.get(pk=665)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-miyapur.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-miyapur.html', context)

def kiraninfertilitycenterhyderabad(request):
    listing = BasicClinic.objects.get(pk=666)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-hyderabad.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-hyderabad.html', context)

def kiraninfertilitycenterkothapet(request):
    listing = BasicClinic.objects.get(pk=667)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-kothapet.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-kothapet.html', context)

def hegdefertilitymalakpet(request):
    listing = BasicClinic.objects.get(pk=668)

    allcliniclisting = BasicClinic.objects.all()

    hyderabadlisting = allcliniclisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'hyderabadlisting': hyderabadlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Hyderabad/hegde-fertility-malakpet.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/hegde-fertility-malakpet.html', context)

#Chennai
def oasisfertchennai(request):
    listing = BasicClinic.objects.get(pk=669)

    allcliniclisting = BasicClinic.objects.all()

    chennailisting = allcliniclisting.filter(is_published=True)
    chennailisting = chennailisting.filter(clinicCity__iexact='Chennai')
    chennailisting = chennailisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'chennailisting': chennailisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Chennai/oasis-fertility-chennai.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chennailisting': chennailisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Chennai/oasis-fertility-chennai.html', context)

def kiraninfertilitycenterchennai(request):
    listing = BasicClinic.objects.get(pk=670)

    allcliniclisting = BasicClinic.objects.all()

    chennailisting = allcliniclisting.filter(is_published=True)
    chennailisting = chennailisting.filter(clinicCity__iexact='Chennai')
    chennailisting = chennailisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'chennailisting': chennailisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Chennai/kiran-infertility-center-chennai.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'chennailisting': chennailisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Chennai/kiran-infertility-center-chennai.html', context)

#Jammu
def indiaivfclinicjammu(request):
    listing = BasicClinic.objects.get(pk=671)

    allcliniclisting = BasicClinic.objects.all()

    jammulisting = allcliniclisting.filter(is_published=True)
    jammulisting = jammulisting.filter(clinicCity__iexact='Jammu')
    jammulisting = jammulisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'jammulisting': jammulisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Jammu/india-ivf-clinic-jammu.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'jammulisting': jammulisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Jammu/india-ivf-clinic-jammu.html', context)

#Madhapur
def hegdehospitalmadhapur(request):
    listing = BasicClinic.objects.get(pk=672)

    allcliniclisting = BasicClinic.objects.all()

    madhapurlisting = allcliniclisting.filter(is_published=True)
    madhapurlisting = madhapurlisting.filter(clinicCity__iexact='Madhapur')
    madhapurlisting = madhapurlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'madhapurlisting': madhapurlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Madhapur/hegde-hospital-madhapur.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'madhapurlisting': madhapurlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Madhapur/hegde-hospital-madhapur.html', context)

#Meerut
def indiaivfclinicmeerut(request):
    listing = BasicClinic.objects.get(pk=673)

    allcliniclisting = BasicClinic.objects.all()

    meerutlisting = allcliniclisting.filter(is_published=True)
    meerutlisting = meerutlisting.filter(clinicCity__iexact='Meerut')
    meerutlisting = meerutlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'meerutlisting': meerutlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Meerut/india-ivf-clinic-meerut.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'meerutlisting': meerutlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Meerut/india-ivf-clinic-meerut.html', context)

#New Delhi
def indiaivfclinicnewdelhi(request):
    listing = BasicClinic.objects.get(pk=674)

    allcliniclisting = BasicClinic.objects.all()

    newdelhilisting = allcliniclisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'newdelhilisting': newdelhilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/New-Delhi/india-ivf-clinic-new-delhi.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'newdelhilisting': newdelhilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/New-Delhi/india-ivf-clinic-new-delhi.html', context)

def selectivfnewdelhi(request):
    listing = BasicClinic.objects.get(pk=675)

    allcliniclisting = BasicClinic.objects.all()

    newdelhilisting = allcliniclisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'newdelhilisting': newdelhilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/New-Delhi/select-ivf-new-delhi.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'newdelhilisting': newdelhilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/New-Delhi/select-ivf-new-delhi.html', context)

def indiraivfcentredelhi(request):
    listing = BasicClinic.objects.get(pk=676)

    allcliniclisting = BasicClinic.objects.all()

    newdelhilisting = allcliniclisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'newdelhilisting': newdelhilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/New-Delhi/indira-ivf-centre-delhi.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'newdelhilisting': newdelhilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/New-Delhi/indira-ivf-centre-delhi.html', context)

#Noida
def indiaivfclinicnoida(request):
    listing = BasicClinic.objects.get(pk=677)

    allcliniclisting = BasicClinic.objects.all()

    noidalisting = allcliniclisting.filter(is_published=True)
    noidalisting = noidalisting.filter(clinicCity__iexact='Noida')
    noidalisting = noidalisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'noidalisting': noidalisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Noida/india-ivf-clinic-noida.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'noidalisting': noidalisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Noida/india-ivf-clinic-noida.html', context)

#Pune
def oasisfertilitypune(request):
    listing = BasicClinic.objects.get(pk=678)

    allcliniclisting = BasicClinic.objects.all()

    punelisting = allcliniclisting.filter(is_published=True)
    punelisting = punelisting.filter(clinicCity__iexact='Pune')
    punelisting = punelisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'punelisting': punelisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Pune/oasis-fertility-pune.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'punelisting': punelisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Pune/oasis-fertility-pune.html', context)

#Ranchi
def oasisfertilityranchi(request):
    listing = BasicClinic.objects.get(pk=679)

    allcliniclisting = BasicClinic.objects.all()

    ranchilisting = allcliniclisting.filter(is_published=True)
    ranchilisting = ranchilisting.filter(clinicCity__iexact='Ranchi')
    ranchilisting = ranchilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'ranchilisting': ranchilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Ranchi/oasis-fertility-ranchi.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'ranchilisting': ranchilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Ranchi/oasis-fertility-ranchi.html', context)

def indiaivfclinicranchi(request):
    listing = BasicClinic.objects.get(pk=680)

    allcliniclisting = BasicClinic.objects.all()

    ranchilisting = allcliniclisting.filter(is_published=True)
    ranchilisting = ranchilisting.filter(clinicCity__iexact='Ranchi')
    ranchilisting = ranchilisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'ranchilisting': ranchilisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Ranchi/india-ivf-clinic-ranchi.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'ranchilisting': ranchilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Ranchi/india-ivf-clinic-ranchi.html', context)

#Rohtak
def indiaivfclinicrohtak(request):
    listing = BasicClinic.objects.get(pk=681)

    allcliniclisting = BasicClinic.objects.all()

    rohtaklisting = allcliniclisting.filter(is_published=True)
    rohtaklisting = rohtaklisting.filter(clinicCity__iexact='Rohtak')
    rohtaklisting = rohtaklisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'rohtaklisting': rohtaklisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Rohtak/india-ivf-clinic-rohtak.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'rohtaklisting': rohtaklisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Rohtak/india-ivf-clinic-rohtak.html', context)

#Vadodara
def oasisfertilityvadodara(request):
    listing = BasicClinic.objects.get(pk=682)

    allcliniclisting = BasicClinic.objects.all()

    vadodaralisting = allcliniclisting.filter(is_published=True)
    vadodaralisting = vadodaralisting.filter(clinicCity__iexact='Vadodara')
    vadodaralisting = vadodaralisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'vadodaralisting': vadodaralisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Vadodara/oasis-fertility-vadodara.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'vadodaralisting': vadodaralisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Vadodara/oasis-fertility-vadodara.html', context)

#Vijayawada
def oasisfertilityvijayawada(request):
    listing = BasicClinic.objects.get(pk=683)

    allcliniclisting = BasicClinic.objects.all()

    vijayawadalisting = allcliniclisting.filter(is_published=True)
    vijayawadalisting = vijayawadalisting.filter(clinicCity__iexact='Vijayawada')
    vijayawadalisting = vijayawadalisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'vijayawadalisting': vijayawadalisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Vijayawada/oasis-fertility-vijayawada.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'vijayawadalisting': vijayawadalisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Vijayawada/oasis-fertility-vijayawada.html', context)

#Visakhapatnam
def oasisfertilityvisakhapatnam(request):
    listing = BasicClinic.objects.get(pk=684)

    allcliniclisting = BasicClinic.objects.all()

    visakhapatnamlisting = allcliniclisting.filter(is_published=True)
    visakhapatnamlisting = visakhapatnamlisting.filter(clinicCity__iexact='Visakhapatnam')
    visakhapatnamlisting = visakhapatnamlisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'visakhapatnamlisting': visakhapatnamlisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Visakhapatnam/oasis-fertility-visakhapatnam.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'visakhapatnamlisting': visakhapatnamlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Visakhapatnam/oasis-fertility-visakhapatnam.html', context)

#Warangal
def oasisfertilitywarangal(request):
    listing = BasicClinic.objects.get(pk=685)

    allcliniclisting = BasicClinic.objects.all()

    warangallisting = allcliniclisting.filter(is_published=True)
    warangallisting = warangallisting.filter(clinicCity__iexact='Warangal')
    warangallisting = warangallisting.count()

    inlisting = allcliniclisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

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
            'warangallisting': warangallisting,
            'inlisting': inlisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/IN/Warangal/oasis-fertility-warangal.html', context)

    else:
        pass

    context = {
        'user_objects_count': user_objects_count,
        'user_objects': user_objects,
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'warangallisting': warangallisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Warangal/oasis-fertility-warangal.html', context)
