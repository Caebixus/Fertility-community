from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.utils import timezone

# Create your views here.
def wfi(request):
    listing = BasicClinic.objects.get(pk=1)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/western-fertility-institute.html', context)

def cifc(request):
    listing = BasicClinic.objects.get(pk=2)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/california-ivf-fertility-center.html', context)

def ncfmcr(request):
    listing = BasicClinic.objects.get(pk=3)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-roseville.html', context)

def ncfmcs(request):
    listing = BasicClinic.objects.get(pk=4)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/northern-california-fertility-medical-center-sacramento.html', context)

def liwla(request):
    listing = BasicClinic.objects.get(pk=5)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-west-los-angeles.html', context)

def lip(request):
    listing = BasicClinic.objects.get(pk=6)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-pasadena.html', context)

def lich(request):
    listing = BasicClinic.objects.get(pk=7)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/California/la-ivf-chino-hills.html', context)

def tcfrm(request):
    listing = BasicClinic.objects.get(pk=8)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Alabama/center-for-reproductive-medicine.html', context)

def af(request):
    listing = BasicClinic.objects.get(pk=9)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Alabama/alabama-fertility.html', context)

def tfc(request):
    listing = BasicClinic.objects.get(pk=10)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-scottsdale.html', context)

def tfg(request):
    listing = BasicClinic.objects.get(pk=11)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-glendale.html', context)

def tfm(request):
    listing = BasicClinic.objects.get(pk=12)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/troche-fertility-mesa.html', context)

def sfc(request):
    listing = BasicClinic.objects.get(pk=13)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/southwest-fertility-center.html', context)

def afcs(request):
    listing = BasicClinic.objects.get(pk=14)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-scottsdale.html', context)

def afcm(request):
    listing = BasicClinic.objects.get(pk=15)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/advanced-fertility-care-mesa.html', context)

def aafrhs(request):
    listing = BasicClinic.objects.get(pk=16)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-scottsdale.html', context)

def aafrhg(request):
    listing = BasicClinic.objects.get(pk=17)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-associates-for-reproductive-health-gilbert.html', context)

def bris(request):
    listing = BasicClinic.objects.get(pk=18)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-scottsdale.html', context)

def brig(request):
    listing = BasicClinic.objects.get(pk=19)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/bloom-reproductive-institute-gilbert.html', context)

def biacs(request):
    listing = BasicClinic.objects.get(pk=20)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-scottsdale.html', context)

def biacch(request):
    listing = BasicClinic.objects.get(pk=21)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-chandler.html', context)

def biacp(request):
    listing = BasicClinic.objects.get(pk=22)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-peoria.html', context)

def biacf(request):
    listing = BasicClinic.objects.get(pk=23)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/boston-ivf-arizona-center-flagstaff.html', context)

def ip(request):
    listing = BasicClinic.objects.get(pk=24)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/ivf-phoenix.html', context)

def ftc(request):
    listing = BasicClinic.objects.get(pk=25)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/fertility-treatment-center.html', context)

def arifc(request):
    listing = BasicClinic.objects.get(pk=26)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arizona/arizona-reproductive-institute-fertility-clinic.html', context)

def irmsco(request):
    listing = BasicClinic.objects.get(pk=27)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-clark-office.html', context)

def irmsewo(request):
    listing = BasicClinic.objects.get(pk=28)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-east-windsor-office.html', context)

def irmsho(request):
    listing = BasicClinic.objects.get(pk=29)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hackensack-office.html', context)

def irmshbo(request):
    listing = BasicClinic.objects.get(pk=30)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-hoboken-office.html', context)

def irmsnjo(request):
    listing = BasicClinic.objects.get(pk=31)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-new-jersey-office.html', context)

def irmslo(request):
    listing = BasicClinic.objects.get(pk=32)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-livingston-office.html', context)

def irmsobo(request):
    listing = BasicClinic.objects.get(pk=33)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/irms-old-bridge-office.html', context)

