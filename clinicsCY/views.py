from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

#Nicosia
def cyprusivfcentre(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def britishcyprusivfhospital(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def eurocareivf(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def dogusfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def pedieosivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

#Famagusta
def crownivfcyprus(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

#Girne
def dunyaivfcyprusfertilityclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))

def kyreniaivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))
