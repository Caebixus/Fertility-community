from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from blog.models import Author, Blog

def index(request):
    blog = Blog.objects.all().order_by('-created_at')[:6]

    listing = BasicClinic.objects.all().exclude(is_published=False)
    listing = listing.count

    ukclinics = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').exclude(is_published=False)
    ukclinics = ukclinics.count()

    usclinics = BasicClinic.objects.filter(clinicState__iexact='United States').exclude(is_published=False)
    usclinics = usclinics.count()

    czclinics = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').exclude(is_published=False)
    czclinics = czclinics.count()

    spclinics = BasicClinic.objects.filter(clinicState__iexact='Spain').exclude(is_published=False)
    spclinics = spclinics.count()

    inclinics = BasicClinic.objects.filter(clinicState__iexact='India').exclude(is_published=False)
    inclinics = inclinics.count()

    grclinics = BasicClinic.objects.filter(clinicState__iexact='Greece').exclude(is_published=False)
    grclinics = grclinics.count()

    cyclinics = BasicClinic.objects.filter(clinicState__iexact='Cyprus').exclude(is_published=False)
    cyclinics = cyclinics.count()

    mxclinics = BasicClinic.objects.filter(clinicState__iexact='Mexico').exclude(is_published=False)
    mxclinics = mxclinics.count()

    #UK CITIES
    londonclinics = BasicClinic.objects.filter(clinicRegion__iexact='London').exclude(is_published=False)
    londonclinics = londonclinics.count()

    bristolclinics = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').exclude(is_published=False)
    bristolclinics = bristolclinics.count()

    leedsclinics = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').exclude(is_published=False)
    leedsclinics = leedsclinics.count()

    nottinghamclinics = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').exclude(is_published=False)
    nottinghamclinics = nottinghamclinics.count()

    birminghamclinics = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').exclude(is_published=False)
    birminghamclinics = birminghamclinics.count()

    exeterclinics = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').exclude(is_published=False)
    exeterclinics = exeterclinics.count()

    liverpoolclinics = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').exclude(is_published=False)
    liverpoolclinics = liverpoolclinics.count()

    portsmouthclinics = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').exclude(is_published=False)
    portsmouthclinics = portsmouthclinics.count()

    bournemouthclinics = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').exclude(is_published=False)
    bournemouthclinics = bournemouthclinics.count()

    glasgowclinics = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').exclude(is_published=False)
    glasgowclinics = glasgowclinics.count()

    manchesterclinics = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').exclude(is_published=False)
    manchesterclinics = manchesterclinics.count()

    sheffieldclinics = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').exclude(is_published=False)
    sheffieldclinics = sheffieldclinics.count()

    #CZ REGIONS
    pragueclinics = BasicClinic.objects.filter(clinicRegion__iexact='Prague').exclude(is_published=False)
    pragueclinics = pragueclinics.count()

    brnoclinics = BasicClinic.objects.filter(clinicRegion__iexact='Brno').exclude(is_published=False)
    brnoclinics = brnoclinics.count()

    #US REGIONS
    californiaclinics = BasicClinic.objects.filter(clinicRegion__iexact='California').exclude(is_published=False)
    californiaclinics = californiaclinics.count()

    alabamaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Alabama').exclude(is_published=False)
    alabamaclinics = alabamaclinics.count()

    arizonaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Arizona').exclude(is_published=False)
    arizonaclinics = arizonaclinics.count()

    floridaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Florida').exclude(is_published=False)
    floridaclinics = floridaclinics.count()

    texasclinics = BasicClinic.objects.filter(clinicRegion__iexact='Texas').exclude(is_published=False)
    texasclinics = texasclinics.count()

    newyorkclinics = BasicClinic.objects.filter(clinicRegion__iexact='New York').exclude(is_published=False)
    newyorkclinics = newyorkclinics.count()

    arkansasclinics = BasicClinic.objects.filter(clinicRegion__iexact='Arkansas').exclude(is_published=False)
    arkansasclinics = arkansasclinics.count()

    coloradoclinics = BasicClinic.objects.filter(clinicRegion__iexact='Colorado').exclude(is_published=False)
    coloradoclinics = coloradoclinics.count()

    hawaiiclinics = BasicClinic.objects.filter(clinicRegion__iexact='Hawaii').exclude(is_published=False)
    hawaiiclinics = hawaiiclinics.count()

    utahclinics = BasicClinic.objects.filter(clinicRegion__iexact='Utah').exclude(is_published=False)
    utahclinics = utahclinics.count()

    connecticutclinics = BasicClinic.objects.filter(clinicRegion__iexact='Connecticut').exclude(is_published=False)
    connecticutclinics = connecticutclinics.count()

    delawareclinics = BasicClinic.objects.filter(clinicRegion__iexact='Delaware').exclude(is_published=False)
    delawareclinics = delawareclinics.count()

    georgiaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Georgia').exclude(is_published=False)
    georgiaclinics = georgiaclinics.count()

    illinoisclinics = BasicClinic.objects.filter(clinicRegion__iexact='Illinois').exclude(is_published=False)
    illinoisclinics = illinoisclinics.count()

    newjerseyclinics = BasicClinic.objects.filter(clinicRegion__iexact='New Jersey').exclude(is_published=False)
    newjerseyclinics = newjerseyclinics.count()

    #SP REGIONS
    alicanteclinics = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').exclude(is_published=False)
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').exclude(is_published=False)
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').exclude(is_published=False)
    madridclinics = madridclinics.count()

    malagaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').exclude(is_published=False)
    malagaclinics = malagaclinics.count()

    sevilleclinics = BasicClinic.objects.filter(clinicRegion__iexact='Seville').exclude(is_published=False)
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').exclude(is_published=False)
    valenciaclinics = valenciaclinics.count()

    #IN REGIONS
    chennaiclinics = BasicClinic.objects.filter(clinicCity__iexact='Chennai').exclude(is_published=False)
    chennaiclinics = chennaiclinics.count()

    hyderabadclinics = BasicClinic.objects.filter(clinicCity__iexact='Hyderabad').exclude(is_published=False)
    hyderabadclinics = hyderabadclinics.count()

    mumbaiclinics = BasicClinic.objects.filter(clinicCity__iexact='Mumbai').exclude(is_published=False)
    mumbaiclinics = mumbaiclinics.count()

    patnaclinics = BasicClinic.objects.filter(clinicCity__iexact='Patna').exclude(is_published=False)
    patnaclinics = patnaclinics.count()

    raipurclinics = BasicClinic.objects.filter(clinicCity__iexact='Raipur').exclude(is_published=False)
    raipurclinics = raipurclinics.count()

    amdavadclinics = BasicClinic.objects.filter(clinicCity__iexact='Amdavad').exclude(is_published=False)
    amdavadclinics = amdavadclinics.count()

    chandigarhclinics = BasicClinic.objects.filter(clinicCity__iexact='Chandigarh').exclude(is_published=False)
    chandigarhclinics = chandigarhclinics.count()

    faridabadclinics = BasicClinic.objects.filter(clinicCity__iexact='Faridabad').exclude(is_published=False)
    faridabadclinics = faridabadclinics.count()

    jamshedpurclinics = BasicClinic.objects.filter(clinicCity__iexact='Jamshedpur').exclude(is_published=False)
    jamshedpurclinics = jamshedpurclinics.count()

    bangaloreclinics = BasicClinic.objects.filter(clinicCity__iexact='Bangalore').exclude(is_published=False)
    bangaloreclinics = bangaloreclinics.count()

    trivandrumclinics = BasicClinic.objects.filter(clinicCity__iexact='Trivandrum').exclude(is_published=False)
    trivandrumclinics = trivandrumclinics.count()

    kochiclinics = BasicClinic.objects.filter(clinicCity__iexact='Kochi').exclude(is_published=False)
    kochiclinics = kochiclinics.count()

    bhopalclinics = BasicClinic.objects.filter(clinicCity__iexact='Bhopal').exclude(is_published=False)
    bhopalclinics = bhopalclinics.count()

    indoreclinics = BasicClinic.objects.filter(clinicCity__iexact='Indore').exclude(is_published=False)
    indoreclinics = indoreclinics.count()

    nagpurclinics = BasicClinic.objects.filter(clinicCity__iexact='Nagpur').exclude(is_published=False)
    nagpurclinics = nagpurclinics.count()

    bhubaneswarclinics = BasicClinic.objects.filter(clinicCity__iexact='Bhubaneswar').exclude(is_published=False)
    bhubaneswarclinics = bhubaneswarclinics.count()

    ludhianaclinics = BasicClinic.objects.filter(clinicCity__iexact='Ludhiana').exclude(is_published=False)
    ludhianaclinics = ludhianaclinics.count()

    jaipurclinics = BasicClinic.objects.filter(clinicCity__iexact='Jaipur').exclude(is_published=False)
    jaipurclinics = jaipurclinics.count()

    lucknowclinics = BasicClinic.objects.filter(clinicCity__iexact='Lucknow').exclude(is_published=False)
    lucknowclinics = lucknowclinics.count()

    kanpurclinics = BasicClinic.objects.filter(clinicCity__iexact='Kanpur').exclude(is_published=False)
    kanpurclinics = kanpurclinics.count()

    dehradunclinics = BasicClinic.objects.filter(clinicCity__iexact='Dehradun').exclude(is_published=False)
    dehradunclinics = dehradunclinics.count()

    kolkataclinics = BasicClinic.objects.filter(clinicCity__iexact='Kolkata').exclude(is_published=False)
    kolkataclinics = kolkataclinics.count()

    #GR REGIONS
    athensclinics = BasicClinic.objects.filter(clinicCity__iexact='Athens').exclude(is_published=False)
    athensclinics = athensclinics.count()

    thessalonikiclinics = BasicClinic.objects.filter(clinicCity__iexact='Thessaloniki').exclude(is_published=False)
    thessalonikiclinics = thessalonikiclinics.count()

    #CY REGIONS
    nicosiaclinics = BasicClinic.objects.filter(clinicCity__iexact='Nicosia').exclude(is_published=False)
    nicosiaclinics = nicosiaclinics.count()

    girneclinics = BasicClinic.objects.filter(clinicCity__iexact='Girne').exclude(is_published=False)
    girneclinics = girneclinics.count()

    #MX REGIONS
    cancunclinics = BasicClinic.objects.filter(clinicCity__iexact='Cancún').exclude(is_published=False)
    cancunclinics = cancunclinics.count()

    mexicocityclinics = BasicClinic.objects.filter(clinicCity__iexact='Mexico City').exclude(is_published=False)
    mexicocityclinics = mexicocityclinics.count()

    context = {
        'blog': blog,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'listing': listing,
        'ukclinics': ukclinics,
        'usclinics': usclinics,
        'czclinics': czclinics,
        'spclinics': spclinics,
        'inclinics': inclinics,
        'grclinics': grclinics,
        'cyclinics': cyclinics,
        'mxclinics': mxclinics,
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
        'chennaiclinics': chennaiclinics,
        'hyderabadclinics': hyderabadclinics,
        'mumbaiclinics': mumbaiclinics,
        'patnaclinics': patnaclinics,
        'raipurclinics': raipurclinics,
        'amdavadclinics': amdavadclinics,
        'chandigarhclinics': chandigarhclinics,
        'faridabadclinics': faridabadclinics,
        'jamshedpurclinics': jamshedpurclinics,
        'bangaloreclinics': bangaloreclinics,
        'trivandrumclinics': trivandrumclinics,
        'kochiclinics': kochiclinics,
        'bhopalclinics': bhopalclinics,
        'indoreclinics': indoreclinics,
        'nagpurclinics': nagpurclinics,
        'bhubaneswarclinics': bhubaneswarclinics,
        'ludhianaclinics': ludhianaclinics,
        'jaipurclinics': jaipurclinics,
        'lucknowclinics': lucknowclinics,
        'kanpurclinics': kanpurclinics,
        'dehradunclinics': dehradunclinics,
        'kolkataclinics': kolkataclinics,
        'athensclinics': athensclinics,
        'thessalonikiclinics': thessalonikiclinics,
        'nicosiaclinics': nicosiaclinics,
        'girneclinics': girneclinics,
        'cancunclinics': cancunclinics,
        'mexicocityclinics': mexicocityclinics,
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

def form(request):
    return render(request, 'main/form.html')

def blog(request):
    blog = Blog.objects.all().order_by('-created_at')

    context = {
        'blog': blog,
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
    blog = Blog.objects.all().order_by('-created_at')[:6]

    context = {
        'blog': blog,
    }

    return render(request, 'main/ivf-explained.html', context)
