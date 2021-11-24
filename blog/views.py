from django.shortcuts import render, get_object_or_404
from blog.models import Author, Blog
from packages.models import Package
from django.utils import timezone

#Authors
def authorlisaholliman(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = author.entries.all()

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/authors/lisa-holliman.html', context)


def ivfabroadcosts(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=7)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)

def fertilityTreatmentAbroadWhatYouNeedToKnow(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=8)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/IVF-abroad/fertility-treatment-abroad-what-you-need-to-know.html', context)

def ivfabroadpackages(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=9)

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
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=10)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/everything-you-need-to-know-about-natural-ivf.html', context)

def whatismildminiivf(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=11)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/what-is-mild-mini-ivf.html', context)

def fertilitytreatmentshowamericanscomparewiththerestoftheworld(request):
    otherBlogs = Blog.objects.order_by('-created_at')[:3]

    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=12)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/research/fertility-treatments-how-americans-compare-with-the-rest-of-the-world.html', context)

def whydoesivffails(request):
    otherBlogs = Blog.objects.order_by('-created_at')[1:4]
    author = get_object_or_404(Author, pk=7)
    blog = get_object_or_404(Blog, pk=13)

    context = {
        'author': author,
        'blog': blog,
        'otherBlogs': otherBlogs,
    }

    return render(request, 'blog/educational/why-does-ivf-fails.html', context)