def cfnyc(request):
    listing = BasicClinic.objects.get(pk=34)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/chelsea-fertility-nyc.html', context)

def ccrmnyfc(request):
    listing = BasicClinic.objects.get(pk=35)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/ccrm-new-york-fertility-clinic.html', context)

def afg(request):
    listing = BasicClinic.objects.get(pk=37)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arkansas/arkansas-fertility-gynecology.html', context)

def ccrmcmclt(request):
    listing = BasicClinic.objects.get(pk=38)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-main-center-lone-tree.html', context)

def ccrmcdo(request):
    listing = BasicClinic.objects.get(pk=39)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-denver-office.html', context)

def ccrmclo(request):
    listing = BasicClinic.objects.get(pk=40)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/ccrm-colorado-louisville-office.html', context)

def ucarmd(request):
    listing = BasicClinic.objects.get(pk=41)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-denver.html', context)

def ucarmcos(request):
    listing = BasicClinic.objects.get(pk=42)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/uc-advanced-reproductive-medicine-co-springs.html', context)

def rmcrm(request):
    listing = BasicClinic.objects.get(pk=43)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Colorado/rocky-mountain-center-reproductive-medicine.html', context)

def carsf(request):
    listing = BasicClinic.objects.get(pk=44)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/cars-farmington.html', context)

def carsh(request):
    listing = BasicClinic.objects.get(pk=45)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/cars-hartford.html', context)

def carsnl(request):
    listing = BasicClinic.objects.get(pk=46)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/cars-new-london.html', context)

def carsb(request):
    listing = BasicClinic.objects.get(pk=47)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/cars-branford.html', context)

def gfg(request):
    listing = BasicClinic.objects.get(pk=48)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-greenwich.html', context)

def gfs(request):
    listing = BasicClinic.objects.get(pk=49)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/greenwich-fertility-stamford.html', context)

def rmactn(request):
    listing = BasicClinic.objects.get(pk=50)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/rmact-norwalk.html', context)

def rmacts(request):
    listing = BasicClinic.objects.get(pk=51)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/rmact-stamford.html', context)

def rmactd(request):
    listing = BasicClinic.objects.get(pk=52)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/rmact-danbury.html', context)

def rmactt(request):
    listing = BasicClinic.objects.get(pk=53)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/rmact-trumbull.html', context)

def paft(request):
    listing = BasicClinic.objects.get(pk=54)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-trumbull.html', context)

def paff(request):
    listing = BasicClinic.objects.get(pk=55)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-fairfield.html', context)

def pafn(request):
    listing = BasicClinic.objects.get(pk=56)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Connecticut/park-avenue-fertility-norwalk.html', context)

def dirmn(request):
    listing = BasicClinic.objects.get(pk=57)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Delaware/dirm-newark.html', context)

def dirmm(request):
    listing = BasicClinic.objects.get(pk=58)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Delaware/dirm-milford.html', context)

def radfn(request):
    listing = BasicClinic.objects.get(pk=59)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Delaware/radfertility-newark.html', context)

def radfw(request):
    listing = BasicClinic.objects.get(pk=60)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Delaware/radfertility-wilmington.html', context)

def radfd(request):
    listing = BasicClinic.objects.get(pk=61)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Delaware/radfertility-dover.html', context)

def bocaf(request):
    listing = BasicClinic.objects.get(pk=62)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/boca-fertility.html', context)

def pbfcbr(request):
    listing = BasicClinic.objects.get(pk=63)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/pbfc-boca-raton.html', context)

def pbfcpbg(request):
    listing = BasicClinic.objects.get(pk=64)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/pbfc-palm-beach-gardens.html', context)

def ffico(request):
    listing = BasicClinic.objects.get(pk=65)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ffi-clearwater-office.html', context)

def ffito(request):
    listing = BasicClinic.objects.get(pk=66)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ffi-tampa-office.html', context)

def cfcg(request):
    listing = BasicClinic.objects.get(pk=67)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-coral-gables.html', context)

