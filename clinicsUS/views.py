from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone
from owners.models import ownerProInterested, ProUser

# Create your views here.
def wfi(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=1)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=1)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/western-fertility-institute.html', context)

def cifc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=2)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=2)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/california-ivf-fertility-center.html', context)

def ncfmcr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=3)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=3)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-roseville.html', context)

def ncfmcs(request):
    listing = BasicClinic.objects.get(pk=4)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=4)

    if request.user.is_authenticated:
        usergroup = ProUser.objects.all()
        usergroup = usergroup.filter(user=request.user)
        usergroup = usergroup.filter(paidPropublished=True)

        context = {
            'usergroup': usergroup,
            'listing': listing,
            'package': package,
            }

        return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

    else:
        pass

    context = {
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

def liwla(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=5)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=5)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/la-ivf-west-los-angeles.html', context)

def lip(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=6)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=6)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/la-ivf-pasadena.html', context)

def lich(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=7)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=7)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/California/la-ivf-chino-hills.html', context)

# ALABAMA Views --------------------------------------------------------------------------------------------------------

def tcfrm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=8)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=8)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Alabama/center-for-reproductive-medicine.html', context)

def af(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=9)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=9)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Alabama/alabama-fertility.html', context)

# ARIZONA Views --------------------------------------------------------------------------------------------------------

def tfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=10)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=10)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-scottsdale.html', context)

def tfg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=11)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=11)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-glendale.html', context)

def tfm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=12)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=12)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-mesa.html', context)

def sfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=13)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=13)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/southwest-fertility-center.html', context)

def afcs(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=14)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=14)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-scottsdale.html', context)

def afcm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=15)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=15)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-mesa.html', context)

def aafrhs(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=16)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=16)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-scottsdale.html', context)

def aafrhg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=17)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=17)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-gilbert.html', context)

def bris(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=18)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=18)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-scottsdale.html', context)

def brig(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=19)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=19)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-gilbert.html', context)

def biacs(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=20)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=20)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-scottsdale.html', context)

def biacch(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=21)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=21)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-chandler.html', context)

def biacp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=22)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=22)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-peoria.html', context)

def biacf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=23)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=23)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-flagstaff.html', context)

def ip(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=24)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=24)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/ivf-phoenix.html', context)

def ftc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=25)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=25)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/fertility-treatment-center.html', context)

def arifc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=26)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=26)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arizona/arizona-reproductive-institute-fertility-clinic.html', context)

# ARKANSAS Views --------------------------------------------------------------------------------------------------------

def afg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=37)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=37)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Arkansas/arkansas-fertility-gynecology.html', context)

# COLORADO Views --------------------------------------------------------------------------------------------------------

def ccrmcmclt(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=38)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=38)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-main-center-lone-tree.html', context)

def ccrmcdo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=39)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=39)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-denver-office.html', context)

def ccrmclo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=40)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=40)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-louisville-office.html', context)

def ucarmd(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=41)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=41)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-denver.html', context)

def ucarmcos(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=42)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=42)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-co-springs.html', context)

def rmcrm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=43)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=43)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Colorado/rocky-mountain-center-reproductive-medicine.html', context)

# CONNECTICUT Views --------------------------------------------------------------------------------------------------------

def carsf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=44)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=44)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/cars-farmington.html', context)

def carsh(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=45)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=45)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/cars-hartford.html', context)

def carsnl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=46)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=46)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/cars-new-london.html', context)

def carsb(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=47)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=47)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/cars-branford.html', context)

def gfg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=48)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=48)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-greenwich.html', context)

def gfs(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=49)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=49)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-stamford.html', context)

def rmactn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=50)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=50)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/rmact-norwalk.html', context)

def rmacts(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=51)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=51)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/rmact-stamford.html', context)

def rmactd(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=52)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=52)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/rmact-danbury.html', context)

def rmactt(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=53)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=53)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/rmact-trumbull.html', context)

def paft(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=54)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=54)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-trumbull.html', context)

def paff(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=55)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=55)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-fairfield.html', context)

def pafn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=56)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=56)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-norwalk.html', context)

# DELAWARE Views --------------------------------------------------------------------------------------------------------

def dirmn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=57)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=57)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Delaware/dirm-newark.html', context)

def dirmm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=58)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=58)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Delaware/dirm-milford.html', context)

def radfn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=59)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=59)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Delaware/radfertility-newark.html', context)

def radfw(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=60)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=60)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Delaware/radfertility-wilmington.html', context)

def radfd(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=61)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=61)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Delaware/radfertility-dover.html', context)

# FLORIDA Views --------------------------------------------------------------------------------------------------------

def bocaf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=62)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=62)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/boca-fertility.html', context)

def pbfcbr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=63)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=63)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/pbfc-boca-raton.html', context)

def pbfcpbg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=64)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=64)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/pbfc-palm-beach-gardens.html', context)

def ffico(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=65)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=65)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ffi-clearwater-office.html', context)

def ffito(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=66)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=66)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ffi-tampa-office.html', context)

def cfcg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=67)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=67)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-coral-gables.html', context)

def cfm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=68)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=68)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-miramar.html', context)

def jcrmj(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=69)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=69)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/jcrm-jacksonville.html', context)

def jcrmg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=70)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=70)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/jcrm-gainesville.html', context)

def jcrmpc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=71)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=71)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/jcrm-panama-city.html', context)

def jcrmo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=72)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=72)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/jcrm-orlando.html', context)

def rmanlm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=73)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=73)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/rma-network-lake-mary.html', context)

def ivffwfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=74)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=74)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-wellington-fertility-center.html', context)

def ivffcgfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=75)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=75)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-coral-gables-fertility-center.html', context)

def ivfppfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=76)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=76)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-pembroke-pines-fertility-center.html', context)

def ivffmfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=77)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=77)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-margate-fertility-center.html', context)

def ivfbrfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=78)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=78)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-boca-raton-fertility-center.html', context)

def ivffjpbgfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=79)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=79)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-jupiter-palm-beach-gardens-fertility-center.html', context)

def ivffplfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=80)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=80)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-port-lucie-fertility-clinic.html', context)

def vfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=81)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=81)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/viera-fertility-center.html', context)

def fivfcm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=82)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=82)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami.html', context)

def fivfcmb(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=83)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=83)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami-beach.html', context)

def fg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=84)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=84)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/fertility-genetics.html', context)

def ivfmdm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=85)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=85)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-miami.html', context)

def ivfmdcc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=86)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=86)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-cooper-city.html', context)

def ivfmdbr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=87)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=87)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-boca-raton.html', context)

