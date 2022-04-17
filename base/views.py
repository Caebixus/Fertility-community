from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

from coaches.models import Snippet, SnippetCity, SnippetState, SnippetCountry, Coaches
from search.choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages
from clinic.models import BasicClinic
from blog.models import Blog, BestClinicArticleCountry, BestClinicArticleCity, BestClinicArticleState

def index(request):
    blog = Blog.objects.all().order_by('-created_at')[:6]

    count_blog1 = Blog.objects.all().count()
    count_blog2 = BestClinicArticleCountry.objects.all().count()
    count_blog3 = BestClinicArticleCity.objects.all().count()
    count_blog4 = BestClinicArticleState.objects.all().count()
    count_blog = count_blog1 + count_blog2 + count_blog3 + count_blog4


    best_city = BestClinicArticleCity.objects.all().order_by('-created_at')[:1]
    best_country = BestClinicArticleCountry.objects.all().order_by('-created_at')[:1]

    listing = BasicClinic.objects.all().exclude(is_published=False)
    listing = listing.count


    context = {
        'blog': blog,
        'count_blog': count_blog,
        'best_city': best_city,
        'best_country': best_country,
        'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA,
        'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE,
        'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'listing': listing,
    }

    return render(request, 'main/index.html', context)

def businessinsiderbacklink(request):
    return HttpResponsePermanentRedirect(reverse('index'))

def forumoldurlredirect(request):
    return HttpResponsePermanentRedirect(reverse('index'))

def backlink2(request):
    return HttpResponsePermanentRedirect(reverse('index'))

def backlink3(request):
    return HttpResponsePermanentRedirect(reverse('index'))

def robots(request):
    return render(request, 'main/robots.txt')

def about(request):
    contributors = Coaches.objects.filter(coach_is_published=True, coach_is_premium=True)

    context = {
        'contributors': contributors,
    }

    return render(request, 'main/about.html', context)

def form(request):
    return render(request, 'main/form.html')

def blog(request):
    blog = Blog.objects.all().order_by('-created_at')

    BestClinicBlogCountry = BestClinicArticleCountry.objects.filter(best_article_country_noindex_sitemap_boolean=True).order_by('-created_at')[:6]
    BestClinicBlogState = BestClinicArticleState.objects.filter(best_article_state_noindex_sitemap_boolean=True).order_by('-created_at')[:6]
    BestClinicBlogCity = BestClinicArticleCity.objects.filter(best_article_city_noindex_sitemap_boolean=True).order_by('-created_at')[:6]

    context = {
        'blog': blog,

        'BestClinicBlogCountry': BestClinicBlogCountry,
        'BestClinicBlogState': BestClinicBlogState,
        'BestClinicBlogCity': BestClinicBlogCity,
    }

    return render(request, 'main/blog.html', context)

def cookies(request):
    return render(request, 'main/cookies.html')

def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy-policy.html')

def contactWebsite(request):
    form = WebsiteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        send_mail(
            'Neregistrovaný user prosí o kontakt',
            'Někdo neregistrovaný napsal na kontaktní formulář - zkontroluj!',
            'info@fertilitycommunity.com',
            ['David.langr@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, 'Your message was sent! We will contact you back as soon as possible!')
        return redirect(index)

    context = {
        'form': form,
    }

    return render(request, 'main/contact.html', context)

def error404(request, exception):
    data = {}
    return render(request,'main/404.html', data)

def error400(request, exception):
    data = {}
    return render(request,'main/400.html', data)

def error500(request):
    data = {}
    return render(request,'main/500.html', data)

# BlogPosts Views --------------------------------------------------------------------------------------------------------

def blog1(request):
    blog = Blog.objects.all().order_by('-created_at')[:6]

    context = {
        'blog': blog,
    }

    return render(request, 'main/ivf-explained.html', context)
