from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SK_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_DK_CITIES, CATEGORY_CHOICES_MX_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from guestblogging.models import GuestBlog, GuestAuthor

# Create your views here.
def fertilityClinicPrague(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Prague')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Prague').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    best_city_article_count = basic_queryset.filter(best_article_city_boolean=True)
    best_city_article_count = best_city_article_count.count()

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog, 'best_city_article_count': best_city_article_count,}

    return render(request, 'locations-cities/Europe/Czech/fertility-clinic-prague.html', context)

def fertilityClinicBrno(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Brno')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Brno').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Czech/fertility-clinic-brno.html', context)

def fertilityClinicBratislava(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bratislava')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Slovakia')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Bratislava').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    best_city_article_count = basic_queryset.filter(best_article_city_boolean=True)
    best_city_article_count = best_city_article_count.count()

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog, 'best_city_article_count': best_city_article_count,}

    return render(request, 'locations-cities/Europe/Slovakia/fertility-clinic-bratislava.html', context)

def fertilityClinicsAberdeen(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Aberdeen')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-aberdeen.html', context)

def fertilityClinicsBath(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bath')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Bath').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-bath.html', context)

def fertilityClinicsBelfast(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Belfast')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-belfast.html', context)

def fertilityClinicsBirmingham(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Birmingham')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-birmingham.html', context)

def fertilityClinicsBournemouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bournemouth')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-bournemouth.html', context)

def fertilityClinicsBrightonHove(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Brighton')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Brighton').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-brighton-hove.html', context)

def fertilityClinicsBristol(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bristol')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-bristol.html', context)

def fertilityClinicsCambridge(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cambridge')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-cambridge.html', context)

def fertilityClinicsCardiff(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cardiff')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-cardiff.html', context)

def fertilityClinicsColchester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Colchester')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-colchester.html', context)

def fertilityClinicsDerby(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Derby')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Derby').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-derby.html', context)

def fertilityClinicsExeter(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Exeter')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-exeter.html', context)

def fertilityClinicsGlasgow(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Glasgow')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-glasgow.html', context)

def fertilityClinicsHull(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Hull')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Hull').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-hull.html', context)

def fertilityClinicsChelmsford(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chelmsford')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-chelmsford.html', context)

def fertilityClinicsLeeds(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Leeds')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-leeds.html', context)

def fertilityClinicsLeicester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Leicester')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-leicester.html', context)

def fertilityClinicsLiverpool(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Liverpool')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-liverpool.html', context)

def fertilityClinicsLondon(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='London')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='London').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-london.html', context)

def fertilityClinicsManchester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Manchester')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-manchester.html', context)

def fertilityClinicsMiddlesbrough(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Middlesbrough')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-middlesbrough.html', context)

def fertilityClinicsNewcastle(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Newcastle')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-newcastle.html', context)

def fertilityClinicsNorwich(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Norwich')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-norwich.html', context)

def fertilityClinicsNottingham(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nottingham')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-nottingham.html', context)

def fertilityClinicsOxford(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Oxford')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-oxford.html', context)

def fertilityClinicsPeterborough(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Peterborough')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-peterborough.html', context)

def fertilityClinicsPlymouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Plymouth')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-plymouth.html', context)

def fertilityClinicsPortsmouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Portsmouth')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-portsmouth.html', context)

def fertilityClinicsSalisbury(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Salisbury')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-salisbury.html', context)

def fertilityClinicsSheffield(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Sheffield')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-sheffield.html', context)

def fertilityClinicsSouthampton(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Southampton')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-southampton.html', context)

def fertilityClinicsSwansea(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Swansea')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/UK/fertility-clinics-swansea.html', context)

def fertilityClinicsAlicante(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Alicante')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-alicante.html', context)

def fertilityClinicsBarcelona(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Barcelona')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-barcelona.html', context)

def fertilityClinicsMadrid(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Madrid')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-madrid.html', context)

def fertilityClinicsMalaga(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Malaga')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-malaga.html', context)

def fertilityClinicsSeville(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Seville')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Seville').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-seville.html', context)

