from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from clinic.models import BasicClinic

from .models import BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity

from packages.models import Package

def bestivfclinicsinczech(request):
    pkid = 1

    clinics = BasicClinic.objects.all()

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid)
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')

    clinics_location_count = clinics.filter(clinicState='Czech Republic')
    clinics_location_count = clinics_location_count.count()

    best_clinics_count = best_clinics.count()

    best_clinics_blogpost = get_object_or_404(BestClinicArticleCountry, pk=pkid)

    context = {
        'best_clinics': best_clinics,
        'best_clinics_blogpost': best_clinics_blogpost,
        'best_clinics_count': best_clinics_count,
        'clinics_location_count': clinics_location_count,
    }

    return render(request, 'blog/best-article/countries/czech-republic/best-clinic-country-CZ.html', context)