def ivfmdj(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=88)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=88)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-jupiter.html', context)

def ivfmdn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=89)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=89)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-naples.html', context)

def ivfmdv(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=90)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=90)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivfmd-viera.html', context)

def sgftw(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=91)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=91)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/sgf-tampa-westshore.html', context)

def sgfb(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=92)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=92)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/sgf-brandon.html', context)

def sgfwc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=93)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=93)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/sgf-wesley-chapel.html', context)

def rmgnto(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=94)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=94)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/rmg-north-tampa-office.html', context)

def rmgsto(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=95)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=95)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/rmg-south-tampa-office.html', context)

def rmgco(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=96)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=96)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/rmg-clearwater-office.html', context)

def rmgbo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=97)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=97)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/rmg-brandon-office.html', context)

def fifrst(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=98)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=98)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/florida-institute-for-reproductive-sciences-technologies.html', context)

def arswp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=99)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=99)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/advanced-reproductive-specialists-winter-park.html', context)

def ivfowp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=100)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=100)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/ivf-orlando-winter-park.html', context)

def fcare(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=101)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=101)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Florida/fertility-center-assisted-reproduction-endocrinology.html', context)

# GEORGIA Views --------------------------------------------------------------------------------------------------------

def afa(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=102)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=102)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/aspire-fertility-atlanta.html', context)

def acrmap(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=103)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=103)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-perimetr.html', context)

def acrmab(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=104)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=104)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-buckhead.html', context)

def acrmjc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=105)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=105)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/acrm-johns-creek.html', context)

def acrmm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=106)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=106)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/acrm-marietta.html', context)

def mfs(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=107)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=107)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/massey-fertility-services.html', context)

def sfi(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=108)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=108)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/servy-fertility-institute.html', context)

def sgfan(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=109)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=109)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/sgf-atlanta-northside.html', context)

def sgfa(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=110)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=110)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/sgf-alpharetta.html', context)

def sgfbp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=111)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=111)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/sgf-buckhead-piedmont.html', context)

def sgfm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=112)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=112)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/sgf-marietta.html', context)

def rbamo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=113)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=113)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–main-office.html', context)

def rbam(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=114)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=114)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–marietta.html', context)

def rbaf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=115)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=115)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–fayetteville.html', context)

def rbal(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=116)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=116)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–lawrenceville.html', context)

def rbac(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=117)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=117)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cumming.html', context)

def rbaph(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=118)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=118)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–piedmont-hospital.html', context)

def rbacar(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=119)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=119)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cartersville.html', context)

def cnyferticentatlanta(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=504)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=504)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/cny-fertility-center-atlanta.html', context)

def coastalfertispecsavannah(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=505)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=505)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Georgia/coastal-fertility-specialists-savannah.html', context)

# HAWAII Views --------------------------------------------------------------------------------------------------------

def arch(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=120)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=120)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Hawaii/advanced-reproductive-center-hawaii.html', context)

def armghh(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=121)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=121)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Hawaii/armgh-honolulu.html', context)

def armghk(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=122)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=122)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Hawaii/armgh-kailua.html', context)

def pivfi(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=123)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=123)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Hawaii/pacific-in-vitro-fertilization-institute.html', context)

# IOWA Views --------------------------------------------------------------------------------------------------------

def mif(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=124)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=124)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Iowa/mid-iowa-fertility.html', context)

# IDAHO Views --------------------------------------------------------------------------------------------------------

def icrm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=125)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=125)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Idaho/idaho-center-reproductive-medicine.html', context)

def reprocarecenteridahofalls(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=503)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=503)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Idaho/reproductive-care-center-idaho-falls.html', context)

# ILLINOIS Views --------------------------------------------------------------------------------------------------------

def crc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=126)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=126)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/center-reproductive-care.html', context)

def fcibgc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=127)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=127)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-buffalo-grove-clinic.html', context)

def fcicnc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=128)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=128)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-chicago-north-clinic.html', context)

def fcigc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=129)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=129)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-glenview-clinic.html', context)

def fcihpc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=130)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=130)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-highland-park-clinic.html', context)

def fcihc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=131)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=131)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-hinsdale-clinic.html', context)

def fcihec(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=132)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=132)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-hoffman-estates-clinic.html', context)

def fcilc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=133)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=133)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-lindenhurst-clinic.html', context)

def fcitpc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=134)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=134)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-tinley-park-clinic.html', context)

def fciwc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=135)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=135)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/fci-warrenville-clinic.html', context)

def ihrc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=136)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=136)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/ihr-chicago.html', context)

def ihro(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=137)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=137)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/ihr-oakbrook.html', context)

def vfica(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=138)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=138)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-aurora.html', context)

def vficwp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=139)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=139)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-wicker-park.html', context)

def vficwlil(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=140)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=140)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-west-loop-ivf-lab.html', context)

def vficg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=141)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=141)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-glenview.html', context)

def vfiche(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=142)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=142)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-hoffman-estates.html', context)

def dfis(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=143)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=143)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/davies-fertility-ivf-specialists.html', context)

def hcr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=144)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=144)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/hinsdale-center-reproduction.html', context)

def ifsah(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=145)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=145)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-arlington-heights.html', context)

def ifscl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=146)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=146)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-crystal-lake.html', context)

def ifshe(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=147)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=147)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-hoffman-estates.html', context)

def ifsn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=148)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=148)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-northbrook.html', context)

def ivf1(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=149)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=149)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/ivf1.html', context)

def rmib(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=150)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=150)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-bloomingdale.html', context)

def rmic(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=151)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=151)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-chicago.html', context)

def rmiel(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=152)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=152)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-elmhurst.html', context)

def rmiev(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=153)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=153)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-evanston.html', context)

def rminb(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=154)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=154)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-northbrook.html', context)

def rmiob(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=155)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=155)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-brook.html', context)

def rmiol(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=156)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=156)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-lawn.html', context)

def civfops(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=157)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=157)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-orland-park–southwest.html', context)

def civfscn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=158)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=158)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-stcharles–northwest.html', context)

def civfnw(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=159)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=159)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-naperville–west.html', context)

# INDIANA Views --------------------------------------------------------------------------------------------------------

def ihrval(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=161)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=161)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/ihr-valparaiso.html', context)

def mfcar(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=162)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=162)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-carmel.html', context)

def mffortwayne(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=165)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=165)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-fort-wayne.html', context)

def civfval(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=163)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=163)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-valparaiso.html', context)

def civfmun(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=164)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=164)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-munster.html', context)

