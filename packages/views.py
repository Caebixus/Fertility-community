from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

def packages1(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def ivfpackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def eggpackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def embryopackages(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))
