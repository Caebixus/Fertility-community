from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
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

# ALABAMA Views --------------------------------------------------------------------------------------------------------

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

# ARIZONA Views --------------------------------------------------------------------------------------------------------

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

# ARKANSAS Views --------------------------------------------------------------------------------------------------------

def afg(request):
    listing = BasicClinic.objects.get(pk=37)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Arkansas/arkansas-fertility-gynecology.html', context)

# COLORADO Views --------------------------------------------------------------------------------------------------------

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

# CONNECTICUT Views --------------------------------------------------------------------------------------------------------

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

# DELAWARE Views --------------------------------------------------------------------------------------------------------

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

# FLORIDA Views --------------------------------------------------------------------------------------------------------

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

    return render(request, 'clinics/US/Florida/ivfmd-cooper-city.html', context)

def ivfmdbr(request):
    listing = BasicClinic.objects.get(pk=87)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-boca-raton.html', context)

def ivfmdj(request):
    listing = BasicClinic.objects.get(pk=88)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-jupiter.html', context)

def ivfmdn(request):
    listing = BasicClinic.objects.get(pk=89)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-naples.html', context)

def ivfmdv(request):
    listing = BasicClinic.objects.get(pk=90)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivfmd-viera.html', context)

def sgftw(request):
    listing = BasicClinic.objects.get(pk=91)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-tampa-westshore.html', context)

def sgfb(request):
    listing = BasicClinic.objects.get(pk=92)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-brandon.html', context)

def sgfwc(request):
    listing = BasicClinic.objects.get(pk=93)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/sgf-wesley-chapel.html', context)

def rmgnto(request):
    listing = BasicClinic.objects.get(pk=94)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-north-tampa-office.html', context)

def rmgsto(request):
    listing = BasicClinic.objects.get(pk=95)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-south-tampa-office.html', context)

def rmgco(request):
    listing = BasicClinic.objects.get(pk=96)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-clearwater-office.html', context)

def rmgbo(request):
    listing = BasicClinic.objects.get(pk=97)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/rmg-brandon-office.html', context)

def fifrst(request):
    listing = BasicClinic.objects.get(pk=98)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/florida-institute-for-reproductive-sciences-technologies.html', context)

def arswp(request):
    listing = BasicClinic.objects.get(pk=99)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/advanced-reproductive-specialists-winter-park.html', context)

def ivfowp(request):
    listing = BasicClinic.objects.get(pk=100)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/ivf-orlando-winter-park.html', context)

def fcare(request):
    listing = BasicClinic.objects.get(pk=101)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Florida/fertility-center-assisted-reproduction-endocrinology.html', context)

# GEORGIA Views --------------------------------------------------------------------------------------------------------

def afa(request):
    listing = BasicClinic.objects.get(pk=102)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/aspire-fertility-atlanta.html', context)

def acrmap(request):
    listing = BasicClinic.objects.get(pk=103)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-perimetr.html', context)

def acrmab(request):
    listing = BasicClinic.objects.get(pk=104)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/acrm-atlanta-buckhead.html', context)

def acrmjc(request):
    listing = BasicClinic.objects.get(pk=105)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/acrm-johns-creek.html', context)

def acrmm(request):
    listing = BasicClinic.objects.get(pk=106)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/acrm-marietta.html', context)

def mfs(request):
    listing = BasicClinic.objects.get(pk=107)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/massey-fertility-services.html', context)

def sfi(request):
    listing = BasicClinic.objects.get(pk=108)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/servy-fertility-institute.html', context)

def sgfan(request):
    listing = BasicClinic.objects.get(pk=109)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/sgf-atlanta-northside.html', context)

def sgfa(request):
    listing = BasicClinic.objects.get(pk=110)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/sgf-alpharetta.html', context)

def sgfbp(request):
    listing = BasicClinic.objects.get(pk=111)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/sgf-buckhead-piedmont.html', context)

def sgfm(request):
    listing = BasicClinic.objects.get(pk=112)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/sgf-marietta.html', context)

def rbamo(request):
    listing = BasicClinic.objects.get(pk=113)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–main-office.html', context)

def rbam(request):
    listing = BasicClinic.objects.get(pk=114)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–marietta.html', context)

def rbaf(request):
    listing = BasicClinic.objects.get(pk=115)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–fayetteville.html', context)

def rbal(request):
    listing = BasicClinic.objects.get(pk=116)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–lawrenceville.html', context)

def rbac(request):
    listing = BasicClinic.objects.get(pk=117)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cumming.html', context)

def rbaph(request):
    listing = BasicClinic.objects.get(pk=118)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–piedmont-hospital.html', context)

def rbacar(request):
    listing = BasicClinic.objects.get(pk=119)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Georgia/reproductive-biology-associates–cartersville.html', context)

# HAWAII Views --------------------------------------------------------------------------------------------------------