def prhmun(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=166)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=166)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/partners-reproductive-health-munster.html', context)

def fbeg(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=167)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=167)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/family-beginnings.html', context)

def ifinst(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=168)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=168)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/indiana-fertility-institute.html', context)

def rcimo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=169)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=169)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-main-office.html', context)

def rcith(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=170)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=170)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-terre-haute.html', context)

def rcilaf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=171)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=171)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-lafayette.html', context)

def rcibmc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=172)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=172)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-mc.html', context)

def rcibws(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=173)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=173)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-ws.html', context)

# KANSAS Views --------------------------------------------------------------------------------------------------------

def midrepc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=174)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=174)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Kansas/midwest-reproductive-center.html', context)

# KENTUCKY Views --------------------------------------------------------------------------------------------------------

def ferendas(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=175)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=175)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Kentucky/fertility-endocrine-associates.html', context)

def ifrhealthflo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=501)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=501)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-florence.html', context)

def ifrhealthlou(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=502)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=502)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Kentucky/institute-for-reproductive-health-louisville.html', context)

# LOUISIANA Views --------------------------------------------------------------------------------------------------------

def feanla(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=176)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=176)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lafayette.html', context)

def feanbaro(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=177)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=177)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-baton-rouge.html', context)

def feanco(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=178)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=178)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-covington.html', context)

def feanlach(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=179)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=179)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lake-charles.html', context)

def fiman(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=180)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=180)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fi-mandeville.html', context)

def fimet(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=181)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=181)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fi-metairie.html', context)

def fibaro(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=182)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=182)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/fi-baton-rouge.html', context)

def audfer(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=183)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=183)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/audubon-fertility.html', context)

def arkferrepmed(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=184)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=184)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Louisiana/arklatex-fertility-reproductive-medicine.html', context)

# MAINE Views --------------------------------------------------------------------------------------------------------

def fcnebc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=186)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=186)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Maine/fcne-bangor-center.html', context)

def bivfbfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=187)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=187)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-bangor-fertility-center.html', context)

def bivfpfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=188)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=188)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-portland-fertility-center.html', context)

# MARYLAND Views --------------------------------------------------------------------------------------------------------

# MASSACHUSETTS Views --------------------------------------------------------------------------------------------------------

def masghfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=185)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=185)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/massachusetts-general-hospital-fertility-center.html', context)

def ccrmbmc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=189)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=189)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-boston-main-center.html', context)

def ccrmmo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=190)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=190)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-metrowest-office.html', context)

def ccrmsso(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=191)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=191)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-south-shore-office.html', context)

def bivfmfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=192)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=192)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-tufts-medical-fertility-center.html', context)

def bivfdbfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=193)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=193)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-downtown-boston-fertility-center.html', context)

def bivflfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=194)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=194)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-lexington-fertility-center.html', context)

def bivfqfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=195)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=195)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-quincy-fertility-center.html', context)

def bivfwfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=196)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=196)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-waltham-fertility-center.html', context)

def bivfsfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=197)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=197)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-stoneham-fertility-center.html', context)

def fcnelc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=198)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=198)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-leominster-center.html', context)

def fcnerc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=199)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=199)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-reading-center.html', context)

def fcnedc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=200)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=200)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-danvers-center.html', context)

def fcnebce(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=201)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=201)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-braintree-center.html', context)

def fcnebcen(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=202)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=202)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-boston-center.html', context)

# MICHIGAN Views --------------------------------------------------------------------------------------------------------

def ivfmfcaafc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=203)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=203)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-ann-arbor-fertility-center.html', context)

def ivfmfcbhfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=204)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=204)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-bloomfield-hills-fertility-center.html', context)

def ivfmfcchebfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=205)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=205)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-cheboygan-fertility-center.html', context)

def ivfmfcdfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=206)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=206)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-dearborn-fertility-center.html', context)

def ivfmfcelfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=207)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=207)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-east-lansing-fertility-center.html', context)

def ivfmfcmfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=208)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=208)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-macomb-fertility-center.html', context)

def ivfmfcpfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=209)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=209)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-petoskey-fertility-center.html', context)

def ivfmfcsfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=210)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=210)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-saginaw-fertility-center.html', context)

def ivfmfctfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=211)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=211)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-toledo-fertility-center.html', context)

def gcffb(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=212)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=212)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-brighton.html', context)

def ggcffl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=213)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=213)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-lansing.html', context)

def ggcffaa(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=214)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=214)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-ann-arbor.html', context)

def tfcgr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=215)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=215)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-grand-rapids.html', context)

def tfcm(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=216)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=216)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-mason.html', context)

def tfck(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=217)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=217)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-kalamazoo.html', context)

def tfctc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=218)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=218)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-traverse-city.html', context)

def ivfmrh(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=219)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=219)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-rochester-hills.html', context)

def ivfmf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=220)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=220)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-flint.html', context)

def ivfmd(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=221)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=221)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-dearborn.html', context)

def rmaom(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=222)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=222)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Michigan/reproductive-medicine-associates-of-michigan.html', context)

# MINNESOTA Views --------------------------------------------------------------------------------------------------------

def cccrmmin(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=223)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=223)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/ccrm-minneapolis.html', context)

def midcfrh(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=224)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=224)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/midwest-center-for-reproductive-health.html', context)

def cenfrmmin(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=225)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=225)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-minneapolis.html', context)

def cenfrmstp(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=226)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=226)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-paul.html', context)

def cenfrmwesog(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=227)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=227)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-western-ob-gyn.html', context)

def cenfremstluobgyna(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=228)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=228)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-lukes-obstetrics-gynecology-associates.html', context)

def repmeinaswoo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=229)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=229)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-woodbury.html', context)

def repmeinasedi(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=230)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=230)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-edina.html', context)

# MISSISSIPPI Views --------------------------------------------------------------------------------------------------------

def cenfrmmfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=231)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=231)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Mississippi/center-for-reproductive-medicine-mississippi-fertility-clinic.html', context)

def missrepmed(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=232)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=232)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Mississippi/mississippi-reproductive-medicine.html', context)

# MISSOURI Views --------------------------------------------------------------------------------------------------------

def vfichisl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=233)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=233)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-saint-louis.html', context)

def vfichiofa(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=234)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=234)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-ofallon.html', context)

def infeceofstlo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=235)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=235)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/infertility-center-of-st-louis.html', context)

def mcrmferstlo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=236)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=236)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-st-louis.html', context)

def mcrmferspring(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=237)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=237)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-springfield.html', context)

def missofer(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=238)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=238)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/missouri-fertility.html', context)

