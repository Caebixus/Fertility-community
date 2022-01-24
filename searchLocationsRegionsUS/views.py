from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from guestblogging.models import GuestBlog, GuestAuthor

year = 2022

# ----------------------------------------------------------------------------
def fertilityClinicsAlabama(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Alabama')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Alabama').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-alabama.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsAlaska(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Alaska')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Alaska').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-alaska.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsArizona(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Arizona')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Arizona').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-arizona.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsArkansas(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Arkansas')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Arkansas').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-arkansas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsCalifornia(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='California')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='California').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-california.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsColorado(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Colorado')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Colorado').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-colorado.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsConnecticut(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Connecticut')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Connecticut').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-connecticut.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsDelaware(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Delaware')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Delaware').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-delaware.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsFlorida(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Florida')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Florida').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-florida.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsGeorgia(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Georgia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Georgia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-georgia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsHawaii(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Hawaii')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Hawaii').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-hawaii.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIdaho(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Idaho')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Idaho').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-idaho.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIllinois(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Illinois')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Illinois').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-illinois.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIndiana(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Indiana')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Indiana').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-indiana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIowa(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Iowa')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Iowa').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-iowa.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsKansas(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Kansas')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Kansas').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-kansas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsKentucky(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Kentucky')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Kentucky').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-kentucky.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsLouisiana(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Louisiana')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Louisiana').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-louisiana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMaine(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Maine')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Maine').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-maine.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMaryland(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Maryland')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Maryland').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-maryland.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMassachusetts(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Massachusetts')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Massachusetts').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-massachusetts.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMichigan(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Michigan')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Michigan').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-michigan.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMinnesota(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Minnesota')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Minnesota').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-minnesota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMississippi(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Mississippi')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Mississippi').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-mississippi.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMissouri(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Missouri')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Missouri').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-missouri.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMontana(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Montana')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Montana').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-montana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNebraska(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Nebraska')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Nebraska').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-nebraska.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewHampshire(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='New Hampshire')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='New Hampshire').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-new-hampshire.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewJersey(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='New Jersey')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='New Jersey').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-new-jersey.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewMexico(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='New Mexico')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='New Mexico').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-new-mexico.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewYork(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='New York')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='New York').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-new-york.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNorthCarolina(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='North Carolina')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='North Carolina').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-north-carolina.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNorthDakota(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='North Dakota')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='North Dakota').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-north-dakota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNevada(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Nevada')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Nevada').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-nevada.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOhio(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Ohio')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Ohio').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-ohio.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOklahoma(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Oklahoma')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Oklahoma').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-oklahoma.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOregon(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Oregon')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Oregon').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-oregon.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsPennsylvania(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Pennsylvania')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Pennsylvania').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-pennsylvania.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsPuertoRico(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Puerto Rico')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Puerto Rico').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-puerto-rico.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsRhodeIsland(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Rhode Island')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Rhode Island').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-rhode-island.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsSouthCarolina(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='South Carolina')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='South Carolina').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-south-carolina.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsSouthDakota(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='South Dakota')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='South Dakota').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-south-dakota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsTennessee(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Tennessee')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Tennessee').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-tennessee.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsTexas(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Texas')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Texas').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-texas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsUtah(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Utah')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Utah').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-utah.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsVermont(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Vermont')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Vermont').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-vermont.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsVirginia(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Virginia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Virginia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-virginia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWashington(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Washington')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Washington').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-washington.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWestVirginia(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='West Virginia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='West Virginia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-west-virginia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWisconsin(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Wisconsin')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Wisconsin').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-wisconsin.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWyoming(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='Wyoming')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Wyoming').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-wyoming.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsDistrictOfColumbia(request):
    guestblog = GuestBlog.objects.filter(guestblogregion__iexact='DistrictOfColumbia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United States')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='DistrictOfColumbia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'guestblog': guestblog, 'year': year, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'my_total_count': my_total_count,}

    return render(request, 'locations-regions/USA/fertility-clinics-district-of-columbia.html', context)

# --------------------------------------->>>>>>>> Redirects
def fertilityClinicsAlabama1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsAlabama'))

def fertilityClinicsAlaska1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsAlaska'))

def fertilityClinicsArizona1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsArizona'))

def fertilityClinicsArkansas1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsArkansas'))

def fertilityClinicsCalifornia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsCalifornia'))

def fertilityClinicsColorado1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsColorado'))

def fertilityClinicsConnecticut1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsConnecticut'))

def fertilityClinicsDelaware1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsDelaware'))

def fertilityClinicsFlorida1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsFlorida'))

def fertilityClinicsGeorgia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsGeorgia'))

def fertilityClinicsHawaii1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsHawaii'))

def fertilityClinicsIdaho1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsIdaho'))

def fertilityClinicsIllinois1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsIllinois'))

def fertilityClinicsIndiana1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsIndiana'))

def fertilityClinicsIowa1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsIowa'))

def fertilityClinicsKansas1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsKansas'))

def fertilityClinicsKentucky1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsKentucky'))

def fertilityClinicsLouisiana1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsLouisiana'))

def fertilityClinicsMaine1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMaine'))

def fertilityClinicsMaryland1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMaryland'))

def fertilityClinicsMassachusetts1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMassachusetts'))

def fertilityClinicsMichigan1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMichigan'))

def fertilityClinicsMinnesota1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMinnesota'))

def fertilityClinicsMississippi1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMississippi'))

def fertilityClinicsMissouri1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMissouri'))

def fertilityClinicsMontana1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMontana'))

def fertilityClinicsNebraska1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNebraska'))

def fertilityClinicsNewHampshire1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNewHampshire'))

def fertilityClinicsNewJersey1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNewJersey'))

def fertilityClinicsNewMexico1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNewMexico'))

def fertilityClinicsNewYork1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNewYork'))

def fertilityClinicsNorthCarolina1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNorthCarolina'))

def fertilityClinicsNorthDakota1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNorthDakota'))

def fertilityClinicsNevada1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNevada'))

def fertilityClinicsOhio1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsOhio'))

def fertilityClinicsOklahoma1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsOklahoma'))

def fertilityClinicsOregon1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsOregon'))

def fertilityClinicsPennsylvania1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsPennsylvania'))

def fertilityClinicsPuertoRico1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsPuertoRico'))

def fertilityClinicsRhodeIsland1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsRhodeIsland'))

def fertilityClinicsSouthCarolina1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSouthCarolina'))

def fertilityClinicsSouthDakota1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSouthDakota'))

def fertilityClinicsTennessee1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsTennessee'))

def fertilityClinicsTexas1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsTexas'))

def fertilityClinicsUtah1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsUtah'))

def fertilityClinicsVermont1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsVermont'))

def fertilityClinicsVirginia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsVirginia'))

def fertilityClinicsWashington1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsWashington'))

def fertilityClinicsWestVirginia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsWestVirginia'))

def fertilityClinicsWisconsin1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsWisconsin'))

def fertilityClinicsWyoming1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsWyoming'))

def fertilityClinicsDistrictOfColumbia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsDistrictOfColumbia'))