def fertilityClinicsValencia(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Valencia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Spain')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/SP/fertility-clinics-valencia.html', context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INDIA
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fertilityClinicsChennai(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chennai')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Chennai').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-chennai.html', context)

def fertilityClinicsHyderabad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Hyderabad')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Hyderabad').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-hyderabad.html', context)

def fertilityClinicsMumbai(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Mumbai')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Mumbai').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-mumbai.html', context)

def fertilityClinicsPatna(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Patna')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Patna').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-patna.html', context)

def fertilityClinicsRaipur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Raipur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Raipur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-raipur.html', context)

def fertilityClinicsAmdavad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Amdavad')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Amdavad').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-amdavad.html', context)

def fertilityClinicsChandigarh(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chandigarh')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Chandigarh').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-chandigarh.html', context)

def fertilityClinicsFaridabad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Faridabad')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Faridabad').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-faridabad.html', context)

def fertilityClinicsJamshedpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jamshedpur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Jamshedpur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-jamshedpur.html', context)

def fertilityClinicsBangalore(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bangalore')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Bangalore').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-bangalore.html', context)

def fertilityClinicsTrivandrum(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Trivandrum')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Trivandrum').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-trivandrum.html', context)

def fertilityClinicsKochi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kochi')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Kochi').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-kochi.html', context)

def fertilityClinicsBhopal(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bhopal')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Bhopal').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-bhopal.html', context)

def fertilityClinicsIndore(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Indore')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Indore').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-indore.html', context)

def fertilityClinicsNagpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nagpur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Nagpur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-nagpur.html', context)

def fertilityClinicsBhubaneswar(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bhubaneswar')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Bhubaneswar').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-bhubaneswar.html', context)

def fertilityClinicsLudhiana(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Ludhiana')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Ludhiana').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-ludhiana.html', context)

def fertilityClinicsJaipur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jaipur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Jaipur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-jaipur.html', context)

def fertilityClinicsLucknow(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Lucknow')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Lucknow').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-lucknow.html', context)

def fertilityClinicsKanpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kanpur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Kanpur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-kanpur.html', context)

def fertilityClinicsDehradun(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Dehradun')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Dehradun').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-dehradun.html', context)

def fertilityClinicsKolkata(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kolkata')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Kolkata').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-kolkata.html', context)

def fertilityClinicsVisakhapatnam(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Visakhapatnam')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Visakhapatnam').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-visakhapatnam.html', context)

def fertilityClinicsVijayawada(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Vijayawada')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Vijayawada').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-vijayawada.html', context)

def fertilityClinicsNewDelhi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='New Delhi')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='New Delhi').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-new-delhi.html', context)

def fertilityClinicsVadodara(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Vadodara')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Vadodara').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-vadodara.html', context)

def fertilityClinicsGurugram(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gurugram')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Gurugram').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-gurugram.html', context)

def fertilityClinicsRohtak(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Rohtak')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Rohtak').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-rohtak.html', context)

def fertilityClinicsJammu(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jammu')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Jammu').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-jammu.html', context)

def fertilityClinicsRanchi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Ranchi')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Ranchi').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-ranchi.html', context)

def fertilityClinicsGwalior(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gwalior')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Gwalior').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-gwalior.html', context)

def fertilityClinicsPune(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Pune')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Pune').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-pune.html', context)

def fertilityClinicsWarangal(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Warangal')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Warangal').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-warangal.html', context)

def fertilityClinicsGachibowli(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gachibowli')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Gachibowli').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-gachibowli.html', context)

def fertilityClinicsMadhapur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Madhapur')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Madhapur').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-madhapur.html', context)

def fertilityClinicsNoida(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Noida')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Noida').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-noida.html', context)

def fertilityClinicsMeerut(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Meerut')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Meerut').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-meerut.html', context)

def fertilityClinicsHaldwani(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Haldwani')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='India')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Haldwani').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Asia/India/fertility-clinics-haldwani.html', context)

def fertilityClinicsAthens(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Athens')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Greece')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Athens').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Greece/fertility-clinic-athens.html', context)

def fertilityClinicsThessaloniki(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Thessaloniki')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Greece')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Thessaloniki').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Greece/fertility-clinic-thessaloniki.html', context)