def shiforrepmestlofecl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=239)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=239)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Missouri/sher-institutes-for-reproductive-medicine-st-louis-fertility-clinic.html', context)

# NEBRASKA Views --------------------------------------------------------------------------------------------------------

def hearceforrepme(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=240)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=240)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Nebraska/heartland-center-for-reproductive-medicine.html', context)

# NEVADA Views --------------------------------------------------------------------------------------------------------

def greevalferpartners(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=241)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=241)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Nevada/green-valley-fertility-partners.html', context)

def theferceoflasvegas(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=242)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=242)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Nevada/the-fertility-center-of-las-vegas.html', context)

def sherinsfrepmedlasvegfecl(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=243)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=243)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Nevada/sher-institutes-for-reproductive-medicine-las-vegas-fertility-clinic.html', context)

def redrofercen(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=244)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=244)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Nevada/red-rock-fertility-center.html', context)

# NEW JERSEY Views --------------------------------------------------------------------------------------------------------

def irmsco(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=27)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=27)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-clark-office.html', context)

def irmsewo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=28)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=28)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-east-windsor-office.html', context)

def irmsho(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=29)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=29)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hackensack-office.html', context)

def irmshbo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=30)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=30)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hoboken-office.html', context)

def irmsnjo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=31)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=31)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-jersey-city-office.html', context)

def irmslo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=32)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=32)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-livingston-office.html', context)

def irmsobo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=33)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=33)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/irms-old-bridge-office.html', context)

def Cenfoarepmedicinefer(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=245)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=245)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/center-for-advanced-reproductive-medicine-fertility.html', context)

def rmanetbasrid(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=246)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=246)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-basking-ridge.html', context)

def rmaneteaton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=247)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=247)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-eatontown.html', context)

def rmanetenglewood(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=248)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=248)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-englewood.html', context)

def rmanetfreehold(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=249)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=249)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-freehold.html', context)

def rmanetmarlton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=250)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=250)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-marlton.html', context)

def rmanetmorristown(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=251)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=251)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-morristown.html', context)

def rmanetprinceston(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=252)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=252)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-princeton.html', context)

def rmanetsomerset(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=253)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=253)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-somerset.html', context)

def rmanetspringfield(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=254)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=254)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-springfield.html', context)

def rmanetwestorang(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=255)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=255)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-west-orange.html', context)

def unirepproassohasbhei(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=256)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=256)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hasbrouck-heights.html', context)

def unirepproassohoboken(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=257)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=257)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hoboken.html', context)

def unirepproassowayne(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=258)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=258)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-wayne.html', context)

def princetonivf(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=259)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=259)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/princeton-ivf.html', context)

def delawvallinsoffergenmarlton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=260)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=260)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-marlton.html', context)

def delawvallinsoffergenvineland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=261)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=261)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-vineland.html', context)

def delawvallinsoffergenprinceton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=262)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=262)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-princeton.html', context)

def southjefecemarlton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=263)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=263)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-marlton.html', context)

def southjefeceburlington(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=264)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=264)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-burlington.html', context)

def southjefecesewell(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=265)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=265)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-sewell.html', context)

def southjefecetownship(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=266)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=266)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-egg-harbor-township.html', context)

def diamondinsmilburn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=267)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=267)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-millburn.html', context)

def diamondinsdover(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=269)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=269)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-dover.html', context)

def diamondinsmtlaurel(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=270)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=270)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-mt-laurel.html', context)

def diamondinsmtmelrosepark(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=271)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=271)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-melrose-park.html', context)

def fertilinstofnewjernewyork(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=272)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=272)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }


    return render(request, 'clinics/US/New-Jersey/fertility-institute-of-new-jersey-new-york.html', context)

def damienfertpartshrewsbury(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=273)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=273)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-shrewsbury.html', context)

def damienfertpartnewjerseycity(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=274)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=274)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-jersey-city.html', context)

def damienfertpartnewark(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=275)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=275)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-newark.html', context)

def islandrepsernewjer(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=276)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=276)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Jersey/island-reproductive-services-new-jersey.html', context)

# NEW MEXICO Views --------------------------------------------------------------------------------------------------------

def ferticentofnewmexico(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=277)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=277)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-Mexico/fertility-center-of-new-mexico.html', context)

# NEW YORK Views --------------------------------------------------------------------------------------------------------

def diamondinsgoshen(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=268)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=268)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/diamond-institute-goshen.html', context)

def cfnyc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=34)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=34)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/chelsea-fertility-nyc.html', context)

def ccrmnyfc(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=35)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=35)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/ccrm-new-york-fertility-clinic.html', context)

def sherinsforrepmednewyorkferclinic(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=278)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=278)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/sher-institutes-for-reproductive-medicine-new-york-fertility-clinic.html', context)

def greenwfertuck(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=279)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=279)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/greenwich-fertility-tuckahoe.html', context)

def rmactnorwalk(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=280)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=280)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/rmact-norwalk.html', context)

def extendfert(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=281)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=281)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/extend-fertility.html', context)

def geneferrepromedibaypark(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=282)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=282)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-bay-parkway.html', context)

def geneferrepromediparkslope(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=283)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=283)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-park-slope.html', context)

def geneferrepromediforesthills(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=284)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=284)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-forest-hills.html', context)

def geneferrepromedistatenisland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=285)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=285)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-staten-island.html', context)

def geneferrepromedilongisland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=286)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=286)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-long-island.html', context)

def buffinferivfas(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=287)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=287)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/buffalo-infertility-and-ivf-associates.html', context)

def hudsvallfert(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=288)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=288)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/hudson-valley-fertility.html', context)

def bostonivfalbany(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=289)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=289)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/boston-ivf–albany.html', context)

def bostonivfsyracusy(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=290)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=290)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/boston-ivf–syracuse.html', context)

def longislivfmelville(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=291)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=291)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-melville.html', context)

def longislivfeastpatchogue(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=292)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=292)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-east-patchogue.html', context)

def longislivfgardencity(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=293)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=293)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-garden-city.html', context)

def longislivfwestislip(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=294)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=294)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-west-islip.html', context)

def longislivflakesuccess(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=295)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=295)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-lake-success.html', context)

def longislivfstonybrooks(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=296)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=296)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-stony-brook.html', context)

def nyulangonerepspenewyorkmineola(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=297)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=297)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-mineola.html', context)

def nyulangonerepspenewyorkbrooklyn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=298)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=298)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-brooklyn.html', context)

def kindboynewyorkmedical(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=299)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=299)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/kindbody-of-new-york-medical.html', context)

