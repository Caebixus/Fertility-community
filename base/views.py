from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic

def index(request):

    listing = BasicClinic.objects.all()
    listing = listing.count

    ukclinics = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    ukclinics = ukclinics.count()

    usclinics = BasicClinic.objects.filter(clinicState__iexact='United States')
    usclinics = usclinics.count()

    czclinics = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
    czclinics = czclinics.count()

    spclinics = BasicClinic.objects.filter(clinicState__iexact='Spain')
    spclinics = spclinics.count()

    #UK CITIES
    londonclinics = BasicClinic.objects.filter(clinicRegion__iexact='London')
    londonclinics = londonclinics.count()

    bristolclinics = BasicClinic.objects.filter(clinicRegion__iexact='Bristol')
    bristolclinics = bristolclinics.count()

    leedsclinics = BasicClinic.objects.filter(clinicRegion__iexact='Leeds')
    leedsclinics = leedsclinics.count()

    nottinghamclinics = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham')
    nottinghamclinics = nottinghamclinics.count()

    birminghamclinics = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham')
    birminghamclinics = birminghamclinics.count()

    exeterclinics = BasicClinic.objects.filter(clinicRegion__iexact='Exeter')
    exeterclinics = exeterclinics.count()

    liverpoolclinics = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool')
    liverpoolclinics = liverpoolclinics.count()

    portsmouthclinics = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth')
    portsmouthclinics = portsmouthclinics.count()

    bournemouthclinics = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclinics = bournemouthclinics.count()

    glasgowclinics = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow')
    glasgowclinics = glasgowclinics.count()

    manchesterclinics = BasicClinic.objects.filter(clinicRegion__iexact='Manchester')
    manchesterclinics = manchesterclinics.count()

    sheffieldclinics = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield')
    sheffieldclinics = sheffieldclinics.count()

    #CZ REGIONS
    pragueclinics = BasicClinic.objects.filter(clinicRegion__iexact='Prague')
    pragueclinics = pragueclinics.count()

    brnoclinics = BasicClinic.objects.filter(clinicRegion__iexact='Brno')
    brnoclinics = brnoclinics.count()

    #US REGIONS
    californiaclinics = BasicClinic.objects.filter(clinicRegion__iexact='California')
    californiaclinics = californiaclinics.count()

    alabamaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Alabama')
    alabamaclinics = alabamaclinics.count()

    arizonaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Arizona')
    arizonaclinics = arizonaclinics.count()

    floridaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Florida')
    floridaclinics = floridaclinics.count()

    texasclinics = BasicClinic.objects.filter(clinicRegion__iexact='Texas')
    texasclinics = texasclinics.count()

    newyorkclinics = BasicClinic.objects.filter(clinicRegion__iexact='New York')
    newyorkclinics = newyorkclinics.count()

    arkansasclinics = BasicClinic.objects.filter(clinicRegion__iexact='Arkansas')
    arkansasclinics = arkansasclinics.count()

    coloradoclinics = BasicClinic.objects.filter(clinicRegion__iexact='Colorado')
    coloradoclinics = coloradoclinics.count()

    hawaiiclinics = BasicClinic.objects.filter(clinicRegion__iexact='Hawaii')
    hawaiiclinics = hawaiiclinics.count()

    utahclinics = BasicClinic.objects.filter(clinicRegion__iexact='Utah')
    utahclinics = utahclinics.count()

    connecticutclinics = BasicClinic.objects.filter(clinicRegion__iexact='Connecticut')
    connecticutclinics = connecticutclinics.count()

    delawareclinics = BasicClinic.objects.filter(clinicRegion__iexact='Delaware')
    delawareclinics = delawareclinics.count()

    georgiaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Georgia')
    georgiaclinics = georgiaclinics.count()

    illinoisclinics = BasicClinic.objects.filter(clinicRegion__iexact='Illinois')
    illinoisclinics = illinoisclinics.count()

    newjerseyclinics = BasicClinic.objects.filter(clinicRegion__iexact='New Jersey')
    newjerseyclinics = newjerseyclinics.count()

    #SP REGIONS
    alicanteclinics = BasicClinic.objects.filter(clinicRegion__iexact='Alicante')
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona')
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = BasicClinic.objects.filter(clinicRegion__iexact='Madrid')
    madridclinics = madridclinics.count()

    malagaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Malaga')
    malagaclinics = malagaclinics.count()

    sevilleclinics = BasicClinic.objects.filter(clinicRegion__iexact='Seville')
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Valencia')
    valenciaclinics = valenciaclinics.count()

    context = {
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'listing': listing,
        'ukclinics': ukclinics,
        'usclinics': usclinics,
        'czclinics': czclinics,
        'spclinics': spclinics,
        'londonclinics': londonclinics,
        'bristolclinics': bristolclinics,
        'leedsclinics': leedsclinics,
        'nottinghamclinics': nottinghamclinics,
        'birminghamclinics': birminghamclinics,
        'exeterclinics': exeterclinics,
        'liverpoolclinics': liverpoolclinics,
        'portsmouthclinics': portsmouthclinics,
        'bournemouthclinics': bournemouthclinics,
        'glasgowclinics': glasgowclinics,
        'manchesterclinics': manchesterclinics,
        'sheffieldclinics': sheffieldclinics,
        'pragueclinics': pragueclinics,
        'brnoclinics': brnoclinics,
        'californiaclinics': californiaclinics,
        'alabamaclinics': alabamaclinics,
        'arizonaclinics': arizonaclinics,
        'floridaclinics': floridaclinics,
        'texasclinics': texasclinics,
        'newyorkclinics': newyorkclinics,
        'arkansasclinics': arkansasclinics,
        'coloradoclinics': coloradoclinics,
        'hawaiiclinics': hawaiiclinics,
        'utahclinics': utahclinics,
        'connecticutclinics': connecticutclinics,
        'delawareclinics': delawareclinics,
        'georgiaclinics': georgiaclinics,
        'illinoisclinics': illinoisclinics,
        'newjerseyclinics': newjerseyclinics,
        'alicanteclinics': alicanteclinics,
        'barcelonaclinics': barcelonaclinics,
        'madridclinics': madridclinics,
        'malagaclinics': malagaclinics,
        'sevilleclinics': sevilleclinics,
        'valenciaclinics': valenciaclinics,
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

def team(request):
    return render(request, 'main/team.html')

def news(request):
    return render(request, 'main/news.html')

def iframe1(request):
    return render(request, 'main/iframepic1.html')

def travelCalculator(request):
    return render(request, 'main/travel-calculator.html')

def cookies(request):
    return render(request, 'main/cookies.html')

def privacy(request):
    return render(request, 'main/privacy-policy.html')

def contactWebsite(request):
    form = WebsiteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        send_mail(
            'Někdo prosí o kontakt',
            'Obyčejný smrtelník prosí o kontakt - zkontroluj!',
            'langr.marketing@gmail.com',
            ['langr.marketing@gmail.com'],
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
    return render(request, 'main/ivf-explained.html')
