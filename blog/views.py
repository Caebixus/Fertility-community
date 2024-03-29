from django.shortcuts import render, get_object_or_404

from blog.functions import count_best_clinics_city, count_best_clinics_country
from blog.models import Author, Blog
from packages.models import Package
from django.utils import timezone
from clinic.models import BasicClinic
from django.db.models import Avg
from django.views.generic.detail import DetailView

from coaches.models import Snippet, Coaches


#Authors
class AuthorDetailView(DetailView):
    model = Author
    template_name = '../templates/blog/authors/author-detail-view.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()

        otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=author.id)[:3]
        context['otherBlogs'] = otherBlogs

        blog = author.entries.all()
        context['blog'] = blog

        return context


def ivfabroadcosts(request):
    blogpk=7
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)


def fertilityTreatmentAbroadWhatYouNeedToKnow(request):
    blogpk=8
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/fertility-treatment-abroad-what-you-need-to-know.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/fertility-treatment-abroad-what-you-need-to-know.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/IVF-abroad/fertility-treatment-abroad-what-you-need-to-know.html', context)


def ivfabroadpackages(request):
    blogpk=9
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    todayDate = timezone.now()

    listing = Package.objects.all()
    prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
    count = listing.count()

    prolisting = prolisting.order_by('-package_end_list_date')[:3]
    ppqlisting = ppqlisting.order_by('-package_end_list_date')[:3]

    order_data = list(ppqlisting) + list(prolisting)

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'listing': listing,
            'count': count,
            'order_data': order_data,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/Packages/ivf-abroad-packages.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'listing': listing,
            'count': count,
            'order_data': order_data,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/Packages/ivf-abroad-packages.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
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

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/everything-you-need-to-know-about-natural-ivf.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/everything-you-need-to-know-about-natural-ivf.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/everything-you-need-to-know-about-natural-ivf.html', context)


def whatismildminiivf(request):
    blogpk=11
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/what-is-mild-mini-ivf.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/what-is-mild-mini-ivf.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/what-is-mild-mini-ivf.html', context)


def fertilitytreatmentshowamericanscomparewiththerestoftheworld(request):
    blogpk=12
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/research/fertility-treatments-how-americans-compare-with-the-rest-of-the-world.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/research/fertility-treatments-how-americans-compare-with-the-rest-of-the-world.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/research/fertility-treatments-how-americans-compare-with-the-rest-of-the-world.html', context)


def whydoesivffails(request):
    blogpk=13
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/why-does-ivf-fails.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/why-does-ivf-fails.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/why-does-ivf-fails.html', context)


def whatisicsitreatment(request):
    blogpk=14
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/what-is-icsi-treatment.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/what-is-icsi-treatment.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/what-is-icsi-treatment.html', context)


def whydoesivfcostsomuch(request):
    blogpk=15
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

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

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
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
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/why-does-ivf-cost-so-much.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
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
            'snippets': snippets,
        }

        return render(request, 'blog/educational/why-does-ivf-cost-so-much.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
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

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/ivf-with-egg-donation-process.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/ivf-with-egg-donation-process.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/ivf-with-egg-donation-process.html', context)


def ivf_in_spain(request):
    blogpk=18
    pkid = 2
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    clinics = BasicClinic.objects.all().filter(clinicState__iexact='Spain')
    numclinics = clinics.filter(is_published=True).filter(clinicState__iexact='Spain')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(
        best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]
    best_clinics_count = best_clinics.count()

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-spain.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-spain.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-spain.html', context)


def ivf_in_greece(request):
    blogpk=19
    pkid = 3
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    clinics = BasicClinic.objects.all().filter(clinicState__iexact='Greece')
    numclinics = clinics.filter(is_published=True).filter(clinicState__iexact='Greece')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(
        best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]
    best_clinics_count = best_clinics.count()

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-greece.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-greece.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-greece.html', context)


def ivf_in_czech_republic(request):
    blogpk=20
    pkid = 1
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    clinics = BasicClinic.objects.all().filter(clinicState__iexact='Czech Republic')
    numclinics = clinics.filter(is_published=True).filter(clinicState__iexact='Czech Republic')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(
        best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]
    best_clinics_count = best_clinics.count()

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-czech-republic.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-czech-republic.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-czech-republic.html', context)


def ivf_in_slovakia(request):
    blogpk=21
    pkid = 4
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    clinics = BasicClinic.objects.all().filter(clinicState__iexact='Slovakia')
    numclinics = clinics.filter(is_published=True).filter(clinicState__iexact='Slovakia')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(
        best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]
    best_clinics_count = best_clinics.count()

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-slovakia.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-slovakia.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-slovakia.html', context)


def ivf_in_prague(request):
    blogpk=22
    pkid = 1
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    clinics = BasicClinic.objects.all().filter(clinicCity__iexact='Prague')
    numclinics = clinics.filter(is_published=True).filter(clinicCity__iexact='Prague')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics_count = count_best_clinics_city(clinics)

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-prague.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-prague.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-prague.html', context)


def ivfmeditation(request):
    blogpk=23
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/educational/ivf-and-meditation.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/educational/ivf-and-meditation.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/educational/ivf-and-meditation.html', context)


def ivf_in_portugal(request):
    blogpk=24
    pkid = 5 #ID pro Best IVF clinics in ...
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]
    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    clinics = BasicClinic.objects.all().filter(clinicState__iexact='Portugal')
    numclinics = clinics.filter(is_published=True).filter(clinicState__iexact='Portugal')
    numclinics = numclinics.count()

    clinicegg = clinics.aggregate(average=Avg('egg_donor_recipients_cost'))

    best_clinics = clinics.filter(best_article_country_blogpost_obj=pkid).exclude(
        best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics = best_clinics.filter(best_article_country_boolean=True).order_by('-digitalTransparencyIndex')[:8]
    best_clinics_count = best_clinics.count()

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/IVF-abroad/ivf-in-portugal.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
            'snippets': snippets,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-portugal.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'clinicegg': clinicegg,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'numclinics': numclinics,
            'best_clinics_count': best_clinics_count,
        }

        return render(request, 'blog/IVF-abroad/ivf-in-portugal.html', context)


def pragueivfreviews(request):
    blogpk=25
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/informational&supportive/reviews-on-ivf-treatment-in-prague.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/informational&supportive/reviews-on-ivf-treatment-in-prague.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/informational&supportive/reviews-on-ivf-treatment-in-prague.html', context)


def ivfstepbystep(request):
    blogpk=26
    otherBlogs = Blog.objects.order_by('-created_at').exclude(pk=blogpk)[:3]

    blog = get_object_or_404(Blog, pk=blogpk)
    author = blog.author

    snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
    count_snippets = snippets.count()

    reviewed_by = Coaches.objects.filter(blog_best_country_review=blogpk)
    coach_premium = Coaches.objects.filter(coach_is_premium=True)

    if count_snippets == 1:
        snippets = Snippet.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
            'one_snippet': 'one_snippet',
        }

        return render(request, 'blog/informational&supportive/ivf-step-by-step.html', context)
    elif count_snippets > 1:
        snippets = Snippet.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)

        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
            'snippets': snippets,
        }

        return render(request, 'blog/informational&supportive/ivf-step-by-step.html', context)
    else:
        context = {
            'reviewed_by': reviewed_by,
            'coach_premium': coach_premium,
            'author': author,
            'blog': blog,
            'otherBlogs': otherBlogs,
        }

        return render(request, 'blog/informational&supportive/ivf-step-by-step.html', context)