def arch(request):
    listing = BasicClinic.objects.get(pk=120)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Hawaii/advanced-reproductive-center-hawaii.html', context)

def armghh(request):
    listing = BasicClinic.objects.get(pk=121)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Hawaii/armgh-honolulu.html', context)

def armghk(request):
    listing = BasicClinic.objects.get(pk=122)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Hawaii/armgh-kailua.html', context)

def pivfi(request):
    listing = BasicClinic.objects.get(pk=123)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Hawaii/pacific-in-vitro-fertilization-institute.html', context)

# IOWA Views --------------------------------------------------------------------------------------------------------

def mif(request):
    listing = BasicClinic.objects.get(pk=124)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Iowa/mid-iowa-fertility.html', context)

# IDAHO Views --------------------------------------------------------------------------------------------------------

def icrm(request):
    listing = BasicClinic.objects.get(pk=125)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Idaho/idaho-center-reproductive-medicine.html', context)

# ILLINOIS Views --------------------------------------------------------------------------------------------------------

def crc(request):
    listing = BasicClinic.objects.get(pk=126)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/center-reproductive-care.html', context)

def fcibgc(request):
    listing = BasicClinic.objects.get(pk=127)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-buffalo-grove-clinic.html', context)

def fcicnc(request):
    listing = BasicClinic.objects.get(pk=128)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-chicago-north-clinic.html', context)

def fcigc(request):
    listing = BasicClinic.objects.get(pk=129)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-glenview-clinic.html', context)

def fcihpc(request):
    listing = BasicClinic.objects.get(pk=130)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-highland-park-clinic.html', context)

def fcihc(request):
    listing = BasicClinic.objects.get(pk=131)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-hinsdale-clinic.html', context)

def fcihec(request):
    listing = BasicClinic.objects.get(pk=132)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-hoffman-estates-clinic.html', context)

def fcilc(request):
    listing = BasicClinic.objects.get(pk=133)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-lindenhurst-clinic.html', context)

def fcitpc(request):
    listing = BasicClinic.objects.get(pk=134)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-tinley-park-clinic.html', context)

def fciwc(request):
    listing = BasicClinic.objects.get(pk=135)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/fci-warrenville-clinic.html', context)

def ihrc(request):
    listing = BasicClinic.objects.get(pk=136)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/ihr-chicago.html', context)

def ihro(request):
    listing = BasicClinic.objects.get(pk=137)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/ihr-oakbrook.html', context)

def vfica(request):
    listing = BasicClinic.objects.get(pk=138)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-aurora.html', context)

def vficwp(request):
    listing = BasicClinic.objects.get(pk=139)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-wicker-park.html', context)

def vficwlil(request):
    listing = BasicClinic.objects.get(pk=140)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-west-loop-ivf-lab.html', context)

def vficg(request):
    listing = BasicClinic.objects.get(pk=141)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-glenview.html', context)

def vfiche(request):
    listing = BasicClinic.objects.get(pk=142)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/vios-fertility-institute-chicago-hoffman-estates.html', context)

def dfis(request):
    listing = BasicClinic.objects.get(pk=143)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/davies-fertility-ivf-specialists.html', context)

def hcr(request):
    listing = BasicClinic.objects.get(pk=144)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/hinsdale-center-reproduction.html', context)

def ifsah(request):
    listing = BasicClinic.objects.get(pk=145)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-arlington-heights.html', context)

def ifscl(request):
    listing = BasicClinic.objects.get(pk=146)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-crystal-lake.html', context)

def ifshe(request):
    listing = BasicClinic.objects.get(pk=147)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-hoffman-estates.html', context)

def ifsn(request):
    listing = BasicClinic.objects.get(pk=148)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/invia-fertility-specialists-northbrook.html', context)

def ivf1(request):
    listing = BasicClinic.objects.get(pk=149)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/ivf1.html', context)

def rmib(request):
    listing = BasicClinic.objects.get(pk=150)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-bloomingdale.html', context)

def rmic(request):
    listing = BasicClinic.objects.get(pk=151)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-chicago.html', context)

def rmiel(request):
    listing = BasicClinic.objects.get(pk=152)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-elmhurst.html', context)

def rmiev(request):
    listing = BasicClinic.objects.get(pk=153)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-evanston.html', context)

def rminb(request):
    listing = BasicClinic.objects.get(pk=154)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-northbrook.html', context)

def rmiob(request):
    listing = BasicClinic.objects.get(pk=155)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-brook.html', context)

def rmiol(request):
    listing = BasicClinic.objects.get(pk=156)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/rmi-oak-lawn.html', context)

def civfops(request):
    listing = BasicClinic.objects.get(pk=157)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-orland-park–southwest.html', context)

def civfscn(request):
    listing = BasicClinic.objects.get(pk=158)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-stcharles–northwest.html', context)