def cfm(request):
    listing = BasicClinic.objects.get(pk=68)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/conceptions-florida-miramar.html', context)

def jcrmj(request):
    listing = BasicClinic.objects.get(pk=69)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/jcrm-jacksonville.html', context)

def jcrmg(request):
    listing = BasicClinic.objects.get(pk=70)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/jcrm-gainesville.html', context)

def jcrmpc(request):
    listing = BasicClinic.objects.get(pk=71)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/jcrm-panama-city.html', context)

def jcrmo(request):
    listing = BasicClinic.objects.get(pk=72)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/jcrm-orlando.html', context)

def rmanlm(request):
    listing = BasicClinic.objects.get(pk=73)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rma-network-lake-mary.html', context)

def ivffwfc(request):
    listing = BasicClinic.objects.get(pk=74)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-wellington-fertility-center.html', context)

def ivffcgfc(request):
    listing = BasicClinic.objects.get(pk=75)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-coral-gables-fertility-center.html', context)

def ivfppfc(request):
    listing = BasicClinic.objects.get(pk=76)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-pembroke-pines-fertility-center.html', context)

def ivffmfc(request):
    listing = BasicClinic.objects.get(pk=77)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-margate-fertility-center.html', context)

def ivfbrfc(request):
    listing = BasicClinic.objects.get(pk=78)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-boca-raton-fertility-center.html', context)

def ivffjpbgfc(request):
    listing = BasicClinic.objects.get(pk=79)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-jupiter-palm-beach-gardens-fertility-center.html', context)

def ivffplfc(request):
    listing = BasicClinic.objects.get(pk=80)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-florida-port-lucie-fertility-clinic.html', context)

def vfc(request):
    listing = BasicClinic.objects.get(pk=81)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/viera-fertility-center.html', context)

def fivfcm(request):
    listing = BasicClinic.objects.get(pk=82)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami.html', context)

def fivfcmb(request):
    listing = BasicClinic.objects.get(pk=83)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/fivfcm-miami-beach.html', context)

def fg(request):
    listing = BasicClinic.objects.get(pk=84)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/fertility-genetics.html', context)

def ivfmdm(request):
    listing = BasicClinic.objects.get(pk=85)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-miami.html', context)

def ivfmdcc(request):
    listing = BasicClinic.objects.get(pk=86)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-cooper-city', context)

def ivfmdbr(request):
    listing = BasicClinic.objects.get(pk=87)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-boca-raton', context)

def ivfmdj(request):
    listing = BasicClinic.objects.get(pk=88)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-jupiter', context)

def ivfmdn(request):
    listing = BasicClinic.objects.get(pk=89)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-naples', context)

def ivfmdv(request):
    listing = BasicClinic.objects.get(pk=90)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-viera', context)

def sgftw(request):
    listing = BasicClinic.objects.get(pk=91)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-tampa-westshore', context)

def sgfb(request):
    listing = BasicClinic.objects.get(pk=92)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-brandon', context)

def sgfwc(request):
    listing = BasicClinic.objects.get(pk=93)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-wesley-chapel', context)

def rmgnto(request):
    listing = BasicClinic.objects.get(pk=94)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-north-tampa-office', context)

def rmgsto(request):
    listing = BasicClinic.objects.get(pk=95)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-south-tampa-office', context)

def rmgco(request):
    listing = BasicClinic.objects.get(pk=96)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-clearwater-office', context)

def rmgbo(request):
    listing = BasicClinic.objects.get(pk=97)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-brandon-office', context)

def fifrst(request):
    listing = BasicClinic.objects.get(pk=98)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/florida-institute-for-reproductive-sciences-technologies', context)

def arswp(request):
    listing = BasicClinic.objects.get(pk=99)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/advanced-reproductive-specialists-winter-park', context)

def ivfowp(request):
    listing = BasicClinic.objects.get(pk=100)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-orlando-winter-park', context)

def fcare(request):
    listing = BasicClinic.objects.get(pk=101)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/fertility-center-assisted-reproduction-endocrinology', context)
