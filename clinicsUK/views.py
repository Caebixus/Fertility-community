from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone

# Create your views here.
def aberfercen(request):
    listing = BasicClinic.objects.get(pk=506)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Aberdeen/aberdeen-fertility-centre.html', context)

#BATH   --------------------------------

def carefertbath(request):
    listing = BasicClinic.objects.get(pk=507)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bath/care-fertility-bath.html', context)

#BELFAST   --------------------------------

def belffert(request):
    listing = BasicClinic.objects.get(pk=509)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Belfast/belfast-fertility.html', context)

#BIRMINGHAM   --------------------------------

def carefertbirmingh(request):
    listing = BasicClinic.objects.get(pk=509)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-birmingham.html', context)

def createfertbirmin(request):
    listing = BasicClinic.objects.get(pk=510)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Birmingham/create-fertility-birmingham.html', context)

def bmitheprioryhosp(request):
    listing = BasicClinic.objects.get(pk=511)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Birmingham/bmi-the-priory-hospital.html', context)

def careferttamworth(request):
    listing = BasicClinic.objects.get(pk=512)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Birmingham/care-fertility-tamworth.html', context)

def stjudesfertclinic(request):
    listing = BasicClinic.objects.get(pk=513)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Birmingham/st-judes-fertility-clinic.html', context)

#BOURNEMOUTH   --------------------------------

def completefertcentbourn(request):
    listing = BasicClinic.objects.get(pk=514)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bournemouth/complete-fertility-centre-bournemouth.html', context)

def poundburyfertdorset(request):
    listing = BasicClinic.objects.get(pk=515)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bournemouth/poundbury-fertility-dorset.html', context)

#BRIGHTON   --------------------------------

def brightfertasso(request):
    listing = BasicClinic.objects.get(pk=516)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Brighton/brighton-fertility-associates.html', context)

def agoragynandfertcentre(request):
    listing = BasicClinic.objects.get(pk=517)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Brighton/agora-gynaecology-and-fertility-centre.html', context)

#BRISTOL   --------------------------------

def abcivfbristol(request):
    listing = BasicClinic.objects.get(pk=518)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/abc-ivf-bristol.html', context)

def bristolcentreforrepromedicine(request):
    listing = BasicClinic.objects.get(pk=519)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine.html', context)

def crgwbristol(request):
    listing = BasicClinic.objects.get(pk=520)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/crgw-bristol.html', context)

def createfertbristol(request):
    listing = BasicClinic.objects.get(pk=521)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/create-fertility-bristol.html', context)

def bristolcenforrepromedspireclinic(request):
    listing = BasicClinic.objects.get(pk=522)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/bristol-centre-for-reproductive-medicine-spire-clinic.html', context)

def londonwomensclinicbristol(request):
    listing = BasicClinic.objects.get(pk=523)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Bristol/london-womens-clinic-bristol.html', context)

#CAMBRIDGE   --------------------------------

def bournhallcliniccambridge(request):
    listing = BasicClinic.objects.get(pk=524)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Cambridge/bourn-hall-clinic-cambridge.html', context)

def cambridgeivf(request):
    listing = BasicClinic.objects.get(pk=525)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Cambridge/cambridge-ivf.html', context)

#CARDIFF   --------------------------------

def crgwcardiff(request):
    listing = BasicClinic.objects.get(pk=526)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Cardiff/crgw-cardiff.html', context)

def londonwomenscliniccardiff(request):
    listing = BasicClinic.objects.get(pk=527)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Cardiff/london-womens-clinic-cardiff.html', context)

def walesfertilityinstitutecardiff(request):
    listing = BasicClinic.objects.get(pk=528)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Cardiff/wales-fertility-institute-cardiff.html', context)

#COLCHESTER   --------------------------------

def bournhallcliniccolchester(request):
    listing = BasicClinic.objects.get(pk=529)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Colchester/bourn-hall-clinic-colchester.html', context)

#DERBY   --------------------------------

def nurturefertburtsatclinic(request):
    listing = BasicClinic.objects.get(pk=530)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Derby/nurture-fertility-burton-satellite-clinic.html', context)

#EXETER   --------------------------------

def fertilityexeter(request):
    listing = BasicClinic.objects.get(pk=531)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Exeter/fertility-exeter.html', context)

#GLASGOW   --------------------------------

def gcrmfertilityglasgow(request):
    listing = BasicClinic.objects.get(pk=532)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Glasgow/gcrm-fertility.html', context)

def semovoglasgow(request):
    listing = BasicClinic.objects.get(pk=533)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Glasgow/semovo-glasgow.html', context)

#KINGSTON UPON HULL   --------------------------------

def hullivfunit(request):
    listing = BasicClinic.objects.get(pk=534)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Kingstonuponhill/hull-ivf-unit.html', context)

