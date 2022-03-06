from django.shortcuts import render, get_object_or_404
from blog.models import Author, Blog
from clinic.models import BasicClinic


def best_ivf_clinics_world(request):
    blogpk=17

    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    clinics = BasicClinic.objects.all().exclude(is_published=False)
    clinics = clinics.filter(singleclinicbestarticletext__clinic_world__in=clinics, singleclinicbestarticletext__best_clinic_world_activated=True)

    best_clinics = clinics.order_by('-digitalTransparencyIndex')[:20]
    best_clinics_count = best_clinics.count()

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'best_clinics': best_clinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/best-article/world/best-clinic-country-world.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'best_clinics': best_clinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/best-article/world/best-clinic-country-world.html', context)
    else:
        context = {
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'best_clinics': best_clinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/best-article/world/best-clinic-country-world.html', context)