def civfnw(request):
    listing = BasicClinic.objects.get(pk=159)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Illinois/chicago-ivf-naperville–west.html', context)

# INDIANA Views --------------------------------------------------------------------------------------------------------

def ihrval(request):
    listing = BasicClinic.objects.get(pk=161)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/ihr-valparaiso.html', context)

def mfcar(request):
    listing = BasicClinic.objects.get(pk=162)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-carmel.html', context)

def mffortwayne(request):
    listing = BasicClinic.objects.get(pk=165)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/midwest-fertility-fort-wayne.html', context)

def civfval(request):
    listing = BasicClinic.objects.get(pk=163)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-valparaiso.html', context)

def civfmun(request):
    listing = BasicClinic.objects.get(pk=164)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/chicago-ivf-munster.html', context)

def prhmun(request):
    listing = BasicClinic.objects.get(pk=166)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/partners-reproductive-health-munster.html', context)

def fbeg(request):
    listing = BasicClinic.objects.get(pk=167)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/family-beginnings.html', context)

def ifinst(request):
    listing = BasicClinic.objects.get(pk=168)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/indiana-fertility-institute.html', context)

def rcimo(request):
    listing = BasicClinic.objects.get(pk=169)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-main-office.html', context)

def rcith(request):
    listing = BasicClinic.objects.get(pk=170)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-terre-haute.html', context)

def rcilaf(request):
    listing = BasicClinic.objects.get(pk=171)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-lafayette.html', context)

def rcibmc(request):
    listing = BasicClinic.objects.get(pk=172)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-mc.html', context)

def rcibws(request):
    listing = BasicClinic.objects.get(pk=173)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Indiana/reproductive-care-indiana-bloomington-ws.html', context)

# KANSAS Views --------------------------------------------------------------------------------------------------------

def midrepc(request):
    listing = BasicClinic.objects.get(pk=174)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Kansas/midwest-reproductive-center.html', context)

# KENTUCKY Views --------------------------------------------------------------------------------------------------------

def ferendas(request):
    listing = BasicClinic.objects.get(pk=175)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Kentucky/fertility-endocrine-associates.html', context)

# LOUISIANA Views --------------------------------------------------------------------------------------------------------

def feanla(request):
    listing = BasicClinic.objects.get(pk=176)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lafayette.html', context)

def feanbaro(request):
    listing = BasicClinic.objects.get(pk=177)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-baton-rouge.html', context)

def feanco(request):
    listing = BasicClinic.objects.get(pk=178)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-covington.html', context)

def feanlach(request):
    listing = BasicClinic.objects.get(pk=179)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fertility-answers-lake-charles.html', context)

def fiman(request):
    listing = BasicClinic.objects.get(pk=180)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fi-mandeville.html', context)

def fimet(request):
    listing = BasicClinic.objects.get(pk=181)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fi-metairie.html', context)

def fibaro(request):
    listing = BasicClinic.objects.get(pk=182)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/fi-baton-rouge.html', context)

def audfer(request):
    listing = BasicClinic.objects.get(pk=183)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/audubon-fertility.html', context)

def arkferrepmed(request):
    listing = BasicClinic.objects.get(pk=184)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Louisiana/arklatex-fertility-reproductive-medicine.html', context)

# MAINE Views --------------------------------------------------------------------------------------------------------

def fcnebc(request):
    listing = BasicClinic.objects.get(pk=186)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Maine/fcne-bangor-center.html', context)

def bivfbfc(request):
    listing = BasicClinic.objects.get(pk=187)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-bangor-fertility-center.html', context)

def bivfpfc(request):
    listing = BasicClinic.objects.get(pk=188)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Maine/boston-ivf-portland-fertility-center.html', context)

# MARYLAND Views --------------------------------------------------------------------------------------------------------

# MASSACHUSETTS Views --------------------------------------------------------------------------------------------------------

def masghfc(request):
    listing = BasicClinic.objects.get(pk=185)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/massachusetts-general-hospital-fertility-center.html', context)

def ccrmbmc(request):
    listing = BasicClinic.objects.get(pk=189)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-boston-main-center.html', context)

def ccrmmo(request):
    listing = BasicClinic.objects.get(pk=190)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-metrowest-office.html', context)

def ccrmsso(request):
    listing = BasicClinic.objects.get(pk=191)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/ccrm-south-shore-office.html', context)

def bivfmfc(request):
    listing = BasicClinic.objects.get(pk=192)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-tufts-medical-fertility-center.html', context)

def bivfdbfc(request):
    listing = BasicClinic.objects.get(pk=193)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-downtown-boston-fertility-center.html', context)

def bivflfc(request):
    listing = BasicClinic.objects.get(pk=194)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-lexington-fertility-center.html', context)

def bivfqfc(request):
    listing = BasicClinic.objects.get(pk=195)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-quincy-fertility-center.html', context)

