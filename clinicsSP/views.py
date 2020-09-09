from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone
from owners.models import ownerProInterested, ProUser

#ALICANTE   --------------------------------
def ivfspainalicante(request):
    listing = BasicClinic.objects.get(pk=617)

    alicantelisting = BasicClinic.objects.all()
    alicantelisting = alicantelisting.filter(is_published=True)
    alicantelisting = alicantelisting.filter(clinicRegion__iexact='Alicante')
    alicantelisting = alicantelisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=617)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'alicantelisting': alicantelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Alicante/ivf-spain-alicante.html', context)

def ivialicante(request):
    listing = BasicClinic.objects.get(pk=619)

    alicantelisting = BasicClinic.objects.all()
    alicantelisting = alicantelisting.filter(is_published=True)
    alicantelisting = alicantelisting.filter(clinicRegion__iexact='Alicante')
    alicantelisting = alicantelisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=619)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=620)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/clinica-de-fertilidad-barcelona-ivf.html', context)

def ferttyinternational(request):
    listing = BasicClinic.objects.get(pk=621)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=621)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fertty-international.html', context)

def fertilabbarcelona(request):
    listing = BasicClinic.objects.get(pk=622)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=622)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fertilab-barcelona.html', context)

def institutmarquesbarcelona(request):
    listing = BasicClinic.objects.get(pk=623)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=623)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/institut-marques-barcelona.html', context)

def ivfforyou(request):
    listing = BasicClinic.objects.get(pk=624)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=624)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/ivf-for-you.html', context)

def gravida(request):
    listing = BasicClinic.objects.get(pk=625)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=625)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/gravida.html', context)

def ivibarcelona(request):
    listing = BasicClinic.objects.get(pk=626)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=626)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/ivi-barcelona.html', context)

def fivmarbellabarcelona(request):
    listing = BasicClinic.objects.get(pk=627)

    barcelonalisting = BasicClinic.objects.all()
    barcelonalisting = barcelonalisting.filter(is_published=True)
    barcelonalisting = barcelonalisting.filter(clinicRegion__iexact='Barcelona')
    barcelonalisting = barcelonalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=627)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'barcelonalisting': barcelonalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Barcelona/fiv-marbella-barcelona.html', context)

#MADRID   --------------------------------
def ivfspainmadrid(request):
    listing = BasicClinic.objects.get(pk=628)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=628)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/ivf-spain-madrid.html', context)

def fertilitymadrid(request):
    listing = BasicClinic.objects.get(pk=629)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=629)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fertility-madrid.html', context)

def evafertilityclinicmadrid(request):
    listing = BasicClinic.objects.get(pk=630)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=630)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/eva-fertility-clinic-madrid.html', context)

def ivimadridaravaca(request):
    listing = BasicClinic.objects.get(pk=631)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=631)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/ivi-madrid-aravaca.html', context)

def clinicatambre(request):
    listing = BasicClinic.objects.get(pk=632)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=632)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/ivi-madrid-aravaca.html', context)

def fertilityclinichru(request):
    listing = BasicClinic.objects.get(pk=633)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=633)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fertility-clinic-hru.html', context)

def fivmarbellamadrid(request):
    listing = BasicClinic.objects.get(pk=634)

    madridlisting = BasicClinic.objects.all()
    madridlisting = madridlisting.filter(is_published=True)
    madridlisting = madridlisting.filter(clinicRegion__iexact='Madrid')
    madridlisting = madridlisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=634)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'madridlisting': madridlisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Madrid/fiv-marbella-madrid.html', context)

#MALAGA   --------------------------------
def ivimalaga(request):
    listing = BasicClinic.objects.get(pk=635)

    malagalisting = BasicClinic.objects.all()
    malagalisting = malagalisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=635)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/ivi-malaga.html', context)

def fivmarbellamalaga(request):
    listing = BasicClinic.objects.get(pk=636)

    malagalisting = BasicClinic.objects.all()
    malagalisting = malagalisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=636)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/fiv-marbella-malaga.html', context)

def hcfertility(request):
    listing = BasicClinic.objects.get(pk=637)

    malagalisting = BasicClinic.objects.all()
    malagalisting = malagalisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=637)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/hc-fertility.html', context)

def clinicafertia(request):
    listing = BasicClinic.objects.get(pk=638)

    malagalisting = BasicClinic.objects.all()
    malagalisting = malagalisting.filter(is_published=True)
    malagalisting = malagalisting.filter(clinicRegion__iexact='Malaga')
    malagalisting = malagalisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=638)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'malagalisting': malagalisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Malaga/clinica-fertia.html', context)

#SEVILLE   --------------------------------
def ivisevilla(request):
    listing = BasicClinic.objects.get(pk=639)

    sevillelisting = BasicClinic.objects.all()
    sevillelisting = sevillelisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=639)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/ivi-sevilla.html', context)

def inebir(request):
    listing = BasicClinic.objects.get(pk=640)

    sevillelisting = BasicClinic.objects.all()
    sevillelisting = sevillelisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=640)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/inebir.html', context)

def ginemedsevilla(request):
    listing = BasicClinic.objects.get(pk=641)

    sevillelisting = BasicClinic.objects.all()
    sevillelisting = sevillelisting.filter(is_published=True)
    sevillelisting = sevillelisting.filter(clinicRegion__iexact='Seville')
    sevillelisting = sevillelisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=641)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'sevillelisting': sevillelisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Seville/ginemed-sevilla.html', context)

#VALENCIA   --------------------------------
def ivivalencia(request):
    listing = BasicClinic.objects.get(pk=642)

    valencialisting = BasicClinic.objects.all()
    valencialisting = valencialisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=642)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/ivi-valencia.html', context)

def equipojuanacrespo(request):
    listing = BasicClinic.objects.get(pk=643)

    valencialisting = BasicClinic.objects.all()
    valencialisting = valencialisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=643)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/equipo-juana-crespo.html', context)

def unidaddereproduccionasistidaimedvalencia(request):
    listing = BasicClinic.objects.get(pk=644)

    valencialisting = BasicClinic.objects.all()
    valencialisting = valencialisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=644)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/unidad-de-reproduccion-asistida-imed-valencia.html', context)

def creavalencia(request):
    listing = BasicClinic.objects.get(pk=645)

    valencialisting = BasicClinic.objects.all()
    valencialisting = valencialisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=645)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/crea-valencia.html', context)

def imerinstitutodemedicinareproductiva(request):
    listing = BasicClinic.objects.get(pk=646)

    valencialisting = BasicClinic.objects.all()
    valencialisting = valencialisting.filter(is_published=True)
    valencialisting = valencialisting.filter(clinicRegion__iexact='Valencia')
    valencialisting = valencialisting.count()

    splisting = BasicClinic.objects.all()
    splisting = splisting.filter(is_published=True)
    splisting = splisting.filter(clinicState__iexact='Spain')
    splisting = splisting.count()

    alllisting = BasicClinic.objects.all()
    alllisting = alllisting.filter(is_published=True)
    alllisting = alllisting.count()

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=646)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
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
        'listing': listing,
        'package': package,
        'valencialisting': valencialisting,
        'splisting': splisting,
        'alllisting': alllisting,
        }

    return render(request, 'clinics/SP/Valencia/imer-instituto-de-medicina-reproductiva.html', context)
