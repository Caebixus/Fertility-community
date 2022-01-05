from django.shortcuts import render, get_object_or_404
from blog.models import Author, Blog
from clinic.models import BasicClinic


def best_ivf_clinics_world(request):
    blogpk=17

    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=blogpk)

    clinics = BasicClinic.objects.all().exclude(is_published=False)
    clinics = clinics.filter(singleclinicbestarticletext__clinic_world__in=clinics, singleclinicbestarticletext__best_clinic_world_activated=True)

    best_clinics = clinics.order_by('-digitalTransparencyIndex')[:20]

    best_clinics_count = best_clinics.count()


    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
        'best_clinics': best_clinics,
        'best_clinics_count': best_clinics_count,
    }

    return render(request, 'blog/best-article/world/best-clinic-country-world.html', context)