#CHELMSFORD   --------------------------------

def simplyfertilitychelm(request):
    listing = BasicClinic.objects.get(pk=535)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Chelmsford/simply-fertility.html', context)

def bournhallclinicwockford(request):
    listing = BasicClinic.objects.get(pk=536)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Chelmsford/bourn-hall-clinic-wickford.html', context)

def carefertilitychester(request):
    listing = BasicClinic.objects.get(pk=537)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Chelmsford/care-fertility-chester.html', context)

#LEEDS   --------------------------------

def leedsfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=538)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Leeds/leeds-fertility-clinic.html', context)

def semovoleeds(request):
    listing = BasicClinic.objects.get(pk=539)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Leeds/semovo-leeds.html', context)

#LEICESTER   --------------------------------

def xyfertility(request):
    listing = BasicClinic.objects.get(pk=540)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Leicester/xy-fertility.html', context)

#LIVERPOOL   --------------------------------

def carefertilityliverpool(request):
    listing = BasicClinic.objects.get(pk=541)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Liverpool/care-fertility-liverpool.html', context)

def thehewittfertilitycentreliverpool(request):
    listing = BasicClinic.objects.get(pk=542)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Liverpool/the-hewitt-fertility-centre-liverpool.html', context)

def semovoliverpool(request):
    listing = BasicClinic.objects.get(pk=543)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Liverpool/semovo-liverpool.html', context)

def centreforreproductivehealth(request):
    listing = BasicClinic.objects.get(pk=544)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Liverpool/centre-for-reproductive-health.html', context)

#LONDON   --------------------------------

def londonwomensclinicbrentwood(request):
    listing = BasicClinic.objects.get(pk=545)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-brentwood.html', context)

def londonwomensclinicharrow(request):
    listing = BasicClinic.objects.get(pk=546)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harrow.html', context)

def abcivfharleystreet(request):
    listing = BasicClinic.objects.get(pk=547)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/abc-ivf-harley-street.html', context)

def abcivfwimbledon(request):
    listing = BasicClinic.objects.get(pk=548)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/abc-ivf-wimbledon.html', context)

def assistedreproandgynaecologycentre(request):
    listing = BasicClinic.objects.get(pk=549)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/assisted-reproduction-and-gynaecology-centre.html', context)

def cityfertility(request):
    listing = BasicClinic.objects.get(pk=550)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/city-fertility.html', context)

def createfertistpauls(request):
    listing = BasicClinic.objects.get(pk=551)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/create-fertility-st-pauls.html', context)

def fertilityplusfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=552)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/fertility-plus-fertility-clinic.html', context)

def londonwomensclinicharleystreet(request):
    listing = BasicClinic.objects.get(pk=553)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-harley-street.html', context)

def poundburyfertilitylondon(request):
    listing = BasicClinic.objects.get(pk=554)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/poundbury-fertility-london.html', context)

def semovolondon(request):
    listing = BasicClinic.objects.get(pk=555)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/semovo-london.html', context)

def londonwomenscliniclondonbridge(request):
    listing = BasicClinic.objects.get(pk=556)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/london-womens-clinic-london-bridge.html', context)

def thamesvalleyfertility(request):
    listing = BasicClinic.objects.get(pk=557)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/thames-valley-fertility.html', context)

def ivflondonelstree(request):
    listing = BasicClinic.objects.get(pk=558)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/ivf-london-elstree.html', context)

def hertsandessexfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=559)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/herts-and-essex-fertility-centre.html', context)

def bostonplace(request):
    listing = BasicClinic.objects.get(pk=560)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/boston-place.html', context)

def carefertilitylondon(request):
    listing = BasicClinic.objects.get(pk=561)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/care-fertility-london.html', context)

def conceptfertility(request):
    listing = BasicClinic.objects.get(pk=562)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/concept-fertility.html', context)

def createfertilitywimbledon(request):
    listing = BasicClinic.objects.get(pk=563)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/create-fertility-wimbledon.html', context)

def evewell(request):
    listing = BasicClinic.objects.get(pk=564)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/evewell.html', context)

def thefertilitygynaecologyacademy(request):
    listing = BasicClinic.objects.get(pk=565)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/the-fertility-gynaecology-academy.html', context)

def harleystreetfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=566)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/harley-street-fertility-clinic.html', context)

def homertonfertilitycentre(request):
    listing = BasicClinic.objects.get(pk=567)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/homerton-fertility-centre.html', context)

def ivilondon(request):
    listing = BasicClinic.objects.get(pk=568)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/ivi-london.html', context)

def kingsfertility(request):
    listing = BasicClinic.objects.get(pk=569)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/kings-fertility.html', context)

def listerfertilityclinic(request):
    listing = BasicClinic.objects.get(pk=570)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/lister-fertility-clinic.html', context)

