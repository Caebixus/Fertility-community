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

#Bengalore
def kiraninfertilitycenterbengaluru(request):
    listing = BasicClinic.objects.get(pk=655)

    bengaloralisting = BasicClinic.objects.all()
    bengaloralisting = bengaloralisting.filter(is_published=True)
    bengaloralisting = bengaloralisting.filter(clinicCity__iexact='Bangalore')
    bengaloralisting = bengaloralisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=655)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'bengaloralisting': bengaloralisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Bangalore/kiran-infertility-center-bangalore.html', context)

def mannatfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=656)

    bengaloralisting = BasicClinic.objects.all()
    bengaloralisting = bengaloralisting.filter(is_published=True)
    bengaloralisting = bengaloralisting.filter(clinicCity__iexact='Bengalore')
    bengaloralisting = bengaloralisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=656)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    gachibowlisting = BasicClinic.objects.all()
    gachibowlisting = gachibowlisting.filter(is_published=True)
    gachibowlisting = gachibowlisting.filter(clinicCity__iexact='Gachibowli')
    gachibowlisting = gachibowlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=657)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    gurugramlisting = BasicClinic.objects.all()
    gurugramlisting = gurugramlisting.filter(is_published=True)
    gurugramlisting = gurugramlisting.filter(clinicCity__iexact='Gurugram')
    gurugramlisting = gurugramlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=658)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    gwaliorlisting = BasicClinic.objects.all()
    gwaliorlisting = gwaliorlisting.filter(is_published=True)
    gwaliorlisting = gwaliorlisting.filter(clinicCity__iexact='Gwalior')
    gwaliorlisting = gwaliorlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=659)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    haldwanilisting = BasicClinic.objects.all()
    haldwanilisting = haldwanilisting.filter(is_published=True)
    haldwanilisting = haldwanilisting.filter(clinicCity__iexact='Haldwani')
    haldwanilisting = haldwanilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=660)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=661)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-banjara-hills.html', context)

def oasisfertilityhyderabadsecunderabad(request):
    listing = BasicClinic.objects.get(pk=662)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=662)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-secunderabad.html', context)

def oasisfertilityhyderabaddilsukhnagar(request):
    listing = BasicClinic.objects.get(pk=663)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=663)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-dilsukhnagar.html', context)

def oasisfertilityhyderabadgachibowli(request):
    listing = BasicClinic.objects.get(pk=664)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=664)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-gachibowli.html', context)

def oasisfertilityhyderabmiyapur(request):
    listing = BasicClinic.objects.get(pk=665)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=665)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/oasis-fertility-hyderabad-miyapur.html', context)

def kiraninfertilitycenterhyderabad(request):
    listing = BasicClinic.objects.get(pk=666)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=666)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-hyderabad.html', context)

def kiraninfertilitycenterkothapet(request):
    listing = BasicClinic.objects.get(pk=667)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=667)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'hyderabadlisting': hyderabadlisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Hyderabad/kiran-infertility-center-kothapet.html', context)

def hegdefertilitymalakpet(request):
    listing = BasicClinic.objects.get(pk=668)

    hyderabadlisting = BasicClinic.objects.all()
    hyderabadlisting = hyderabadlisting.filter(is_published=True)
    hyderabadlisting = hyderabadlisting.filter(clinicCity__iexact='Hyderabad')
    hyderabadlisting = hyderabadlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=668)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    chennailisting = BasicClinic.objects.all()
    chennailisting = chennailisting.filter(is_published=True)
    chennailisting = chennailisting.filter(clinicCity__iexact='Chennai')
    chennailisting = chennailisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=669)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'chennailisting': chennailisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Chennai/oasis-fertility-chennai.html', context)