def bivfwfc(request):
    listing = BasicClinic.objects.get(pk=196)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-waltham-fertility-center.html', context)

def bivfsfc(request):
    listing = BasicClinic.objects.get(pk=197)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/boston-ivf-stoneham-fertility-center.html', context)

def fcnelc(request):
    listing = BasicClinic.objects.get(pk=198)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-leominster-center.html', context)

def fcnerc(request):
    listing = BasicClinic.objects.get(pk=199)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-reading-center.html', context)

def fcnedc(request):
    listing = BasicClinic.objects.get(pk=200)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-danvers-center.html', context)

def fcnebce(request):
    listing = BasicClinic.objects.get(pk=201)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-braintree-center.html', context)

def fcnebcen(request):
    listing = BasicClinic.objects.get(pk=202)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Massachusetts/fertility-centers-new-england-boston-center.html', context)

# MICHIGAN Views --------------------------------------------------------------------------------------------------------

def ivfmfcaafc(request):
    listing = BasicClinic.objects.get(pk=203)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-ann-arbor-fertility-center.html', context)

def ivfmfcbhfc(request):
    listing = BasicClinic.objects.get(pk=204)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-bloomfield-hills-fertility-center.html', context)

def ivfmfcchebfc(request):
    listing = BasicClinic.objects.get(pk=205)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-cheboygan-fertility-center.html', context)

def ivfmfcdfc(request):
    listing = BasicClinic.objects.get(pk=206)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-dearborn-fertility-center.html', context)

def ivfmfcelfc(request):
    listing = BasicClinic.objects.get(pk=207)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-east-lansing-fertility-center.html', context)

def ivfmfcmfc(request):
    listing = BasicClinic.objects.get(pk=208)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-macomb-fertility-center.html', context)

def ivfmfcpfc(request):
    listing = BasicClinic.objects.get(pk=209)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-petoskey-fertility-center.html', context)

def ivfmfcsfc(request):
    listing = BasicClinic.objects.get(pk=210)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-saginaw-fertility-center.html', context)

def ivfmfctfc(request):
    listing = BasicClinic.objects.get(pk=211)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-fertility-center-toledo-fertility-center.html', context)

def gcffb(request):
    listing = BasicClinic.objects.get(pk=212)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-brighton.html', context)

def ggcffl(request):
    listing = BasicClinic.objects.get(pk=213)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-lansing.html', context)

def ggcffaa(request):
    listing = BasicClinic.objects.get(pk=214)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/gago-center-for-fertility-ann-arbor.html', context)

def tfcgr(request):
    listing = BasicClinic.objects.get(pk=215)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-grand-rapids.html', context)

def tfcm(request):
    listing = BasicClinic.objects.get(pk=216)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-mason.html', context)

def tfck(request):
    listing = BasicClinic.objects.get(pk=217)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-kalamazoo.html', context)

def tfctc(request):
    listing = BasicClinic.objects.get(pk=218)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/the-fertility-center-traverse-city.html', context)

def ivfmrh(request):
    listing = BasicClinic.objects.get(pk=219)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-rochester-hills.html', context)

def ivfmf(request):
    listing = BasicClinic.objects.get(pk=220)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-flint.html', context)

def ivfmd(request):
    listing = BasicClinic.objects.get(pk=221)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/ivf-michigan-dearborn.html', context)

def rmaom(request):
    listing = BasicClinic.objects.get(pk=222)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Michigan/reproductive-medicine-associates-of-michigan.html', context)

# MINNESOTA Views --------------------------------------------------------------------------------------------------------

def cccrmmin(request):
    listing = BasicClinic.objects.get(pk=223)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/ccrm-minneapolis.html', context)

def midcfrh(request):
    listing = BasicClinic.objects.get(pk=224)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/midwest-center-for-reproductive-health.html', context)

def cenfrmmin(request):
    listing = BasicClinic.objects.get(pk=225)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-minneapolis.html', context)

def cenfrmstp(request):
    listing = BasicClinic.objects.get(pk=226)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-paul.html', context)

def cenfrmwesog(request):
    listing = BasicClinic.objects.get(pk=227)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-western-ob-gyn.html', context)

def cenfremstluobgyna(request):
    listing = BasicClinic.objects.get(pk=228)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/center-for-reproductive-medicine-st-lukes-obstetrics-gynecology-associates.html', context)

def repmeinaswoo(request):
    listing = BasicClinic.objects.get(pk=229)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-woodbury.html', context)

def repmeinasedi(request):
    listing = BasicClinic.objects.get(pk=230)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Minnesota/reproductive-medicine-infertility-associates-edina.html', context)

# MISSISSIPPI Views --------------------------------------------------------------------------------------------------------

def cenfrmmfc(request):
    listing = BasicClinic.objects.get(pk=231)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Mississippi/center-for-reproductive-medicine-mississippi-fertility-clinic.html', context)

