from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.views.generic.detail import DetailView
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

from searchLocationsCountries import views


def bestclinicczech(request):
    return render(request, 'blog/best-article/best-article.html')








# Create your views here.
def wfi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cifc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ncfmcr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ncfmcs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def liwla(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def lip(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def lich(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# ALABAMA Views --------------------------------------------------------------------------------------------------------

def tcfrm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def af(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aminstrepbir(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aminstrephomeb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def newlifemobile(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def newlifedothan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertinstofnorthal(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def huntsrepromed(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def artfertproofal(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# ARIZONA Views --------------------------------------------------------------------------------------------------------

def tfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def afcs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def afcm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aafrhs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aafrhg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bris(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def brig(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def biacs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def biacch(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def biacp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def biacf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ip(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ftc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def arifc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# ARKANSAS Views --------------------------------------------------------------------------------------------------------

def afg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# COLORADO Views --------------------------------------------------------------------------------------------------------

def ccrmcmclt(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmcdo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmclo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ucarmd(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ucarmcos(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmcrm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# CONNECTICUT Views --------------------------------------------------------------------------------------------------------

def carsf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carsh(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carsnl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carsb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def gfg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def gfs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmactn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmacts(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmactd(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmactt(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def paft(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def paff(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pafn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# DELAWARE Views --------------------------------------------------------------------------------------------------------

def dirmn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dirmm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def radfn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def radfw(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def radfd(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# FLORIDA Views --------------------------------------------------------------------------------------------------------

def bocaf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pbfcbr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pbfcpbg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ffico(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ffito(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cfcg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cfm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def jcrmj(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def jcrmg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def jcrmpc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def jcrmo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanlm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivffwfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivffcgfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfppfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivffmfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfbrfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivffjpbgfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivffplfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fivfcm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fivfcmb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdcc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdbr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdj(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdv(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgftw(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfwc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmgnto(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmgsto(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmgco(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmgbo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fifrst(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def arswp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfowp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcare(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# GEORGIA Views --------------------------------------------------------------------------------------------------------

def afa(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def acrmap(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def acrmab(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def acrmjc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def acrmm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mfs(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sfi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfa(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbamo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbam(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbaf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbal(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbac(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbaph(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rbacar(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cnyferticentatlanta(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def coastalfertispecsavannah(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# HAWAII Views --------------------------------------------------------------------------------------------------------

def arch(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def armghh(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def armghk(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pivfi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# IOWA Views --------------------------------------------------------------------------------------------------------

def mif(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# IDAHO Views --------------------------------------------------------------------------------------------------------

def icrm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprocarecenteridahofalls(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# ILLINOIS Views --------------------------------------------------------------------------------------------------------

def crc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcibgc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcicnc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcigc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcihpc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcihc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcihec(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfbp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcilc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcitpc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fciwc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ihrc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ihro(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vfica(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vficwp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vficwlil(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vficg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vfiche(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dfis(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def hcr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifsah(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifscl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifshe(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifsn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivf1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmib(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmiel(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmiev(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rminb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmiob(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmiol(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def civfops(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def civfscn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def civfnw(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# INDIANA Views --------------------------------------------------------------------------------------------------------

def ihrval(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mfcar(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mffortwayne(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def civfval(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def civfmun(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def prhmun(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fbeg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifinst(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rcimo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rcith(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rcilaf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rcibmc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rcibws(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# KANSAS Views --------------------------------------------------------------------------------------------------------

def midrepc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# KENTUCKY Views --------------------------------------------------------------------------------------------------------

def ferendas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifrhealthflo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ifrhealthlou(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# LOUISIANA Views --------------------------------------------------------------------------------------------------------

def feanla(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def feanbaro(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def feanco(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def feanlach(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fiman(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fimet(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fibaro(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def audfer(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def arkferrepmed(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MAINE Views --------------------------------------------------------------------------------------------------------

def fcnebc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfbfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfpfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MARYLAND Views --------------------------------------------------------------------------------------------------------

def montgofercert(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MASSACHUSETTS Views --------------------------------------------------------------------------------------------------------

def masghfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmbmc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmmo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmsso(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfmfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfdbfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivflfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfqfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfwfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bivfsfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcnelc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcnerc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcnedc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcnebce(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fcnebcen(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MICHIGAN Views --------------------------------------------------------------------------------------------------------

def ivfmfcaafc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcbhfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcchebfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcdfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcelfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcmfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcpfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfcsfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmfctfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def gcffb(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ggcffl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ggcffaa(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfcgr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfcm(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfck(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tfctc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmrh(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmd(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmaom(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MINNESOTA Views --------------------------------------------------------------------------------------------------------

def cccrmmin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def midcfrh(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cenfrmmin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cenfrmstp(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cenfrmwesog(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cenfremstluobgyna(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repmeinaswoo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repmeinasedi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MISSISSIPPI Views --------------------------------------------------------------------------------------------------------

def cenfrmmfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def missrepmed(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# MISSOURI Views --------------------------------------------------------------------------------------------------------

def vfichisl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def vfichiofa(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def infeceofstlo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mcrmferstlo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mcrmferspring(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def missofer(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shiforrepmestlofecl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NEBRASKA Views --------------------------------------------------------------------------------------------------------

def hearceforrepme(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NEVADA Views --------------------------------------------------------------------------------------------------------

def greevalferpartners(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def theferceoflasvegas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sherinsfrepmedlasvegfecl(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def redrofercen(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NEW JERSEY Views --------------------------------------------------------------------------------------------------------

def irmsco(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmsewo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmsho(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmshbo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmsnjo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmslo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def irmsobo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def Cenfoarepmedicinefer(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetbasrid(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmaneteaton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetenglewood(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetfreehold(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetmarlton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetmorristown(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetprinceston(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetsomerset(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetspringfield(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetwestorang(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def unirepproassohasbhei(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def unirepproassohoboken(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def unirepproassowayne(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def princetonivf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def delawvallinsoffergenmarlton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def delawvallinsoffergenvineland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def delawvallinsoffergenprinceton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def southjefecemarlton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def southjefeceburlington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def southjefecesewell(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def southjefecetownship(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def diamondinsmilburn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def diamondinsdover(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def diamondinsmtlaurel(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def diamondinsmtmelrosepark(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilinstofnewjernewyork(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def damienfertpartshrewsbury(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def damienfertpartnewjerseycity(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def damienfertpartnewark(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def islandrepsernewjer(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NEW MEXICO Views --------------------------------------------------------------------------------------------------------

def ferticentofnewmexico(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NEW YORK Views --------------------------------------------------------------------------------------------------------

def diamondinsgoshen(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cfnyc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmnyfc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sherinsforrepmednewyorkferclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def greenwfertuck(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmactnorwalk(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def extendfert(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneferrepromedibaypark(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneferrepromediparkslope(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneferrepromediforesthills(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneferrepromedistatenisland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneferrepromedilongisland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def buffinferivfas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def hudsvallfert(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bostonivfalbany(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bostonivfsyracusy(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivfmelville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivfeastpatchogue(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivfgardencity(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivfwestislip(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivflakesuccess(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def longislivfstonybrooks(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nyulangonerepspenewyorkmineola(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nyulangonerepspenewyorkbrooklyn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def kindboynewyorkmedical(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def kofifertgroupstatenisland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def kofifertgroupupperwestside(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def kofifertgrouplowermanhattan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sgfmanhattan(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def newaymedical(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkeastside(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkwestside(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkdowntown(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkbrooklyn(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkwestchester(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedassocnewyorkmountsinai(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def islandreproservicesstatenisland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cnyfercensyracuse(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cnyfercenalbany(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cnyfercenrochester(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def cnyfercenbuffalo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nyulangonefertilitycenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NORTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def northcarcenfrepmedic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproendoassoofcharlotte(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproendoassoofcharlottelakenorman(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def atlanticreprmedspec(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolinaconcerale(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolinaconcewilmington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolinaconcehampstead(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolinaconcegreenville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolfertinstgreens(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolfertinstwinstonsalem(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def carolfertinstcharlotte(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def piedmoreproendogroupashe(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# NORTH DAKOTA Views --------------------------------------------------------------------------------------------------------

def midwecenforreprohealfargo(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def midwecenforreprohealminot(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# OHIO Views --------------------------------------------------------------------------------------------------------

def ivfmichiganohio(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def northeasternohiofertcen(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprogyninferakron(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprogyninfercolumbus(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprogyninfercleveland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprogyninferyoungstown(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reprogyninfercanton(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def springcreekfertility(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def instituteforhealthcincinnati(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def instituteforhealthwestche(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ohioreproductivemedicine(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilitywellnessinstohio(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# OKLAHOMA Views --------------------------------------------------------------------------------------------------------

def ouphysiciansrepromedicine(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tulsafertcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# OREGON Views --------------------------------------------------------------------------------------------------------

def ormfertilityclidownportland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ormfertilitycliwestsideportland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ormfertilityclisouthportland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# PENNSYLVANIA Views --------------------------------------------------------------------------------------------------------

def sincerarepromedabington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedbethlehem(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedfortwashington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedkingofprussia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedlancaster(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedlanghorne(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedlansdale(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sincerarepromedwestchester(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def rmanetwork(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def familyfertilitycenterbethlehem(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def familyfertilitycenterclarkssummit(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinebrynmawr(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinepaoli(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinephiladelphia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinewestchester(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinehavertown(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def mainlinefertilityrepromedicinereading(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shadygrovefertilityphiladelphia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shadygrovefertilitychesterbrook(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shadygrovefertilitymechanicsburg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shadygrovefertilitylancaster(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def shadygrovefertilitywarrington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# PUERTO RICO Views --------------------------------------------------------------------------------------------------------

def puertoricofertilitycenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# SOUTH CAROLINA Views --------------------------------------------------------------------------------------------------------

def piedmontreproendogroupgreenville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))


def piedmontreproendogroupspartanburg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def piedmontreproendogroupcolumbia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def coastalfertspecimountpleasant(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def coastalfertspecinorthcharleston(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def coastalfertspecilexington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def coastalfertspecimyrtlebeach(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# TENNESSEE Views --------------------------------------------------------------------------------------------------------

def tenrepromedchattaivffertclin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def myfertilitycenterchatt(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def myfertilitycenterknoxville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def tennesseefertiinstitute(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertiassoofmemphis(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nashvillefertnashville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nashvillefertmurfreesboro(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def nashvillefertfranklin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerforreprohealthnash(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# TEXAS Views --------------------------------------------------------------------------------------------------------

def sherinsforrepmedicinedallas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmdallasfortworth(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmhoustonmaincenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmhoustonmedicalcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmhoustonsugarland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertaustinfertilitycenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertbeecavefertcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertadison(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertclearlake(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertfanninfece(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertkatyfertce(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertmainstreet(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertsugarlandfertcen(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertwillowbrookfertcent(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertsanantoniofertcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def aspirefertsatellitecliniclocation(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdcenterarlington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfmdcenterirving(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def austinfertrepmedwestlake(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def austinfertrepmedsouthlocation(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def austinfertrepmedroundrock(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycentercentralaustin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycenterroundrock(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycentersouthaustin(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycenternewbraunfels(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycentersanantonio(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texasfertilitycentercorpuschristi(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerforassistedreprobedford(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerforassistedreprofortworth(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasfortworthfertilityassociates(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasfortworthfertilityassociatessouthlake(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasfortworthfertilityassociatesmedicalcity(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilitycenterofdallas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycenterdallas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycentergrapevine(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycentermckinney(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycenterrockwall(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycentertyler(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def repromedfertilitycentermckinneysurgicalcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def sherfertilityclinicdallas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def texascenterforreproductivehealth(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fortworthfertility(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasivffriscofertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))


def dallasivfdallasfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasivfmckinleyfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasivfplanofertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dallasivftylerfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityspecialistsoftexasfrisco(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityspecialistsoftexasdallas(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityspecialistsoftexasrockwall(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityspecialistsoftexassouthlake(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def advancedfertilitycenteroftexasmemorialcity(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def advancedfertilitycenteroftexasspring(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def advancedfertilitycenteroftexascollegestation(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerofreproductivemedicinehouston(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerofreproductivemedicinememorialcity(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerofreproductivemedicineclearlake(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def centerofreproductivemedicinebeaumont(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutehoustonoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcentermemorialhermann(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterwomanshospital(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterkatyoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcentersugarland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterclearlakeoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcentermemorialcityoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterwillowbrookoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterwoodlandsoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterbeaumontoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcentercypresstoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterkingwoodoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def houstonfertilityinstitutemedicalcenterpearlandoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def odessaivf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ivfplano(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityceofsanantsanantoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityceofsanantstoneoakoffice(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def hartivffertilityclinicwoodlands(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def hartivffertilityclinickingwood(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# UTAH Views --------------------------------------------------------------------------------------------------------

def utahfertilitycenterogden(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def conceptionsfertility(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproductivecarecenterclearfield(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproductivecarecentersandy(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproductivecarecenterpleasantgrove(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# VERMONT Views --------------------------------------------------------------------------------------------------------

def northeasternreproductivemedicinecolchester(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# VIRGINIA Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociatesarlington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmmaincenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def ccrmcolumbia(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def washingtonfertilitycenterannandale(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def washingtonfertilitycenterfredericksburg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def washingtonfertilitycenterreston(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dominionfertilityarlington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dominionfertilityfairfax(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproductivemedicineandsurgerycenterofvirginiacharlottesville(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def reproductivemedicineandsurgerycenterofvirginialynchburg(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def geneticsivfinstitute(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def virginiacenterforreproductivemedicine(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def thenewhopecenterforreproductivemedicine(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# WASHINGTON Views --------------------------------------------------------------------------------------------------------

def orgfertilityclinicbellevue(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def dominionfertilitywashington(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def bellevuefertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pomafertility(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))


def pacificnwfertilityseattle(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def pacificnwfertilitybellevue(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicineseattle(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicinebellevue(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicinetacoma(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicinekirkland(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicineeverett(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def seattlereproductivemedicinespokane(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def soundfertilitycare(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def thecenterforreproductivehealth(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# WISCONSIN Views --------------------------------------------------------------------------------------------------------

def viosfertilityinstitutechicagomilwaukee(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def viosfertilityinstitutechicagolakecountry(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def wisconsinfertilityinstitute(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

# WASHINGTON-DC Views --------------------------------------------------------------------------------------------------------

def columbiafertilityassociateswashingtondc(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def gwmedicalfacultyassociates(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))


# --------------------------------------->>>>>>>> Redirects
def redvficwlil(request):
    return HttpResponsePermanentRedirect(reverse('vficwlil'))
