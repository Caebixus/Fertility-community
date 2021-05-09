from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_MX_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from guestblogging.models import GuestBlog, GuestAuthor

# Create your views here.
def fertilityClinicPrague(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Prague')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Prague')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Prague')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Prague')

    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Czech/fertility-clinic-prague.html', context)

def fertilityClinicBrno(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Brno')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Brno')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Brno')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Brno')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Czech/fertility-clinic-brno.html', context)

def fertilityClinicsAberdeen(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Aberdeen')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Aberdeen')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Aberdeen')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Aberdeen')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Aberdeen')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-aberdeen.html', context)

def fertilityClinicsBath(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bath')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bath')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bath')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bath')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bath')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-bath.html', context)

def fertilityClinicsBelfast(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Belfast')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Belfast')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Belfast')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Belfast')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Belfast')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-belfast.html', context)

def fertilityClinicsBirmingham(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Birmingham')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Birmingham')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Birmingham')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Birmingham')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Birmingham')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-birmingham.html', context)

def fertilityClinicsBournemouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bournemouth')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bournemouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bournemouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bournemouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bournemouth')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-bournemouth.html', context)

def fertilityClinicsBrightonHove(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='BrightonHove')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='BrightonHove')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='BrightonHove')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='BrightonHove')

    my_total_count = my_total_count.filter(clinicRegion__iexact='BrightonHove')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-brighton-hove.html', context)

def fertilityClinicsBristol(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bristol')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bristol')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bristol')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bristol')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bristol')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-bristol.html', context)

def fertilityClinicsCambridge(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cambridge')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Cambridge')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Cambridge')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Cambridge')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Cambridge')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-cambridge.html', context)

def fertilityClinicsCardiff(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cardiff')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Cardiff')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Cardiff')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Cardiff')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Cardiff')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-cardiff.html', context)

def fertilityClinicsColchester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Colchester')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Colchester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Colchester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Colchester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Colchester')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-colchester.html', context)

def fertilityClinicsDerby(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Derby')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Derby')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Derby')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Derby')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Derby')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-derby.html', context)

def fertilityClinicsExeter(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Exeter')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Exeter')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Exeter')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Exeter')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Exeter')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-exeter.html', context)

def fertilityClinicsGlasgow(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Glasgow')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Glasgow')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Glasgow')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Glasgow')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Glasgow')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-glasgow.html', context)

def fertilityClinicsHull(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Hull')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Hull')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Hull')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Hull')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Hull')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-hull.html', context)

def fertilityClinicsChelmsford(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chelmsford')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Chelmsford')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Chelmsford')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Chelmsford')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Chelmsford')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-chelmsford.html', context)

def fertilityClinicsLeeds(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Leeds')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Leeds')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Leeds')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Leeds')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Leeds')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-leeds.html', context)

def fertilityClinicsLeicester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Leicester')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Leicester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Leicester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Leicester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Leicester')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-leicester.html', context)

def fertilityClinicsLiverpool(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Liverpool')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Liverpool')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Liverpool')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Liverpool')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Liverpool')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-liverpool.html', context)

def fertilityClinicsLondon(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='London')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='London')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='London')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='London')

    my_total_count = my_total_count.filter(clinicRegion__iexact='London')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-london.html', context)

def fertilityClinicsManchester(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Manchester')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Manchester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Manchester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Manchester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Manchester')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-manchester.html', context)

def fertilityClinicsMiddlesbrough(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Middlesbrough')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Middlesbrough')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Middlesbrough')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Middlesbrough')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Middlesbrough')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-middlesbrough.html', context)

def fertilityClinicsNewcastle(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Newcastle')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Newcastle')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Newcastle')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Newcastle')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Newcastle')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-newcastle.html', context)

def fertilityClinicsNorwich(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Norwich')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Norwich')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Norwich')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Norwich')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Norwich')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-norwich.html', context)

def fertilityClinicsNottingham(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nottingham')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Nottingham')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Nottingham')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Nottingham')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Nottingham')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-nottingham.html', context)

def fertilityClinicsOxford(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Oxford')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Oxford')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Oxford')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Oxford')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Oxford')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-oxford.html', context)

def fertilityClinicsPeterborough(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Peterborough')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Peterborough')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Peterborough')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Peterborough')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Peterborough')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-peterborough.html', context)

def fertilityClinicsPlymouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Plymouth')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Plymouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Plymouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Plymouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Plymouth')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-plymouth.html', context)

def fertilityClinicsPortsmouth(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Portsmouth')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Portsmouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Portsmouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Portsmouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Portsmouth')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-portsmouth.html', context)

