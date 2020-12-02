from django.urls import path

from . import views

urlpatterns = [
    # Czech Republic
    path('locations/fertility-clinics-prague', views.fertilityClinicPrague1, name='fertilityClinicPrague1'),
    path('locations/fertility-clinics-brno', views.fertilityClinicBrno1, name='fertilityClinicBrno1'),
    path('fertility-clinics-prague', views.fertilityClinicPrague, name='fertilityClinicPrague'),
    path('fertility-clinics-brno', views.fertilityClinicBrno, name='fertilityClinicBrno'),

    # United Kingdom
    path('fertility-clinics-aberdeen', views.fertilityClinicsAberdeen, name='fertilityClinicsAberdeen'),
    path('fertility-clinics-bath', views.fertilityClinicsBath, name='fertilityClinicsBath'),
    path('fertility-clinics-belfast', views.fertilityClinicsBelfast, name='fertilityClinicsBelfast'),
    path('fertility-clinics-birmingham', views.fertilityClinicsBirmingham, name='fertilityClinicsBirmingham'),
    path('fertility-clinics-bournemouth', views.fertilityClinicsBournemouth, name='fertilityClinicsBournemouth'),
    path('fertility-clinics-brighton-hove', views.fertilityClinicsBrightonHove, name='fertilityClinicsBrightonHove'),
    path('fertility-clinics-bristol', views.fertilityClinicsBristol, name='fertilityClinicsBristol'),
    path('fertility-clinics-cambridge', views.fertilityClinicsCambridge, name='fertilityClinicsCambridge'),
    path('fertility-clinics-cardiff', views.fertilityClinicsCardiff, name='fertilityClinicsCardiff'),
    path('fertility-clinics-colchester', views.fertilityClinicsColchester, name='fertilityClinicsColchester'),
    path('fertility-clinics-derby', views.fertilityClinicsDerby, name='fertilityClinicsDerby'),
    path('fertility-clinics-exeter', views.fertilityClinicsExeter, name='fertilityClinicsExeter'),
    path('fertility-clinics-glasgow', views.fertilityClinicsGlasgow, name='fertilityClinicsGlasgow'),
    path('fertility-clinics-kingston-upon-hull', views.fertilityClinicsHull, name='fertilityClinicsHull'),
    path('fertility-clinics-chelmsford', views.fertilityClinicsChelmsford, name='fertilityClinicsChelmsford'),
    path('fertility-clinics-leeds', views.fertilityClinicsLeeds, name='fertilityClinicsLeeds'),
    path('fertility-clinics-leicester', views.fertilityClinicsLeicester, name='fertilityClinicsLeicester'),
    path('fertility-clinics-liverpool', views.fertilityClinicsLiverpool, name='fertilityClinicsLiverpool'),
    path('fertility-clinics-london', views.fertilityClinicsLondon, name='fertilityClinicsLondon'),
    path('fertility-clinics-manchester', views.fertilityClinicsManchester, name='fertilityClinicsManchester'),
    path('fertility-clinics-middlesbrough', views.fertilityClinicsMiddlesbrough, name='fertilityClinicsMiddlesbrough'),
    path('fertility-clinics-newcastle', views.fertilityClinicsNewcastle, name='fertilityClinicsNewcastle'),
    path('fertility-clinics-norwich', views.fertilityClinicsNorwich, name='fertilityClinicsNorwich'),
    path('fertility-clinics-nottingham', views.fertilityClinicsNottingham, name='fertilityClinicsNottingham'),
    path('fertility-clinics-oxford', views.fertilityClinicsOxford, name='fertilityClinicsOxford'),
    path('fertility-clinics-peterborough', views.fertilityClinicsPeterborough, name='fertilityClinicsPeterborough'),
    path('fertility-clinics-plymouth', views.fertilityClinicsPlymouth, name='fertilityClinicsPlymouth'),
    path('fertility-clinics-portsmouth', views.fertilityClinicsPortsmouth, name='fertilityClinicsPortsmouth'),
    path('fertility-clinics-salisbury', views.fertilityClinicsSalisbury, name='fertilityClinicsSalisbury'),
    path('fertility-clinics-sheffield', views.fertilityClinicsSheffield, name='fertilityClinicsSheffield'),
    path('fertility-clinics-southampton', views.fertilityClinicsSouthampton, name='fertilityClinicsSouthampton'),
    path('fertility-clinics-swansea', views.fertilityClinicsSwansea, name='fertilityClinicsSwansea'),

    # Spain
    path('fertility-clinics-alicante', views.fertilityClinicsAlicante, name='fertilityClinicsAlicante'),
    path('fertility-clinics-barcelona', views.fertilityClinicsBarcelona, name='fertilityClinicsBarcelona'),
    path('fertility-clinics-madrid', views.fertilityClinicsMadrid, name='fertilityClinicsMadrid'),
    path('fertility-clinics-malaga', views.fertilityClinicsMalaga, name='fertilityClinicsMalaga'),
    path('fertility-clinics-seville', views.fertilityClinicsSeville, name='fertilityClinicsSeville'),
    path('fertility-clinics-valencia', views.fertilityClinicsValencia, name='fertilityClinicsValencia'),

    # India
    path('fertility-clinics/india/gujarat/amdavad', views.fertilityClinicsAmdavad, name='fertilityClinicsAmdavad'),
    path('fertility-clinics/india/karnataka/bangalore', views.fertilityClinicsBangalore, name='fertilityClinicsBangalore'),
    path('fertility-clinics/india/madhya-pradesh/bhopal', views.fertilityClinicsBhopal, name='fertilityClinicsBhopal'),
    path('fertility-clinics/india/odisha/bhubaneswar', views.fertilityClinicsBhubaneswar, name='fertilityClinicsBhubaneswar'),
    path('fertility-clinics/india/uttarakhand/dehradun', views.fertilityClinicsDehradun, name='fertilityClinicsDehradun'),
    path('fertility-clinics/india/haryana/faridabad', views.fertilityClinicsFaridabad, name='fertilityClinicsFaridabad'),
    path('fertility-clinics/india/telangana/hyderabad', views.fertilityClinicsHyderabad, name='fertilityClinicsHyderabad'),
    path('fertility-clinics/india/chandigarh', views.fertilityClinicsChandigarh, name='fertilityClinicsChandigarh'),
    path('fertility-clinics/india/tamil-nadu/chennai', views.fertilityClinicsChennai, name='fertilityClinicsChennai'),
    path('fertility-clinics/india/madhya-pradesh/indore', views.fertilityClinicsIndore, name='fertilityClinicsIndore'),
    path('fertility-clinics/india/rajasthan/jaipur', views.fertilityClinicsJaipur, name='fertilityClinicsJaipur'),
    path('fertility-clinics/india/jharkhand/jamshedpur', views.fertilityClinicsJamshedpur, name='fertilityClinicsJamshedpur'),
    path('fertility-clinics/india/uttar-pradesh/kanpur', views.fertilityClinicsKanpur, name='fertilityClinicsKanpur'),
    path('fertility-clinics/india/kerala/kochi', views.fertilityClinicsKochi, name='fertilityClinicsKochi'),
    path('fertility-clinics/india/west-bengal/kolkata', views.fertilityClinicsKolkata, name='fertilityClinicsKolkata'),
    path('fertility-clinics/india/uttar-pradesh/lucknow', views.fertilityClinicsLucknow, name='fertilityClinicsLucknow'),
    path('fertility-clinics/india/maharashtra/mumbai', views.fertilityClinicsMumbai, name='fertilityClinicsMumbai'),
    path('fertility-clinics/india/maharashtra/nagpur', views.fertilityClinicsNagpur, name='fertilityClinicsNagpur'),
    path('fertility-clinics/india/bihar/patna', views.fertilityClinicsPatna, name='fertilityClinicsPatna'),
    path('fertility-clinics/india/chhattisgarh/raipur', views.fertilityClinicsRaipur, name='fertilityClinicsRaipur'),
    path('fertility-clinics/india/kerala/trivandrum', views.fertilityClinicsTrivandrum, name='fertilityClinicsTrivandrum'),
    path('fertility-clinics/india/punjab/ludhiana', views.fertilityClinicsLudhiana, name='fertilityClinicsLudhiana'),
    path('fertility-clinics/india/andhra-pradesh/visakhapatnam', views.fertilityClinicsVisakhapatnam, name='fertilityClinicsVisakhapatnam'),
    path('fertility-clinics/india/andhra-pradesh/vijayawada', views.fertilityClinicsVijayawada, name='fertilityClinicsVijayawada'),
    path('fertility-clinics/india/delhi/new-delhi', views.fertilityClinicsNewDelhi, name='fertilityClinicsNewDelhi'),
    path('fertility-clinics/india/gujarat/vadodara', views.fertilityClinicsVadodara, name='fertilityClinicsVadodara'),
    path('fertility-clinics/india/haryana/gurugram', views.fertilityClinicsGurugram, name='fertilityClinicsGurugram'),
    path('fertility-clinics/india/haryana/rohtak', views.fertilityClinicsRohtak, name='fertilityClinicsRohtak'),
    path('fertility-clinics/india/jammu-and-kashmir/jammu', views.fertilityClinicsJammu, name='fertilityClinicsJammu'),
    path('fertility-clinics/india/jharkhand/ranchi', views.fertilityClinicsRanchi, name='fertilityClinicsRanchi'),
    path('fertility-clinics/india/madhya-pradesh/gwalior', views.fertilityClinicsGwalior, name='fertilityClinicsGwalior'),
    path('fertility-clinics/india/maharashtra/pune', views.fertilityClinicsPune, name='fertilityClinicsPune'),
    path('fertility-clinics/india/telangana/warangal', views.fertilityClinicsWarangal, name='fertilityClinicsWarangal'),
    path('fertility-clinics/india/telangana/gachibowli', views.fertilityClinicsGachibowli, name='fertilityClinicsGachibowli'),
    path('fertility-clinics/india/telangana/madhapur', views.fertilityClinicsMadhapur, name='fertilityClinicsMadhapur'),
    path('fertility-clinics/india/uttar-pradesh/noida', views.fertilityClinicsNoida, name='fertilityClinicsNoida'),
    path('fertility-clinics/india/uttar-pradesh/meerut', views.fertilityClinicsMeerut, name='fertilityClinicsMeerut'),
    path('fertility-clinics/india/uttarakhand/haldwani', views.fertilityClinicsHaldwani, name='fertilityClinicsHaldwani'),

    # Greece
    path('fertility-clinics/greece/athens', views.fertilityClinicsAthens, name='fertilityClinicsAthens'),
    path('fertility-clinics/greece/thessaloniki', views.fertilityClinicsThessaloniki, name='fertilityClinicsThessaloniki'),

    # Cyprus
    path('fertility-clinics/cyprus/nicosia', views.fertilityClinicsNicosia, name='fertilityClinicsNicosia'),
    path('fertility-clinics/cyprus/girne', views.fertilityClinicsGirne, name='fertilityClinicsGirne'),
]