def fertilityClinicsNicosia(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nicosia')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Cyprus')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Nicosia').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Cyprus/fertility-clinics-nicosia.html', context)

def fertilityClinicsGirne(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Girne')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Cyprus')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Girne').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Cyprus/fertility-clinics-girne.html', context)

def fertilityClinicsCancun(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cancún')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Mexico')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Cancún').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/NorthAmerica/Mexico/fertility-clinics-cancun.html', context)

def fertilityClinicsMexicoCity(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Mexico City')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Mexico')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicCity__iexact='Mexico City').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/NorthAmerica/Mexico/fertility-clinics-mexico-city.html', context)

def fertilityClinicCopenhagen(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Copenhagen')
    guestblog = guestblog.filter(guestblogactive=True)

    all_clinic_count = BasicClinic.objects.filter(is_published=True)
    all_clinic_count = all_clinic_count.count()

    average = BasicClinic.objects.filter(clinicState__iexact='Denmark')
    averageIVFPrice = average.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = average.aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = average.aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = average.aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = average.aggregate(average=Avg('icsi_treatment_cost'))

    basic_queryset = BasicClinic.objects.filter(clinicRegion__iexact='Copenhagen').filter(is_published=True)

    my_total_count = basic_queryset.filter(is_published=True)
    my_total_count = my_total_count.count()

    queryset_list = basic_queryset.order_by('-digitalTransparencyIndex')

    order_data = list(queryset_list)

    paginator = Paginator(order_data, 10)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Europe/Denmark/fertility-clinics-copenhagen.html', context)

# --------------------------------------->>>>>>>> Redirects
def fertilityClinicPrague1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicPrague'))

def fertilityClinicBrno1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicBrno'))

def fertilityClinicPrague2(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicPrague'))

def fertilityClinicBrno2(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicBrno'))

def fertilityClinicsAberdeen1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsAberdeen'))

def fertilityClinicsBath1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBath'))

def fertilityClinicsBelfast1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBelfast'))

def fertilityClinicsBirmingham1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBirmingham'))

def fertilityClinicsBournemouth1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBournemouth'))

def fertilityClinicsBrightonHove1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBrightonHove'))

def fertilityClinicsBristol1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBristol'))

def fertilityClinicsCambridge1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsCambridge'))

def fertilityClinicsCardiff1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsCardiff'))

def fertilityClinicsColchester1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsColchester'))

def fertilityClinicsDerby1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsDerby'))

def fertilityClinicsExeter1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsExeter'))

def fertilityClinicsGlasgow1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsGlasgow'))

def fertilityClinicsHull1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsHull'))

def fertilityClinicsChelmsford1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsChelmsford'))

def fertilityClinicsLeeds1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsLeeds'))

def fertilityClinicsLeicester1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsLeicester'))

def fertilityClinicsLiverpool1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsLiverpool'))

def fertilityClinicsLondon1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsLondon'))

def fertilityClinicsManchester1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsManchester'))

def fertilityClinicsMiddlesbrough1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMiddlesbrough'))

def fertilityClinicsNewcastle1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNewcastle'))

def fertilityClinicsNorwich1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNorwich'))

def fertilityClinicsNottingham1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsNottingham'))

def fertilityClinicsOxford1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsOxford'))

def fertilityClinicsPeterborough1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsPeterborough'))

def fertilityClinicsPlymouth1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsPlymouth'))

def fertilityClinicsPortsmouth1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsPortsmouth'))

def fertilityClinicsSalisbury1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSalisbury'))

def fertilityClinicsSheffield1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSheffield'))

def fertilityClinicsSouthampton1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSouthampton'))

def fertilityClinicsSwansea1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSwansea'))

def fertilityClinicsAlicante1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsAlicante'))

def fertilityClinicsBarcelona1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsBarcelona'))

def fertilityClinicsMadrid1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMadrid'))

def fertilityClinicsMalaga1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsMalaga'))

def fertilityClinicsSeville1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsSeville'))

def fertilityClinicsValencia1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicsValencia'))