def fertilityClinicsSalisbury(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Salisbury')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Salisbury')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Salisbury')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Salisbury')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Salisbury')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-salisbury.html', context)

def fertilityClinicsSheffield(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Sheffield')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Sheffield')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Sheffield')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Sheffield')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Sheffield')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-sheffield.html', context)

def fertilityClinicsSouthampton(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Southampton')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Southampton')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Southampton')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Southampton')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Southampton')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-southampton.html', context)

def fertilityClinicsSwansea(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Swansea')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Swansea')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Swansea')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Swansea')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Swansea')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/UK/fertility-clinics-swansea.html', context)

def fertilityClinicsAlicante(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Alicante')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Alicante')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Alicante')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Alicante')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Alicante')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-alicante.html', context)

def fertilityClinicsBarcelona(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Barcelona')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Barcelona')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Barcelona')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Barcelona')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Barcelona')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-barcelona.html', context)

def fertilityClinicsMadrid(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Madrid')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Madrid')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Madrid')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Madrid')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Madrid')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-madrid.html', context)

def fertilityClinicsMalaga(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Malaga')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Malaga')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Malaga')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Malaga')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Malaga')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-malaga.html', context)

def fertilityClinicsSeville(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Seville')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Seville')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Seville')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Seville')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Seville')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-seville.html', context)

def fertilityClinicsValencia(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Valencia')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Valencia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Valencia')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Valencia')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Valencia')
    my_total_count = my_total_count.count()


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/SP/fertility-clinics-valencia.html', context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INDIA
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fertilityClinicsChennai(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chennai')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Chennai')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Chennai')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Chennai')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Chennai')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-chennai.html', context)

def fertilityClinicsHyderabad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Hyderabad')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Hyderabad')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Hyderabad')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Hyderabad')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Hyderabad')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-hyderabad.html', context)

def fertilityClinicsMumbai(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Mumbai')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Mumbai')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Mumbai')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Mumbai')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Mumbai')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-mumbai.html', context)

def fertilityClinicsPatna(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Patna')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Patna')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Patna')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Patna')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Patna')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-patna.html', context)

def fertilityClinicsRaipur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Raipur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Raipur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Raipur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Raipur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Raipur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-raipur.html', context)

def fertilityClinicsAmdavad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Amdavad')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Amdavad')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Amdavad')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Amdavad')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Amdavad')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-amdavad.html', context)

def fertilityClinicsChandigarh(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Chandigarh')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Chandigarh')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Chandigarh')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Chandigarh')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Chandigarh')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-chandigarh.html', context)

def fertilityClinicsFaridabad(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Faridabad')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Faridabad')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Faridabad')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Faridabad')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Faridabad')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-faridabad.html', context)

def fertilityClinicsJamshedpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jamshedpur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Jamshedpur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Jamshedpur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Jamshedpur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Jamshedpur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-jamshedpur.html', context)

def fertilityClinicsBangalore(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bangalore')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Bangalore')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Bangalore')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Bangalore')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Bangalore')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-bangalore.html', context)

def fertilityClinicsTrivandrum(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Trivandrum')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Trivandrum')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Trivandrum')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Trivandrum')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Trivandrum')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-trivandrum.html', context)

def fertilityClinicsKochi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kochi')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Kochi')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Kochi')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Kochi')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Kochi')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-kochi.html', context)

def fertilityClinicsBhopal(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bhopal')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Bhopal')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Bhopal')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Bhopal')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Bhopal')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-bhopal.html', context)

def fertilityClinicsIndore(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Indore')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Indore')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Indore')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Indore')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Indore')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-indore.html', context)

def fertilityClinicsNagpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nagpur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Nagpur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Nagpur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Nagpur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Nagpur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-nagpur.html', context)

def fertilityClinicsBhubaneswar(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Bhubaneswar')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Bhubaneswar')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Bhubaneswar')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Bhubaneswar')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Bhubaneswar')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-bhubaneswar.html', context)

def fertilityClinicsLudhiana(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Ludhiana')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Ludhiana')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Ludhiana')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Ludhiana')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Ludhiana')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-ludhiana.html', context)

def fertilityClinicsJaipur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jaipur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Jaipur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Jaipur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Jaipur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Jaipur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-jaipur.html', context)

def fertilityClinicsLucknow(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Lucknow')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Lucknow')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Lucknow')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Lucknow')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Lucknow')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-lucknow.html', context)

def fertilityClinicsKanpur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kanpur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Kanpur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Kanpur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Kanpur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Kanpur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-kanpur.html', context)

