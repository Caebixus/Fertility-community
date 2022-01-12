from django.urls import path

from . import views

urlpatterns = [
    # Czech Republic
    path('fertility-clinics/czech-republic/prague', views.fertilityClinicPrague, name='fertilityClinicPrague'),
    path('fertility-clinics/czech-republic/brno', views.fertilityClinicBrno, name='fertilityClinicBrno'),

    # Slovakia
    path('fertility-clinics/slovakia/bratislava', views.fertilityClinicBratislava, name='fertilityClinicBratislava'),

    # Denmark
    path('fertility-clinics/denmark/copenhagen', views.fertilityClinicCopenhagen, name='fertilityClinicCopenhagen'),

    # United Kingdom
    path('fertility-clinics/uk/aberdeen', views.fertilityClinicsAberdeen, name='fertilityClinicsAberdeen'),
    path('fertility-clinics/uk/bath', views.fertilityClinicsBath, name='fertilityClinicsBath'),
    path('fertility-clinics/uk/belfast', views.fertilityClinicsBelfast, name='fertilityClinicsBelfast'),
    path('fertility-clinics/uk/birmingham', views.fertilityClinicsBirmingham, name='fertilityClinicsBirmingham'),
    path('fertility-clinics/uk/bournemouth', views.fertilityClinicsBournemouth, name='fertilityClinicsBournemouth'),
    path('fertility-clinics/uk/brighton-and-hove', views.fertilityClinicsBrightonHove, name='fertilityClinicsBrightonHove'),
    path('fertility-clinics/uk/bristol', views.fertilityClinicsBristol, name='fertilityClinicsBristol'),
    path('fertility-clinics/uk/cambridge', views.fertilityClinicsCambridge, name='fertilityClinicsCambridge'),
    path('fertility-clinics/uk/cardiff', views.fertilityClinicsCardiff, name='fertilityClinicsCardiff'),
    path('fertility-clinics/uk/colchester', views.fertilityClinicsColchester, name='fertilityClinicsColchester'),
    path('fertility-clinics/uk/derby', views.fertilityClinicsDerby, name='fertilityClinicsDerby'),
    path('fertility-clinics/uk/exeter', views.fertilityClinicsExeter, name='fertilityClinicsExeter'),
    path('fertility-clinics/uk/glasgow', views.fertilityClinicsGlasgow, name='fertilityClinicsGlasgow'),
    path('fertility-clinics/uk/kingston-upon-hull', views.fertilityClinicsHull, name='fertilityClinicsHull'),
    path('fertility-clinics/uk/chelmsford', views.fertilityClinicsChelmsford, name='fertilityClinicsChelmsford'),
    path('fertility-clinics/uk/leeds', views.fertilityClinicsLeeds, name='fertilityClinicsLeeds'),
    path('fertility-clinics/uk/leicester', views.fertilityClinicsLeicester, name='fertilityClinicsLeicester'),
    path('fertility-clinics/uk/liverpool', views.fertilityClinicsLiverpool, name='fertilityClinicsLiverpool'),
    path('fertility-clinics/uk/london', views.fertilityClinicsLondon, name='fertilityClinicsLondon'),
    path('fertility-clinics/uk/manchester', views.fertilityClinicsManchester, name='fertilityClinicsManchester'),
    path('fertility-clinics/uk/middlesbrough', views.fertilityClinicsMiddlesbrough, name='fertilityClinicsMiddlesbrough'),
    path('fertility-clinics/uk/newcastle-upon-tyne', views.fertilityClinicsNewcastle, name='fertilityClinicsNewcastle'),
    path('fertility-clinics/uk/norwich', views.fertilityClinicsNorwich, name='fertilityClinicsNorwich'),
    path('fertility-clinics/uk/nottingham', views.fertilityClinicsNottingham, name='fertilityClinicsNottingham'),
    path('fertility-clinics/uk/oxford', views.fertilityClinicsOxford, name='fertilityClinicsOxford'),
    path('fertility-clinics/uk/peterborough', views.fertilityClinicsPeterborough, name='fertilityClinicsPeterborough'),
    path('fertility-clinics/uk/plymouth', views.fertilityClinicsPlymouth, name='fertilityClinicsPlymouth'),
    path('fertility-clinics/uk/portsmouth', views.fertilityClinicsPortsmouth, name='fertilityClinicsPortsmouth'),
    path('fertility-clinics/uk/salisbury', views.fertilityClinicsSalisbury, name='fertilityClinicsSalisbury'),
    path('fertility-clinics/uk/sheffield', views.fertilityClinicsSheffield, name='fertilityClinicsSheffield'),
    path('fertility-clinics/uk/southampton', views.fertilityClinicsSouthampton, name='fertilityClinicsSouthampton'),
    path('fertility-clinics/uk/swansea', views.fertilityClinicsSwansea, name='fertilityClinicsSwansea'),

    # Spain
    path('fertility-clinics/spain/alicante', views.fertilityClinicsAlicante, name='fertilityClinicsAlicante'),
    path('fertility-clinics/spain/barcelona', views.fertilityClinicsBarcelona, name='fertilityClinicsBarcelona'),
    path('fertility-clinics/spain/madrid', views.fertilityClinicsMadrid, name='fertilityClinicsMadrid'),
    path('fertility-clinics/spain/malaga', views.fertilityClinicsMalaga, name='fertilityClinicsMalaga'),
    path('fertility-clinics/spain/seville', views.fertilityClinicsSeville, name='fertilityClinicsSeville'),
    path('fertility-clinics/spain/valencia', views.fertilityClinicsValencia, name='fertilityClinicsValencia'),

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

    # Germany
    path('fertility-clinics/germany/berlin', views.fertilityClinicBerlin, name='fertilityClinicBerlin'),

    # Portugal
    path('fertility-clinics/portugal/lisbon', views.fertilityClinicLisbon, name='fertilityClinicLisbon'),

    # Latvia
    path('fertility-clinics/latvia/riga', views.fertilityClinicRiga, name='fertilityClinicRiga'),

    # Mexico
    path('fertility-clinics/mexico/cancun', views.fertilityClinicsCancun, name='fertilityClinicsCancun'),
    path('fertility-clinics/mexico/mexico-city', views.fertilityClinicsMexicoCity, name='fertilityClinicsMexicoCity'),

    # --------------------------------------->>>>>>>> Redirects
    path('locations/fertility-clinics-prague', views.fertilityClinicPrague1, name='fertilityClinicPrague1'),
    path('locations/fertility-clinics-brno', views.fertilityClinicBrno1, name='fertilityClinicBrno1'),
    path('fertility-clinics-prague', views.fertilityClinicPrague2, name='fertilityClinicPrague2'),
    path('fertility-clinics-brno', views.fertilityClinicBrno2, name='fertilityClinicBrno2'),

    path('fertility-clinics-aberdeen', views.fertilityClinicsAberdeen1, name='fertilityClinicsAberdeen1'),
    path('fertility-clinics-bath', views.fertilityClinicsBath1, name='fertilityClinicsBath1'),
    path('fertility-clinics-belfast', views.fertilityClinicsBelfast1, name='fertilityClinicsBelfast1'),
    path('fertility-clinics-birmingham', views.fertilityClinicsBirmingham1, name='fertilityClinicsBirmingham1'),
    path('fertility-clinics-bournemouth', views.fertilityClinicsBournemouth1, name='fertilityClinicsBournemouth1'),
    path('fertility-clinics-brighton-hove', views.fertilityClinicsBrightonHove1, name='fertilityClinicsBrightonHove1'),
    path('fertility-clinics-bristol', views.fertilityClinicsBristol1, name='fertilityClinicsBristol1'),
    path('fertility-clinics-cambridge', views.fertilityClinicsCambridge1, name='fertilityClinicsCambridge1'),
    path('fertility-clinics-cardiff', views.fertilityClinicsCardiff1, name='fertilityClinicsCardiff1'),
    path('fertility-clinics-colchester', views.fertilityClinicsColchester1, name='fertilityClinicsColchester1'),
    path('fertility-clinics-derby', views.fertilityClinicsDerby1, name='fertilityClinicsDerby1'),
    path('fertility-clinics-exeter', views.fertilityClinicsExeter1, name='fertilityClinicsExeter1'),
    path('fertility-clinics-glasgow', views.fertilityClinicsGlasgow1, name='fertilityClinicsGlasgow1'),
    path('fertility-clinics-kingston-upon-hull', views.fertilityClinicsHull1, name='fertilityClinicsHull1'),
    path('fertility-clinics-chelmsford', views.fertilityClinicsChelmsford1, name='fertilityClinicsChelmsford1'),
    path('fertility-clinics-leeds', views.fertilityClinicsLeeds1, name='fertilityClinicsLeeds1'),
    path('fertility-clinics-leicester', views.fertilityClinicsLeicester1, name='fertilityClinicsLeicester1'),
    path('fertility-clinics-liverpool', views.fertilityClinicsLiverpool1, name='fertilityClinicsLiverpool1'),
    path('fertility-clinics-london', views.fertilityClinicsLondon1, name='fertilityClinicsLondon1'),
    path('fertility-clinics-manchester', views.fertilityClinicsManchester1, name='fertilityClinicsManchester1'),
    path('fertility-clinics-middlesbrough', views.fertilityClinicsMiddlesbrough1, name='fertilityClinicsMiddlesbrough1'),
    path('fertility-clinics-newcastle', views.fertilityClinicsNewcastle1, name='fertilityClinicsNewcastle1'),
    path('fertility-clinics-norwich', views.fertilityClinicsNorwich1, name='fertilityClinicsNorwich1'),
    path('fertility-clinics-nottingham', views.fertilityClinicsNottingham1, name='fertilityClinicsNottingham1'),
    path('fertility-clinics-oxford', views.fertilityClinicsOxford1, name='fertilityClinicsOxford1'),
    path('fertility-clinics-peterborough', views.fertilityClinicsPeterborough1, name='fertilityClinicsPeterborough1'),
    path('fertility-clinics-plymouth', views.fertilityClinicsPlymouth1, name='fertilityClinicsPlymouth1'),
    path('fertility-clinics-portsmouth', views.fertilityClinicsPortsmouth1, name='fertilityClinicsPortsmouth1'),
    path('fertility-clinics-salisbury', views.fertilityClinicsSalisbury1, name='fertilityClinicsSalisbury1'),
    path('fertility-clinics-sheffield', views.fertilityClinicsSheffield1, name='fertilityClinicsSheffield1'),
    path('fertility-clinics-southampton', views.fertilityClinicsSouthampton1, name='fertilityClinicsSouthampton1'),
    path('fertility-clinics-swansea', views.fertilityClinicsSwansea1, name='fertilityClinicsSwansea1'),

    path('fertility-clinics-alicante', views.fertilityClinicsAlicante1, name='fertilityClinicsAlicante1'),
    path('fertility-clinics-barcelona', views.fertilityClinicsBarcelona1, name='fertilityClinicsBarcelona1'),
    path('fertility-clinics-madrid', views.fertilityClinicsMadrid1, name='fertilityClinicsMadrid1'),
    path('fertility-clinics-malaga', views.fertilityClinicsMalaga1, name='fertilityClinicsMalaga1'),
    path('fertility-clinics-seville', views.fertilityClinicsSeville1, name='fertilityClinicsSeville1'),
    path('fertility-clinics-valencia', views.fertilityClinicsValencia1, name='fertilityClinicsValencia1'),
]