def kofifertgroupstatenisland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=300)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=300)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-staten-island.html', context)

def kofifertgroupupperwestside(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=301)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=301)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-upper-west-side.html', context)

def kofifertgrouplowermanhattan(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=302)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=302)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-lower-manhattan.html', context)

def sgfmanhattan(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=303)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=303)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/sgf-manhattan.html', context)

def newaymedical(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=304)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=304)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/neway-medical.html', context)

def repromedassocnewyorkeastside(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=305)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=305)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-eastside.html', context)

def repromedassocnewyorkwestside(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=306)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=306)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westside.html', context)

def repromedassocnewyorkdowntown(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=307)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=307)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-downtown.html', context)

def repromedassocnewyorkbrooklyn(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=308)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=308)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-brooklyn.html', context)

def repromedassocnewyorkwestchester(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=309)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=309)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westchester.html', context)

def repromedassocnewyorkmountsinai(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=310)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=310)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-mount-sinai.html', context)

def islandreproservicesstatenisland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=311)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=311)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/island-reproductive-services-staten-island.html', context)

def cnyfercensyracuse(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=312)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=312)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-syracuse.html', context)

def cnyfercenalbany(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=313)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=313)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-albany.html', context)

def cnyfercenrochester(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=314)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=314)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-rochester.html', context)

def cnyfercenbuffalo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=315)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=315)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-buffalo.html', context)

# NORTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def northcarcenfrepmedic(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=316)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=316)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/north-carolina-center-for-reproductive-medicine.html', context)

def reproendoassoofcharlotte(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=317)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=317)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte.html', context)

def reproendoassoofcharlottelakenorman(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=318)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=318)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte-lake-norman.html', context)

def atlanticreprmedspec(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=319)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=319)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/atlantic-reproductive-medicine-specialists.html', context)

def carolinaconcerale(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=320)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=320)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-raleigh.html', context)

def carolinaconcewilmington(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=321)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=321)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-wilmington.html', context)

def carolinaconcehampstead(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=322)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=322)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-hampstead.html', context)

def carolinaconcegreenville(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=323)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=323)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-greenville.html', context)

def carolfertinstgreens(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=324)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=324)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-greensboro.html', context)

def carolfertinstwinstonsalem(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=325)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=325)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-winston-salem.html', context)

def carolfertinstcharlotte(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=326)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=326)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-charlotte.html', context)

def piedmoreproendogroupashe(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=327)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=327)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Carolina/piedmont-reproductive-endocrinology-group-asheville.html', context)

# NORTH DAKOTA Views --------------------------------------------------------------------------------------------------------

def midwecenforreprohealfargo(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=328)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=328)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-fargo.html', context)

def midwecenforreprohealminot(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=329)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=329)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-minot.html', context)

# OHIO Views --------------------------------------------------------------------------------------------------------

def ivfmichiganohio(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=330)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=330)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/ivf-michigan-ohio.html', context)

def northeasternohiofertcen(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=331)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=331)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/northeastern-ohio-fertility-center.html', context)

def reprogyninferakron(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=332)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=332)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-akron.html', context)

def reprogyninfercolumbus(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=333)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=333)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-columbus.html', context)

def reprogyninfercleveland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=334)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=334)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-cleveland.html', context)

def reprogyninferyoungstown(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=335)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=335)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-youngstown.html', context)

def reprogyninfercanton(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=336)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=336)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-canton.html', context)

def springcreekfertility(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=337)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=337)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/springcreek-fertility.html', context)

def instituteforhealthcincinnati(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=338)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=338)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-cincinnati.html', context)

def instituteforhealthwestche(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=339)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=339)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-west-chester.html', context)

def ohioreproductivemedicine(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=340)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=340)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/ohio-reproductive-medicine.html', context)

def fertilitywellnessinstohio(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=341)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=341)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Ohio/fertility-wellness-institute-of-ohio.html', context)

# OKLAHOMA Views --------------------------------------------------------------------------------------------------------

def ouphysiciansrepromedicine(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=342)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=342)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Oklahoma/ou-physicians-reproductive-medicine.html', context)

def tulsafertcenter(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=343)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=343)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Oklahoma/tulsa-fertility-center.html', context)

# OREGON Views --------------------------------------------------------------------------------------------------------

def ormfertilityclidownportland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=344)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=344)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-downtown-portland.html', context)

def ormfertilitycliwestsideportland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=345)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=345)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-westside-portland.html', context)

def ormfertilityclisouthportland(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=346)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=346)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-southside-portland.html', context)

# PENNSYLVANIA Views --------------------------------------------------------------------------------------------------------

def sincerarepromedabington(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=347)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=347)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-abington.html', context)

def sincerarepromedbethlehem(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=348)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=348)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-bethlehem.html', context)

def sincerarepromedfortwashington(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=349)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=349)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-fort-washington.html', context)

def sincerarepromedkingofprussia(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=350)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=350)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-king-of-prussia.html', context)

def sincerarepromedlancaster(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=351)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=351)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lancaster.html', context)

def sincerarepromedlanghorne(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=352)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=352)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-langhorne.html', context)

def sincerarepromedlansdale(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=353)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=353)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lansdale.html', context)

def sincerarepromedwestchester(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=354)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=354)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-west-chester.html', context)

def rmanetwork(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=355)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=355)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/rma-network-allentown.html', context)

def familyfertilitycenterbethlehem(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=356)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=356)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-bethlehem.html', context)

def familyfertilitycenterclarkssummit(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=357)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=357)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-clarks-summit.html', context)

def mainlinefertilityrepromedicinebrynmawr(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=358)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=358)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-bryn-mawr.html', context)

def mainlinefertilityrepromedicinepaoli(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=359)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=359)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-paoli.html', context)

def mainlinefertilityrepromedicinephiladelphia(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=360)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=360)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-philadelphia.html', context)

def mainlinefertilityrepromedicinewestchester(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=361)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=361)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-west-chester.html', context)

def mainlinefertilityrepromedicinehavertown(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=362)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=362)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-havertown.html', context)

def mainlinefertilityrepromedicinereading(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=363)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=363)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-reading.html', context)

def shadygrovefertilityphiladelphia(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=364)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=364)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-philadelphia.html', context)

