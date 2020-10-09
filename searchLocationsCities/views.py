from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def fertilityClinicPrague1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicPrague'))

def fertilityClinicBrno1(request):
    return HttpResponsePermanentRedirect(reverse('fertilityClinicBrno'))

def fertilityClinicPrague(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Prague').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Prague').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Prague').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Prague').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Prague').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Prague')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Prague')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Prague')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/Czech/fertility-clinic-prague.html', context)

def fertilityClinicBrno(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Brno').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Brno').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Brno').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Brno').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Brno').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Brno')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Brno')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Brno')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/Czech/fertility-clinic-brno.html', context)


def fertilityClinicsAberdeen(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Aberdeen').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Aberdeen')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Aberdeen')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Aberdeen')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Aberdeen')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-aberdeen.html', context)

def fertilityClinicsBath(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bath').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bath').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bath').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bath').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bath').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bath')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bath')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bath')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bath')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-bath.html', context)

def fertilityClinicsBelfast(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Belfast').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Belfast')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Belfast')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Belfast')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Belfast')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-belfast.html', context)

def fertilityClinicsBirmingham(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Birmingham').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Birmingham')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Birmingham')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Birmingham')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Birmingham')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-birmingham.html', context)

def fertilityClinicsBournemouth(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bournemouth').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bournemouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bournemouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bournemouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bournemouth')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-bournemouth.html', context)

def fertilityClinicsBrightonHove(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='BrightonHove').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='BrightonHove').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='BrightonHove').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='BrightonHove').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='BrightonHove').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='BrightonHove')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='BrightonHove')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='BrightonHove')

    my_total_count = my_total_count.filter(clinicRegion__iexact='BrightonHove')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-brighton-hove.html', context)

def fertilityClinicsBristol(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Bristol').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Bristol')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Bristol')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Bristol')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Bristol')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-bristol.html', context)

def fertilityClinicsCambridge(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cambridge').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Cambridge')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Cambridge')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Cambridge')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Cambridge')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-cambridge.html', context)

def fertilityClinicsCardiff(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Cardiff').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Cardiff')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Cardiff')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Cardiff')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Cardiff')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-cardiff.html', context)

def fertilityClinicsColchester(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Colchester').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Colchester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Colchester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Colchester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Colchester')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-colchester.html', context)

def fertilityClinicsDerby(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Derby').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Derby').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Derby').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Derby').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Derby').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Derby')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Derby')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Derby')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Derby')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-derby.html', context)

def fertilityClinicsExeter(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Exeter').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Exeter')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Exeter')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Exeter')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Exeter')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-exeter.html', context)

def fertilityClinicsGlasgow(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Glasgow').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Glasgow')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Glasgow')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Glasgow')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Glasgow')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-glasgow.html', context)

def fertilityClinicsHull(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Hull').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Hull').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Hull').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Hull').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Hull').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Hull')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Hull')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Hull')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Hull')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-hull.html', context)

def fertilityClinicsChelmsford(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Chelmsford').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Chelmsford')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Chelmsford')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Chelmsford')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Chelmsford')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-chelmsford.html', context)

def fertilityClinicsLeeds(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leeds').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Leeds')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Leeds')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Leeds')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Leeds')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-leeds.html', context)

def fertilityClinicsLeicester(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Leicester').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Leicester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Leicester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Leicester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Leicester')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-leicester.html', context)

def fertilityClinicsLiverpool(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Liverpool').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Liverpool')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Liverpool')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Liverpool')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Liverpool')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-liverpool.html', context)

def fertilityClinicsLondon(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='London').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='London').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='London').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='London').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='London').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='London')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='London')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='London')

    my_total_count = my_total_count.filter(clinicRegion__iexact='London')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-london.html', context)

def fertilityClinicsManchester(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Manchester').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Manchester')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Manchester')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Manchester')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Manchester')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-manchester.html', context)

def fertilityClinicsMiddlesbrough(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Middlesbrough').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Middlesbrough')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Middlesbrough')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Middlesbrough')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Middlesbrough')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-middlesbrough.html', context)

def fertilityClinicsNewcastle(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Newcastle').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Newcastle')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Newcastle')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Newcastle')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Newcastle')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-newcastle.html', context)

def fertilityClinicsNorwich(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Norwich').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Norwich')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Norwich')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Norwich')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Norwich')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-norwich.html', context)

def fertilityClinicsNottingham(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Nottingham').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Nottingham')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Nottingham')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Nottingham')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Nottingham')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-nottingham.html', context)

def fertilityClinicsOxford(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Oxford').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Oxford')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Oxford')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Oxford')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Oxford')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-oxford.html', context)

def fertilityClinicsPeterborough(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Peterborough').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Peterborough')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Peterborough')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Peterborough')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Peterborough')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-peterborough.html', context)

def fertilityClinicsPlymouth(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Plymouth').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Plymouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Plymouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Plymouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Plymouth')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-plymouth.html', context)

def fertilityClinicsPortsmouth(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Portsmouth').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Portsmouth')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Portsmouth')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Portsmouth')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Portsmouth')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-portsmouth.html', context)

def fertilityClinicsSalisbury(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Salisbury').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Salisbury')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Salisbury')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Salisbury')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Salisbury')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-salisbury.html', context)

def fertilityClinicsSheffield(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Sheffield').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Sheffield')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Sheffield')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Sheffield')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Sheffield')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-sheffield.html', context)

def fertilityClinicsSouthampton(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Southampton').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Southampton')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Southampton')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Southampton')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Southampton')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-southampton.html', context)

def fertilityClinicsSwansea(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Swansea').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Swansea')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Swansea')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Swansea')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Swansea')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/UK/fertility-clinics-swansea.html', context)

def fertilityClinicsAlicante(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Alicante').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Alicante')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Alicante')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Alicante')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Alicante')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-alicante.html', context)

def fertilityClinicsBarcelona(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Barcelona').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Barcelona')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Barcelona')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Barcelona')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Barcelona')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-barcelona.html', context)

def fertilityClinicsMadrid(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Madrid').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Madrid')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Madrid')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Madrid')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Madrid')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-madrid.html', context)

def fertilityClinicsMalaga(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Malaga').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Malaga')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Malaga')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Malaga')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Malaga')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-malaga.html', context)

def fertilityClinicsSeville(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Seville').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Seville').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Seville').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Seville').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Seville').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Seville')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Seville')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Seville')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Seville')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-seville.html', context)

def fertilityClinicsValencia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='Valencia').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicRegion__iexact='Valencia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Valencia')
    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Valencia')

    my_total_count = my_total_count.filter(clinicRegion__iexact='Valencia')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 12)
    page = request.GET.get('page')
    paginationing = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'order_data': paginationing,
        'paginationing': paginationing,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-cities/SP/fertility-clinics-valencia.html', context)
