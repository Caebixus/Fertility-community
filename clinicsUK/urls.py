from django.urls import path

from . import views

urlpatterns = [
    #ABERDEEN
    path('clinics/uk/aberdeen/aberdeen-fertility-centre', views.aberfercen, name='aberfercen'),
    #BATH
    path('clinics/uk/bath/care-fertility-bath', views.carefertbath, name='carefertbath'),
    #BELFAST
    path('clinics/uk/belfast/belfast-fertility', views.belffert, name='belffert'),
    #BIRMINGHAM
    path('clinics/uk/birmingham/care-fertility-birmingham', views.carefertbirmingh, name='carefertbirmingh'),
    path('clinics/uk/birmingham/create-fertility-birmingham', views.createfertbirmin, name='createfertbirmin'),
    path('clinics/uk/birmingham/bmi-the-priory-hospital', views.bmitheprioryhosp, name='bmitheprioryhosp'),
    path('clinics/uk/birmingham/care-fertility-tamworth', views.careferttamworth, name='careferttamworth'),
    path('clinics/uk/birmingham/st-judes-fertility-clinic', views.stjudesfertclinic, name='stjudesfertclinic'),
    #BOURNEMOUTH
    path('clinics/uk/bournemouth/complete-fertility-centre-bournemouth', views.completefertcentbourn, name='completefertcentbourn'),
    path('clinics/uk/bournemouth/poundbury-fertility-dorset', views.poundburyfertdorset, name='poundburyfertdorset'),
    #BRIGHTON
    path('clinics/uk/brighton-and-hove/brighton-fertility-associates', views.brightfertasso, name='brightfertasso'),
    path('clinics/uk/brighton-and-hove/agora-gynaecology-and-fertility-centre', views.agoragynandfertcentre, name='agoragynandfertcentre'),
    #BRISTOL
    path('clinics/uk/bristol/abc-ivf-bristol', views.abcivfbristol, name='abcivfbristol'),
    path('clinics/uk/bristol/bristol-centre-for-reproductive-medicine', views.bristolcentreforrepromedicine, name='bristolcentreforrepromedicine'),
    path('clinics/uk/bristol/crgw-bristol', views.crgwbristol, name='crgwbristol'),
    path('clinics/uk/bristol/create-fertility-bristol', views.createfertbristol, name='createfertbristol'),
    path('clinics/uk/bristol/bristol-centre-for-reproductive-medicine-spire-clinic', views.bristolcenforrepromedspireclinic, name='bristolcenforrepromedspireclinic'),
    path('clinics/uk/bristol/london-womens-clinic-bristol', views.londonwomensclinicbristol, name='londonwomensclinicbristol'),
    #CAMBRIDGE
    path('clinics/uk/cambridge/bourn-hall-clinic-cambridge', views.bournhallcliniccambridge, name='bournhallcliniccambridge'),
    path('clinics/uk/cambridge/cambridge-ivf', views.cambridgeivf, name='cambridgeivf'),
    #CARDIFF
    path('clinics/uk/cardiff/crgw-cardiff', views.crgwcardiff, name='crgwcardiff'),
    path('clinics/uk/cardiff/london-womens-clinic-cardiff', views.londonwomenscliniccardiff, name='londonwomenscliniccardiff'),
    path('clinics/uk/cardiff/wales-fertility-institute-cardiff', views.walesfertilityinstitutecardiff, name='walesfertilityinstitutecardiff'),
    #COLCHESTER
    path('clinics/uk/colchester/bourn-hall-clinic-colchester', views.bournhallcliniccolchester, name='bournhallcliniccolchester'),
    #DERBY
    path('clinics/uk/derby/nurture-fertility-burton-satellite-clinic', views.nurturefertburtsatclinic, name='nurturefertburtsatclinic'),
    #EXETER
    path('clinics/uk/exeter/fertility-exeter', views.fertilityexeter, name='fertilityexeter'),
    #GLASGOW
    path('clinics/uk/glasgow/gcrm-fertility', views.gcrmfertilityglasgow, name='gcrmfertilityglasgow'),
    path('clinics/uk/glasgow/semovo-glasgow', views.semovoglasgow, name='semovoglasgow'),
    #KINGSTON UPON HULL
    path('clinics/uk/kingston-upon-hull/hull-ivf-unit', views.hullivfunit, name='hullivfunit'),
    #CHELMSFORD
    path('clinics/uk/chelmsford/simply-fertility', views.simplyfertilitychelm, name='simplyfertilitychelm'),
    path('clinics/uk/chelmsford/bourn-hall-clinic-wickford', views.bournhallclinicwockford, name='bournhallclinicwockford'),
    #LEEDS
    path('clinics/uk/leeds/leeds-fertility-clinic', views.leedsfertilityclinic, name='leedsfertilityclinic'),
    path('clinics/uk/leeds/semovo-leeds', views.semovoleeds, name='semovoleeds'),
    #LEICESTER
    path('clinics/uk/leicester/xy-fertility', views.xyfertility, name='xyfertility'),
    #LIVERPOOL
    path('clinics/uk/liverpool/care-fertility-chester', views.carefertilitychester, name='carefertilitychester'),
    path('clinics/uk/liverpool/care-fertility-liverpool', views.carefertilityliverpool, name='carefertilityliverpool'),
    path('clinics/uk/liverpool/the-hewitt-fertility-centre-liverpool', views.thehewittfertilitycentreliverpool, name='thehewittfertilitycentreliverpool'),
    path('clinics/uk/liverpool/semovo-liverpool', views.semovoliverpool, name='semovoliverpool'),
    path('clinics/uk/liverpool/centre-for-reproductive-health', views.centreforreproductivehealth, name='centreforreproductivehealth'),
    #LONDON
    path('clinics/uk/london/london-womens-clinic-brentwood', views.londonwomensclinicbrentwood, name='londonwomensclinicbrentwood'),
    path('clinics/uk/london/london-womens-clinic-harrow', views.londonwomensclinicharrow, name='londonwomensclinicharrow'),
    path('clinics/uk/london/abc-ivf-harley-street', views.abcivfharleystreet, name='abcivfharleystreet'),
    path('clinics/uk/london/abc-ivf-wimbledon', views.abcivfwimbledon, name='abcivfwimbledon'),
    path('clinics/uk/london/assisted-reproduction-and-gynaecology-centre', views.assistedreproandgynaecologycentre, name='assistedreproandgynaecologycentre'),
    path('clinics/uk/london/city-fertility', views.cityfertility, name='cityfertility'),
    path('clinics/uk/london/create-fertility-st-pauls', views.createfertistpauls, name='createfertistpauls'),
    path('clinics/uk/london/fertility-plus-fertility-clinic', views.fertilityplusfertilityclinic, name='fertilityplusfertilityclinic'),
    path('clinics/uk/london/london-womens-clinic-harley-street', views.londonwomensclinicharleystreet, name='londonwomensclinicharleystreet'),
    path('clinics/uk/london/poundbury-fertility-london', views.poundburyfertilitylondon, name='poundburyfertilitylondon'),
    path('clinics/uk/london/semovo-london', views.semovolondon, name='semovolondon'),
    path('clinics/uk/london/london-womens-clinic-london-bridge', views.londonwomenscliniclondonbridge, name='londonwomenscliniclondonbridge'),
    path('clinics/uk/london/thames-valley-fertility', views.thamesvalleyfertility, name='thamesvalleyfertility'),
    path('clinics/uk/london/ivf-london-elstree', views.ivflondonelstree, name='ivflondonelstree'),
    path('clinics/uk/london/herts-and-essex-fertility-centre', views.hertsandessexfertilitycentre, name='hertsandessexfertilitycentre'),
    path('clinics/uk/london/boston-place', views.bostonplace, name='bostonplace'),
    path('clinics/uk/london/care-fertility-london', views.carefertilitylondon, name='carefertilitylondon'),
    path('clinics/uk/london/concept-fertility', views.conceptfertility, name='conceptfertility'),
    path('clinics/uk/london/create-fertility-wimbledon', views.createfertilitywimbledon, name='createfertilitywimbledon'),
    path('clinics/uk/london/evewell', views.evewell, name='evewell'),
    path('clinics/uk/london/the-fertility-gynaecology-academy', views.thefertilitygynaecologyacademy, name='thefertilitygynaecologyacademy'),
    path('clinics/uk/london/harley-street-fertility-clinic', views.harleystreetfertilityclinic, name='harleystreetfertilityclinic'),
    path('clinics/uk/london/homerton-fertility-centre', views.homertonfertilitycentre, name='homertonfertilitycentre'),
    path('clinics/uk/london/ivi-london', views.ivilondon, name='ivilondon'),
    path('clinics/uk/london/kings-fertility', views.kingsfertility, name='kingsfertility'),
    path('clinics/uk/london/lister-fertility-clinic', views.listerfertilityclinic, name='listerfertilityclinic'),
    path('clinics/uk/london/create-fertility-hertfordshire', views.createfertilityhertfordshire, name='createfertilityhertfordshire'),
    #MANCHESTER
    path('clinics/uk/manchester/manchester-fertility', views.manchesterfertility, name='manchesterfertility'),
    path('clinics/uk/manchester/semovo-manchester-south', views.semovomanchestersouth, name='semovomanchestersouth'),
    path('clinics/uk/manchester/the-hewitt-fertility-centre-knutsford', views.thehewittfertilitycentreknutsford, name='thehewittfertilitycentreknutsford'),
    path('clinics/uk/manchester/aurora-reproductive-healthcare-altrincham', views.aurorareprohealthaltrincham, name='aurorareprohealthaltrincham'),
    path('clinics/uk/manchester/abc-ivf-manchester', views.abcivfmanchester, name='abcivfmanchester'),
    path('clinics/uk/manchester/create-fertility-manchester', views.createfertilitymanchester, name='createfertilitymanchester'),
    path('clinics/uk/manchester/semovo-manchester-city-centre', views.semovomanchestercitycentre, name='semovomanchestercitycentre'),
    path('clinics/uk/manchester/fertility-fusion', views.fertilityfusion, name='fertilityfusion'),
    path('clinics/uk/manchester/care-fertility-manchester', views.carefertilitymanchester, name='carefertilitymanchester'),
    #MIDDLESBROUGH
    path('clinics/uk/middlesbrough/london-womens-clinic-darlington', views.londonwomensclinicdarlington, name='londonwomensclinicdarlington'),
    #NEWCASTLE
    path('clinics/uk/newcastle-upon-tyne/newcastle-fertility-centre', views.newcastlefertilitycentre, name='newcastlefertilitycentre'),
    #NORWICH
    path('clinics/uk/norwich/bourn-hall-clinic-norwich', views.bournhallclinicnorwich, name='bournhallclinicnorwich'),
    #NOTTINGHAM
    path('clinics/uk/nottingham/nurture-fertility-nottingham', views.nurturefertilitynottingham, name='nurturefertilitynottingham'),
    path('clinics/uk/nottingham/care-fertility-nottingham', views.carefertilitynottingham, name='carefertilitynottingham'),
    #OXFORD
    path('clinics/uk/oxford/create-fertility-oxford', views.createfertilityoxford, name='createfertilityoxford'),
    path('clinics/uk/oxford/oxford-fertility', views.oxfordfertility, name='oxfordfertility'),
    path('clinics/uk/oxford/abc-ivf-oxford', views.abcivfoxford, name='abcivfoxford'),
    #PETERBOROUGH
    path('clinics/uk/peterborough/bourn-hall-clinic-peterborough', views.bournhallclinicpeterborough, name='bournhallclinicpeterborough'),
    #PLYMOUTH
    path('clinics/uk/plymouth/crgw-plymouth', views.crgwplymouth, name='crgwplymouth'),
    #PORTSMOUTH
    path('clinics/uk/portsmouth/complete-fertility-centre-portsmouth', views.completefertilitycentreportsmouth, name='completefertilitycentreportsmouth'),
    #SALISBURY
    path('clinics/uk/salisbury/salisbury-fertility-centre', views.salisburyfertcentre, name='salisburyfertcentre'),
    #SHEFFIELD
    path('clinics/uk/sheffield/nurture-fertility-chesterfield', views.nurturefertilitychesterfield, name='nurturefertilitychesterfield'),
    path('clinics/uk/sheffield/care-fertility-sheffield', views.carefertilitysheffield, name='carefertilitysheffield'),
    #SOUTHAMPTON
    path('clinics/uk/southampton/complete-fertility-centre-southampton', views.completefertilitycentresouthampton, name='completefertilitycentresouthampton'),
    path('clinics/uk/southampton/wessex-fertility', views.wessexfertility, name='wessexfertility'),
    #SWANSEA
    path('clinics/uk/swansea/wales-fertility-institute-neath', views.walesfertilityinstituteneath, name='walesfertilityinstituteneath'),
    path('clinics/uk/swansea/crgw-swansea', views.crgwswansea, name='crgwswansea'),
    path('clinics/uk/swansea/london-womens-clinic-swansea', views.londonwomensclinicswansea, name='londonwomensclinicswansea'),
]
