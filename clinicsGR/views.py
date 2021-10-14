from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

#Thessaloniki
def newlifeivfclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryoclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryolab(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

#Athens
def serumivfcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def ivfathenscenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embryolandivfcenterathens(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def embiomedicalcenter(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def mitosisivfclinic(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def eugoniaassistedreproductionunit(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

#Chania
def mediterraneanfertilityinstitute(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))