def missrepmed(request):
    listing = BasicClinic.objects.get(pk=232)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Mississippi/mississippi-reproductive-medicine.html', context)

# MISSOURI Views --------------------------------------------------------------------------------------------------------

def vfichisl(request):
    listing = BasicClinic.objects.get(pk=233)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-saint-louis.html', context)

def vfichiofa(request):
    listing = BasicClinic.objects.get(pk=234)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/vios-fertility-institute-chicago-ofallon.html', context)

def infeceofstlo(request):
    listing = BasicClinic.objects.get(pk=235)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/infertility-center-of-st-louis.html', context)

def mcrmferstlo(request):
    listing = BasicClinic.objects.get(pk=236)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-st-louis.html', context)

def mcrmferspring(request):
    listing = BasicClinic.objects.get(pk=237)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/mcrm-fertility-springfield.html', context)

def missofer(request):
    listing = BasicClinic.objects.get(pk=238)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/missouri-fertility.html', context)

def shiforrepmestlofecl(request):
    listing = BasicClinic.objects.get(pk=239)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Missouri/sher-institutes-for-reproductive-medicine-st-louis-fertility-clinic.html', context)

# NEBRASKA Views --------------------------------------------------------------------------------------------------------

def hearceforrepme(request):
    listing = BasicClinic.objects.get(pk=240)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Nebraska/heartland-center-for-reproductive-medicine.html', context)

# NEVADA Views --------------------------------------------------------------------------------------------------------

def greevalferpartners(request):
    listing = BasicClinic.objects.get(pk=241)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Nevada/green-valley-fertility-partners.html', context)

def theferceoflasvegas(request):
    listing = BasicClinic.objects.get(pk=242)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Nevada/the-fertility-center-of-las-vegas.html', context)

def sherinsfrepmedlasvegfecl(request):
    listing = BasicClinic.objects.get(pk=243)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Nevada/sher-institutes-for-reproductive-medicine-las-vegas-fertility-clinic.html', context)

def redrofercen(request):
    listing = BasicClinic.objects.get(pk=244)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Nevada/red-rock-fertility-center.html', context)

# NEW JERSEY Views --------------------------------------------------------------------------------------------------------

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

    return render(request, 'clinics/US/New-Jersey/irms-jersey-city-office.html', context)

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

def Cenfoarepmedicinefer(request):
    listing = BasicClinic.objects.get(pk=245)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/center-for-advanced-reproductive-medicine-fertility.html', context)

def rmanetbasrid(request):
    listing = BasicClinic.objects.get(pk=246)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-basking-ridge.html', context)

def rmaneteaton(request):
    listing = BasicClinic.objects.get(pk=247)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-eatontown.html', context)

def rmanetenglewood(request):
    listing = BasicClinic.objects.get(pk=248)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-englewood.html', context)

def rmanetfreehold(request):
    listing = BasicClinic.objects.get(pk=249)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-freehold.html', context)

def rmanetmarlton(request):
    listing = BasicClinic.objects.get(pk=250)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-marlton.html', context)

def rmanetmorristown(request):
    listing = BasicClinic.objects.get(pk=251)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-morristown.html', context)

def rmanetprinceston(request):
    listing = BasicClinic.objects.get(pk=252)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-princeton.html', context)

def rmanetsomerset(request):
    listing = BasicClinic.objects.get(pk=253)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-somerset.html', context)

def rmanetspringfield(request):
    listing = BasicClinic.objects.get(pk=254)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-springfield.html', context)

def rmanetwestorang(request):
    listing = BasicClinic.objects.get(pk=255)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/rma-network-west-orange.html', context)

def unirepproassohasbhei(request):
    listing = BasicClinic.objects.get(pk=256)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hasbrouck-heights.html', context)

def unirepproassohoboken(request):
    listing = BasicClinic.objects.get(pk=257)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-hoboken.html', context)

def unirepproassowayne(request):
    listing = BasicClinic.objects.get(pk=258)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/university-reproductive-associates-wayne.html', context)

def princetonivf(request):
    listing = BasicClinic.objects.get(pk=259)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/princeton-ivf.html', context)

def delawvallinsoffergenmarlton(request):
    listing = BasicClinic.objects.get(pk=260)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-marlton.html', context)

def delawvallinsoffergenvineland(request):
    listing = BasicClinic.objects.get(pk=261)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-vineland.html', context)

def delawvallinsoffergenprinceton(request):
    listing = BasicClinic.objects.get(pk=262)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/delaware-valley-institute-of-fertility-genetics-princeton.html', context)

def southjefecemarlton(request):
    listing = BasicClinic.objects.get(pk=263)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-marlton.html', context)

def southjefeceburlington(request):
    listing = BasicClinic.objects.get(pk=264)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-burlington.html', context)