def shadygrovefertilitychesterbrook(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listing = BasicClinic.objects.get(pk=365)

    package = Packages.objects.all()
    package = package.filter(packageClinic__id=365)

    context = {
        'usergroup': usergroup,
        'listing': listing,
        'package': package,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-chesterbrook.html', context)

def shadygrovefertilitymechanicsburg(request):
    listing = BasicClinic.objects.get(pk=366)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-mechanicsburg.html', context)

def shadygrovefertilitylancaster(request):
    listing = BasicClinic.objects.get(pk=367)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-lancaster.html', context)

def shadygrovefertilitywarrington(request):
    listing = BasicClinic.objects.get(pk=368)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-warrington.html', context)

# PUERTO RICO Views --------------------------------------------------------------------------------------------------------

def puertoricofertilitycenter(request):
    listing = BasicClinic.objects.get(pk=369)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Puerto-Rico/puerto-rico-fertility-center.html', context)

# SOUTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def piedmontreproendogroupgreenville(request):
    listing = BasicClinic.objects.get(pk=370)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-greenville.html', context)

def piedmontreproendogroupspartanburg(request):
    listing = BasicClinic.objects.get(pk=371)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-spartanburg.html', context)

def piedmontreproendogroupcolumbia(request):
    listing = BasicClinic.objects.get(pk=372)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/piedmont-reproductive-endocrinology-group-columbia.html', context)

def coastalfertspecimountpleasant(request):
    listing = BasicClinic.objects.get(pk=373)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-mount-pleasant.html', context)

def coastalfertspecinorthcharleston(request):
    listing = BasicClinic.objects.get(pk=374)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-north-charleston.html', context)

def coastalfertspecilexington(request):
    listing = BasicClinic.objects.get(pk=375)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-lexington.html', context)

def coastalfertspecimyrtlebeach(request):
    listing = BasicClinic.objects.get(pk=376)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/South-Carolina/coastal-fertility-specialists-myrtle-beach.html', context)

# TENNESSEE Views --------------------------------------------------------------------------------------------------------

def tenrepromedchattaivffertclin(request):
    listing = BasicClinic.objects.get(pk=377)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/tennessee-reproductive-medicine-chattanooga-ivf-fertility-clinic.html', context)

def myfertilitycenterchatt(request):
    listing = BasicClinic.objects.get(pk=378)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/my-fertility-center-chattanooga.html', context)

def myfertilitycenterknoxville(request):
    listing = BasicClinic.objects.get(pk=379)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/my-fertility-center-knoxville.html', context)

def tennesseefertiinstitute(request):
    listing = BasicClinic.objects.get(pk=380)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/tennessee-fertility-institute.html', context)

def fertiassoofmemphis(request):
    listing = BasicClinic.objects.get(pk=381)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/fertility-associates-of-memphis.html', context)

def nashvillefertnashville(request):
    listing = BasicClinic.objects.get(pk=382)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-nashville.html', context)

def nashvillefertmurfreesboro(request):
    listing = BasicClinic.objects.get(pk=383)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-murfreesboro.html', context)

def nashvillefertfranklin(request):
    listing = BasicClinic.objects.get(pk=384)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/nashville-fertility-franklin.html', context)

def centerforreprohealthnash(request):
    listing = BasicClinic.objects.get(pk=385)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Tennessee/the-center-for-reproductive-health-nashville.html', context)

# TEXAS Views --------------------------------------------------------------------------------------------------------

def sherinsforrepmedicinedallas(request):
    listing = BasicClinic.objects.get(pk=386)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/sher-institutes-for-reproductive-medicine-dallas.html', context)

def ccrmdallasfortworth(request):
    listing = BasicClinic.objects.get(pk=387)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ccrm-dallas-fort-worth.html', context)

def ccrmhoustonmaincenter(request):
    listing = BasicClinic.objects.get(pk=388)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-main-center.html', context)

def ccrmhoustonmedicalcenter(request):
    listing = BasicClinic.objects.get(pk=389)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-medical-center.html', context)

def ccrmhoustonsugarland(request):
    listing = BasicClinic.objects.get(pk=390)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ccrm-houston-sugar-land.html', context)

def aspirefertaustinfertilitycenter(request):
    listing = BasicClinic.objects.get(pk=391)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-austin-fertility-center.html', context)

def aspirefertbeecavefertcenter(request):
    listing = BasicClinic.objects.get(pk=392)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-bee-cave-fertility-center.html', context)

def aspirefertadison(request):
    listing = BasicClinic.objects.get(pk=393)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-adison.html', context)

def aspirefertclearlake(request):
    listing = BasicClinic.objects.get(pk=394)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-clear-lake-fertility-center.html', context)

def aspirefertfanninfece(request):
    listing = BasicClinic.objects.get(pk=395)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-fannin-fertility-center.html', context)

def aspirefertkatyfertce(request):
    listing = BasicClinic.objects.get(pk=396)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-katy-fertility-center.html', context)

def aspirefertmainstreet(request):
    listing = BasicClinic.objects.get(pk=397)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-main-street-fertility-center.html', context)

def aspirefertsugarlandfertcen(request):
    listing = BasicClinic.objects.get(pk=398)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-sugar-land-fertility-center.html', context)

def aspirefertwillowbrookfertcent(request):
    listing = BasicClinic.objects.get(pk=399)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-willowbrook-fertility-center.html', context)

def aspirefertsanantoniofertcenter(request):
    listing = BasicClinic.objects.get(pk=400)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-san-antonio-fertility-center.html', context)

def aspirefertsatellitecliniclocation(request):
    listing = BasicClinic.objects.get(pk=401)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/aspire-fertility-satellite-clinic-location.html', context)

def ivfmdcenterarlington(request):
    listing = BasicClinic.objects.get(pk=402)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ivfmd-center-arlington.html', context)

def ivfmdcenterirving(request):
    listing = BasicClinic.objects.get(pk=403)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ivfmd-center-irving.html', context)

def austinfertrepmedwestlake(request):
    listing = BasicClinic.objects.get(pk=404)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-westlake.html', context)

def austinfertrepmedsouthlocation(request):
    listing = BasicClinic.objects.get(pk=405)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-south-location.html', context)

def austinfertrepmedroundrock(request):
    listing = BasicClinic.objects.get(pk=406)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/austin-fertility-reproductive-medicine-round-rock.html', context)

def texasfertilitycentercentralaustin(request):
    listing = BasicClinic.objects.get(pk=407)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-central-austin.html', context)

def texasfertilitycenterroundrock(request):
    listing = BasicClinic.objects.get(pk=408)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-round-rock.html', context)

def texasfertilitycentersouthaustin(request):
    listing = BasicClinic.objects.get(pk=409)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-new-braunfels.html', context)

def texasfertilitycenternewbraunfels(request):
    listing = BasicClinic.objects.get(pk=410)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-south-austin.html', context)

def texasfertilitycentersanantonio(request):
    listing = BasicClinic.objects.get(pk=411)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-san-antonio.html', context)

def texasfertilitycentercorpuschristi(request):
    listing = BasicClinic.objects.get(pk=412)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-fertility-center-corpus-christi.html', context)

def centerforassistedreprobedford(request):
    listing = BasicClinic.objects.get(pk=413)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-bedford.html', context)

def centerforassistedreprofortworth(request):
    listing = BasicClinic.objects.get(pk=414)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-for-assisted-reproduction-fort-worth.html', context)

def dallasfortworthfertilityassociates(request):
    listing = BasicClinic.objects.get(pk=415)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-dallas-fertility-center.html', context)

def dallasfortworthfertilityassociatessouthlake(request):
    listing = BasicClinic.objects.get(pk=416)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-southlake-fertility-center.html', context)

def dallasfortworthfertilityassociatesmedicalcity(request):
    listing = BasicClinic.objects.get(pk=417)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-fort-worth-fertility-associates-medical-city-office.html', context)

def fertilitycenterofdallas(request):
    listing = BasicClinic.objects.get(pk=418)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-dallas.html', context)

def repromedfertilitycenterdallas(request):
    listing = BasicClinic.objects.get(pk=419)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-dallas.html', context)

def repromedfertilitycentergrapevine(request):
    listing = BasicClinic.objects.get(pk=420)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-grapevine.html', context)

def repromedfertilitycentermckinney(request):
    listing = BasicClinic.objects.get(pk=421)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney.html', context)

def repromedfertilitycenterrockwall(request):
    listing = BasicClinic.objects.get(pk=422)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-rockwall.html', context)

def repromedfertilitycentertyler(request):
    listing = BasicClinic.objects.get(pk=423)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-tyler.html', context)

def repromedfertilitycentermckinneysurgicalcenter(request):
    listing = BasicClinic.objects.get(pk=424)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/repromed-fertility-center-mckinney-surgical-center.html', context)

def sherfertilityclinicdallas(request):
    listing = BasicClinic.objects.get(pk=425)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/sher-fertility-clinic-dallas.html', context)

def texascenterforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=426)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/texas-center-for-reproductive-health.html', context)

def fortworthfertility(request):
    listing = BasicClinic.objects.get(pk=427)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fort-worth-fertility.html', context)

def dallasivffriscofertilityclinic(request):
    listing = BasicClinic.objects.get(pk=428)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-frisco-fertility-clinic.html', context)


def dallasivfdallasfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=429)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-dallas-fertility-clinic.html', context)

def dallasivfmckinleyfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=430)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-mckinney-fertility-clinic.html', context)

def dallasivfplanofertilityclinic(request):
    listing = BasicClinic.objects.get(pk=431)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-plano-fertility-clinic.html', context)

def dallasivftylerfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=432)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/dallas-ivf-tyler-fertility-clinic.html', context)

def fertilityspecialistsoftexasfrisco(request):
    listing = BasicClinic.objects.get(pk=433)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-frisco.html', context)

def fertilityspecialistsoftexasdallas(request):
    listing = BasicClinic.objects.get(pk=434)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-dallas.html', context)

def fertilityspecialistsoftexasrockwall(request):
    listing = BasicClinic.objects.get(pk=435)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-rockwall.html', context)

def fertilityspecialistsoftexassouthlake(request):
    listing = BasicClinic.objects.get(pk=436)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-specialists-of-texas-southlake.html', context)

def advancedfertilitycenteroftexasmemorialcity(request):
    listing = BasicClinic.objects.get(pk=437)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-memorial-city.html', context)

def advancedfertilitycenteroftexasspring(request):
    listing = BasicClinic.objects.get(pk=438)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-spring.html', context)

def advancedfertilitycenteroftexascollegestation(request):
    listing = BasicClinic.objects.get(pk=439)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/advanced-fertility-center-of-texas-college-station.html', context)

def centerofreproductivemedicinehouston(request):
    listing = BasicClinic.objects.get(pk=440)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-houston.html', context)

def centerofreproductivemedicinememorialcity(request):
    listing = BasicClinic.objects.get(pk=441)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-memorial-city.html', context)

def centerofreproductivemedicineclearlake(request):
    listing = BasicClinic.objects.get(pk=442)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-clear-lake.html', context)

def centerofreproductivemedicinebeaumont(request):
    listing = BasicClinic.objects.get(pk=443)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/center-of-reproductive-medicine-beaumont.html', context)

def houstonfertilityinstitutehoustonoffice(request):
    listing = BasicClinic.objects.get(pk=444)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-houston-office-ivf-lab.html', context)

def houstonfertilityinstitutemedicalcentermemorialhermann(request):
    listing = BasicClinic.objects.get(pk=445)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–memorial-hermann.html', context)

def houstonfertilityinstitutemedicalcenterwomanshospital(request):
    listing = BasicClinic.objects.get(pk=446)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-medical-center–womans-hospital.html', context)

def houstonfertilityinstitutemedicalcenterkatyoffice(request):
    listing = BasicClinic.objects.get(pk=447)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-katy-office.html', context)

def houstonfertilityinstitutemedicalcentersugarland(request):
    listing = BasicClinic.objects.get(pk=448)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-sugar-land-office.html', context)

def houstonfertilityinstitutemedicalcenterclearlakeoffice(request):
    listing = BasicClinic.objects.get(pk=449)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-clear-lake-office.html', context)

def houstonfertilityinstitutemedicalcentermemorialcityoffice(request):
    listing = BasicClinic.objects.get(pk=450)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-memorial-city-office.html', context)

def houstonfertilityinstitutemedicalcenterwillowbrookoffice(request):
    listing = BasicClinic.objects.get(pk=451)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-willowbrook-office.html', context)

def houstonfertilityinstitutemedicalcenterwoodlandsoffice(request):
    listing = BasicClinic.objects.get(pk=452)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-woodlands-office.html', context)

def houstonfertilityinstitutemedicalcenterbeaumontoffice(request):
    listing = BasicClinic.objects.get(pk=453)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-beaumont-office.html', context)

def houstonfertilityinstitutemedicalcentercypresstoffice(request):
    listing = BasicClinic.objects.get(pk=454)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-cypress-office.html', context)

def houstonfertilityinstitutemedicalcenterkingwoodoffice(request):
    listing = BasicClinic.objects.get(pk=455)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-kingwood-office.html', context)

def houstonfertilityinstitutemedicalcenterpearlandoffice(request):
    listing = BasicClinic.objects.get(pk=456)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/houston-fertility-institute-pearland-office.html', context)

