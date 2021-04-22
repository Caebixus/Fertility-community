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

#Nicosia
def cyprusivfcentre(request):
    listing = BasicClinic.objects.get(pk=697)

    nicosialisting = BasicClinic.objects.all()
    nicosialisting = nicosialisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=697)

    author = GuestAuthor.objects.filter(guestauthor_id=697)
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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/cyprus-ivf-centre.html', context)

    else:
        pass

    context = {
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

    nicosialisting = BasicClinic.objects.all()
    nicosialisting = nicosialisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=698)

    author = GuestAuthor.objects.filter(guestauthor_id=698)
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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/british-cyprus-ivf-hospital.html', context)

    else:
        pass

    context = {
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

    nicosialisting = BasicClinic.objects.all()
    nicosialisting = nicosialisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=699)

    author = GuestAuthor.objects.filter(guestauthor_id=699)
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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/eurocareivf.html', context)

    else:
        pass

    context = {
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

    nicosialisting = BasicClinic.objects.all()
    nicosialisting = nicosialisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=700)

    author = GuestAuthor.objects.filter(guestauthor_id=700)
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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/dogus-fertility-clinic.html', context)

    else:
        pass

    context = {
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

    nicosialisting = BasicClinic.objects.all()
    nicosialisting = nicosialisting.filter(is_published=True)
    nicosialisting = nicosialisting.filter(clinicCity__iexact='Nicosia')
    nicosialisting = nicosialisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=701)

    author = GuestAuthor.objects.filter(guestauthor_id=701)
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
            'nicosialisting': nicosialisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Nicosia/pedieos-ivf-center.html', context)

    else:
        pass

    context = {
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

    famagustalisting = BasicClinic.objects.all()
    famagustalisting = famagustalisting.filter(is_published=True)
    famagustalisting = famagustalisting.filter(clinicCity__iexact='Famagusta')
    famagustalisting = famagustalisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=702)

    author = GuestAuthor.objects.filter(guestauthor_id=702)
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
            'famagustalisting': famagustalisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Famagusta/crown-ivf-cyprus.html', context)

    else:
        pass

    context = {
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

    girnelisting = BasicClinic.objects.all()
    girnelisting = girnelisting.filter(is_published=True)
    girnelisting = girnelisting.filter(clinicCity__iexact='Girne')
    girnelisting = girnelisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=703)

    author = GuestAuthor.objects.filter(guestauthor_id=703)
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
            'girnelisting': girnelisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Girne/dunya-ivf-cyprus-fertility-clinic.html', context)

    else:
        pass

    context = {
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

    girnelisting = BasicClinic.objects.all()
    girnelisting = girnelisting.filter(is_published=True)
    girnelisting = girnelisting.filter(clinicCity__iexact='Girne')
    girnelisting = girnelisting.count()

    cylisting = BasicClinic.objects.all()
    cylisting = cylisting.filter(is_published=True)
    cylisting = cylisting.filter(clinicState__iexact='Cyprus')
    cylisting = cylisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=704)

    author = GuestAuthor.objects.filter(guestauthor_id=704)
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
            'girnelisting': girnelisting,
            'cylisting': cylisting,
            'alllisting': alllisting,
            }

        return render(request, 'clinics/CY/Girne/kyrenia-ivf-center.html', context)

    else:
        pass

    context = {
        'guestblog': guestblog,
        'listing': listing,
        'package': package,
        'girnelisting': girnelisting,
        'cylisting': cylisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/CY/Girne/kyrenia-ivf-center.html', context)
