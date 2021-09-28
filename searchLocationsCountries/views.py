from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_MX_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from guestblogging.models import GuestBlog, GuestAuthor


# Create your views here.
# ----------------------------------------------------------------------------
def fertilityClinicUSA(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='United States')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='United States').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #US REGIONS
    texasclinics = basic_queryset.filter(clinicRegion__iexact='Texas').exclude(is_published=False)
    texasclinics = texasclinics.count()

    newyorkclinics = basic_queryset.filter(clinicRegion__iexact='New York').exclude(is_published=False)
    newyorkclinics = newyorkclinics.count()

    floridaclinics = basic_queryset.filter(clinicRegion__iexact='Florida').exclude(is_published=False)
    floridaclinics = floridaclinics.count()

    newjerseyclinics = basic_queryset.filter(clinicRegion__iexact='New Jersey').exclude(is_published=False)
    newjerseyclinics = newjerseyclinics.count()

    illinoisclinics = basic_queryset.filter(clinicRegion__iexact='Illinois').exclude(is_published=False)
    illinoisclinics = illinoisclinics.count()

    pennsylvaniaclinics = basic_queryset.filter(clinicRegion__iexact='Pennsylvania').exclude(is_published=False)
    pennsylvaniaclinics = pennsylvaniaclinics.count()

    michiganclinics = basic_queryset.filter(clinicRegion__iexact='Michigan').exclude(is_published=False)
    michiganclinics = michiganclinics.count()

    georgiaclinics = basic_queryset.filter(clinicRegion__iexact='Georgia').exclude(is_published=False)
    georgiaclinics = georgiaclinics.count()

    arizonaclinics = basic_queryset.filter(clinicRegion__iexact='Arizona').exclude(is_published=False)
    arizonaclinics = arizonaclinics.count()

    massachusettsclinics = basic_queryset.filter(clinicRegion__iexact='Massachusetts').exclude(is_published=False)
    massachusettsclinics = massachusettsclinics.count()

    washingtonclinics = basic_queryset.filter(clinicRegion__iexact='Washington').exclude(is_published=False)
    washingtonclinics = washingtonclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count, 'texasclinics': texasclinics, 'newyorkclinics': newyorkclinics, 'floridaclinics': floridaclinics, 'newjerseyclinics': newjerseyclinics, 'illinoisclinics': illinoisclinics, 'pennsylvaniaclinics': pennsylvaniaclinics, 'michiganclinics': michiganclinics, 'georgiaclinics': georgiaclinics, 'arizonaclinics': arizonaclinics, 'massachusettsclinics': massachusettsclinics, 'washingtonclinics': washingtonclinics,}

    return render(request, 'locations-states/USA/fertility-clinic-usa.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicUK(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='United Kingdom')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #UK CITIES
    londonclinics = basic_queryset.filter(clinicRegion__iexact='London').exclude(is_published=False)
    londonclinics = londonclinics.count()

    bristolclinics = basic_queryset.filter(clinicRegion__iexact='Bristol').exclude(is_published=False)
    bristolclinics = bristolclinics.count()

    birminghamclinics = basic_queryset.filter(clinicRegion__iexact='Birmingham').exclude(is_published=False)
    birminghamclinics = birminghamclinics.count()

    liverpoolclinics = basic_queryset.filter(clinicRegion__iexact='Liverpool').exclude(is_published=False)
    liverpoolclinics = liverpoolclinics.count()

    swanseaclinics = basic_queryset.filter(clinicRegion__iexact='Swansea').exclude(is_published=False)
    swanseaclinics = swanseaclinics.count()

    cardiffclinics = basic_queryset.filter(clinicRegion__iexact='Cardiff').exclude(is_published=False)
    cardiffclinics = cardiffclinics.count()

    manchesterclinics = basic_queryset.filter(clinicRegion__iexact='Manchester').exclude(is_published=False)
    manchesterclinics = manchesterclinics.count()

    oxfordclinics = basic_queryset.filter(clinicRegion__iexact='Oxford').exclude(is_published=False)
    oxfordclinics = oxfordclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'my_total_count': my_total_count, 'londonclinics': londonclinics, 'bristolclinics': bristolclinics, 'birminghamclinics': birminghamclinics, 'liverpoolclinics': liverpoolclinics, 'swanseaclinics': swanseaclinics, 'cardiffclinics': cardiffclinics, 'manchesterclinics': manchesterclinics, 'oxfordclinics': oxfordclinics,}

    return render(request, 'locations-states/UK/fertility-clinic-uk.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicSpain(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='Spain')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='Spain').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #SP CITIES
    alicanteclinics = basic_queryset.filter(clinicRegion__iexact='Alicante').exclude(is_published=False)
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = basic_queryset.filter(clinicRegion__iexact='Barcelona').exclude(is_published=False)
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = basic_queryset.filter(clinicRegion__iexact='Madrid').exclude(is_published=False)
    madridclinics = madridclinics.count()

    malagaclinics = basic_queryset.filter(clinicRegion__iexact='Malaga').exclude(is_published=False)
    malagaclinics = malagaclinics.count()

    sevilleclinics = basic_queryset.filter(clinicRegion__iexact='Seville').exclude(is_published=False)
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = basic_queryset.filter(clinicRegion__iexact='Valencia').exclude(is_published=False)
    valenciaclinics = valenciaclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'my_total_count': my_total_count, 'alicanteclinics': alicanteclinics, 'barcelonaclinics': barcelonaclinics, 'madridclinics': madridclinics, 'malagaclinics': malagaclinics, 'sevilleclinics': sevilleclinics, 'valenciaclinics': valenciaclinics,}

    return render(request, 'locations-states/Spain/fertility-clinic-spain.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicIndia(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='India')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='India').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #IN CITIES
    hyderabadclinics = basic_queryset.filter(clinicCity__iexact='Hyderabad').exclude(is_published=False)
    hyderabadclinics = hyderabadclinics.count()

    newdelhiclinics = basic_queryset.filter(clinicCity__iexact='New Delhi').exclude(is_published=False)
    newdelhiclinics = newdelhiclinics.count()

    gachibowliclinics = basic_queryset.filter(clinicCity__iexact='Gachibowli').exclude(is_published=False)
    gachibowliclinics = gachibowliclinics.count()

    bangaloreclinics = basic_queryset.filter(clinicCity__iexact='Bangalore').exclude(is_published=False)
    bangaloreclinics = bangaloreclinics.count()

    chennaiclinics = basic_queryset.filter(clinicCity__iexact='Chennai').exclude(is_published=False)
    chennaiclinics = chennaiclinics.count()

    vadodaraclinics = basic_queryset.filter(clinicCity__iexact='Vandodara').exclude(is_published=False)
    vadodaraclinics = vadodaraclinics.count()

    madhapurclinics = basic_queryset.filter(clinicCity__iexact='Madhapur').exclude(is_published=False)
    madhapurclinics = madhapurclinics.count()

    gwaliorclinics = basic_queryset.filter(clinicCity__iexact='Gwalior').exclude(is_published=False)
    gwaliorclinics = gwaliorclinics.count()

    mumbaiclinics = basic_queryset.filter(clinicCity__iexact='Mumbai').exclude(is_published=False)
    mumbaiclinics = mumbaiclinics.count()

    faridabadclinics = basic_queryset.filter(clinicCity__iexact='Faridabad').exclude(is_published=False)
    faridabadclinics = faridabadclinics.count()

    kolkataclinics = basic_queryset.filter(clinicCity__iexact='Kolkata').exclude(is_published=False)
    kolkataclinics = kolkataclinics.count()

    rohtakclinics = basic_queryset.filter(clinicCity__iexact='Rohtak').exclude(is_published=False)
    rohtakclinics = rohtakclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'my_total_count': my_total_count, 'hyderabadclinics': hyderabadclinics, 'newdelhiclinics': newdelhiclinics, 'gachibowliclinics': gachibowliclinics, 'bangaloreclinics': bangaloreclinics, 'chennaiclinics': chennaiclinics, 'vadodaraclinics': vadodaraclinics, 'madhapurclinics': madhapurclinics, 'gwaliorclinics': gwaliorclinics, 'mumbaiclinics': mumbaiclinics, 'faridabadclinics': faridabadclinics, 'kolkataclinics': kolkataclinics, 'rohtakclinics': rohtakclinics,}

    return render(request, 'locations-states/India/fertility-clinic-india.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicGreece(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='Greece')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='Greece').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #GR CITIES
    athensclinics = basic_queryset.filter(clinicCity__iexact='Athens').exclude(is_published=False)
    athensclinics = athensclinics.count()

    thessalonikiclinics = basic_queryset.filter(clinicCity__iexact='Thessaloniki').exclude(is_published=False)
    thessalonikiclinics = thessalonikiclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'my_total_count': my_total_count, 'athensclinics': athensclinics, 'thessalonikiclinics': thessalonikiclinics,}

    return render(request, 'locations-states/Greece/fertility-clinic-greece.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicCzech(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='Czech Republic')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    pkid = 1
    best_clinics = basic_queryset.filter(best_article_country_blogpost_obj=pkid)
    best_clinics = best_clinics.filter(best_article_country_boolean=True)
    best_clinics_count = best_clinics.count()

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #CZ CITIES
    pragueclinics = basic_queryset.filter(clinicRegion__iexact='Prague').exclude(is_published=False)
    pragueclinics = pragueclinics.count()

    brnoclinics = basic_queryset.filter(clinicRegion__iexact='Brno').exclude(is_published=False)
    brnoclinics = brnoclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'my_total_count': my_total_count, 'pragueclinics': pragueclinics, 'brnoclinics': brnoclinics, 'best_clinics_count': best_clinics_count}

    return render(request, 'locations-states/CZ/fertility-clinic-czech-republic.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicCyprus(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='Cyprus')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='Cyprus').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #CY CITIES
    girneclinics = basic_queryset.filter(clinicCity__iexact='Girne').exclude(is_published=False)
    girneclinics = girneclinics.count()

    nicosiaclinics = basic_queryset.filter(clinicCity__iexact='Nicosia').exclude(is_published=False)
    nicosiaclinics = nicosiaclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'my_total_count': my_total_count, 'nicosiaclinics': nicosiaclinics, 'girneclinics': girneclinics,}

    return render(request, 'locations-states/Cyprus/fertility-clinic-cyprus.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicMexico(request):
    guestblog = GuestBlog.objects.filter(guestblogcountry__iexact='Mexico')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    basic_queryset = BasicClinic.objects.filter(clinicState__iexact='Mexico').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    averageIVFPrice = basic_queryset.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = basic_queryset.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = basic_queryset.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = basic_queryset.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = basic_queryset.aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    #CY CITIES
    cancunclinics = basic_queryset.filter(clinicCity__iexact='Cancún').exclude(is_published=False)
    cancunclinics = cancunclinics.count()

    mexicocityclinics = basic_queryset.filter(clinicCity__iexact='Mexico City').exclude(is_published=False)
    mexicocityclinics = mexicocityclinics.count()

    context = {'guestblog': guestblog, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'cancunclinics': cancunclinics, 'mexicocityclinics': mexicocityclinics,}

    return render(request, 'locations-states/Mexico/fertility-clinic-mexico.html', context)

# --------------------------------------->>>>>>>> Redirects
def fertilityClinicUSA1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUSA'))

def fertilityClinicUK1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicUK'))

def fertilityClinicSpain1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicSpain'))

def fertilityClinicIndia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicIndia'))

def fertilityClinicGreece1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicGreece'))

def fertilityClinicCzech1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCzech'))

def fertilityClinicCyprus1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicCyprus'))
