from django.shortcuts import render, get_object_or_404
from clinic.models import BasicClinic
from coaches.models import SnippetCity
from .models import BestClinicArticleCity


def bestivfclinicsinprague(request):
    pkid = 1

    clinics = BasicClinic.objects.all().exclude(is_published=False)

    best_clinics = clinics.filter(best_article_city_blogpost_obj=pkid).exclude(best_article_city_actual_text__isnull=True).exclude(best_article_city_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_city_boolean=True).order_by('-digitalTransparencyIndex')[:5]

    clinics_location_count = clinics.filter(clinicRegion__iexact='Prague')
    clinics_location_count = clinics_location_count.count()

    best_clinics_count = best_clinics.count()
    best_clinics_blogpost = get_object_or_404(BestClinicArticleCity, pk=pkid)
    author = best_clinics_blogpost.author

    snippets = SnippetCity.objects.filter(blog=pkid, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    if count_snippets == 1:
        snippets = SnippetCity.objects.get(blog=pkid, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'best_clinics': best_clinics,
            'blog': best_clinics_blogpost,
            'author': author,
            'best_clinics_count': best_clinics_count,
            'clinics_location_count': clinics_location_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/best-article/cities/czech-republic/best-ivf-clinic-prague.html', context)
    elif count_snippets > 1:
        snippets = SnippetCountry.objects.filter(blog=pkid, status='is published', owner__coach_is_premium=True,
                                                 owner__coach_is_published=True)

        context = {
            'best_clinics': best_clinics,
            'blog': best_clinics_blogpost,
            'author': author,
            'best_clinics_count': best_clinics_count,
            'clinics_location_count': clinics_location_count,
            'snippets': snippets,
        }

        return render(request, 'blog/best-article/cities/czech-republic/best-ivf-clinic-prague.html', context)
    else:
        context = {
            'best_clinics': best_clinics,
            'blog': best_clinics_blogpost,
            'author': author,
            'best_clinics_count': best_clinics_count,
            'clinics_location_count': clinics_location_count,
        }

        return render(request, 'blog/best-article/cities/czech-republic/best-ivf-clinic-prague.html', context)