def southjefecesewell(request):
    listing = BasicClinic.objects.get(pk=265)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-sewell.html', context)

def southjefecetownship(request):
    listing = BasicClinic.objects.get(pk=266)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/south-jersey-fertility-center-egg-harbor-township.html', context)

def diamondinsmilburn(request):
    listing = BasicClinic.objects.get(pk=267)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-millburn.html', context)

def diamondinsdover(request):
    listing = BasicClinic.objects.get(pk=269)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/diamond-institute-dover.html', context)

def diamondinsmtlaurel(request):
    listing = BasicClinic.objects.get(pk=270)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-mt-laurel.html', context)

def diamondinsmtmelrosepark(request):
    listing = BasicClinic.objects.get(pk=271)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/cooper-institute-melrose-park.html', context)

def fertilinstofnewjernewyork(request):
    listing = BasicClinic.objects.get(pk=272)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/fertility-institute-of-new-jersey-new-york.html', context)

def damienfertpartshrewsbury(request):
    listing = BasicClinic.objects.get(pk=273)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-shrewsbury.html', context)

def damienfertpartnewjerseycity(request):
    listing = BasicClinic.objects.get(pk=274)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-jersey-city.html', context)

def damienfertpartnewark(request):
    listing = BasicClinic.objects.get(pk=275)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/damien-fertility-partners-newark.html', context)

def islandrepsernewjer(request):
    listing = BasicClinic.objects.get(pk=276)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Jersey/island-reproductive-services-new-jersey.html', context)

# NEW MEXICO Views --------------------------------------------------------------------------------------------------------

def ferticentofnewmexico(request):
    listing = BasicClinic.objects.get(pk=277)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-Mexico/fertility-center-of-new-mexico.html', context)

# NEW YORK Views --------------------------------------------------------------------------------------------------------

def diamondinsgoshen(request):
    listing = BasicClinic.objects.get(pk=268)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/diamond-institute-goshen.html', context)

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

def sherinsforrepmednewyorkferclinic(request):
    listing = BasicClinic.objects.get(pk=278)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/sher-institutes-for-reproductive-medicine-new-york-fertility-clinic.html', context)

def greenwfertuck(request):
    listing = BasicClinic.objects.get(pk=279)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/greenwich-fertility-tuckahoe.html', context)

def rmactnorwalk(request):
    listing = BasicClinic.objects.get(pk=280)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/rmact-norwalk.html', context)

def extendfert(request):
    listing = BasicClinic.objects.get(pk=281)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/extend-fertility.html', context)

def geneferrepromedibaypark(request):
    listing = BasicClinic.objects.get(pk=282)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-bay-parkway.html', context)

def geneferrepromediparkslope(request):
    listing = BasicClinic.objects.get(pk=283)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-park-slope.html', context)

def geneferrepromediforesthills(request):
    listing = BasicClinic.objects.get(pk=284)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-forest-hills.html', context)

def geneferrepromedistatenisland(request):
    listing = BasicClinic.objects.get(pk=285)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-staten-island.html', context)

def geneferrepromedilongisland(request):
    listing = BasicClinic.objects.get(pk=286)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/genesis-fertility-reproductive-medicine-long-island.html', context)

def buffinferivfas(request):
    listing = BasicClinic.objects.get(pk=287)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/buffalo-infertility-and-ivf-associates.html', context)

def hudsvallfert(request):
    listing = BasicClinic.objects.get(pk=288)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/hudson-valley-fertility.html', context)

def bostonivfalbany(request):
    listing = BasicClinic.objects.get(pk=289)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/boston-ivf–albany.html', context)

def bostonivfsyracusy(request):
    listing = BasicClinic.objects.get(pk=290)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/boston-ivf–syracuse.html', context)

def longislivfmelville(request):
    listing = BasicClinic.objects.get(pk=291)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-melville.html', context)

def longislivfeastpatchogue(request):
    listing = BasicClinic.objects.get(pk=292)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-east-patchogue.html', context)

def longislivfgardencity(request):
    listing = BasicClinic.objects.get(pk=293)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-garden-city.html', context)

def longislivfwestislip(request):
    listing = BasicClinic.objects.get(pk=294)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-west-islip.html', context)

def longislivflakesuccess(request):
    listing = BasicClinic.objects.get(pk=295)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-lake-success.html', context)

def longislivfstonybrooks(request):
    listing = BasicClinic.objects.get(pk=296)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/long-island-ivf-stony-brook.html', context)

def nyulangonerepspenewyorkmineola(request):
    listing = BasicClinic.objects.get(pk=297)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-mineola.html', context)

def nyulangonerepspenewyorkbrooklyn(request):
    listing = BasicClinic.objects.get(pk=298)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/nyu-langone-reproductive-specialis-of-new-york-brooklyn.html', context)

