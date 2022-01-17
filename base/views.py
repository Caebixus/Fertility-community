from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
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

    clinicsall = BasicClinic.objects.all().exclude(is_published=False)

    ukclinics = clinicsall.filter(clinicState__iexact='United Kingdom')
    ukclinics = ukclinics.count()

    usclinics = clinicsall.filter(clinicState__iexact='United States')
    usclinics = usclinics.count()

    czclinics = clinicsall.filter(clinicState__iexact='Czech Republic')
    czclinics = czclinics.count()

    skclinics = clinicsall.filter(clinicState__iexact='Slovakia')
    skclinics = skclinics.count()

    spclinics = clinicsall.filter(clinicState__iexact='Spain')
    spclinics = spclinics.count()

    declinics = clinicsall.filter(clinicState__iexact='Germany')
    declinics = declinics.count()

    lvclinics = clinicsall.filter(clinicState__iexact='Latvia')
    lvclinics = lvclinics.count()

    ptclinics = clinicsall.filter(clinicState__iexact='Portugal')
    ptclinics = ptclinics.count()

    dkclinics = clinicsall.filter(clinicState__iexact='Denmark')
    dkclinics = dkclinics.count()

    inclinics = clinicsall.filter(clinicState__iexact='India')
    inclinics = inclinics.count()

    grclinics = clinicsall.filter(clinicState__iexact='Greece')
    grclinics = grclinics.count()

    cyclinics = clinicsall.filter(clinicState__iexact='Cyprus')
    cyclinics = cyclinics.count()

    mxclinics = clinicsall.filter(clinicState__iexact='Mexico')
    mxclinics = mxclinics.count()

    #UK CITIES
    londonclinics = clinicsall.filter(clinicRegion__iexact='London')
    londonclinics = londonclinics.count()

    bristolclinics = clinicsall.filter(clinicRegion__iexact='Bristol')
    bristolclinics = bristolclinics.count()

    leedsclinics = clinicsall.filter(clinicRegion__iexact='Leeds')
    leedsclinics = leedsclinics.count()

    nottinghamclinics = clinicsall.filter(clinicRegion__iexact='Nottingham')
    nottinghamclinics = nottinghamclinics.count()

    birminghamclinics = clinicsall.filter(clinicRegion__iexact='Birmingham')
    birminghamclinics = birminghamclinics.count()

    exeterclinics = clinicsall.filter(clinicRegion__iexact='Exeter')
    exeterclinics = exeterclinics.count()

    liverpoolclinics = clinicsall.filter(clinicRegion__iexact='Liverpool')
    liverpoolclinics = liverpoolclinics.count()

    portsmouthclinics = clinicsall.filter(clinicRegion__iexact='Portsmouth')
    portsmouthclinics = portsmouthclinics.count()

    bournemouthclinics = clinicsall.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclinics = bournemouthclinics.count()

    glasgowclinics = clinicsall.filter(clinicRegion__iexact='Glasgow')
    glasgowclinics = glasgowclinics.count()

    manchesterclinics = clinicsall.filter(clinicRegion__iexact='Manchester')
    manchesterclinics = manchesterclinics.count()

    sheffieldclinics = clinicsall.filter(clinicRegion__iexact='Sheffield')
    sheffieldclinics = sheffieldclinics.count()

    #CZ REGIONS
    pragueclinics = clinicsall.filter(clinicRegion__iexact='Prague')
    pragueclinics = pragueclinics.count()

    brnoclinics = clinicsall.filter(clinicRegion__iexact='Brno')
    brnoclinics = brnoclinics.count()

    #SK REGIONS
    bratislavaclinics = clinicsall.filter(clinicRegion__iexact='Bratislava')
    bratislavaclinics = bratislavaclinics.count()

    #US REGIONS
    californiaclinics = clinicsall.filter(clinicRegion__iexact='California')
    californiaclinics = californiaclinics.count()

    alabamaclinics = clinicsall.filter(clinicRegion__iexact='Alabama')
    alabamaclinics = alabamaclinics.count()

    arizonaclinics = clinicsall.filter(clinicRegion__iexact='Arizona')
    arizonaclinics = arizonaclinics.count()

    floridaclinics = clinicsall.filter(clinicRegion__iexact='Florida')
    floridaclinics = floridaclinics.count()

    texasclinics = clinicsall.filter(clinicRegion__iexact='Texas')
    texasclinics = texasclinics.count()

    newyorkclinics = clinicsall.filter(clinicRegion__iexact='New York')
    newyorkclinics = newyorkclinics.count()

    arkansasclinics = clinicsall.filter(clinicRegion__iexact='Arkansas')
    arkansasclinics = arkansasclinics.count()

    coloradoclinics = clinicsall.filter(clinicRegion__iexact='Colorado')
    coloradoclinics = coloradoclinics.count()

    hawaiiclinics = clinicsall.filter(clinicRegion__iexact='Hawaii')
    hawaiiclinics = hawaiiclinics.count()

    utahclinics = clinicsall.filter(clinicRegion__iexact='Utah')
    utahclinics = utahclinics.count()

    connecticutclinics = clinicsall.filter(clinicRegion__iexact='Connecticut')
    connecticutclinics = connecticutclinics.count()

    delawareclinics = clinicsall.filter(clinicRegion__iexact='Delaware')
    delawareclinics = delawareclinics.count()

    georgiaclinics = clinicsall.filter(clinicRegion__iexact='Georgia')
    georgiaclinics = georgiaclinics.count()

    illinoisclinics = clinicsall.filter(clinicRegion__iexact='Illinois')
    illinoisclinics = illinoisclinics.count()

    newjerseyclinics = clinicsall.filter(clinicRegion__iexact='New Jersey')
    newjerseyclinics = newjerseyclinics.count()

    #SP REGIONS
    alicanteclinics = clinicsall.filter(clinicRegion__iexact='Alicante')
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = clinicsall.filter(clinicRegion__iexact='Barcelona')
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = clinicsall.filter(clinicRegion__iexact='Madrid')
    madridclinics = madridclinics.count()

    malagaclinics = clinicsall.filter(clinicRegion__iexact='Malaga')
    malagaclinics = malagaclinics.count()

    sevilleclinics = clinicsall.filter(clinicRegion__iexact='Seville')
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = clinicsall.filter(clinicRegion__iexact='Valencia')
    valenciaclinics = valenciaclinics.count()

    #IN REGIONS
    chennaiclinics = clinicsall.filter(clinicCity__iexact='Chennai')
    chennaiclinics = chennaiclinics.count()

    hyderabadclinics = clinicsall.filter(clinicCity__iexact='Hyderabad')
    hyderabadclinics = hyderabadclinics.count()

    mumbaiclinics = clinicsall.filter(clinicCity__iexact='Mumbai')
    mumbaiclinics = mumbaiclinics.count()

    patnaclinics = clinicsall.filter(clinicCity__iexact='Patna')
    patnaclinics = patnaclinics.count()

    raipurclinics = clinicsall.filter(clinicCity__iexact='Raipur')
    raipurclinics = raipurclinics.count()

    amdavadclinics = clinicsall.filter(clinicCity__iexact='Amdavad')
    amdavadclinics = amdavadclinics.count()

    chandigarhclinics = clinicsall.filter(clinicCity__iexact='Chandigarh')
    chandigarhclinics = chandigarhclinics.count()

    faridabadclinics = clinicsall.filter(clinicCity__iexact='Faridabad')
    faridabadclinics = faridabadclinics.count()

    jamshedpurclinics = clinicsall.filter(clinicCity__iexact='Jamshedpur')
    jamshedpurclinics = jamshedpurclinics.count()

    bangaloreclinics = clinicsall.filter(clinicCity__iexact='Bangalore')
    bangaloreclinics = bangaloreclinics.count()

    trivandrumclinics = clinicsall.filter(clinicCity__iexact='Trivandrum')
    trivandrumclinics = trivandrumclinics.count()

    kochiclinics = clinicsall.filter(clinicCity__iexact='Kochi')
    kochiclinics = kochiclinics.count()

    bhopalclinics = clinicsall.filter(clinicCity__iexact='Bhopal')
    bhopalclinics = bhopalclinics.count()

    indoreclinics = clinicsall.filter(clinicCity__iexact='Indore')
    indoreclinics = indoreclinics.count()

    nagpurclinics = clinicsall.filter(clinicCity__iexact='Nagpur')
    nagpurclinics = nagpurclinics.count()

    bhubaneswarclinics = clinicsall.filter(clinicCity__iexact='Bhubaneswar')
    bhubaneswarclinics = bhubaneswarclinics.count()

    ludhianaclinics = clinicsall.filter(clinicCity__iexact='Ludhiana')
    ludhianaclinics = ludhianaclinics.count()

    jaipurclinics = clinicsall.filter(clinicCity__iexact='Jaipur')
    jaipurclinics = jaipurclinics.count()

    lucknowclinics = clinicsall.filter(clinicCity__iexact='Lucknow')
    lucknowclinics = lucknowclinics.count()

    kanpurclinics = clinicsall.filter(clinicCity__iexact='Kanpur')
    kanpurclinics = kanpurclinics.count()

    dehradunclinics = clinicsall.filter(clinicCity__iexact='Dehradun')
    dehradunclinics = dehradunclinics.count()

    kolkataclinics = clinicsall.filter(clinicCity__iexact='Kolkata')
    kolkataclinics = kolkataclinics.count()

    #GR REGIONS
    athensclinics = clinicsall.filter(clinicCity__iexact='Athens')
    athensclinics = athensclinics.count()

    thessalonikiclinics = clinicsall.filter(clinicCity__iexact='Thessaloniki')
    thessalonikiclinics = thessalonikiclinics.count()

    #CY REGIONS
    nicosiaclinics = clinicsall.filter(clinicCity__iexact='Nicosia')
    nicosiaclinics = nicosiaclinics.count()

    girneclinics = clinicsall.filter(clinicCity__iexact='Girne')
    girneclinics = girneclinics.count()

    #MX REGIONS
    cancunclinics = clinicsall.filter(clinicCity__iexact='Cancún')
    cancunclinics = cancunclinics.count()

    mexicocityclinics = clinicsall.filter(clinicCity__iexact='Mexico City')
    mexicocityclinics = mexicocityclinics.count()

    #DK REGIONS
    copenhagenclinics = clinicsall.filter(clinicCity__iexact='Copenhagen')
    copenhagenclinics = copenhagenclinics.count()

    #PT REGIONS
    lisbonclinics = clinicsall.filter(clinicCity__iexact='Lisbon')
    lisbonclinics = lisbonclinics.count()

    #LV REGIONS
    rigaclinics = clinicsall.filter(clinicCity__iexact='Riga')
    rigaclinics = rigaclinics.count()

    #DE REGIONS
    berlinclinics = clinicsall.filter(clinicCity__iexact='Berlin')
    berlinclinics = berlinclinics.count()

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
        'ukclinics': ukclinics,
        'usclinics': usclinics,
        'czclinics': czclinics,
        'skclinics': skclinics,
        'spclinics': spclinics,
        'dkclinics': dkclinics,
        'inclinics': inclinics,
        'grclinics': grclinics,
        'cyclinics': cyclinics,
        'mxclinics': mxclinics,
        'declinics': declinics,
        'ptclinics': ptclinics,
        'lvclinics': lvclinics,
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
        'bratislavaclinics': bratislavaclinics,
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
        'copenhagenclinics': copenhagenclinics,
        'lisbonclinics': lisbonclinics,
        'rigaclinics': rigaclinics,
        'berlinclinics': berlinclinics,
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