def fertilityClinicsDehradun(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Dehradun')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Dehradun')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Dehradun')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Dehradun')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Dehradun')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-dehradun.html', context)

def fertilityClinicsKolkata(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Kolkata')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Kolkata')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Kolkata')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Kolkata')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Kolkata')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-kolkata.html', context)

def fertilityClinicsVisakhapatnam(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Visakhapatnam')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Visakhapatnam')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Visakhapatnam')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Visakhapatnam')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Visakhapatnam')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-visakhapatnam.html', context)

def fertilityClinicsVijayawada(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Vijayawada')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Vijayawada')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Vijayawada')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Vijayawada')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Vijayawada')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-vijayawada.html', context)

def fertilityClinicsNewDelhi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='New Delhi')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='New Delhi')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='New Delhi')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='New Delhi')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='New Delhi')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-new-delhi.html', context)

def fertilityClinicsVadodara(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Vadodara')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Vadodara')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Vadodara')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Vadodara')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Vadodara')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-vadodara.html', context)

def fertilityClinicsGurugram(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gurugram')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Gurugram')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Gurugram')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Gurugram')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Gurugram')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-gurugram.html', context)

def fertilityClinicsRohtak(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Rohtak')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Rohtak')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Rohtak')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Rohtak')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Rohtak')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-rohtak.html', context)

def fertilityClinicsJammu(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Jammu')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Jammu')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Jammu')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Jammu')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Jammu')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-jammu.html', context)

def fertilityClinicsRanchi(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Ranchi')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Ranchi')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Ranchi')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Ranchi')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Ranchi')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-ranchi.html', context)

def fertilityClinicsGwalior(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gwalior')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Gwalior')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Gwalior')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Gwalior')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Gwalior')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-gwalior.html', context)

def fertilityClinicsPune(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Pune')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Pune')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Pune')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Pune')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Pune')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-pune.html', context)

def fertilityClinicsWarangal(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Warangal')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Warangal')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Warangal')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Warangal')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Warangal')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-warangal.html', context)

def fertilityClinicsGachibowli(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Gachibowli')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Gachibowli')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Gachibowli')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Gachibowli')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Gachibowli')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-gachibowli.html', context)

def fertilityClinicsMadhapur(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Madhapur')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Madhapur')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Madhapur')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Madhapur')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Madhapur')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-madhapur.html', context)

def fertilityClinicsNoida(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Noida')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Noida')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Noida')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Noida')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Noida')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-noida.html', context)

def fertilityClinicsMeerut(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Meerut')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Meerut')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Meerut')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Meerut')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Meerut')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-meerut.html', context)

def fertilityClinicsHaldwani(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Haldwani')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Haldwani')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Haldwani')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Haldwani')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Haldwani')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/India/fertility-clinics-haldwani.html', context)

def fertilityClinicsAthens(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Athens')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Athens')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Athens')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Athens')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Athens')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Greece/fertility-clinic-athens.html', context)

def fertilityClinicsThessaloniki(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Thessaloniki')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Thessaloniki')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Thessaloniki')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Thessaloniki')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Thessaloniki')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Greece/fertility-clinic-thessaloniki.html', context)

def fertilityClinicsNicosia(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Nicosia')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Nicosia')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Nicosia')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Nicosia')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Nicosia')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Cyprus/fertility-clinics-nicosia.html', context)

def fertilityClinicsGirne(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Girne')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Girne')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Girne')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Girne')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Girne')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Cyprus/fertility-clinics-girne.html', context)

def fertilityClinicsCancun(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Cancún')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Cancún')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Cancún')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Cancún')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Cancún')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Mexico/fertility-clinics-cancun.html', context)

def fertilityClinicsMexicoCity(request):
    guestblog = GuestBlog.objects.filter(guestblogcity__iexact='Mexico City')
    guestblog = guestblog.filter(guestblogactive=True)

    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicCity__iexact='Mexico City')
    my_total_count = my_total_count.filter(is_published=True)

    all_clinic_count = BasicClinic.objects.all()
    all_clinic_count = all_clinic_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Mexico').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicCity__iexact='Mexico City')
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='Mexico City')
    ppq_queryset_list = ppq_queryset_list.filter(clinicCity__iexact='Mexico City')


    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = context = {'listings': queryset_list, 'all_clinic_count': all_clinic_count, 'pro_listings': pro_queryset_list, 'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'guestblog': guestblog,}

    return render(request, 'locations-cities/Mexico/fertility-clinics-mexico-city.html', context)

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