def odessaivf(request):
    listing = BasicClinic.objects.get(pk=457)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/odessa-ivf.html', context)

def ivfplano(request):
    listing = BasicClinic.objects.get(pk=458)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/ivf-plano.html', context)

def fertilityceofsanantsanantoffice(request):
    listing = BasicClinic.objects.get(pk=459)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-san-antonio-office.html', context)

def fertilityceofsanantstoneoakoffice(request):
    listing = BasicClinic.objects.get(pk=460)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/fertility-center-of-san-antonio-stone-oak-office.html', context)

def hartivffertilityclinicwoodlands(request):
    listing = BasicClinic.objects.get(pk=461)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-woodlands.html', context)

def hartivffertilityclinickingwood(request):
    listing = BasicClinic.objects.get(pk=462)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Texas/hart-ivf-fertility-clinic-kingwood.html', context)

# UTAH Views --------------------------------------------------------------------------------------------------------

def utahfertilitycenterogden(request):
    listing = BasicClinic.objects.get(pk=463)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Utah/utah-fertility-center-ogden.html', context)

def conceptionsfertility(request):
    listing = BasicClinic.objects.get(pk=464)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Utah/conceptions-fertility.html', context)

def reproductivecarecenterclearfield(request):
    listing = BasicClinic.objects.get(pk=465)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-clearfield.html', context)

def reproductivecarecentersandy(request):
    listing = BasicClinic.objects.get(pk=466)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-sandy.html', context)

def reproductivecarecenterpleasantgrove(request):
    listing = BasicClinic.objects.get(pk=467)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Utah/reproductive-care-center-pleasant-grove.html', context)

# VERMONT Views --------------------------------------------------------------------------------------------------------

def northeasternreproductivemedicinecolchester(request):
    listing = BasicClinic.objects.get(pk=468)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Vermont/northeastern-reproductive-medicine-colchester.html', context)

# VIRGINIA Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociatesarlington(request):
    listing = BasicClinic.objects.get(pk=469)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/columbia-fertility-associates-arlington.html', context)

def ccrmmaincenter(request):
    listing = BasicClinic.objects.get(pk=470)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/ccrm-main-center.html', context)

def ccrmcolumbia(request):
    listing = BasicClinic.objects.get(pk=471)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/ccrm-columbia.html', context)

def washingtonfertilitycenterannandale(request):
    listing = BasicClinic.objects.get(pk=472)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-annandale.html', context)

def washingtonfertilitycenterfredericksburg(request):
    listing = BasicClinic.objects.get(pk=473)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-fredericksburg.html', context)

def washingtonfertilitycenterreston(request):
    listing = BasicClinic.objects.get(pk=474)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/washington-fertility-center-reston.html', context)

def dominionfertilityarlington(request):
    listing = BasicClinic.objects.get(pk=475)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/dominion-fertility-arlington.html', context)

def dominionfertilityfairfax(request):
    listing = BasicClinic.objects.get(pk=476)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/dominion-fertility-fairfax.html', context)

def reproductivemedicineandsurgerycenterofvirginiacharlottesville(request):
    listing = BasicClinic.objects.get(pk=477)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-charlottesville.html', context)

def reproductivemedicineandsurgerycenterofvirginialynchburg(request):
    listing = BasicClinic.objects.get(pk=478)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/reproductive-medicine-and-surgery-center-of-virginia-lynchburg.html', context)

def geneticsivfinstitute(request):
    listing = BasicClinic.objects.get(pk=479)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/genetics-ivf-institute.html', context)

def virginiacenterforreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=480)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/virginia-center-for-reproductive-medicine.html', context)

def thenewhopecenterforreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=481)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Virginia/the-new-hope-center-for-reproductive-medicine.html', context)

# WASHINGTON Views --------------------------------------------------------------------------------------------------------

def orgfertilityclinicbellevue(request):
    listing = BasicClinic.objects.get(pk=482)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/orm-fertility-clinic-bellevue.html', context)

def dominionfertilitywashington(request):
    listing = BasicClinic.objects.get(pk=483)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/dominion-fertility-washington.html', context)

def bellevuefertilityclinic(request):
    listing = BasicClinic.objects.get(pk=484)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/bellevue-fertility-clinic.html', context)

def pomafertility(request):
    listing = BasicClinic.objects.get(pk=485)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/poma-fertility.html', context)


def pacificnwfertilityseattle(request):
    listing = BasicClinic.objects.get(pk=486)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/pacific-nw-fertility-seattle.html', context)

def pacificnwfertilitybellevue(request):
    listing = BasicClinic.objects.get(pk=487)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/pacific-nw-fertility-bellevue.html', context)

def seattlereproductivemedicineseattle(request):
    listing = BasicClinic.objects.get(pk=488)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-seattle.html', context)

def seattlereproductivemedicinebellevue(request):
    listing = BasicClinic.objects.get(pk=489)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-bellevue.html', context)

def seattlereproductivemedicinetacoma(request):
    listing = BasicClinic.objects.get(pk=490)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-tacoma.html', context)

def seattlereproductivemedicinekirkland(request):
    listing = BasicClinic.objects.get(pk=491)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-kirkland.html', context)

def seattlereproductivemedicineeverett(request):
    listing = BasicClinic.objects.get(pk=492)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-everett.html', context)

def seattlereproductivemedicinespokane(request):
    listing = BasicClinic.objects.get(pk=493)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/seattle-reproductive-medicine-spokane.html', context)

def soundfertilitycare(request):
    listing = BasicClinic.objects.get(pk=494)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/sound-fertility-care.html', context)

def thecenterforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=495)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington/the-center-for-reproductive-health.html', context)

# WISCONSIN Views --------------------------------------------------------------------------------------------------------

def viosfertilityinstitutechicagomilwaukee(request):
    listing = BasicClinic.objects.get(pk=496)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-milwaukee.html', context)

def viosfertilityinstitutechicagolakecountry(request):
    listing = BasicClinic.objects.get(pk=497)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Wisconsin/vios-fertility-institute-chicago-lake-country.html', context)

def wisconsinfertilityinstitute(request):
    listing = BasicClinic.objects.get(pk=498)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Wisconsin/wisconsin-fertility-institute.html', context)

# WASHINGTON-DC Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociateswashingtondc(request):
    listing = BasicClinic.objects.get(pk=499)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington-Dc/columbia-fertility-associates-washington-dc.html', context)

def gwmedicalfacultyassociates(request):
    listing = BasicClinic.objects.get(pk=500)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Washington-Dc/gw-medical-faculty-associates.html', context)
