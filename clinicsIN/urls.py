from django.urls import path

from . import views

urlpatterns = [
    #Bengalore
    path('clinics/in/bangalore/kiran-infertility-center-bangalore', views.kiraninfertilitycenterbengaluru, name='kiraninfertilitycenterbengaluru'),
    path('clinics/in/bangalore/mannat-fertility-centre', views.mannatfertilitycentre, name='mannatfertilitycentre'),

    #Gachibowli
    path('clinics/in/gachibowli/hyderabad-women-fertility-centre-gachibowli', views.hyderabadwomenfertilitycentregachibowli, name='hyderabadwomenfertilitycentregachibowli'),

    #Gurugram
    path('clinics/in/gurugram/india-ivf-clinic-gurgaon', views.indiaivfclinicgurgaon, name='indiaivfclinicgurgaon'),

    #Gwalior
    path('clinics/in/gwalior/india-ivf-clinic-gwalior', views.indiaivfclinicgwalior, name='indiaivfclinicgwalior'),

    #Haldwani
    path('clinics/in/haldwani/india-ivf-clinic-haldwani', views.indiaivfclinichaldwani, name='indiaivfclinichaldwani'),

    #Hyderabad
    path('clinics/in/hyderabad/oasis-fertility-hyderabad-banjara-hills', views.oasisfertilityhyderabadbanjarahills, name='oasisfertilityhyderabadbanjarahills'),
    path('clinics/in/hyderabad/oasis-fertility-hyderabad-secunderabad', views.oasisfertilityhyderabadsecunderabad, name='oasisfertilityhyderabadsecunderabad'),
    path('clinics/in/hyderabad/oasis-fertility-hyderabad-dilsukhnagar', views.oasisfertilityhyderabaddilsukhnagar, name='oasisfertilityhyderabaddilsukhnagar'),
    path('clinics/in/hyderabad/oasis-fertility-hyderabad-gachibowli', views.oasisfertilityhyderabadgachibowli, name='oasisfertilityhyderabadgachibowli'),
    path('clinics/in/hyderabad/oasis-fertility-hyderabad-miyapur', views.oasisfertilityhyderabmiyapur, name='oasisfertilityhyderabmiyapur'),
    path('clinics/in/hyderabad/kiran-infertility-center-hyderabad', views.kiraninfertilitycenterhyderabad, name='kiraninfertilitycenterhyderabad'),
    path('clinics/in/hyderabad/kiran-infertility-center-kothapet', views.kiraninfertilitycenterkothapet, name='kiraninfertilitycenterkothapet'),
    path('clinics/in/hyderabad/hegde-fertility-malakpet', views.hegdefertilitymalakpet, name='hegdefertilitymalakpet'),

    #Chennai
    path('clinics/in/chennai/oasis-fertility-chennai', views.oasisfertchennai, name='oasisfertchennai'),
    path('clinics/in/chennai/kiran-infertility-center-chennai', views.kiraninfertilitycenterchennai, name='kiraninfertilitycenterchennai'),

    #Jammu
    path('clinics/in/jammu/india-ivf-clinic-jammu', views.indiaivfclinicjammu, name='indiaivfclinicjammu'),

    #Madhapur
    path('clinics/in/madhapur/hegde-hospital-madhapur', views.hegdehospitalmadhapur, name='hegdehospitalmadhapur'),

    #Meerut
    path('clinics/in/meerut/india-ivf-clinic-meerut', views.indiaivfclinicmeerut, name='indiaivfclinicmeerut'),

    #New Delhi
    path('clinics/in/new-delhi/india-ivf-clinic-new-delhi', views.indiaivfclinicnewdelhi, name='indiaivfclinicnewdelhi'),
    path('clinics/in/new-delhi/select-ivf-new-delhi', views.selectivfnewdelhi, name='selectivfnewdelhi'),
    path('clinics/in/new-delhi/indira-ivf-centre-delhi', views.indiraivfcentredelhi, name='indiraivfcentredelhi'),

    #Noida
    path('clinics/in/noida/india-ivf-clinic-noida', views.indiaivfclinicnoida, name='indiaivfclinicnoida'),

    #Pune
    path('clinics/in/pune/oasis-fertility-pune', views.oasisfertilitypune, name='oasisfertilitypune'),

    #Ranchi
    path('clinics/in/ranchi/oasis-fertility-ranchi', views.oasisfertilityranchi, name='oasisfertilityranchi'),
    path('clinics/in/ranchi/india-ivf-clinic-ranchi', views.indiaivfclinicranchi, name='indiaivfclinicranchi'),

    #Rohtak
    path('clinics/in/rohtak/india-ivf-clinic-rohtak', views.indiaivfclinicrohtak, name='indiaivfclinicrohtak'),

    #Vadodara
    path('clinics/in/vadodara/oasis-fertility-vadodara', views.oasisfertilityvadodara, name='oasisfertilityvadodara'),

    #Vijayawada
    path('clinics/in/vijayawada/oasis-fertility-vijayawada', views.oasisfertilityvijayawada, name='oasisfertilityvijayawada'),

    #Visakhapatnam
    path('clinics/in/visakhapatnam/oasis-fertility-visakhapatnam', views.oasisfertilityvisakhapatnam, name='oasisfertilityvisakhapatnam'),

    #Warangal
    path('clinics/in/warangal/oasis-fertility-warangal', views.oasisfertilitywarangal, name='oasisfertilitywarangal'),
    ]
