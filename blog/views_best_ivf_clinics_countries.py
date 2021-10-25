from django.shortcuts import render, get_object_or_404
from clinic.models import BasicClinic
from .models import BestClinicArticleCountry
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


def bestivfclinicsinczech(request):
    pkid = 1

    clinics = BasicClinic.objects.all()

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid)
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]

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


def bestivfclinicsinczechbezin(request):
    return HttpResponsePermanentRedirect(reverse('bestivfclinicsinczech'))