def kindboynewyorkmedical(request):
    listing = BasicClinic.objects.get(pk=299)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/kindbody-of-new-york-medical.html', context)

def kofifertgroupstatenisland(request):
    listing = BasicClinic.objects.get(pk=300)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-staten-island.html', context)

def kofifertgroupupperwestside(request):
    listing = BasicClinic.objects.get(pk=301)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-upper-west-side.html', context)

def kofifertgrouplowermanhattan(request):
    listing = BasicClinic.objects.get(pk=302)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/kofinas-fertility-group-lower-manhattan.html', context)

def sgfmanhattan(request):
    listing = BasicClinic.objects.get(pk=303)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/sgf-manhattan.html', context)

def newaymedical(request):
    listing = BasicClinic.objects.get(pk=304)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/neway-medical.html', context)

def repromedassocnewyorkeastside(request):
    listing = BasicClinic.objects.get(pk=305)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-eastside.html', context)

def repromedassocnewyorkwestside(request):
    listing = BasicClinic.objects.get(pk=306)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westside.html', context)

def repromedassocnewyorkdowntown(request):
    listing = BasicClinic.objects.get(pk=307)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-downtown.html', context)

def repromedassocnewyorkbrooklyn(request):
    listing = BasicClinic.objects.get(pk=308)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-brooklyn.html', context)

def repromedassocnewyorkwestchester(request):
    listing = BasicClinic.objects.get(pk=309)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-westchester.html', context)

def repromedassocnewyorkmountsinai(request):
    listing = BasicClinic.objects.get(pk=310)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/reproductive-medicine-associates-of-new-york-mount-sinai.html', context)

def islandreproservicesstatenisland(request):
    listing = BasicClinic.objects.get(pk=311)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/island-reproductive-services-staten-island.html', context)

def cnyfercensyracuse(request):
    listing = BasicClinic.objects.get(pk=312)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-syracuse.html', context)

def cnyfercenalbany(request):
    listing = BasicClinic.objects.get(pk=313)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-albany.html', context)

def cnyfercenrochester(request):
    listing = BasicClinic.objects.get(pk=314)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-rochester.html', context)

def cnyfercenbuffalo(request):
    listing = BasicClinic.objects.get(pk=315)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/New-York/cny-fertility-center-buffalo.html', context)

# NORTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def northcarcenfrepmedic(request):
    listing = BasicClinic.objects.get(pk=316)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/north-carolina-center-for-reproductive-medicine.html', context)

def reproendoassoofcharlotte(request):
    listing = BasicClinic.objects.get(pk=317)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte.html', context)

def reproendoassoofcharlottelakenorman(request):
    listing = BasicClinic.objects.get(pk=318)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/reproductive-endocrinology-associates-of-charlotte-lake-norman.html', context)

def atlanticreprmedspec(request):
    listing = BasicClinic.objects.get(pk=319)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/atlantic-reproductive-medicine-specialists.html', context)

def carolinaconcerale(request):
    listing = BasicClinic.objects.get(pk=320)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-raleigh.html', context)

def carolinaconcewilmington(request):
    listing = BasicClinic.objects.get(pk=321)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-wilmington.html', context)

def carolinaconcehampstead(request):
    listing = BasicClinic.objects.get(pk=322)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-hampstead.html', context)

def carolinaconcegreenville(request):
    listing = BasicClinic.objects.get(pk=323)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolina-conceptions-greenville.html', context)

def carolfertinstgreens(request):
    listing = BasicClinic.objects.get(pk=324)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-greensboro.html', context)

def carolfertinstwinstonsalem(request):
    listing = BasicClinic.objects.get(pk=325)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-winston-salem.html', context)

def carolfertinstcharlotte(request):
    listing = BasicClinic.objects.get(pk=326)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/carolinas-fertility-institute-charlotte.html', context)

def piedmoreproendogroupashe(request):
    listing = BasicClinic.objects.get(pk=327)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Carolina/piedmont-reproductive-endocrinology-group-asheville.html', context)

# NORTH DAKOTA Views --------------------------------------------------------------------------------------------------------

def midwecenforreprohealfargo(request):
    listing = BasicClinic.objects.get(pk=328)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-fargo.html', context)

def midwecenforreprohealminot(request):
    listing = BasicClinic.objects.get(pk=329)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/North-Dakota/midwest-center-for-reproductive-health-minot.html', context)

# OHIO Views --------------------------------------------------------------------------------------------------------

def ivfmichiganohio(request):
    listing = BasicClinic.objects.get(pk=330)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/ivf-michigan-ohio.html', context)

def northeasternohiofertcen(request):
    listing = BasicClinic.objects.get(pk=331)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/northeastern-ohio-fertility-center.html', context)

def reprogyninferakron(request):
    listing = BasicClinic.objects.get(pk=332)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-akron.html', context)

