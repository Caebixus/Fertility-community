from django.shortcuts import render, get_object_or_404
from blog.models import Author, Blog
from packages.models import Package
from django.utils import timezone
from clinic.models import BasicClinic
from django.db.models import Avg

#Authors
def authorlisaholliman(request):
    blogpk=6
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=blogpk)
    blog = author.entries.all()

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/authors/lisa-holliman.html', context)


def ivfabroadcosts(request):
    blogpk=7
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)

def fertilityTreatmentAbroadWhatYouNeedToKnow(request):
    blogpk=8
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/IVF-abroad/fertility-treatment-abroad-what-you-need-to-know.html', context)

def ivfabroadpackages(request):
    blogpk=9
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)[:3]
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)[:3]
    count = listing.count()

    order_data = list(ppqlisting) + list(prolisting)

    context = {
        'listing': listing,
        'count': count,
        'order_data': order_data,
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/Packages/ivf-abroad-packages.html', context)

def everythingYouNeedToKnowAboutNaturalIvf(request):
    blogpk=10
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/everything-you-need-to-know-about-natural-ivf.html', context)

def whatismildminiivf(request):
    blogpk=11
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/what-is-mild-mini-ivf.html', context)

def fertilitytreatmentshowamericanscomparewiththerestoftheworld(request):
    blogpk=12
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/research/fertility-treatments-how-americans-compare-with-the-rest-of-the-world.html', context)

def whydoesivffails(request):
    blogpk=13
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/why-does-ivf-fails.html', context)

def whatisicsitreatment(request):
    blogpk=14
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/what-is-icsi-treatment.html', context)

def whydoesivfcostsomuch(request):
    blogpk=15
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=blogpk)

    usclinics = BasicClinic.objects.all()
    usclinics = usclinics.filter(is_published=True).filter(clinicState__iexact='United States')
    countclinicsusa = usclinics.count()

    usclinicivf = usclinics.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    usclinicivf2 = usclinicivf['average'] * 2
    usclinicivf3 = usclinicivf['average'] * 3

    usclinicegg = usclinics.aggregate(average=Avg('egg_donor_recipients_cost'))
    usclinicembryo = usclinics.aggregate(average=Avg('embryo_donor_recipients_cost'))
    usclinicsperm = usclinics.aggregate(average=Avg('sperm_donor_recipients_cost'))
    usclinicicsi = usclinics.aggregate(average=Avg('icsi_treatment_cost'))
    uscliniciui = usclinics.aggregate(average=Avg('iui_treatment_cost'))

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
        'usclinicivf': usclinicivf,
        'usclinicegg': usclinicegg,
        'usclinicembryo': usclinicembryo,
        'usclinicsperm': usclinicsperm,
        'usclinicicsi': usclinicicsi,
        'uscliniciui': uscliniciui,
        'countclinicsusa': countclinicsusa,
        'usclinicivf2': usclinicivf2,
        'usclinicivf3': usclinicivf3,
    }

    return render(request, 'blog/educational/why-does-ivf-cost-so-much.html', context)

def whatisivfwitheggdonation(request):
    blogpk=16
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=blogpk)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/ivf-with-egg-donation-process.html', context)