def kiraninfertilitycenterchennai(request):
    listing = BasicClinic.objects.get(pk=670)

    chennailisting = BasicClinic.objects.all()
    chennailisting = chennailisting.filter(is_published=True)
    chennailisting = chennailisting.filter(clinicCity__iexact='Chennai')
    chennailisting = chennailisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=670)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    jammulisting = BasicClinic.objects.all()
    jammulisting = jammulisting.filter(is_published=True)
    jammulisting = jammulisting.filter(clinicCity__iexact='Jammu')
    jammulisting = jammulisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=671)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    madhapurlisting = BasicClinic.objects.all()
    madhapurlisting = madhapurlisting.filter(is_published=True)
    madhapurlisting = madhapurlisting.filter(clinicCity__iexact='Madhapur')
    madhapurlisting = madhapurlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=672)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    meerutlisting = BasicClinic.objects.all()
    meerutlisting = meerutlisting.filter(is_published=True)
    meerutlisting = meerutlisting.filter(clinicCity__iexact='Meerut')
    meerutlisting = meerutlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=673)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    newdelhilisting = BasicClinic.objects.all()
    newdelhilisting = newdelhilisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=674)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'newdelhilisting': newdelhilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/New-Delhi/india-ivf-clinic-new-delhi.html', context)

def selectivfnewdelhi(request):
    listing = BasicClinic.objects.get(pk=675)

    newdelhilisting = BasicClinic.objects.all()
    newdelhilisting = newdelhilisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=675)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'newdelhilisting': newdelhilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/New-Delhi/select-ivf-new-delhi.html', context)

def indiraivfcentredelhi(request):
    listing = BasicClinic.objects.get(pk=676)

    newdelhilisting = BasicClinic.objects.all()
    newdelhilisting = newdelhilisting.filter(is_published=True)
    newdelhilisting = newdelhilisting.filter(clinicCity__iexact='New Delhi')
    newdelhilisting = newdelhilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=676)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    noidalisting = BasicClinic.objects.all()
    noidalisting = noidalisting.filter(is_published=True)
    noidalisting = noidalisting.filter(clinicCity__iexact='Noida')
    noidalisting = noidalisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=677)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    punelisting = BasicClinic.objects.all()
    punelisting = punelisting.filter(is_published=True)
    punelisting = punelisting.filter(clinicCity__iexact='Pune')
    punelisting = punelisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=678)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    ranchilisting = BasicClinic.objects.all()
    ranchilisting = ranchilisting.filter(is_published=True)
    ranchilisting = ranchilisting.filter(clinicCity__iexact='Ranchi')
    ranchilisting = ranchilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=679)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'ranchilisting': ranchilisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Ranchi/oasis-fertility-ranchi.html', context)

def indiaivfclinicranchi(request):
    listing = BasicClinic.objects.get(pk=680)

    ranchilisting = BasicClinic.objects.all()
    ranchilisting = ranchilisting.filter(is_published=True)
    ranchilisting = ranchilisting.filter(clinicCity__iexact='Ranchi')
    ranchilisting = ranchilisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=680)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    rohtaklisting = BasicClinic.objects.all()
    rohtaklisting = rohtaklisting.filter(is_published=True)
    rohtaklisting = rohtaklisting.filter(clinicCity__iexact='Rohtak')
    rohtaklisting = rohtaklisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=681)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    vadodaralisting = BasicClinic.objects.all()
    vadodaralisting = vadodaralisting.filter(is_published=True)
    vadodaralisting = vadodaralisting.filter(clinicCity__iexact='Vadodara')
    vadodaralisting = vadodaralisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=682)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    vijayawadalisting = BasicClinic.objects.all()
    vijayawadalisting = vijayawadalisting.filter(is_published=True)
    vijayawadalisting = vijayawadalisting.filter(clinicCity__iexact='Vijayawada')
    vijayawadalisting = vijayawadalisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=683)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    visakhapatnamlisting = BasicClinic.objects.all()
    visakhapatnamlisting = visakhapatnamlisting.filter(is_published=True)
    visakhapatnamlisting = visakhapatnamlisting.filter(clinicCity__iexact='Visakhapatnam')
    visakhapatnamlisting = visakhapatnamlisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=684)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    warangallisting = BasicClinic.objects.all()
    warangallisting = warangallisting.filter(is_published=True)
    warangallisting = warangallisting.filter(clinicCity__iexact='Warangal')
    warangallisting = warangallisting.count()

    inlisting = BasicClinic.objects.all()
    inlisting = inlisting.filter(is_published=True)
    inlisting = inlisting.filter(clinicState__iexact='India')
    inlisting = inlisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    todayDate = timezone.now()
    package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
    package = package.filter(packageclinic__id=685)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'warangallisting': warangallisting,
        'inlisting': inlisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/IN/Warangal/oasis-fertility-warangal.html', context)