def reprogyninfercolumbus(request):
    listing = BasicClinic.objects.get(pk=333)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-columbus.html', context)

def reprogyninfercleveland(request):
    listing = BasicClinic.objects.get(pk=334)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-cleveland.html', context)

def reprogyninferyoungstown(request):
    listing = BasicClinic.objects.get(pk=335)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-youngstown.html', context)

def reprogyninfercanton(request):
    listing = BasicClinic.objects.get(pk=336)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/reproductive-gynecology-infertility-canton.html', context)

def springcreekfertility(request):
    listing = BasicClinic.objects.get(pk=337)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/springcreek-fertility.html', context)

def instituteforhealthcincinnati(request):
    listing = BasicClinic.objects.get(pk=338)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-cincinnati.html', context)

def instituteforhealthwestche(request):
    listing = BasicClinic.objects.get(pk=339)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/institute-for-reproductive-health-west-chester.html', context)

def ohioreproductivemedicine(request):
    listing = BasicClinic.objects.get(pk=340)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/ohio-reproductive-medicine.html', context)

def fertilitywellnessinstohio(request):
    listing = BasicClinic.objects.get(pk=341)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Ohio/fertility-wellness-institute-of-ohio.html', context)

# OKLAHOMA Views --------------------------------------------------------------------------------------------------------

def ouphysiciansrepromedicine(request):
    listing = BasicClinic.objects.get(pk=342)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Oklahoma/ou-physicians-reproductive-medicine.html', context)

def tulsafertcenter(request):
    listing = BasicClinic.objects.get(pk=343)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Oklahoma/tulsa-fertility-center.html', context)

# OREGON Views --------------------------------------------------------------------------------------------------------

def ormfertilityclidownportland(request):
    listing = BasicClinic.objects.get(pk=344)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-downtown-portland.html', context)

def ormfertilitycliwestsideportland(request):
    listing = BasicClinic.objects.get(pk=345)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-westside-portland.html', context)

def ormfertilityclisouthportland(request):
    listing = BasicClinic.objects.get(pk=346)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Oregon/orm-fertility-clinic-southside-portland.html', context)

# PENNSYLVANIA Views --------------------------------------------------------------------------------------------------------

def sincerarepromedabington(request):
    listing = BasicClinic.objects.get(pk=347)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-abington.html', context)

def sincerarepromedbethlehem(request):
    listing = BasicClinic.objects.get(pk=348)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-bethlehem.html', context)

def sincerarepromedfortwashington(request):
    listing = BasicClinic.objects.get(pk=349)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-fort-washington.html', context)

def sincerarepromedkingofprussia(request):
    listing = BasicClinic.objects.get(pk=350)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-king-of-prussia.html', context)

def sincerarepromedlancaster(request):
    listing = BasicClinic.objects.get(pk=351)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lancaster.html', context)

def sincerarepromedlanghorne(request):
    listing = BasicClinic.objects.get(pk=352)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-langhorne.html', context)

def sincerarepromedlansdale(request):
    listing = BasicClinic.objects.get(pk=353)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-lansdale.html', context)

def sincerarepromedwestchester(request):
    listing = BasicClinic.objects.get(pk=354)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/sincera-reproductive-medicine-west-chester.html', context)

def rmanetwork(request):
    listing = BasicClinic.objects.get(pk=355)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/rma-network-allentown.html', context)

def familyfertilitycenterbethlehem(request):
    listing = BasicClinic.objects.get(pk=356)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-bethlehem.html', context)

def familyfertilitycenterclarkssummit(request):
    listing = BasicClinic.objects.get(pk=357)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/family-fertility-center-clarks-summit.html', context)

def mainlinefertilityrepromedicinebrynmawr(request):
    listing = BasicClinic.objects.get(pk=358)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-bryn-mawr.html', context)

def mainlinefertilityrepromedicinepaoli(request):
    listing = BasicClinic.objects.get(pk=359)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-paoli.html', context)

def mainlinefertilityrepromedicinephiladelphia(request):
    listing = BasicClinic.objects.get(pk=360)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-philadelphia.html', context)

def mainlinefertilityrepromedicinewestchester(request):
    listing = BasicClinic.objects.get(pk=361)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-west-chester.html', context)

def mainlinefertilityrepromedicinehavertown(request):
    listing = BasicClinic.objects.get(pk=362)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-havertown.html', context)

def mainlinefertilityrepromedicinereading(request):
    listing = BasicClinic.objects.get(pk=363)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/main-line-fertility-reproductive-medicine-reading.html', context)

def shadygrovefertilityphiladelphia(request):
    listing = BasicClinic.objects.get(pk=364)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/US/Pennsylvania/shady-grove-fertility-philadelphia.html', context)

def shadygrovefertilitychesterbrook(request):
    listing = BasicClinic.objects.get(pk=365)
    context = {
        'listing': listing,
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
