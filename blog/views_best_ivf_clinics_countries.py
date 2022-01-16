from django.shortcuts import render, get_object_or_404
from clinic.models import BasicClinic
from .models import BestClinicArticleCountry
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

clinics = BasicClinic.objects.all()

def bestivfclinicsinczechbezin(request):
    return HttpResponsePermanentRedirect(reverse('bestivfclinicsinczech'))

def bestivfclinicsinczech(request):
    pkid = 1

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]

    clinics_location_count = clinics.filter(clinicState='Czech Republic').exclude(is_published=False)
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

def bestivfclinicsinspain(request):
    pkid = 2

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]

    clinics_location_count = clinics.filter(clinicState='Spain').exclude(is_published=False)
    clinics_location_count = clinics_location_count.count()

    best_clinics_count = best_clinics.count()

    best_clinics_blogpost = get_object_or_404(BestClinicArticleCountry, pk=pkid)

    context = {
        'best_clinics': best_clinics,
        'best_clinics_blogpost': best_clinics_blogpost,
        'best_clinics_count': best_clinics_count,
        'clinics_location_count': clinics_location_count,
    }

    return render(request, 'blog/best-article/countries/spain/best-clinic-country-SP.html', context)

def bestivfclinicsingreece(request):
    pkid = 3

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:5]

    clinics_location_count = clinics.filter(clinicState='Greece').exclude(is_published=False)
    clinics_location_count = clinics_location_count.count()

    best_clinics_count = best_clinics.count()

    best_clinics_blogpost = get_object_or_404(BestClinicArticleCountry, pk=pkid)

    context = {
        'best_clinics': best_clinics,
        'best_clinics_blogpost': best_clinics_blogpost,
        'best_clinics_count': best_clinics_count,
        'clinics_location_count': clinics_location_count,
    }

    return render(request, 'blog/best-article/countries/greece/best-clinic-country-GR.html', context)

def bestivfclinicsinslovakia(request):
    pkid = 4

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:5]

    clinics_location_count = clinics.filter(clinicState='Slovakia').exclude(is_published=False)
    clinics_location_count = clinics_location_count.count()

    best_clinics_count = best_clinics.count()

    best_clinics_blogpost = get_object_or_404(BestClinicArticleCountry, pk=pkid)

    context = {
        'best_clinics': best_clinics,
        'best_clinics_blogpost': best_clinics_blogpost,
        'best_clinics_count': best_clinics_count,
        'clinics_location_count': clinics_location_count,
    }

    return render(request, 'blog/best-article/countries/slovakia/best-clinic-country-SK.html', context)