def createfertilityhertfordshire(request):
    listing = BasicClinic.objects.get(pk=571)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/London/create-fertility-hertfordshire.html', context)

#MANCHESTER   --------------------------------

def manchesterfertility(request):
    listing = BasicClinic.objects.get(pk=572)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/manchester-fertility.html', context)

def semovomanchestersouth(request):
    listing = BasicClinic.objects.get(pk=573)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-south.html', context)

def thehewittfertilitycentreknutsford(request):
    listing = BasicClinic.objects.get(pk=574)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/the-hewitt-fertility-centre-knutsford.html', context)

def aurorareprohealthaltrincham(request):
    listing = BasicClinic.objects.get(pk=575)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/aurora-reproductive-healthcare-altrincham.html', context)

def abcivfmanchester(request):
    listing = BasicClinic.objects.get(pk=576)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/abc-ivf-manchester.html', context)

def createfertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=577)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/create-fertility-manchester.html', context)

def semovomanchestercitycentre(request):
    listing = BasicClinic.objects.get(pk=578)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/semovo-manchester-city-centre.html', context)

def fertilityfusion(request):
    listing = BasicClinic.objects.get(pk=579)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/fertility-fusion.html', context)

def carefertilitymanchester(request):
    listing = BasicClinic.objects.get(pk=580)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Manchester/care-fertility-manchester.html', context)

#MIDDLESBROUGH   --------------------------------

def londonwomensclinicdarlington(request):
    listing = BasicClinic.objects.get(pk=581)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Middlesbrough/london-womens-clinic-darlington.html', context)

#NEWCASTLE   --------------------------------

def newcastlefertilitycentre(request):
    listing = BasicClinic.objects.get(pk=582)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Newcastle/newcastle-fertility-centre.html', context)

#NORWICH   --------------------------------

def bournhallclinicnorwich(request):
    listing = BasicClinic.objects.get(pk=583)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Norwich/bourn-hall-clinic-norwich.html', context)

#NOTTINGHAM   --------------------------------

def nurturefertilitynottingham(request):
    listing = BasicClinic.objects.get(pk=584)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Nottingham/nurture-fertility-nottingham.html', context)

def carefertilitynottingham(request):
    listing = BasicClinic.objects.get(pk=585)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Nottingham/care-fertility-nottingham.html', context)

#OXFORD   --------------------------------

def createfertilityoxford(request):
    listing = BasicClinic.objects.get(pk=586)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Oxford/create-fertility-oxford.html', context)

def oxfordfertility(request):
    listing = BasicClinic.objects.get(pk=587)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Oxford/oxford-fertility.html', context)

def abcivfoxford(request):
    listing = BasicClinic.objects.get(pk=588)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Oxford/abc-ivf-oxford.html', context)

#PETERBOROUGH   --------------------------------

def bournhallclinicpeterborough(request):
    listing = BasicClinic.objects.get(pk=589)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Peterborough/bourn-hall-clinic-peterborough.html', context)

#PLYMOUTH   --------------------------------

def crgwplymouth(request):
    listing = BasicClinic.objects.get(pk=590)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Plymouth/crgw-plymouth.html', context)

#PORTSMOUTH   --------------------------------

def completefertilitycentreportsmouth(request):
    listing = BasicClinic.objects.get(pk=591)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Portsmouth/complete-fertility-centre-portsmouth.html', context)

#SALISBURY   --------------------------------

def salisburyfertcentre(request):
    listing = BasicClinic.objects.get(pk=592)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Salisbury/salisbury-fertility-centre.html', context)

#SHEFFIELD   --------------------------------

def nurturefertilitychesterfield(request):
    listing = BasicClinic.objects.get(pk=593)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Sheffield/nurture-fertility-chesterfield.html', context)

def carefertilitysheffield(request):
    listing = BasicClinic.objects.get(pk=594)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Sheffield/care-fertility-sheffield.html', context)

#SOUTHAMPTON   --------------------------------

def completefertilitycentresouthampton(request):
    listing = BasicClinic.objects.get(pk=595)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Southampton/complete-fertility-centre-southampton.html', context)

def wessexfertility(request):
    listing = BasicClinic.objects.get(pk=596)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Southampton/wessex-fertility.html', context)

#SWANSEA   --------------------------------

def walesfertilityinstituteneath(request):
    listing = BasicClinic.objects.get(pk=597)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Swansea/wales-fertility-institute-neath.html', context)

def crgwswansea(request):
    listing = BasicClinic.objects.get(pk=598)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Swansea/crgw-swansea.html', context)

def londonwomensclinicswansea(request):
    listing = BasicClinic.objects.get(pk=599)
    context = {
        'listing': listing,
        }

    return render(request, 'clinics/UK/Swansea/london-womens-clinic-swansea.html', context)
