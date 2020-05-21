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

# GEORGIA Views

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

# HAWAII Views

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
