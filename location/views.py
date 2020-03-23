from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
gbpToEur = 1.16
gbpToUsd = 1.29

usdToGbp = 0.81
usdToEur = 0.90

def locations(request):
    queryset_list_uk = BasicClinic.objects.all()
    queryset_list_uk = queryset_list_uk.filter(clinicState__iexact='United Kingdom')
    queryset_list_uk_ivf = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_uk_ivf.items():
        gbpCurrency_uk_ivf = val
        if gbpCurrency_uk_ivf is not None:
            usdCurrency_uk_ivf = val * gbpToUsd
            eurCurrency_uk_ivf = val * gbpToEur
        else:
            usdCurrency_uk_ivf = None
            eurCurrency_uk_ivf = None

    queryset_list_uk_egg = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_uk_egg.items():
        gbpCurrency_uk_egg = val
        if gbpCurrency_uk_egg is not None:
            usdCurrency_uk_egg = val * gbpToUsd
            eurCurrency_uk_egg = val * gbpToEur
        else:
            usdCurrency_uk_egg = None
            eurCurrency_uk_egg = None

    queryset_list_uk_embryo = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_uk_embryo.items():
        gbpCurrency_uk_embryo = val
        if gbpCurrency_uk_embryo is not None:
            usdCurrency_uk_embryo = val * gbpToUsd
            eurCurrency_uk_embryo = val * gbpToEur
        else:
            usdCurrency_uk_embryo = None
            eurCurrency_uk_embryo = None

    queryset_list_uk_sperm = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_uk_sperm.items():
        gbpCurrency_uk_sperm = val
        if gbpCurrency_uk_sperm is not None:
            usdCurrency_uk_sperm = val * gbpToUsd
            eurCurrency_uk_sperm = val * gbpToEur
        else:
            usdCurrency_uk_sperm = None
            eurCurrency_uk_sperm = None

    queryset_list_uk_icsi = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_uk_icsi.items():
        gbpCurrency_uk_icsi = val
        if gbpCurrency_uk_icsi is not None:
            usdCurrency_uk_icsi = val * gbpToUsd
            eurCurrency_uk_icsi = val * gbpToEur
        else:
            usdCurrency_uk_icsi = None
            eurCurrency_uk_icsi = None

    queryset_list_uk_iui = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_uk_iui.items():
        gbpCurrency_uk_iui = val
        if gbpCurrency_uk_iui is not None:
            usdCurrency_uk_iui = val * gbpToUsd
            eurCurrency_uk_iui = val * gbpToEur
        else:
            usdCurrency_uk_iui = None
            eurCurrency_uk_iui = None

#-------------------------------------------------------------------------------
    queryset_list_us = BasicClinic.objects.all()
    queryset_list_us = queryset_list_us.filter(clinicState__iexact='United States')
    queryset_list_us_ivf = queryset_list_us.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_us_ivf.items():
        usdCurrency_us_ivf = val
        if usdCurrency_us_ivf is not None:
            gbpCurrency_us_ivf = val * usdToGbp
            eurCurrency_us_ivf = val * usdToEur
        else:
            gbpCurrency_us_ivf = None
            eurCurrency_us_ivf = None

    queryset_list_us_egg = queryset_list_us.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_us_egg.items():
        usdCurrency_us_egg = val
        if usdCurrency_us_egg is not None:
            gbpCurrency_us_egg = val * usdToGbp
            eurCurrency_us_egg = val * usdToEur
        else:
            gbpCurrency_us_egg = None
            eurCurrency_us_egg = None

    queryset_list_us_embryo = queryset_list_us.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_us_embryo.items():
        usdCurrency_us_embryo = val
        if usdCurrency_us_embryo is not None:
            gbpCurrency_us_embryo = val * usdToGbp
            eurCurrency_us_embryo = val * usdToEur
        else:
            gbpCurrency_us_embryo = None
            eurCurrency_us_embryo = None

    queryset_list_us_sperm = queryset_list_us.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_us_sperm.items():
        usdCurrency_us_sperm = val
        if usdCurrency_us_sperm is not None:
            gbpCurrency_us_sperm = val * usdToGbp
            eurCurrency_us_sperm = val * usdToEur
        else:
            gbpCurrency_us_sperm = None
            eurCurrency_us_sperm = None

    queryset_list_us_icsi = queryset_list_us.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_us_icsi.items():
        usdCurrency_us_icsi = val
        if usdCurrency_us_icsi is not None:
            gbpCurrency_us_icsi = val * usdToGbp
            eurCurrency_us_icsi = val * usdToEur
        else:
            gbpCurrency_us_icsi = None
            eurCurrency_us_icsi = None

    queryset_list_us_iui = queryset_list_us.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_us_iui.items():
        usdCurrency_us_iui = val
        if usdCurrency_us_iui is not None:
            gbpCurrency_us_iui = val * usdToGbp
            eurCurrency_us_iui = val * usdToEur
        else:
            gbpCurrency_us_iui = None
            eurCurrency_us_iui = None

    context = {
        'gbpCurrency_uk_ivf': gbpCurrency_uk_ivf,
        'usdCurrency_uk_ivf': usdCurrency_uk_ivf,
        'eurCurrency_uk_ivf': eurCurrency_uk_ivf,
        'gbpCurrency_uk_egg': gbpCurrency_uk_egg,
        'usdCurrency_uk_egg': usdCurrency_uk_egg,
        'eurCurrency_uk_egg': eurCurrency_uk_egg,
        'gbpCurrency_uk_embryo': gbpCurrency_uk_embryo,
        'usdCurrency_uk_embryo': usdCurrency_uk_embryo,
        'eurCurrency_uk_embryo': eurCurrency_uk_embryo,
        'gbpCurrency_uk_sperm': gbpCurrency_uk_sperm,
        'usdCurrency_uk_sperm': usdCurrency_uk_sperm,
        'eurCurrency_uk_sperm': eurCurrency_uk_sperm,
        'gbpCurrency_uk_icsi': gbpCurrency_uk_icsi,
        'usdCurrency_uk_icsi': usdCurrency_uk_icsi,
        'eurCurrency_uk_icsi': eurCurrency_uk_icsi,
        'gbpCurrency_uk_iui': gbpCurrency_uk_iui,
        'usdCurrency_uk_iui': usdCurrency_uk_iui,
        'eurCurrency_uk_iui': eurCurrency_uk_iui,
        'gbpCurrency_us_ivf': gbpCurrency_us_ivf,
        'usdCurrency_us_ivf': usdCurrency_us_ivf,
        'eurCurrency_us_ivf': eurCurrency_us_ivf,
        'gbpCurrency_us_egg': gbpCurrency_us_egg,
        'usdCurrency_us_egg': usdCurrency_us_egg,
        'eurCurrency_us_egg': eurCurrency_us_egg,
        'gbpCurrency_us_embryo': gbpCurrency_us_embryo,
        'usdCurrency_us_embryo': usdCurrency_us_embryo,
        'eurCurrency_us_embryo': eurCurrency_us_embryo,
        'gbpCurrency_us_sperm': gbpCurrency_us_sperm,
        'usdCurrency_us_sperm': usdCurrency_us_sperm,
        'eurCurrency_us_sperm': eurCurrency_us_sperm,
        'gbpCurrency_us_icsi': gbpCurrency_us_icsi,
        'usdCurrency_us_icsi': usdCurrency_us_icsi,
        'eurCurrency_us_icsi': eurCurrency_us_icsi,
        'gbpCurrency_us_iui': gbpCurrency_us_iui,
        'usdCurrency_us_iui': usdCurrency_us_iui,
        'eurCurrency_us_iui': eurCurrency_us_iui,
        }

    return render(request, 'main/locations.html', context)


def locationsUSRegions(request):
    queryset_list_us = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_alabama = queryset_list_us.filter(clinicRegion__iexact='Alabama')
    queryset_list_alabama_ivf = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_alabama_ivf.items():
        usdCurrency_alabama_ivf = val
        if usdCurrency_alabama_ivf is not None:
            gbpCurrency_alabama_ivf = val * usdToGbp
            eurCurrency_alabama_ivf = val * usdToEur
        else:
            gbpCurrency_alabama_ivf = None
            eurCurrency_alabama_ivf = None

    queryset_list_alabama_egg = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alabama_egg.items():
        usdCurrency_alabama_egg = val
        if usdCurrency_alabama_egg is not None:
            gbpCurrency_alabama_egg = val * usdToGbp
            eurCurrency_alabama_egg = val * usdToEur
        else:
            gbpCurrency_alabama_egg = None
            eurCurrency_alabama_egg = None

    queryset_list_alabama_embryo = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alabama_embryo.items():
        usdCurrency_alabama_embryo = val
        if usdCurrency_alabama_embryo is not None:
            gbpCurrency_alabama_embryo = val * usdToGbp
            eurCurrency_alabama_embryo = val * usdToEur
        else:
            gbpCurrency_alabama_embryo = None
            eurCurrency_alabama_embryo = None

    queryset_list_alabama_sperm = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alabama_sperm.items():
        usdCurrency_alabama_sperm = val
        if usdCurrency_alabama_sperm is not None:
            gbpCurrency_alabama_sperm = val * usdToGbp
            eurCurrency_alabama_sperm = val * usdToEur
        else:
            gbpCurrency_alabama_sperm = None
            eurCurrency_alabama_sperm = None

    queryset_list_alabama_icsi = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alabama_icsi.items():
        usdCurrency_alabama_icsi = val
        if usdCurrency_alabama_icsi is not None:
            gbpCurrency_alabama_icsi = val * usdToGbp
            eurCurrency_alabama_icsi = val * usdToEur
        else:
            gbpCurrency_alabama_icsi = None
            eurCurrency_alabama_icsi = None

    queryset_list_alabama_iui = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alabama_iui.items():
        usdCurrency_alabama_iui = val
        if usdCurrency_alabama_iui is not None:
            gbpCurrency_alabama_iui = val * usdToGbp
            eurCurrency_alabama_iui = val * usdToEur
        else:
            gbpCurrency_alabama_iui = None
            eurCurrency_alabama_iui = None

    #--------------------------------------------------------------------------
    queryset_list_alaska = queryset_list_us.filter(clinicRegion__iexact='Alaska')
    queryset_list_alaska_ivf = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_alaska_ivf.items():
        usdCurrency_alaska_ivf = val
        if usdCurrency_alaska_ivf is not None:
            gbpCurrency_alaska_ivf = val * usdToGbp
            eurCurrency_alaska_ivf = val * usdToEur
        else:
            gbpCurrency_alaska_ivf = None
            eurCurrency_alaska_ivf = None

    queryset_list_alaska_egg = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alaska_egg.items():
        usdCurrency_alaska_egg = val
        if usdCurrency_alaska_egg is not None:
            gbpCurrency_alaska_egg = val * usdToGbp
            eurCurrency_alaska_egg = val * usdToEur
        else:
            gbpCurrency_alaska_egg = None
            eurCurrency_alaska_egg = None

    queryset_list_alaska_embryo = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alaska_embryo.items():
        usdCurrency_alaska_embryo = val
        if usdCurrency_alaska_embryo is not None:
            gbpCurrency_alaska_embryo = val * usdToGbp
            eurCurrency_alaska_embryo = val * usdToEur
        else:
            gbpCurrency_alaska_embryo = None
            eurCurrency_alaska_embryo = None

    queryset_list_alaska_sperm = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alaska_sperm.items():
        usdCurrency_alaska_sperm = val
        if usdCurrency_alaska_sperm is not None:
            gbpCurrency_alaska_sperm = val * usdToGbp
            eurCurrency_alaska_sperm = val * usdToEur
        else:
            gbpCurrency_alaska_sperm = None
            eurCurrency_alaska_sperm = None

    queryset_list_alaska_icsi = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alaska_icsi.items():
        usdCurrency_alaska_icsi = val
        if usdCurrency_alaska_icsi is not None:
            gbpCurrency_alaska_icsi = val * usdToGbp
            eurCurrency_alaska_icsi = val * usdToEur
        else:
            gbpCurrency_alaska_icsi = None
            eurCurrency_alaska_icsi = None

    queryset_list_alaska_iui = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alaska_iui.items():
        usdCurrency_alaska_iui = val
        if usdCurrency_alaska_iui is not None:
            gbpCurrency_alaska_iui = val * usdToGbp
            eurCurrency_alaska_iui = val * usdToEur
        else:
            gbpCurrency_alaska_iui = None
            eurCurrency_alaska_iui = None

    #--------------------------------------------------------------------------
    queryset_list_arizona = queryset_list_us.filter(clinicRegion__iexact='Arizona')
    queryset_list_arizona_ivf = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_arizona_ivf.items():
        usdCurrency_arizona_ivf = val
        if usdCurrency_arizona_ivf is not None:
            gbpCurrency_arizona_ivf = val * usdToGbp
            eurCurrency_arizona_ivf = val * usdToEur
        else:
            gbpCurrency_arizona_ivf = None
            eurCurrency_arizona_ivf = None

    queryset_list_arizona_egg = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_arizona_egg.items():
        usdCurrency_arizona_egg = val
        if usdCurrency_arizona_egg is not None:
            gbpCurrency_arizona_egg = val * usdToGbp
            eurCurrency_arizona_egg = val * usdToEur
        else:
            gbpCurrency_arizona_egg = None
            eurCurrency_arizona_egg = None

    queryset_list_arizona_embryo = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_arizona_embryo.items():
        usdCurrency_arizona_embryo = val
        if usdCurrency_arizona_embryo is not None:
            gbpCurrency_arizona_embryo = val * usdToGbp
            eurCurrency_arizona_embryo = val * usdToEur
        else:
            gbpCurrency_arizona_embryo = None
            eurCurrency_arizona_embryo = None

    queryset_list_arizona_sperm = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_arizona_sperm.items():
        usdCurrency_arizona_sperm = val
        if usdCurrency_arizona_sperm is not None:
            gbpCurrency_arizona_sperm = val * usdToGbp
            eurCurrency_arizona_sperm = val * usdToEur
        else:
            gbpCurrency_arizona_sperm = None
            eurCurrency_arizona_sperm = None

    queryset_list_arizona_icsi = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_arizona_icsi.items():
        usdCurrency_arizona_icsi = val
        if usdCurrency_arizona_icsi is not None:
            gbpCurrency_arizona_icsi = val * usdToGbp
            eurCurrency_arizona_icsi = val * usdToEur
        else:
            gbpCurrency_arizona_icsi = None
            eurCurrency_arizona_icsi = None

    queryset_list_arizona_iui = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_arizona_iui.items():
        usdCurrency_arizona_iui = val
        if usdCurrency_arizona_iui is not None:
            gbpCurrency_arizona_iui = val * usdToGbp
            eurCurrency_arizona_iui = val * usdToEur
        else:
            gbpCurrency_arizona_iui = None
            eurCurrency_arizona_iui = None

    #--------------------------------------------------------------------------
    queryset_list_arkansas = queryset_list_us.filter(clinicRegion__iexact='Arkansas')
    queryset_list_arkansas_ivf = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_arkansas_ivf.items():
        usdCurrency_arkansas_ivf = val
        if usdCurrency_arkansas_ivf is not None:
            gbpCurrency_arkansas_ivf = val * usdToGbp
            eurCurrency_arkansas_ivf = val * usdToEur
        else:
            gbpCurrency_arkansas_ivf = None
            eurCurrency_arkansas_ivf = None

    queryset_list_arkansas_egg = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_egg.items():
        usdCurrency_arkansas_egg = val
        if usdCurrency_arkansas_egg is not None:
            gbpCurrency_arkansas_egg = val * usdToGbp
            eurCurrency_arkansas_egg = val * usdToEur
        else:
            gbpCurrency_arkansas_egg = None
            eurCurrency_arkansas_egg = None

    queryset_list_arkansas_embryo = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_embryo.items():
        usdCurrency_arkansas_embryo = val
        if usdCurrency_arkansas_embryo is not None:
            gbpCurrency_arkansas_embryo = val * usdToGbp
            eurCurrency_arkansas_embryo = val * usdToEur
        else:
            gbpCurrency_arkansas_embryo = None
            eurCurrency_arkansas_embryo = None

    queryset_list_arkansas_sperm = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_sperm.items():
        usdCurrency_arkansas_sperm = val
        if usdCurrency_arkansas_sperm is not None:
            gbpCurrency_arkansas_sperm = val * usdToGbp
            eurCurrency_arkansas_sperm = val * usdToEur
        else:
            gbpCurrency_arkansas_sperm = None
            eurCurrency_arkansas_sperm = None

    queryset_list_arkansas_icsi = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_arkansas_icsi.items():
        usdCurrency_arkansas_icsi = val
        if usdCurrency_arkansas_icsi is not None:
            gbpCurrency_arkansas_icsi = val * usdToGbp
            eurCurrency_arkansas_icsi = val * usdToEur
        else:
            gbpCurrency_arkansas_icsi = None
            eurCurrency_arkansas_icsi = None

    queryset_list_arkansas_iui = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_arkansas_iui.items():
        usdCurrency_arkansas_iui = val
        if usdCurrency_arkansas_iui is not None:
            gbpCurrency_arkansas_iui = val * usdToGbp
            eurCurrency_arkansas_iui = val * usdToEur
        else:
            gbpCurrency_arkansas_iui = None
            eurCurrency_arkansas_iui = None

    #--------------------------------------------------------------------------
    queryset_list_california = queryset_list_us.filter(clinicRegion__iexact='California')
    queryset_list_california_ivf = queryset_list_california.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_california_ivf.items():
        usdCurrency_california_ivf = val
        if usdCurrency_california_ivf is not None:
            gbpCurrency_california_ivf = val * usdToGbp
            eurCurrency_california_ivf = val * usdToEur
        else:
            gbpCurrency_california_ivf = None
            eurCurrency_california_ivf = None

    queryset_list_california_egg = queryset_list_california.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_california_egg.items():
        usdCurrency_california_egg = val
        if usdCurrency_california_egg is not None:
            gbpCurrency_california_egg = val * usdToGbp
            eurCurrency_california_egg = val * usdToEur
        else:
            gbpCurrency_california_egg = None
            eurCurrency_california_egg = None

    queryset_list_california_embryo = queryset_list_california.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_california_embryo.items():
        usdCurrency_california_embryo = val
        if usdCurrency_california_embryo is not None:
            gbpCurrency_california_embryo = val * usdToGbp
            eurCurrency_california_embryo = val * usdToEur
        else:
            gbpCurrency_california_embryo = None
            eurCurrency_california_embryo = None

    queryset_list_california_sperm = queryset_list_california.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_california_sperm.items():
        usdCurrency_california_sperm = val
        if usdCurrency_california_sperm is not None:
            gbpCurrency_california_sperm = val * usdToGbp
            eurCurrency_california_sperm = val * usdToEur
        else:
            gbpCurrency_california_sperm = None
            eurCurrency_california_sperm = None

    queryset_list_california_icsi = queryset_list_california.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_california_icsi.items():
        usdCurrency_california_icsi = val
        if usdCurrency_california_icsi is not None:
            gbpCurrency_california_icsi = val * usdToGbp
            eurCurrency_california_icsi = val * usdToEur
        else:
            gbpCurrency_california_icsi = None
            eurCurrency_california_icsi = None

    queryset_list_california_iui = queryset_list_california.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_california_iui.items():
        usdCurrency_california_iui = val
        if usdCurrency_california_iui is not None:
            gbpCurrency_california_iui = val * usdToGbp
            eurCurrency_california_iui = val * usdToEur
        else:
            gbpCurrency_california_iui = None
            eurCurrency_california_iui = None

    #--------------------------------------------------------------------------
    queryset_list_colorado = queryset_list_us.filter(clinicRegion__iexact='Colorado')
    queryset_list_colorado_ivf = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_colorado_ivf.items():
        usdCurrency_colorado_ivf = val
        if usdCurrency_colorado_ivf is not None:
            gbpCurrency_colorado_ivf = val * usdToGbp
            eurCurrency_colorado_ivf = val * usdToEur
        else:
            gbpCurrency_colorado_ivf = None
            eurCurrency_colorado_ivf = None

    queryset_list_colorado_egg = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_colorado_egg.items():
        usdCurrency_colorado_egg = val
        if usdCurrency_colorado_egg is not None:
            gbpCurrency_colorado_egg = val * usdToGbp
            eurCurrency_colorado_egg = val * usdToEur
        else:
            gbpCurrency_colorado_egg = None
            eurCurrency_colorado_egg = None

    queryset_list_colorado_embryo = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_colorado_embryo.items():
        usdCurrency_colorado_embryo = val
        if usdCurrency_colorado_embryo is not None:
            gbpCurrency_colorado_embryo = val * usdToGbp
            eurCurrency_colorado_embryo = val * usdToEur
        else:
            gbpCurrency_colorado_embryo = None
            eurCurrency_colorado_embryo = None

    queryset_list_colorado_sperm = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_colorado_sperm.items():
        usdCurrency_colorado_sperm = val
        if usdCurrency_colorado_sperm is not None:
            gbpCurrency_colorado_sperm = val * usdToGbp
            eurCurrency_colorado_sperm = val * usdToEur
        else:
            gbpCurrency_colorado_sperm = None
            eurCurrency_colorado_sperm = None

    queryset_list_colorado_icsi = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_colorado_icsi.items():
        usdCurrency_colorado_icsi = val
        if usdCurrency_colorado_icsi is not None:
            gbpCurrency_colorado_icsi = val * usdToGbp
            eurCurrency_colorado_icsi = val * usdToEur
        else:
            gbpCurrency_colorado_icsi = None
            eurCurrency_colorado_icsi = None

    queryset_list_colorado_iui = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_colorado_iui.items():
        usdCurrency_colorado_iui = val
        if usdCurrency_colorado_iui is not None:
            gbpCurrency_colorado_iui = val * usdToGbp
            eurCurrency_colorado_iui = val * usdToEur
        else:
            gbpCurrency_colorado_iui = None
            eurCurrency_colorado_iui = None

    #--------------------------------------------------------------------------
    queryset_list_connecticut = queryset_list_us.filter(clinicRegion__iexact='Connecticut')
    queryset_list_connecticut_ivf = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_connecticut_ivf.items():
        usdCurrency_connecticut_ivf = val
        if usdCurrency_connecticut_ivf is not None:
            gbpCurrency_connecticut_ivf = val * usdToGbp
            eurCurrency_connecticut_ivf = val * usdToEur
        else:
            gbpCurrency_connecticut_ivf = None
            eurCurrency_connecticut_ivf = None

    queryset_list_connecticut_egg = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_egg.items():
        usdCurrency_connecticut_egg = val
        if usdCurrency_connecticut_egg is not None:
            gbpCurrency_connecticut_egg = val * usdToGbp
            eurCurrency_connecticut_egg = val * usdToEur
        else:
            gbpCurrency_connecticut_egg = None
            eurCurrency_connecticut_egg = None

    queryset_list_connecticut_embryo = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_embryo.items():
        usdCurrency_connecticut_embryo = val
        if usdCurrency_connecticut_embryo is not None:
            gbpCurrency_connecticut_embryo = val * usdToGbp
            eurCurrency_connecticut_embryo = val * usdToEur
        else:
            gbpCurrency_connecticut_embryo = None
            eurCurrency_connecticut_embryo = None

    queryset_list_connecticut_sperm = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_sperm.items():
        usdCurrency_connecticut_sperm = val
        if usdCurrency_connecticut_sperm is not None:
            gbpCurrency_connecticut_sperm = val * usdToGbp
            eurCurrency_connecticut_sperm = val * usdToEur
        else:
            gbpCurrency_connecticut_sperm = None
            eurCurrency_connecticut_sperm = None

    queryset_list_connecticut_icsi = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_connecticut_icsi.items():
        usdCurrency_connecticut_icsi = val
        if usdCurrency_connecticut_icsi is not None:
            gbpCurrency_connecticut_icsi = val * usdToGbp
            eurCurrency_connecticut_icsi = val * usdToEur
        else:
            gbpCurrency_connecticut_icsi = None
            eurCurrency_connecticut_icsi = None

    queryset_list_connecticut_iui = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_connecticut_iui.items():
        usdCurrency_connecticut_iui = val
        if usdCurrency_connecticut_iui is not None:
            gbpCurrency_connecticut_iui = val * usdToGbp
            eurCurrency_connecticut_iui = val * usdToEur
        else:
            gbpCurrency_connecticut_iui = None
            eurCurrency_connecticut_iui = None

    #--------------------------------------------------------------------------
    queryset_list_delaware = queryset_list_us.filter(clinicRegion__iexact='Delaware')
    queryset_list_delaware_ivf = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_delaware_ivf.items():
        usdCurrency_delaware_ivf = val
        if usdCurrency_delaware_ivf is not None:
            gbpCurrency_delaware_ivf = val * usdToGbp
            eurCurrency_delaware_ivf = val * usdToEur
        else:
            gbpCurrency_delaware_ivf = None
            eurCurrency_delaware_ivf = None

    queryset_list_delaware_egg = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_delaware_egg.items():
        usdCurrency_delaware_egg = val
        if usdCurrency_delaware_egg is not None:
            gbpCurrency_delaware_egg = val * usdToGbp
            eurCurrency_delaware_egg = val * usdToEur
        else:
            gbpCurrency_delaware_egg = None
            eurCurrency_delaware_egg = None

    queryset_list_delaware_embryo = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_delaware_embryo.items():
        usdCurrency_delaware_embryo = val
        if usdCurrency_delaware_embryo is not None:
            gbpCurrency_delaware_embryo = val * usdToGbp
            eurCurrency_delaware_embryo = val * usdToEur
        else:
            gbpCurrency_delaware_embryo = None
            eurCurrency_delaware_embryo = None

    queryset_list_delaware_sperm = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_delaware_sperm.items():
        usdCurrency_delaware_sperm = val
        if usdCurrency_delaware_sperm is not None:
            gbpCurrency_delaware_sperm = val * usdToGbp
            eurCurrency_delaware_sperm = val * usdToEur
        else:
            gbpCurrency_delaware_sperm = None
            eurCurrency_delaware_sperm = None

    queryset_list_delaware_icsi = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_delaware_icsi.items():
        usdCurrency_delaware_icsi = val
        if usdCurrency_delaware_icsi is not None:
            gbpCurrency_delaware_icsi = val * usdToGbp
            eurCurrency_delaware_icsi = val * usdToEur
        else:
            gbpCurrency_delaware_icsi = None
            eurCurrency_delaware_icsi = None

    queryset_list_delaware_iui = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_delaware_iui.items():
        usdCurrency_delaware_iui = val
        if usdCurrency_delaware_iui is not None:
            gbpCurrency_delaware_iui = val * usdToGbp
            eurCurrency_delaware_iui = val * usdToEur
        else:
            gbpCurrency_delaware_iui = None
            eurCurrency_delaware_iui = None

    #--------------------------------------------------------------------------
    queryset_list_florida = queryset_list_us.filter(clinicRegion__iexact='Florida')
    queryset_list_florida_ivf = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_florida_ivf.items():
        usdCurrency_florida_ivf = val
        if usdCurrency_florida_ivf is not None:
            gbpCurrency_florida_ivf = val * usdToGbp
            eurCurrency_florida_ivf = val * usdToEur
        else:
            gbpCurrency_florida_ivf = None
            eurCurrency_florida_ivf = None

    queryset_list_florida_egg = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_florida_egg.items():
        usdCurrency_florida_egg = val
        if usdCurrency_florida_egg is not None:
            gbpCurrency_florida_egg = val * usdToGbp
            eurCurrency_florida_egg = val * usdToEur
        else:
            gbpCurrency_florida_egg = None
            eurCurrency_florida_egg = None

    queryset_list_florida_embryo = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_florida_embryo.items():
        usdCurrency_florida_embryo = val
        if usdCurrency_florida_embryo is not None:
            gbpCurrency_florida_embryo = val * usdToGbp
            eurCurrency_florida_embryo = val * usdToEur
        else:
            gbpCurrency_florida_embryo = None
            eurCurrency_florida_embryo = None

    queryset_list_florida_sperm = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_florida_sperm.items():
        usdCurrency_florida_sperm = val
        if usdCurrency_florida_sperm is not None:
            gbpCurrency_florida_sperm = val * usdToGbp
            eurCurrency_florida_sperm = val * usdToEur
        else:
            gbpCurrency_florida_sperm = None
            eurCurrency_florida_sperm = None

    queryset_list_florida_icsi = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_florida_icsi.items():
        usdCurrency_florida_icsi = val
        if usdCurrency_florida_icsi is not None:
            gbpCurrency_florida_icsi = val * usdToGbp
            eurCurrency_florida_icsi = val * usdToEur
        else:
            gbpCurrency_florida_icsi = None
            eurCurrency_florida_icsi = None

    queryset_list_florida_iui = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_florida_iui.items():
        usdCurrency_florida_iui = val
        if usdCurrency_florida_iui is not None:
            gbpCurrency_florida_iui = val * usdToGbp
            eurCurrency_florida_iui = val * usdToEur
        else:
            gbpCurrency_florida_iui = None
            eurCurrency_florida_iui = None

    #--------------------------------------------------------------------------
    queryset_list_georgia = queryset_list_us.filter(clinicRegion__iexact='Georgia')
    queryset_list_georgia_ivf = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_georgia_ivf.items():
        usdCurrency_georgia_ivf = val
        if usdCurrency_georgia_ivf is not None:
            gbpCurrency_georgia_ivf = val * usdToGbp
            eurCurrency_georgia_ivf = val * usdToEur
        else:
            gbpCurrency_georgia_ivf = None
            eurCurrency_georgia_ivf = None

    queryset_list_georgia_egg = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_georgia_egg.items():
        usdCurrency_georgia_egg = val
        if usdCurrency_georgia_egg is not None:
            gbpCurrency_georgia_egg = val * usdToGbp
            eurCurrency_georgia_egg = val * usdToEur
        else:
            gbpCurrency_georgia_egg = None
            eurCurrency_georgia_egg = None

    queryset_list_georgia_embryo = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_georgia_embryo.items():
        usdCurrency_georgia_embryo = val
        if usdCurrency_georgia_embryo is not None:
            gbpCurrency_georgia_embryo = val * usdToGbp
            eurCurrency_georgia_embryo = val * usdToEur
        else:
            gbpCurrency_georgia_embryo = None
            eurCurrency_georgia_embryo = None

    queryset_list_georgia_sperm = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_georgia_sperm.items():
        usdCurrency_georgia_sperm = val
        if usdCurrency_georgia_sperm is not None:
            gbpCurrency_georgia_sperm = val * usdToGbp
            eurCurrency_georgia_sperm = val * usdToEur
        else:
            gbpCurrency_georgia_sperm = None
            eurCurrency_georgia_sperm = None

    queryset_list_georgia_icsi = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_georgia_icsi.items():
        usdCurrency_georgia_icsi = val
        if usdCurrency_georgia_icsi is not None:
            gbpCurrency_georgia_icsi = val * usdToGbp
            eurCurrency_georgia_icsi = val * usdToEur
        else:
            gbpCurrency_georgia_icsi = None
            eurCurrency_georgia_icsi = None

    queryset_list_georgia_iui = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_georgia_iui.items():
        usdCurrency_georgia_iui = val
        if usdCurrency_georgia_iui is not None:
            gbpCurrency_georgia_iui = val * usdToGbp
            eurCurrency_georgia_iui = val * usdToEur
        else:
            gbpCurrency_georgia_iui = None
            eurCurrency_georgia_iui = None

    #--------------------------------------------------------------------------
    queryset_list_hawaii = queryset_list_us.filter(clinicRegion__iexact='Hawaii')
    queryset_list_hawaii_ivf = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_hawaii_ivf.items():
        usdCurrency_hawaii_ivf = val
        if usdCurrency_hawaii_ivf is not None:
            gbpCurrency_hawaii_ivf = val * usdToGbp
            eurCurrency_hawaii_ivf = val * usdToEur
        else:
            gbpCurrency_hawaii_ivf = None
            eurCurrency_hawaii_ivf = None

    queryset_list_hawaii_egg = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_egg.items():
        usdCurrency_hawaii_egg = val
        if usdCurrency_hawaii_egg is not None:
            gbpCurrency_hawaii_egg = val * usdToGbp
            eurCurrency_hawaii_egg = val * usdToEur
        else:
            gbpCurrency_hawaii_egg = None
            eurCurrency_hawaii_egg = None

    queryset_list_hawaii_embryo = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_embryo.items():
        usdCurrency_hawaii_embryo = val
        if usdCurrency_hawaii_embryo is not None:
            gbpCurrency_hawaii_embryo = val * usdToGbp
            eurCurrency_hawaii_embryo = val * usdToEur
        else:
            gbpCurrency_hawaii_embryo = None
            eurCurrency_hawaii_embryo = None

    queryset_list_hawaii_sperm = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_sperm.items():
        usdCurrency_hawaii_sperm = val
        if usdCurrency_hawaii_sperm is not None:
            gbpCurrency_hawaii_sperm = val * usdToGbp
            eurCurrency_hawaii_sperm = val * usdToEur
        else:
            gbpCurrency_hawaii_sperm = None
            eurCurrency_hawaii_sperm = None

    queryset_list_hawaii_icsi = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_hawaii_icsi.items():
        usdCurrency_hawaii_icsi = val
        if usdCurrency_hawaii_icsi is not None:
            gbpCurrency_hawaii_icsi = val * usdToGbp
            eurCurrency_hawaii_icsi = val * usdToEur
        else:
            gbpCurrency_hawaii_icsi = None
            eurCurrency_hawaii_icsi = None

    queryset_list_hawaii_iui = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_hawaii_iui.items():
        usdCurrency_hawaii_iui = val
        if usdCurrency_hawaii_iui is not None:
            gbpCurrency_hawaii_iui = val * usdToGbp
            eurCurrency_hawaii_iui = val * usdToEur
        else:
            gbpCurrency_hawaii_iui = None
            eurCurrency_hawaii_iui = None

    #--------------------------------------------------------------------------
    queryset_list_idaho = queryset_list_us.filter(clinicRegion__iexact='Idaho')
    queryset_list_idaho_ivf = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_idaho_ivf.items():
        usdCurrency_idaho_ivf = val
        if usdCurrency_idaho_ivf is not None:
            gbpCurrency_idaho_ivf = val * usdToGbp
            eurCurrency_idaho_ivf = val * usdToEur
        else:
            gbpCurrency_idaho_ivf = None
            eurCurrency_idaho_ivf = None

    queryset_list_idaho_egg = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_idaho_egg.items():
        usdCurrency_idaho_egg = val
        if usdCurrency_idaho_egg is not None:
            gbpCurrency_idaho_egg = val * usdToGbp
            eurCurrency_idaho_egg = val * usdToEur
        else:
            gbpCurrency_idaho_egg = None
            eurCurrency_idaho_egg = None

    queryset_list_idaho_embryo = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_idaho_embryo.items():
        usdCurrency_idaho_embryo = val
        if usdCurrency_idaho_embryo is not None:
            gbpCurrency_idaho_embryo = val * usdToGbp
            eurCurrency_idaho_embryo = val * usdToEur
        else:
            gbpCurrency_idaho_embryo = None
            eurCurrency_idaho_embryo = None

    queryset_list_idaho_sperm = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_idaho_sperm.items():
        usdCurrency_idaho_sperm = val
        if usdCurrency_idaho_sperm is not None:
            gbpCurrency_idaho_sperm = val * usdToGbp
            eurCurrency_idaho_sperm = val * usdToEur
        else:
            gbpCurrency_idaho_sperm = None
            eurCurrency_idaho_sperm = None

    queryset_list_idaho_icsi = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_idaho_icsi.items():
        usdCurrency_idaho_icsi = val
        if usdCurrency_idaho_icsi is not None:
            gbpCurrency_idaho_icsi = val * usdToGbp
            eurCurrency_idaho_icsi = val * usdToEur
        else:
            gbpCurrency_idaho_icsi = None
            eurCurrency_idaho_icsi = None

    queryset_list_idaho_iui = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_idaho_iui.items():
        usdCurrency_idaho_iui = val
        if usdCurrency_idaho_iui is not None:
            gbpCurrency_idaho_iui = val * usdToGbp
            eurCurrency_idaho_iui = val * usdToEur
        else:
            gbpCurrency_idaho_iui = None
            eurCurrency_idaho_iui = None

    #--------------------------------------------------------------------------
    queryset_list_illinois = queryset_list_us.filter(clinicRegion__iexact='Illinois')
    queryset_list_illinois_ivf = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_illinois_ivf.items():
        usdCurrency_illinois_ivf = val
        if usdCurrency_illinois_ivf is not None:
            gbpCurrency_illinois_ivf = val * usdToGbp
            eurCurrency_illinois_ivf = val * usdToEur
        else:
            gbpCurrency_illinois_ivf = None
            eurCurrency_illinois_ivf = None

    queryset_list_illinois_egg = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_illinois_egg.items():
        usdCurrency_illinois_egg = val
        if usdCurrency_illinois_egg is not None:
            gbpCurrency_illinois_egg = val * usdToGbp
            eurCurrency_illinois_egg = val * usdToEur
        else:
            gbpCurrency_illinois_egg = None
            eurCurrency_illinois_egg = None

    queryset_list_illinois_embryo = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_illinois_embryo.items():
        usdCurrency_illinois_embryo = val
        if usdCurrency_illinois_embryo is not None:
            gbpCurrency_illinois_embryo = val * usdToGbp
            eurCurrency_illinois_embryo = val * usdToEur
        else:
            gbpCurrency_illinois_embryo = None
            eurCurrency_illinois_embryo = None

    queryset_list_illinois_sperm = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_illinois_sperm.items():
        usdCurrency_illinois_sperm = val
        if usdCurrency_illinois_sperm is not None:
            gbpCurrency_illinois_sperm = val * usdToGbp
            eurCurrency_illinois_sperm = val * usdToEur
        else:
            gbpCurrency_illinois_sperm = None
            eurCurrency_illinois_sperm = None

    queryset_list_illinois_icsi = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_illinois_icsi.items():
        usdCurrency_illinois_icsi = val
        if usdCurrency_illinois_icsi is not None:
            gbpCurrency_illinois_icsi = val * usdToGbp
            eurCurrency_illinois_icsi = val * usdToEur
        else:
            gbpCurrency_illinois_icsi = None
            eurCurrency_illinois_icsi = None

    queryset_list_illinois_iui = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_illinois_iui.items():
        usdCurrency_illinois_iui = val
        if usdCurrency_illinois_iui is not None:
            gbpCurrency_illinois_iui = val * usdToGbp
            eurCurrency_illinois_iui = val * usdToEur
        else:
            gbpCurrency_illinois_iui = None
            eurCurrency_illinois_iui = None

    #--------------------------------------------------------------------------
    queryset_list_indiana = queryset_list_us.filter(clinicRegion__iexact='Indiana')
    queryset_list_indiana_ivf = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_indiana_ivf.items():
        usdCurrency_indiana_ivf = val
        if usdCurrency_indiana_ivf is not None:
            gbpCurrency_indiana_ivf = val * usdToGbp
            eurCurrency_indiana_ivf = val * usdToEur
        else:
            gbpCurrency_indiana_ivf = None
            eurCurrency_indiana_ivf = None

    queryset_list_indiana_egg = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_indiana_egg.items():
        usdCurrency_indiana_egg = val
        if usdCurrency_indiana_egg is not None:
            gbpCurrency_indiana_egg = val * usdToGbp
            eurCurrency_indiana_egg = val * usdToEur
        else:
            gbpCurrency_indiana_egg = None
            eurCurrency_indiana_egg = None

    queryset_list_indiana_embryo = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_indiana_embryo.items():
        usdCurrency_indiana_embryo = val
        if usdCurrency_indiana_embryo is not None:
            gbpCurrency_indiana_embryo = val * usdToGbp
            eurCurrency_indiana_embryo = val * usdToEur
        else:
            gbpCurrency_indiana_embryo = None
            eurCurrency_indiana_embryo = None

    queryset_list_indiana_sperm = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_indiana_sperm.items():
        usdCurrency_indiana_sperm = val
        if usdCurrency_indiana_sperm is not None:
            gbpCurrency_indiana_sperm = val * usdToGbp
            eurCurrency_indiana_sperm = val * usdToEur
        else:
            gbpCurrency_indiana_sperm = None
            eurCurrency_indiana_sperm = None

    queryset_list_indiana_icsi = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_indiana_icsi.items():
        usdCurrency_indiana_icsi = val
        if usdCurrency_indiana_icsi is not None:
            gbpCurrency_indiana_icsi = val * usdToGbp
            eurCurrency_indiana_icsi = val * usdToEur
        else:
            gbpCurrency_indiana_icsi = None
            eurCurrency_indiana_icsi = None

    queryset_list_indiana_iui = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_indiana_iui.items():
        usdCurrency_indiana_iui = val
        if usdCurrency_indiana_iui is not None:
            gbpCurrency_indiana_iui = val * usdToGbp
            eurCurrency_indiana_iui = val * usdToEur
        else:
            gbpCurrency_indiana_iui = None
            eurCurrency_indiana_iui = None

    #--------------------------------------------------------------------------
    queryset_list_iowa = queryset_list_us.filter(clinicRegion__iexact='Iowa')
    queryset_list_iowa_ivf = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_iowa_ivf.items():
        usdCurrency_iowa_ivf = val
        if usdCurrency_iowa_ivf is not None:
            gbpCurrency_iowa_ivf = val * usdToGbp
            eurCurrency_iowa_ivf = val * usdToEur
        else:
            gbpCurrency_iowa_ivf = None
            eurCurrency_iowa_ivf = None

    queryset_list_iowa_egg = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_iowa_egg.items():
        usdCurrency_iowa_egg = val
        if usdCurrency_iowa_egg is not None:
            gbpCurrency_iowa_egg = val * usdToGbp
            eurCurrency_iowa_egg = val * usdToEur
        else:
            gbpCurrency_iowa_egg = None
            eurCurrency_iowa_egg = None

    queryset_list_iowa_embryo = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_iowa_embryo.items():
        usdCurrency_iowa_embryo = val
        if usdCurrency_iowa_embryo is not None:
            gbpCurrency_iowa_embryo = val * usdToGbp
            eurCurrency_iowa_embryo = val * usdToEur
        else:
            gbpCurrency_iowa_embryo = None
            eurCurrency_iowa_embryo = None

    queryset_list_iowa_sperm = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_iowa_sperm.items():
        usdCurrency_iowa_sperm = val
        if usdCurrency_iowa_sperm is not None:
            gbpCurrency_iowa_sperm = val * usdToGbp
            eurCurrency_iowa_sperm = val * usdToEur
        else:
            gbpCurrency_iowa_sperm = None
            eurCurrency_iowa_sperm = None

    queryset_list_iowa_icsi = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_iowa_icsi.items():
        usdCurrency_iowa_icsi = val
        if usdCurrency_iowa_icsi is not None:
            gbpCurrency_iowa_icsi = val * usdToGbp
            eurCurrency_iowa_icsi = val * usdToEur
        else:
            gbpCurrency_iowa_icsi = None
            eurCurrency_iowa_icsi = None

    queryset_list_iowa_iui = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_iowa_iui.items():
        usdCurrency_iowa_iui = val
        if usdCurrency_iowa_iui is not None:
            gbpCurrency_iowa_iui = val * usdToGbp
            eurCurrency_iowa_iui = val * usdToEur
        else:
            gbpCurrency_iowa_iui = None
            eurCurrency_iowa_iui = None

    #--------------------------------------------------------------------------
    queryset_list_kansas = queryset_list_us.filter(clinicRegion__iexact='Kansas')
    queryset_list_kansas_ivf = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_kansas_ivf.items():
        usdCurrency_kansas_ivf = val
        if usdCurrency_kansas_ivf is not None:
            gbpCurrency_kansas_ivf = val * usdToGbp
            eurCurrency_kansas_ivf = val * usdToEur
        else:
            gbpCurrency_kansas_ivf = None
            eurCurrency_kansas_ivf = None

    queryset_list_kansas_egg = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kansas_egg.items():
        usdCurrency_kansas_egg = val
        if usdCurrency_kansas_egg is not None:
            gbpCurrency_kansas_egg = val * usdToGbp
            eurCurrency_kansas_egg = val * usdToEur
        else:
            gbpCurrency_kansas_egg = None
            eurCurrency_kansas_egg = None

    queryset_list_kansas_embryo = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kansas_embryo.items():
        usdCurrency_kansas_embryo = val
        if usdCurrency_kansas_embryo is not None:
            gbpCurrency_kansas_embryo = val * usdToGbp
            eurCurrency_kansas_embryo = val * usdToEur
        else:
            gbpCurrency_kansas_embryo = None
            eurCurrency_kansas_embryo = None

    queryset_list_kansas_sperm = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kansas_sperm.items():
        usdCurrency_kansas_sperm = val
        if usdCurrency_kansas_sperm is not None:
            gbpCurrency_kansas_sperm = val * usdToGbp
            eurCurrency_kansas_sperm = val * usdToEur
        else:
            gbpCurrency_kansas_sperm = None
            eurCurrency_kansas_sperm = None

    queryset_list_kansas_icsi = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kansas_icsi.items():
        usdCurrency_kansas_icsi = val
        if usdCurrency_kansas_icsi is not None:
            gbpCurrency_kansas_icsi = val * usdToGbp
            eurCurrency_kansas_icsi = val * usdToEur
        else:
            gbpCurrency_kansas_icsi = None
            eurCurrency_kansas_icsi = None

    queryset_list_kansas_iui = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kansas_iui.items():
        usdCurrency_kansas_iui = val
        if usdCurrency_kansas_iui is not None:
            gbpCurrency_kansas_iui = val * usdToGbp
            eurCurrency_kansas_iui = val * usdToEur
        else:
            gbpCurrency_kansas_iui = None
            eurCurrency_kansas_iui = None

    #--------------------------------------------------------------------------
    queryset_list_kentucky = queryset_list_us.filter(clinicRegion__iexact='Kentucky')
    queryset_list_kentucky_ivf = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_kentucky_ivf.items():
        usdCurrency_kentucky_ivf = val
        if usdCurrency_kentucky_ivf is not None:
            gbpCurrency_kentucky_ivf = val * usdToGbp
            eurCurrency_kentucky_ivf = val * usdToEur
        else:
            gbpCurrency_kentucky_ivf = None
            eurCurrency_kentucky_ivf = None

    queryset_list_kentucky_egg = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_egg.items():
        usdCurrency_kentucky_egg = val
        if usdCurrency_kentucky_egg is not None:
            gbpCurrency_kentucky_egg = val * usdToGbp
            eurCurrency_kentucky_egg = val * usdToEur
        else:
            gbpCurrency_kentucky_egg = None
            eurCurrency_kentucky_egg = None

    queryset_list_kentucky_embryo = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_embryo.items():
        usdCurrency_kentucky_embryo = val
        if usdCurrency_kentucky_embryo is not None:
            gbpCurrency_kentucky_embryo = val * usdToGbp
            eurCurrency_kentucky_embryo = val * usdToEur
        else:
            gbpCurrency_kentucky_embryo = None
            eurCurrency_kentucky_embryo = None

    queryset_list_kentucky_sperm = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_sperm.items():
        usdCurrency_kentucky_sperm = val
        if usdCurrency_kentucky_sperm is not None:
            gbpCurrency_kentucky_sperm = val * usdToGbp
            eurCurrency_kentucky_sperm = val * usdToEur
        else:
            gbpCurrency_kentucky_sperm = None
            eurCurrency_kentucky_sperm = None

    queryset_list_kentucky_icsi = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kentucky_icsi.items():
        usdCurrency_kentucky_icsi = val
        if usdCurrency_kentucky_icsi is not None:
            gbpCurrency_kentucky_icsi = val * usdToGbp
            eurCurrency_kentucky_icsi = val * usdToEur
        else:
            gbpCurrency_kentucky_icsi = None
            eurCurrency_kentucky_icsi = None

    queryset_list_kentucky_iui = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kentucky_iui.items():
        usdCurrency_kentucky_iui = val
        if usdCurrency_kentucky_iui is not None:
            gbpCurrency_kentucky_iui = val * usdToGbp
            eurCurrency_kentucky_iui = val * usdToEur
        else:
            gbpCurrency_kentucky_iui = None
            eurCurrency_kentucky_iui = None

    #--------------------------------------------------------------------------
    queryset_list_louisiana = queryset_list_us.filter(clinicRegion__iexact='Louisiana')
    queryset_list_louisiana_ivf = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_louisiana_ivf.items():
        usdCurrency_louisiana_ivf = val
        if usdCurrency_louisiana_ivf is not None:
            gbpCurrency_louisiana_ivf = val * usdToGbp
            eurCurrency_louisiana_ivf = val * usdToEur
        else:
            gbpCurrency_louisiana_ivf = None
            eurCurrency_louisiana_ivf = None

    queryset_list_louisiana_egg = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_egg.items():
        usdCurrency_louisiana_egg = val
        if usdCurrency_louisiana_egg is not None:
            gbpCurrency_louisiana_egg = val * usdToGbp
            eurCurrency_louisiana_egg = val * usdToEur
        else:
            gbpCurrency_louisiana_egg = None
            eurCurrency_louisiana_egg = None

    queryset_list_louisiana_embryo = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_embryo.items():
        usdCurrency_louisiana_embryo = val
        if usdCurrency_louisiana_embryo is not None:
            gbpCurrency_louisiana_embryo = val * usdToGbp
            eurCurrency_louisiana_embryo = val * usdToEur
        else:
            gbpCurrency_louisiana_embryo = None
            eurCurrency_louisiana_embryo = None

    queryset_list_louisiana_sperm = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_sperm.items():
        usdCurrency_louisiana_sperm = val
        if usdCurrency_louisiana_sperm is not None:
            gbpCurrency_louisiana_sperm = val * usdToGbp
            eurCurrency_louisiana_sperm = val * usdToEur
        else:
            gbpCurrency_louisiana_sperm = None
            eurCurrency_louisiana_sperm = None

    queryset_list_louisiana_icsi = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_louisiana_icsi.items():
        usdCurrency_louisiana_icsi = val
        if usdCurrency_louisiana_icsi is not None:
            gbpCurrency_louisiana_icsi = val * usdToGbp
            eurCurrency_louisiana_icsi = val * usdToEur
        else:
            gbpCurrency_louisiana_icsi = None
            eurCurrency_louisiana_icsi = None

    queryset_list_louisiana_iui = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_louisiana_iui.items():
        usdCurrency_louisiana_iui = val
        if usdCurrency_louisiana_iui is not None:
            gbpCurrency_louisiana_iui = val * usdToGbp
            eurCurrency_louisiana_iui = val * usdToEur
        else:
            gbpCurrency_louisiana_iui = None
            eurCurrency_louisiana_iui = None

    #--------------------------------------------------------------------------
    queryset_list_maine = queryset_list_us.filter(clinicRegion__iexact='Maine')
    queryset_list_maine_ivf = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_maine_ivf.items():
        usdCurrency_maine_ivf = val
        if usdCurrency_maine_ivf is not None:
            gbpCurrency_maine_ivf = val * usdToGbp
            eurCurrency_maine_ivf = val * usdToEur
        else:
            gbpCurrency_maine_ivf = None
            eurCurrency_maine_ivf = None

    queryset_list_maine_egg = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_maine_egg.items():
        usdCurrency_maine_egg = val
        if usdCurrency_maine_egg is not None:
            gbpCurrency_maine_egg = val * usdToGbp
            eurCurrency_maine_egg = val * usdToEur
        else:
            gbpCurrency_maine_egg = None
            eurCurrency_maine_egg = None

    queryset_list_maine_embryo = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_maine_embryo.items():
        usdCurrency_maine_embryo = val
        if usdCurrency_maine_embryo is not None:
            gbpCurrency_maine_embryo = val * usdToGbp
            eurCurrency_maine_embryo = val * usdToEur
        else:
            gbpCurrency_maine_embryo = None
            eurCurrency_maine_embryo = None

    queryset_list_maine_sperm = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_maine_sperm.items():
        usdCurrency_maine_sperm = val
        if usdCurrency_maine_sperm is not None:
            gbpCurrency_maine_sperm = val * usdToGbp
            eurCurrency_maine_sperm = val * usdToEur
        else:
            gbpCurrency_maine_sperm = None
            eurCurrency_maine_sperm = None

    queryset_list_maine_icsi = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_maine_icsi.items():
        usdCurrency_maine_icsi = val
        if usdCurrency_maine_icsi is not None:
            gbpCurrency_maine_icsi = val * usdToGbp
            eurCurrency_maine_icsi = val * usdToEur
        else:
            gbpCurrency_maine_icsi = None
            eurCurrency_maine_icsi = None

    queryset_list_maine_iui = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_maine_iui.items():
        usdCurrency_maine_iui = val
        if usdCurrency_maine_iui is not None:
            gbpCurrency_maine_iui = val * usdToGbp
            eurCurrency_maine_iui = val * usdToEur
        else:
            gbpCurrency_maine_iui = None
            eurCurrency_maine_iui = None

    #--------------------------------------------------------------------------
    queryset_list_maryland = queryset_list_us.filter(clinicRegion__iexact='Maryland')
    queryset_list_maryland_ivf = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_maryland_ivf.items():
        usdCurrency_maryland_ivf = val
        if usdCurrency_maryland_ivf is not None:
            gbpCurrency_maryland_ivf = val * usdToGbp
            eurCurrency_maryland_ivf = val * usdToEur
        else:
            gbpCurrency_maryland_ivf = None
            eurCurrency_maryland_ivf = None

    queryset_list_maryland_egg = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_maryland_egg.items():
        usdCurrency_maryland_egg = val
        if usdCurrency_maryland_egg is not None:
            gbpCurrency_maryland_egg = val * usdToGbp
            eurCurrency_maryland_egg = val * usdToEur
        else:
            gbpCurrency_maryland_egg = None
            eurCurrency_maryland_egg = None

    queryset_list_maryland_embryo = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_maryland_embryo.items():
        usdCurrency_maryland_embryo = val
        if usdCurrency_maryland_embryo is not None:
            gbpCurrency_maryland_embryo = val * usdToGbp
            eurCurrency_maryland_embryo = val * usdToEur
        else:
            gbpCurrency_maryland_embryo = None
            eurCurrency_maryland_embryo = None

    queryset_list_maryland_sperm = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_maryland_sperm.items():
        usdCurrency_maryland_sperm = val
        if usdCurrency_maryland_sperm is not None:
            gbpCurrency_maryland_sperm = val * usdToGbp
            eurCurrency_maryland_sperm = val * usdToEur
        else:
            gbpCurrency_maryland_sperm = None
            eurCurrency_maryland_sperm = None

    queryset_list_maryland_icsi = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_maryland_icsi.items():
        usdCurrency_maryland_icsi = val
        if usdCurrency_maryland_icsi is not None:
            gbpCurrency_maryland_icsi = val * usdToGbp
            eurCurrency_maryland_icsi = val * usdToEur
        else:
            gbpCurrency_maryland_icsi = None
            eurCurrency_maryland_icsi = None

    queryset_list_maryland_iui = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_maryland_iui.items():
        usdCurrency_maryland_iui = val
        if usdCurrency_maryland_iui is not None:
            gbpCurrency_maryland_iui = val * usdToGbp
            eurCurrency_maryland_iui = val * usdToEur
        else:
            gbpCurrency_maryland_iui = None
            eurCurrency_maryland_iui = None

    #--------------------------------------------------------------------------
    queryset_list_massachusetts = queryset_list_us.filter(clinicRegion__iexact='Massachusetts')
    queryset_list_massachusetts_ivf = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_massachusetts_ivf.items():
        usdCurrency_massachusetts_ivf = val
        if usdCurrency_massachusetts_ivf is not None:
            gbpCurrency_massachusetts_ivf = val * usdToGbp
            eurCurrency_massachusetts_ivf = val * usdToEur
        else:
            gbpCurrency_massachusetts_ivf = None
            eurCurrency_massachusetts_ivf = None

    queryset_list_massachusetts_egg = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_egg.items():
        usdCurrency_massachusetts_egg = val
        if usdCurrency_massachusetts_egg is not None:
            gbpCurrency_massachusetts_egg = val * usdToGbp
            eurCurrency_massachusetts_egg = val * usdToEur
        else:
            gbpCurrency_massachusetts_egg = None
            eurCurrency_massachusetts_egg = None

    queryset_list_massachusetts_embryo = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_embryo.items():
        usdCurrency_massachusetts_embryo = val
        if usdCurrency_massachusetts_embryo is not None:
            gbpCurrency_massachusetts_embryo = val * usdToGbp
            eurCurrency_massachusetts_embryo = val * usdToEur
        else:
            gbpCurrency_massachusetts_embryo = None
            eurCurrency_massachusetts_embryo = None

    queryset_list_massachusetts_sperm = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_sperm.items():
        usdCurrency_massachusetts_sperm = val
        if usdCurrency_massachusetts_sperm is not None:
            gbpCurrency_massachusetts_sperm = val * usdToGbp
            eurCurrency_massachusetts_sperm = val * usdToEur
        else:
            gbpCurrency_massachusetts_sperm = None
            eurCurrency_massachusetts_sperm = None

    queryset_list_massachusetts_icsi = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_massachusetts_icsi.items():
        usdCurrency_massachusetts_icsi = val
        if usdCurrency_massachusetts_icsi is not None:
            gbpCurrency_massachusetts_icsi = val * usdToGbp
            eurCurrency_massachusetts_icsi = val * usdToEur
        else:
            gbpCurrency_massachusetts_icsi = None
            eurCurrency_massachusetts_icsi = None

    queryset_list_massachusetts_iui = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_massachusetts_iui.items():
        usdCurrency_massachusetts_iui = val
        if usdCurrency_massachusetts_iui is not None:
            gbpCurrency_massachusetts_iui = val * usdToGbp
            eurCurrency_massachusetts_iui = val * usdToEur
        else:
            gbpCurrency_massachusetts_iui = None
            eurCurrency_massachusetts_iui = None

    #--------------------------------------------------------------------------
    queryset_list_michigan = queryset_list_us.filter(clinicRegion__iexact='Michigan')
    queryset_list_michigan_ivf = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_michigan_ivf.items():
        usdCurrency_michigan_ivf = val
        if usdCurrency_michigan_ivf is not None:
            gbpCurrency_michigan_ivf = val * usdToGbp
            eurCurrency_michigan_ivf = val * usdToEur
        else:
            gbpCurrency_michigan_ivf = None
            eurCurrency_michigan_ivf = None

    queryset_list_michigan_egg = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_michigan_egg.items():
        usdCurrency_michigan_egg = val
        if usdCurrency_michigan_egg is not None:
            gbpCurrency_michigan_egg = val * usdToGbp
            eurCurrency_michigan_egg = val * usdToEur
        else:
            gbpCurrency_michigan_egg = None
            eurCurrency_michigan_egg = None

    queryset_list_michigan_embryo = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_michigan_embryo.items():
        usdCurrency_michigan_embryo = val
        if usdCurrency_michigan_embryo is not None:
            gbpCurrency_michigan_embryo = val * usdToGbp
            eurCurrency_michigan_embryo = val * usdToEur
        else:
            gbpCurrency_michigan_embryo = None
            eurCurrency_michigan_embryo = None

    queryset_list_michigan_sperm = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_michigan_sperm.items():
        usdCurrency_michigan_sperm = val
        if usdCurrency_michigan_sperm is not None:
            gbpCurrency_michigan_sperm = val * usdToGbp
            eurCurrency_michigan_sperm = val * usdToEur
        else:
            gbpCurrency_michigan_sperm = None
            eurCurrency_michigan_sperm = None

    queryset_list_michigan_icsi = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_michigan_icsi.items():
        usdCurrency_michigan_icsi = val
        if usdCurrency_michigan_icsi is not None:
            gbpCurrency_michigan_icsi = val * usdToGbp
            eurCurrency_michigan_icsi = val * usdToEur
        else:
            gbpCurrency_michigan_icsi = None
            eurCurrency_michigan_icsi = None

    queryset_list_michigan_iui = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_michigan_iui.items():
        usdCurrency_michigan_iui = val
        if usdCurrency_michigan_iui is not None:
            gbpCurrency_michigan_iui = val * usdToGbp
            eurCurrency_michigan_iui = val * usdToEur
        else:
            gbpCurrency_michigan_iui = None
            eurCurrency_michigan_iui = None

    #--------------------------------------------------------------------------
    queryset_list_minnesota = queryset_list_us.filter(clinicRegion__iexact='Minnesota')
    queryset_list_minnesota_ivf = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_minnesota_ivf.items():
        usdCurrency_minnesota_ivf = val
        if usdCurrency_minnesota_ivf is not None:
            gbpCurrency_minnesota_ivf = val * usdToGbp
            eurCurrency_minnesota_ivf = val * usdToEur
        else:
            gbpCurrency_minnesota_ivf = None
            eurCurrency_minnesota_ivf = None

    queryset_list_minnesota_egg = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_egg.items():
        usdCurrency_minnesota_egg = val
        if usdCurrency_minnesota_egg is not None:
            gbpCurrency_minnesota_egg = val * usdToGbp
            eurCurrency_minnesota_egg = val * usdToEur
        else:
            gbpCurrency_minnesota_egg = None
            eurCurrency_minnesota_egg = None

    queryset_list_minnesota_embryo = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_embryo.items():
        usdCurrency_minnesota_embryo = val
        if usdCurrency_minnesota_embryo is not None:
            gbpCurrency_minnesota_embryo = val * usdToGbp
            eurCurrency_minnesota_embryo = val * usdToEur
        else:
            gbpCurrency_minnesota_embryo = None
            eurCurrency_minnesota_embryo = None

    queryset_list_minnesota_sperm = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_sperm.items():
        usdCurrency_minnesota_sperm = val
        if usdCurrency_minnesota_sperm is not None:
            gbpCurrency_minnesota_sperm = val * usdToGbp
            eurCurrency_minnesota_sperm = val * usdToEur
        else:
            gbpCurrency_minnesota_sperm = None
            eurCurrency_minnesota_sperm = None

    queryset_list_minnesota_icsi = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_minnesota_icsi.items():
        usdCurrency_minnesota_icsi = val
        if usdCurrency_minnesota_icsi is not None:
            gbpCurrency_minnesota_icsi = val * usdToGbp
            eurCurrency_minnesota_icsi = val * usdToEur
        else:
            gbpCurrency_minnesota_icsi = None
            eurCurrency_minnesota_icsi = None

    queryset_list_minnesota_iui = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_minnesota_iui.items():
        usdCurrency_minnesota_iui = val
        if usdCurrency_minnesota_iui is not None:
            gbpCurrency_minnesota_iui = val * usdToGbp
            eurCurrency_minnesota_iui = val * usdToEur
        else:
            gbpCurrency_minnesota_iui = None
            eurCurrency_minnesota_iui = None

    #--------------------------------------------------------------------------
    queryset_list_mississippi = queryset_list_us.filter(clinicRegion__iexact='Mississippi')
    queryset_list_mississippi_ivf = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_mississippi_ivf.items():
        usdCurrency_mississippi_ivf = val
        if usdCurrency_mississippi_ivf is not None:
            gbpCurrency_mississippi_ivf = val * usdToGbp
            eurCurrency_mississippi_ivf = val * usdToEur
        else:
            gbpCurrency_mississippi_ivf = None
            eurCurrency_mississippi_ivf = None

    queryset_list_mississippi_egg = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_egg.items():
        usdCurrency_mississippi_egg = val
        if usdCurrency_mississippi_egg is not None:
            gbpCurrency_mississippi_egg = val * usdToGbp
            eurCurrency_mississippi_egg = val * usdToEur
        else:
            gbpCurrency_mississippi_egg = None
            eurCurrency_mississippi_egg = None

    queryset_list_mississippi_embryo = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_embryo.items():
        usdCurrency_mississippi_embryo = val
        if usdCurrency_mississippi_embryo is not None:
            gbpCurrency_mississippi_embryo = val * usdToGbp
            eurCurrency_mississippi_embryo = val * usdToEur
        else:
            gbpCurrency_mississippi_embryo = None
            eurCurrency_mississippi_embryo = None

    queryset_list_mississippi_sperm = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_sperm.items():
        usdCurrency_mississippi_sperm = val
        if usdCurrency_mississippi_sperm is not None:
            gbpCurrency_mississippi_sperm = val * usdToGbp
            eurCurrency_mississippi_sperm = val * usdToEur
        else:
            gbpCurrency_mississippi_sperm = None
            eurCurrency_mississippi_sperm = None

    queryset_list_mississippi_icsi = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_mississippi_icsi.items():
        usdCurrency_mississippi_icsi = val
        if usdCurrency_mississippi_icsi is not None:
            gbpCurrency_mississippi_icsi = val * usdToGbp
            eurCurrency_mississippi_icsi = val * usdToEur
        else:
            gbpCurrency_mississippi_icsi = None
            eurCurrency_mississippi_icsi = None

    queryset_list_mississippi_iui = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_mississippi_iui.items():
        usdCurrency_mississippi_iui = val
        if usdCurrency_mississippi_iui is not None:
            gbpCurrency_mississippi_iui = val * usdToGbp
            eurCurrency_mississippi_iui = val * usdToEur
        else:
            gbpCurrency_mississippi_iui = None
            eurCurrency_mississippi_iui = None

    #--------------------------------------------------------------------------
    queryset_list_missouri = queryset_list_us.filter(clinicRegion__iexact='Missouri')
    queryset_list_missouri_ivf = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_missouri_ivf.items():
        usdCurrency_missouri_ivf = val
        if usdCurrency_missouri_ivf is not None:
            gbpCurrency_missouri_ivf = val * usdToGbp
            eurCurrency_missouri_ivf = val * usdToEur
        else:
            gbpCurrency_missouri_ivf = None
            eurCurrency_missouri_ivf = None

    queryset_list_missouri_egg = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_missouri_egg.items():
        usdCurrency_missouri_egg = val
        if usdCurrency_missouri_egg is not None:
            gbpCurrency_missouri_egg = val * usdToGbp
            eurCurrency_missouri_egg = val * usdToEur
        else:
            gbpCurrency_missouri_egg = None
            eurCurrency_missouri_egg = None

    queryset_list_missouri_embryo = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_missouri_embryo.items():
        usdCurrency_missouri_embryo = val
        if usdCurrency_missouri_embryo is not None:
            gbpCurrency_missouri_embryo = val * usdToGbp
            eurCurrency_missouri_embryo = val * usdToEur
        else:
            gbpCurrency_missouri_embryo = None
            eurCurrency_missouri_embryo = None

    queryset_list_missouri_sperm = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_missouri_sperm.items():
        usdCurrency_missouri_sperm = val
        if usdCurrency_missouri_sperm is not None:
            gbpCurrency_missouri_sperm = val * usdToGbp
            eurCurrency_missouri_sperm = val * usdToEur
        else:
            gbpCurrency_missouri_sperm = None
            eurCurrency_missouri_sperm = None

    queryset_list_missouri_icsi = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_missouri_icsi.items():
        usdCurrency_missouri_icsi = val
        if usdCurrency_missouri_icsi is not None:
            gbpCurrency_missouri_icsi = val * usdToGbp
            eurCurrency_missouri_icsi = val * usdToEur
        else:
            gbpCurrency_missouri_icsi = None
            eurCurrency_missouri_icsi = None

    queryset_list_missouri_iui = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_missouri_iui.items():
        usdCurrency_missouri_iui = val
        if usdCurrency_missouri_iui is not None:
            gbpCurrency_missouri_iui = val * usdToGbp
            eurCurrency_missouri_iui = val * usdToEur
        else:
            gbpCurrency_missouri_iui = None
            eurCurrency_missouri_iui = None

    #--------------------------------------------------------------------------
    queryset_list_nebraska = queryset_list_us.filter(clinicRegion__iexact='Nebraska')
    queryset_list_nebraska_ivf = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_nebraska_ivf.items():
        usdCurrency_nebraska_ivf = val
        if usdCurrency_nebraska_ivf is not None:
            gbpCurrency_nebraska_ivf = val * usdToGbp
            eurCurrency_nebraska_ivf = val * usdToEur
        else:
            gbpCurrency_nebraska_ivf = None
            eurCurrency_nebraska_ivf = None

    queryset_list_nebraska_egg = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_egg.items():
        usdCurrency_nebraska_egg = val
        if usdCurrency_nebraska_egg is not None:
            gbpCurrency_nebraska_egg = val * usdToGbp
            eurCurrency_nebraska_egg = val * usdToEur
        else:
            gbpCurrency_nebraska_egg = None
            eurCurrency_nebraska_egg = None

    queryset_list_nebraska_embryo = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_embryo.items():
        usdCurrency_nebraska_embryo = val
        if usdCurrency_nebraska_embryo is not None:
            gbpCurrency_nebraska_embryo = val * usdToGbp
            eurCurrency_nebraska_embryo = val * usdToEur
        else:
            gbpCurrency_nebraska_embryo = None
            eurCurrency_nebraska_embryo = None

    queryset_list_nebraska_sperm = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_sperm.items():
        usdCurrency_nebraska_sperm = val
        if usdCurrency_nebraska_sperm is not None:
            gbpCurrency_nebraska_sperm = val * usdToGbp
            eurCurrency_nebraska_sperm = val * usdToEur
        else:
            gbpCurrency_nebraska_sperm = None
            eurCurrency_nebraska_sperm = None

    queryset_list_nebraska_icsi = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nebraska_icsi.items():
        usdCurrency_nebraska_icsi = val
        if usdCurrency_nebraska_icsi is not None:
            gbpCurrency_nebraska_icsi = val * usdToGbp
            eurCurrency_nebraska_icsi = val * usdToEur
        else:
            gbpCurrency_nebraska_icsi = None
            eurCurrency_nebraska_icsi = None

    queryset_list_nebraska_iui = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nebraska_iui.items():
        usdCurrency_nebraska_iui = val
        if usdCurrency_nebraska_iui is not None:
            gbpCurrency_nebraska_iui = val * usdToGbp
            eurCurrency_nebraska_iui = val * usdToEur
        else:
            gbpCurrency_nebraska_iui = None
            eurCurrency_nebraska_iui = None

    #--------------------------------------------------------------------------
    queryset_list_newhampshire = queryset_list_us.filter(clinicRegion__iexact='New Hampshire')
    queryset_list_newhampshire_ivf = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_newhampshire_ivf.items():
        usdCurrency_newhampshire_ivf = val
        if usdCurrency_newhampshire_ivf is not None:
            gbpCurrency_newhampshire_ivf = val * usdToGbp
            eurCurrency_newhampshire_ivf = val * usdToEur
        else:
            gbpCurrency_newhampshire_ivf = None
            eurCurrency_newhampshire_ivf = None

    queryset_list_newhampshire_egg = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_egg.items():
        usdCurrency_newhampshire_egg = val
        if usdCurrency_newhampshire_egg is not None:
            gbpCurrency_newhampshire_egg = val * usdToGbp
            eurCurrency_newhampshire_egg = val * usdToEur
        else:
            gbpCurrency_newhampshire_egg = None
            eurCurrency_newhampshire_egg = None

    queryset_list_newhampshire_embryo = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_embryo.items():
        usdCurrency_newhampshire_embryo = val
        if usdCurrency_newhampshire_embryo is not None:
            gbpCurrency_newhampshire_embryo = val * usdToGbp
            eurCurrency_newhampshire_embryo = val * usdToEur
        else:
            gbpCurrency_newhampshire_embryo = None
            eurCurrency_newhampshire_embryo = None

    queryset_list_newhampshire_sperm = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_sperm.items():
        usdCurrency_newhampshire_sperm = val
        if usdCurrency_newhampshire_sperm is not None:
            gbpCurrency_newhampshire_sperm = val * usdToGbp
            eurCurrency_newhampshire_sperm = val * usdToEur
        else:
            gbpCurrency_newhampshire_sperm = None
            eurCurrency_newhampshire_sperm = None

    queryset_list_newhampshire_icsi = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newhampshire_icsi.items():
        usdCurrency_newhampshire_icsi = val
        if usdCurrency_newhampshire_icsi is not None:
            gbpCurrency_newhampshire_icsi = val * usdToGbp
            eurCurrency_newhampshire_icsi = val * usdToEur
        else:
            gbpCurrency_newhampshire_icsi = None
            eurCurrency_newhampshire_icsi = None

    queryset_list_newhampshire_iui = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newhampshire_iui.items():
        usdCurrency_newhampshire_iui = val
        if usdCurrency_newhampshire_iui is not None:
            gbpCurrency_newhampshire_iui = val * usdToGbp
            eurCurrency_newhampshire_iui = val * usdToEur
        else:
            gbpCurrency_newhampshire_iui = None
            eurCurrency_newhampshire_iui = None

    #--------------------------------------------------------------------------
    queryset_list_newjersey = queryset_list_us.filter(clinicRegion__iexact='New Jersey')
    queryset_list_newjersey_ivf = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_newjersey_ivf.items():
        usdCurrency_newjersey_ivf = val
        if usdCurrency_newjersey_ivf is not None:
            gbpCurrency_newjersey_ivf = val * usdToGbp
            eurCurrency_newjersey_ivf = val * usdToEur
        else:
            gbpCurrency_newjersey_ivf = None
            eurCurrency_newjersey_ivf = None

    queryset_list_newjersey_egg = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_egg.items():
        usdCurrency_newjersey_egg = val
        if usdCurrency_newjersey_egg is not None:
            gbpCurrency_newjersey_egg = val * usdToGbp
            eurCurrency_newjersey_egg = val * usdToEur
        else:
            gbpCurrency_newjersey_egg = None
            eurCurrency_newjersey_egg = None

    queryset_list_newjersey_embryo = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_embryo.items():
        usdCurrency_newjersey_embryo = val
        if usdCurrency_newjersey_embryo is not None:
            gbpCurrency_newjersey_embryo = val * usdToGbp
            eurCurrency_newjersey_embryo = val * usdToEur
        else:
            gbpCurrency_newjersey_embryo = None
            eurCurrency_newjersey_embryo = None

    queryset_list_newjersey_sperm = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_sperm.items():
        usdCurrency_newjersey_sperm = val
        if usdCurrency_newjersey_sperm is not None:
            gbpCurrency_newjersey_sperm = val * usdToGbp
            eurCurrency_newjersey_sperm = val * usdToEur
        else:
            gbpCurrency_newjersey_sperm = None
            eurCurrency_newjersey_sperm = None

    queryset_list_newjersey_icsi = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newjersey_icsi.items():
        usdCurrency_newjersey_icsi = val
        if usdCurrency_newjersey_icsi is not None:
            gbpCurrency_newjersey_icsi = val * usdToGbp
            eurCurrency_newjersey_icsi = val * usdToEur
        else:
            gbpCurrency_newjersey_icsi = None
            eurCurrency_newjersey_icsi = None

    queryset_list_newjersey_iui = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newjersey_iui.items():
        usdCurrency_newjersey_iui = val
        if usdCurrency_newjersey_iui is not None:
            gbpCurrency_newjersey_iui = val * usdToGbp
            eurCurrency_newjersey_iui = val * usdToEur
        else:
            gbpCurrency_newjersey_iui = None
            eurCurrency_newjersey_iui = None

    #--------------------------------------------------------------------------
    queryset_list_newmexico = queryset_list_us.filter(clinicRegion__iexact='New Mexico')
    queryset_list_newmexico_ivf = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_newmexico_ivf.items():
        usdCurrency_newmexico_ivf = val
        if usdCurrency_newmexico_ivf is not None:
            gbpCurrency_newmexico_ivf = val * usdToGbp
            eurCurrency_newmexico_ivf = val * usdToEur
        else:
            gbpCurrency_newmexico_ivf = None
            eurCurrency_newmexico_ivf = None

    queryset_list_newmexico_egg = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_egg.items():
        usdCurrency_newmexico_egg = val
        if usdCurrency_newmexico_egg is not None:
            gbpCurrency_newmexico_egg = val * usdToGbp
            eurCurrency_newmexico_egg = val * usdToEur
        else:
            gbpCurrency_newmexico_egg = None
            eurCurrency_newmexico_egg = None

    queryset_list_newmexico_embryo = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_embryo.items():
        usdCurrency_newmexico_embryo = val
        if usdCurrency_newmexico_embryo is not None:
            gbpCurrency_newmexico_embryo = val * usdToGbp
            eurCurrency_newmexico_embryo = val * usdToEur
        else:
            gbpCurrency_newmexico_embryo = None
            eurCurrency_newmexico_embryo = None

    queryset_list_newmexico_sperm = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_sperm.items():
        usdCurrency_newmexico_sperm = val
        if usdCurrency_newmexico_sperm is not None:
            gbpCurrency_newmexico_sperm = val * usdToGbp
            eurCurrency_newmexico_sperm = val * usdToEur
        else:
            gbpCurrency_newmexico_sperm = None
            eurCurrency_newmexico_sperm = None

    queryset_list_newmexico_icsi = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newmexico_icsi.items():
        usdCurrency_newmexico_icsi = val
        if usdCurrency_newmexico_icsi is not None:
            gbpCurrency_newmexico_icsi = val * usdToGbp
            eurCurrency_newmexico_icsi = val * usdToEur
        else:
            gbpCurrency_newmexico_icsi = None
            eurCurrency_newmexico_icsi = None

    queryset_list_newmexico_iui = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newmexico_iui.items():
        usdCurrency_newmexico_iui = val
        if usdCurrency_newmexico_iui is not None:
            gbpCurrency_newmexico_iui = val * usdToGbp
            eurCurrency_newmexico_iui = val * usdToEur
        else:
            gbpCurrency_newmexico_iui = None
            eurCurrency_newmexico_iui = None

    #--------------------------------------------------------------------------
    queryset_list_newyork = queryset_list_us.filter(clinicRegion__iexact='New York')
    queryset_list_newyork_ivf = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))
    for key,val in queryset_list_newyork_ivf.items():
        usdCurrency_newyork_ivf = val
        if usdCurrency_newyork_ivf is not None:
            gbpCurrency_newyork_ivf = val * usdToGbp
            eurCurrency_newyork_ivf = val * usdToEur
        else:
            gbpCurrency_newyork_ivf = None
            eurCurrency_newyork_ivf = None

    queryset_list_newyork_egg = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newyork_egg.items():
        usdCurrency_newyork_egg = val
        if usdCurrency_newyork_egg is not None:
            gbpCurrency_newyork_egg = val * usdToGbp
            eurCurrency_newyork_egg = val * usdToEur
        else:
            gbpCurrency_newyork_egg = None
            eurCurrency_newyork_egg = None

    queryset_list_newyork_embryo = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newyork_embryo.items():
        usdCurrency_newyork_embryo = val
        if usdCurrency_newyork_embryo is not None:
            gbpCurrency_newyork_embryo = val * usdToGbp
            eurCurrency_newyork_embryo = val * usdToEur
        else:
            gbpCurrency_newyork_embryo = None
            eurCurrency_newyork_embryo = None

    queryset_list_newyork_sperm = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newyork_sperm.items():
        usdCurrency_newyork_sperm = val
        if usdCurrency_newyork_sperm is not None:
            gbpCurrency_newyork_sperm = val * usdToGbp
            eurCurrency_newyork_sperm = val * usdToEur
        else:
            gbpCurrency_newyork_sperm = None
            eurCurrency_newyork_sperm = None

    queryset_list_newyork_icsi = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newyork_icsi.items():
        usdCurrency_newyork_icsi = val
        if usdCurrency_newyork_icsi is not None:
            gbpCurrency_newyork_icsi = val * usdToGbp
            eurCurrency_newyork_icsi = val * usdToEur
        else:
            gbpCurrency_newyork_icsi = None
            eurCurrency_newyork_icsi = None

    queryset_list_newyork_iui = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newyork_iui.items():
        usdCurrency_newyork_iui = val
        if usdCurrency_newyork_iui is not None:
            gbpCurrency_newyork_iui = val * usdToGbp
            eurCurrency_newyork_iui = val * usdToEur
        else:
            gbpCurrency_newyork_iui = None
            eurCurrency_newyork_iui = None

    context = {
        'gbpCurrency_alabama_ivf': gbpCurrency_alabama_ivf,
        'usdCurrency_alabama_ivf': usdCurrency_alabama_ivf,
        'eurCurrency_alabama_ivf': eurCurrency_alabama_ivf,
        'gbpCurrency_alabama_egg': gbpCurrency_alabama_egg,
        'usdCurrency_alabama_egg': usdCurrency_alabama_egg,
        'eurCurrency_alabama_egg': eurCurrency_alabama_egg,
        'gbpCurrency_alabama_embryo': gbpCurrency_alabama_embryo,
        'usdCurrency_alabama_embryo': usdCurrency_alabama_embryo,
        'eurCurrency_alabama_embryo': eurCurrency_alabama_embryo,
        'gbpCurrency_alabama_sperm': gbpCurrency_alabama_sperm,
        'usdCurrency_alabama_sperm': usdCurrency_alabama_sperm,
        'eurCurrency_alabama_sperm': eurCurrency_alabama_sperm,
        'gbpCurrency_alabama_icsi': gbpCurrency_alabama_icsi,
        'usdCurrency_alabama_icsi': usdCurrency_alabama_icsi,
        'eurCurrency_alabama_icsi': eurCurrency_alabama_icsi,
        'gbpCurrency_alabama_iui': gbpCurrency_alabama_iui,
        'usdCurrency_alabama_iui': usdCurrency_alabama_iui,
        'eurCurrency_alabama_iui': eurCurrency_alabama_iui,
        'gbpCurrency_alaska_ivf': gbpCurrency_alaska_ivf,
        'usdCurrency_alaska_ivf': usdCurrency_alaska_ivf,
        'eurCurrency_alaska_ivf': eurCurrency_alaska_ivf,
        'gbpCurrency_alaska_egg': gbpCurrency_alaska_egg,
        'usdCurrency_alaska_egg': usdCurrency_alaska_egg,
        'eurCurrency_alaska_egg': eurCurrency_alaska_egg,
        'gbpCurrency_alaska_embryo': gbpCurrency_alaska_embryo,
        'usdCurrency_alaska_embryo': usdCurrency_alaska_embryo,
        'eurCurrency_alaska_embryo': eurCurrency_alaska_embryo,
        'gbpCurrency_alaska_sperm': gbpCurrency_alaska_sperm,
        'usdCurrency_alaska_sperm': usdCurrency_alaska_sperm,
        'eurCurrency_alaska_sperm': eurCurrency_alaska_sperm,
        'gbpCurrency_alaska_icsi': gbpCurrency_alaska_icsi,
        'usdCurrency_alaska_icsi': usdCurrency_alaska_icsi,
        'eurCurrency_alaska_icsi': eurCurrency_alaska_icsi,
        'gbpCurrency_alaska_iui': gbpCurrency_alaska_iui,
        'usdCurrency_alaska_iui': usdCurrency_alaska_iui,
        'eurCurrency_alaska_iui': eurCurrency_alaska_iui,
        'gbpCurrency_arkansas_ivf': gbpCurrency_arkansas_ivf,
        'usdCurrency_arkansas_ivf': usdCurrency_arkansas_ivf,
        'eurCurrency_arkansas_ivf': eurCurrency_arkansas_ivf,
        'gbpCurrency_arkansas_egg': gbpCurrency_arkansas_egg,
        'usdCurrency_arkansas_egg': usdCurrency_arkansas_egg,
        'eurCurrency_arkansas_egg': eurCurrency_arkansas_egg,
        'gbpCurrency_arkansas_embryo': gbpCurrency_arkansas_embryo,
        'usdCurrency_arkansas_embryo': usdCurrency_arkansas_embryo,
        'eurCurrency_arkansas_embryo': eurCurrency_arkansas_embryo,
        'gbpCurrency_arkansas_sperm': gbpCurrency_arkansas_sperm,
        'usdCurrency_arkansas_sperm': usdCurrency_arkansas_sperm,
        'eurCurrency_arkansas_sperm': eurCurrency_arkansas_sperm,
        'gbpCurrency_arkansas_icsi': gbpCurrency_arkansas_icsi,
        'usdCurrency_arkansas_icsi': usdCurrency_arkansas_icsi,
        'eurCurrency_arkansas_icsi': eurCurrency_arkansas_icsi,
        'gbpCurrency_arkansas_iui': gbpCurrency_arkansas_iui,
        'usdCurrency_arkansas_iui': usdCurrency_arkansas_iui,
        'eurCurrency_arkansas_iui': eurCurrency_arkansas_iui,

        'gbpCurrency_california_ivf': gbpCurrency_california_ivf,
        'usdCurrency_california_ivf': usdCurrency_california_ivf,
        'eurCurrency_california_ivf': eurCurrency_california_ivf,
        'gbpCurrency_california_egg': gbpCurrency_california_egg,
        'usdCurrency_california_egg': usdCurrency_california_egg,
        'eurCurrency_california_egg': eurCurrency_california_egg,
        'gbpCurrency_california_embryo': gbpCurrency_california_embryo,
        'usdCurrency_california_embryo': usdCurrency_california_embryo,
        'eurCurrency_california_embryo': eurCurrency_california_embryo,
        'gbpCurrency_california_sperm': gbpCurrency_california_sperm,
        'usdCurrency_california_sperm': usdCurrency_california_sperm,
        'eurCurrency_california_sperm': eurCurrency_california_sperm,
        'gbpCurrency_california_icsi': gbpCurrency_california_icsi,
        'usdCurrency_california_icsi': usdCurrency_california_icsi,
        'eurCurrency_california_icsi': eurCurrency_california_icsi,
        'gbpCurrency_california_iui': gbpCurrency_california_iui,
        'usdCurrency_california_iui': usdCurrency_california_iui,
        'eurCurrency_california_iui': eurCurrency_california_iui,

        'gbpCurrency_colorado_ivf': gbpCurrency_colorado_ivf,
        'usdCurrency_colorado_ivf': usdCurrency_colorado_ivf,
        'eurCurrency_colorado_ivf': eurCurrency_colorado_ivf,
        'gbpCurrency_colorado_egg': gbpCurrency_colorado_egg,
        'usdCurrency_colorado_egg': usdCurrency_colorado_egg,
        'eurCurrency_colorado_egg': eurCurrency_colorado_egg,
        'gbpCurrency_colorado_embryo': gbpCurrency_colorado_embryo,
        'usdCurrency_colorado_embryo': usdCurrency_colorado_embryo,
        'eurCurrency_colorado_embryo': eurCurrency_colorado_embryo,
        'gbpCurrency_colorado_sperm': gbpCurrency_colorado_sperm,
        'usdCurrency_colorado_sperm': usdCurrency_colorado_sperm,
        'eurCurrency_colorado_sperm': eurCurrency_colorado_sperm,
        'gbpCurrency_colorado_icsi': gbpCurrency_colorado_icsi,
        'usdCurrency_colorado_icsi': usdCurrency_colorado_icsi,
        'eurCurrency_colorado_icsi': eurCurrency_colorado_icsi,
        'gbpCurrency_colorado_iui': gbpCurrency_colorado_iui,
        'usdCurrency_colorado_iui': usdCurrency_colorado_iui,
        'eurCurrency_colorado_iui': eurCurrency_colorado_iui,

        'gbpCurrency_connecticut_ivf': gbpCurrency_connecticut_ivf,
        'usdCurrency_connecticut_ivf': usdCurrency_connecticut_ivf,
        'eurCurrency_connecticut_ivf': eurCurrency_connecticut_ivf,
        'gbpCurrency_connecticut_egg': gbpCurrency_connecticut_egg,
        'usdCurrency_connecticut_egg': usdCurrency_connecticut_egg,
        'eurCurrency_connecticut_egg': eurCurrency_connecticut_egg,
        'gbpCurrency_connecticut_embryo': gbpCurrency_connecticut_embryo,
        'usdCurrency_connecticut_embryo': usdCurrency_connecticut_embryo,
        'eurCurrency_connecticut_embryo': eurCurrency_connecticut_embryo,
        'gbpCurrency_connecticut_sperm': gbpCurrency_connecticut_sperm,
        'usdCurrency_connecticut_sperm': usdCurrency_connecticut_sperm,
        'eurCurrency_connecticut_sperm': eurCurrency_connecticut_sperm,
        'gbpCurrency_connecticut_icsi': gbpCurrency_connecticut_icsi,
        'usdCurrency_connecticut_icsi': usdCurrency_connecticut_icsi,
        'eurCurrency_connecticut_icsi': eurCurrency_connecticut_icsi,
        'gbpCurrency_connecticut_iui': gbpCurrency_connecticut_iui,
        'usdCurrency_connecticut_iui': usdCurrency_connecticut_iui,
        'eurCurrency_connecticut_iui': eurCurrency_connecticut_iui,

        'gbpCurrency_delaware_ivf': gbpCurrency_delaware_ivf,
        'usdCurrency_delaware_ivf': usdCurrency_delaware_ivf,
        'eurCurrency_delaware_ivf': eurCurrency_delaware_ivf,
        'gbpCurrency_delaware_egg': gbpCurrency_delaware_egg,
        'usdCurrency_delaware_egg': usdCurrency_delaware_egg,
        'eurCurrency_delaware_egg': eurCurrency_delaware_egg,
        'gbpCurrency_delaware_embryo': gbpCurrency_delaware_embryo,
        'usdCurrency_delaware_embryo': usdCurrency_delaware_embryo,
        'eurCurrency_delaware_embryo': eurCurrency_delaware_embryo,
        'gbpCurrency_delaware_sperm': gbpCurrency_delaware_sperm,
        'usdCurrency_delaware_sperm': usdCurrency_delaware_sperm,
        'eurCurrency_delaware_sperm': eurCurrency_delaware_sperm,
        'gbpCurrency_delaware_icsi': gbpCurrency_delaware_icsi,
        'usdCurrency_delaware_icsi': usdCurrency_delaware_icsi,
        'eurCurrency_delaware_icsi': eurCurrency_delaware_icsi,
        'gbpCurrency_delaware_iui': gbpCurrency_delaware_iui,
        'usdCurrency_delaware_iui': usdCurrency_delaware_iui,
        'eurCurrency_delaware_iui': eurCurrency_delaware_iui,

        'gbpCurrency_florida_ivf': gbpCurrency_florida_ivf,
        'usdCurrency_florida_ivf': usdCurrency_florida_ivf,
        'eurCurrency_florida_ivf': eurCurrency_florida_ivf,
        'gbpCurrency_florida_egg': gbpCurrency_florida_egg,
        'usdCurrency_florida_egg': usdCurrency_florida_egg,
        'eurCurrency_florida_egg': eurCurrency_florida_egg,
        'gbpCurrency_florida_embryo': gbpCurrency_florida_embryo,
        'usdCurrency_florida_embryo': usdCurrency_florida_embryo,
        'eurCurrency_florida_embryo': eurCurrency_florida_embryo,
        'gbpCurrency_florida_sperm': gbpCurrency_florida_sperm,
        'usdCurrency_florida_sperm': usdCurrency_florida_sperm,
        'eurCurrency_florida_sperm': eurCurrency_florida_sperm,
        'gbpCurrency_florida_icsi': gbpCurrency_florida_icsi,
        'usdCurrency_florida_icsi': usdCurrency_florida_icsi,
        'eurCurrency_florida_icsi': eurCurrency_florida_icsi,
        'gbpCurrency_florida_iui': gbpCurrency_florida_iui,
        'usdCurrency_florida_iui': usdCurrency_florida_iui,
        'eurCurrency_florida_iui': eurCurrency_florida_iui,

        'gbpCurrency_georgia_ivf': gbpCurrency_georgia_ivf,
        'usdCurrency_georgia_ivf': usdCurrency_georgia_ivf,
        'eurCurrency_georgia_ivf': eurCurrency_georgia_ivf,
        'gbpCurrency_georgia_egg': gbpCurrency_georgia_egg,
        'usdCurrency_georgia_egg': usdCurrency_georgia_egg,
        'eurCurrency_georgia_egg': eurCurrency_georgia_egg,
        'gbpCurrency_georgia_embryo': gbpCurrency_georgia_embryo,
        'usdCurrency_georgia_embryo': usdCurrency_georgia_embryo,
        'eurCurrency_georgia_embryo': eurCurrency_georgia_embryo,
        'gbpCurrency_georgia_sperm': gbpCurrency_georgia_sperm,
        'usdCurrency_georgia_sperm': usdCurrency_georgia_sperm,
        'eurCurrency_georgia_sperm': eurCurrency_georgia_sperm,
        'gbpCurrency_georgia_icsi': gbpCurrency_georgia_icsi,
        'usdCurrency_georgia_icsi': usdCurrency_georgia_icsi,
        'eurCurrency_georgia_icsi': eurCurrency_georgia_icsi,
        'gbpCurrency_georgia_iui': gbpCurrency_georgia_iui,
        'usdCurrency_georgia_iui': usdCurrency_georgia_iui,
        'eurCurrency_georgia_iui': eurCurrency_georgia_iui,

        'gbpCurrency_hawaii_ivf': gbpCurrency_hawaii_ivf,
        'usdCurrency_hawaii_ivf': usdCurrency_hawaii_ivf,
        'eurCurrency_hawaii_ivf': eurCurrency_hawaii_ivf,
        'gbpCurrency_hawaii_egg': gbpCurrency_hawaii_egg,
        'usdCurrency_hawaii_egg': usdCurrency_hawaii_egg,
        'eurCurrency_hawaii_egg': eurCurrency_hawaii_egg,
        'gbpCurrency_hawaii_embryo': gbpCurrency_hawaii_embryo,
        'usdCurrency_hawaii_embryo': usdCurrency_hawaii_embryo,
        'eurCurrency_hawaii_embryo': eurCurrency_hawaii_embryo,
        'gbpCurrency_hawaii_sperm': gbpCurrency_hawaii_sperm,
        'usdCurrency_hawaii_sperm': usdCurrency_hawaii_sperm,
        'eurCurrency_hawaii_sperm': eurCurrency_hawaii_sperm,
        'gbpCurrency_hawaii_icsi': gbpCurrency_hawaii_icsi,
        'usdCurrency_hawaii_icsi': usdCurrency_hawaii_icsi,
        'eurCurrency_hawaii_icsi': eurCurrency_hawaii_icsi,
        'gbpCurrency_hawaii_iui': gbpCurrency_hawaii_iui,
        'usdCurrency_hawaii_iui': usdCurrency_hawaii_iui,
        'eurCurrency_hawaii_iui': eurCurrency_hawaii_iui,

        'gbpCurrency_idaho_ivf': gbpCurrency_idaho_ivf,
        'usdCurrency_idaho_ivf': usdCurrency_idaho_ivf,
        'eurCurrency_idaho_ivf': eurCurrency_idaho_ivf,
        'gbpCurrency_idaho_egg': gbpCurrency_idaho_egg,
        'usdCurrency_idaho_egg': usdCurrency_idaho_egg,
        'eurCurrency_idaho_egg': eurCurrency_idaho_egg,
        'gbpCurrency_idaho_embryo': gbpCurrency_idaho_embryo,
        'usdCurrency_idaho_embryo': usdCurrency_idaho_embryo,
        'eurCurrency_idaho_embryo': eurCurrency_idaho_embryo,
        'gbpCurrency_idaho_sperm': gbpCurrency_idaho_sperm,
        'usdCurrency_idaho_sperm': usdCurrency_idaho_sperm,
        'eurCurrency_idaho_sperm': eurCurrency_idaho_sperm,
        'gbpCurrency_idaho_icsi': gbpCurrency_idaho_icsi,
        'usdCurrency_idaho_icsi': usdCurrency_idaho_icsi,
        'eurCurrency_idaho_icsi': eurCurrency_idaho_icsi,
        'gbpCurrency_idaho_iui': gbpCurrency_idaho_iui,
        'usdCurrency_idaho_iui': usdCurrency_idaho_iui,
        'eurCurrency_idaho_iui': eurCurrency_idaho_iui,

        'gbpCurrency_illinois_ivf': gbpCurrency_illinois_ivf,
        'usdCurrency_illinois_ivf': usdCurrency_illinois_ivf,
        'eurCurrency_illinois_ivf': eurCurrency_illinois_ivf,
        'gbpCurrency_illinois_egg': gbpCurrency_illinois_egg,
        'usdCurrency_illinois_egg': usdCurrency_illinois_egg,
        'eurCurrency_illinois_egg': eurCurrency_illinois_egg,
        'gbpCurrency_illinois_embryo': gbpCurrency_illinois_embryo,
        'usdCurrency_illinois_embryo': usdCurrency_illinois_embryo,
        'eurCurrency_illinois_embryo': eurCurrency_illinois_embryo,
        'gbpCurrency_illinois_sperm': gbpCurrency_illinois_sperm,
        'usdCurrency_illinois_sperm': usdCurrency_illinois_sperm,
        'eurCurrency_illinois_sperm': eurCurrency_illinois_sperm,
        'gbpCurrency_illinois_icsi': gbpCurrency_illinois_icsi,
        'usdCurrency_illinois_icsi': usdCurrency_illinois_icsi,
        'eurCurrency_illinois_icsi': eurCurrency_illinois_icsi,
        'gbpCurrency_illinois_iui': gbpCurrency_illinois_iui,
        'usdCurrency_illinois_iui': usdCurrency_illinois_iui,
        'eurCurrency_illinois_iui': eurCurrency_illinois_iui,

        'gbpCurrency_indiana_ivf': gbpCurrency_indiana_ivf,
        'usdCurrency_indiana_ivf': usdCurrency_indiana_ivf,
        'eurCurrency_indiana_ivf': eurCurrency_indiana_ivf,
        'gbpCurrency_indiana_egg': gbpCurrency_indiana_egg,
        'usdCurrency_indiana_egg': usdCurrency_indiana_egg,
        'eurCurrency_indiana_egg': eurCurrency_indiana_egg,
        'gbpCurrency_indiana_embryo': gbpCurrency_indiana_embryo,
        'usdCurrency_indiana_embryo': usdCurrency_indiana_embryo,
        'eurCurrency_indiana_embryo': eurCurrency_indiana_embryo,
        'gbpCurrency_indiana_sperm': gbpCurrency_indiana_sperm,
        'usdCurrency_indiana_sperm': usdCurrency_indiana_sperm,
        'eurCurrency_indiana_sperm': eurCurrency_indiana_sperm,
        'gbpCurrency_indiana_icsi': gbpCurrency_indiana_icsi,
        'usdCurrency_indiana_icsi': usdCurrency_indiana_icsi,
        'eurCurrency_indiana_icsi': eurCurrency_indiana_icsi,
        'gbpCurrency_indiana_iui': gbpCurrency_indiana_iui,
        'usdCurrency_indiana_iui': usdCurrency_indiana_iui,
        'eurCurrency_indiana_iui': eurCurrency_indiana_iui,

        'gbpCurrency_iowa_ivf': gbpCurrency_iowa_ivf,
        'usdCurrency_iowa_ivf': usdCurrency_iowa_ivf,
        'eurCurrency_iowa_ivf': eurCurrency_iowa_ivf,
        'gbpCurrency_iowa_egg': gbpCurrency_iowa_egg,
        'usdCurrency_iowa_egg': usdCurrency_iowa_egg,
        'eurCurrency_iowa_egg': eurCurrency_iowa_egg,
        'gbpCurrency_iowa_embryo': gbpCurrency_iowa_embryo,
        'usdCurrency_iowa_embryo': usdCurrency_iowa_embryo,
        'eurCurrency_iowa_embryo': eurCurrency_iowa_embryo,
        'gbpCurrency_iowa_sperm': gbpCurrency_iowa_sperm,
        'usdCurrency_iowa_sperm': usdCurrency_iowa_sperm,
        'eurCurrency_iowa_sperm': eurCurrency_iowa_sperm,
        'gbpCurrency_iowa_icsi': gbpCurrency_iowa_icsi,
        'usdCurrency_iowa_icsi': usdCurrency_iowa_icsi,
        'eurCurrency_iowa_icsi': eurCurrency_iowa_icsi,
        'gbpCurrency_iowa_iui': gbpCurrency_iowa_iui,
        'usdCurrency_iowa_iui': usdCurrency_iowa_iui,
        'eurCurrency_iowa_iui': eurCurrency_iowa_iui,

        'gbpCurrency_kansas_ivf': gbpCurrency_kansas_ivf,
        'usdCurrency_kansas_ivf': usdCurrency_kansas_ivf,
        'eurCurrency_kansas_ivf': eurCurrency_kansas_ivf,
        'gbpCurrency_kansas_egg': gbpCurrency_kansas_egg,
        'usdCurrency_kansas_egg': usdCurrency_kansas_egg,
        'eurCurrency_kansas_egg': eurCurrency_kansas_egg,
        'gbpCurrency_kansas_embryo': gbpCurrency_kansas_embryo,
        'usdCurrency_kansas_embryo': usdCurrency_kansas_embryo,
        'eurCurrency_kansas_embryo': eurCurrency_kansas_embryo,
        'gbpCurrency_kansas_sperm': gbpCurrency_kansas_sperm,
        'usdCurrency_kansas_sperm': usdCurrency_kansas_sperm,
        'eurCurrency_kansas_sperm': eurCurrency_kansas_sperm,
        'gbpCurrency_kansas_icsi': gbpCurrency_kansas_icsi,
        'usdCurrency_kansas_icsi': usdCurrency_kansas_icsi,
        'eurCurrency_kansas_icsi': eurCurrency_kansas_icsi,
        'gbpCurrency_kansas_iui': gbpCurrency_kansas_iui,
        'usdCurrency_kansas_iui': usdCurrency_kansas_iui,
        'eurCurrency_kansas_iui': eurCurrency_kansas_iui,

        'gbpCurrency_kentucky_ivf': gbpCurrency_kentucky_ivf,
        'usdCurrency_kentucky_ivf': usdCurrency_kentucky_ivf,
        'eurCurrency_kentucky_ivf': eurCurrency_kentucky_ivf,
        'gbpCurrency_kentucky_egg': gbpCurrency_kentucky_egg,
        'usdCurrency_kentucky_egg': usdCurrency_kentucky_egg,
        'eurCurrency_kentucky_egg': eurCurrency_kentucky_egg,
        'gbpCurrency_kentucky_embryo': gbpCurrency_kentucky_embryo,
        'usdCurrency_kentucky_embryo': usdCurrency_kentucky_embryo,
        'eurCurrency_kentucky_embryo': eurCurrency_kentucky_embryo,
        'gbpCurrency_kentucky_sperm': gbpCurrency_kentucky_sperm,
        'usdCurrency_kentucky_sperm': usdCurrency_kentucky_sperm,
        'eurCurrency_kentucky_sperm': eurCurrency_kentucky_sperm,
        'gbpCurrency_kentucky_icsi': gbpCurrency_kentucky_icsi,
        'usdCurrency_kentucky_icsi': usdCurrency_kentucky_icsi,
        'eurCurrency_kentucky_icsi': eurCurrency_kentucky_icsi,
        'gbpCurrency_kentucky_iui': gbpCurrency_kentucky_iui,
        'usdCurrency_kentucky_iui': usdCurrency_kentucky_iui,
        'eurCurrency_kentucky_iui': eurCurrency_kentucky_iui,

        'gbpCurrency_louisiana_ivf': gbpCurrency_louisiana_ivf,
        'usdCurrency_louisiana_ivf': usdCurrency_louisiana_ivf,
        'eurCurrency_louisiana_ivf': eurCurrency_louisiana_ivf,
        'gbpCurrency_louisiana_egg': gbpCurrency_louisiana_egg,
        'usdCurrency_louisiana_egg': usdCurrency_louisiana_egg,
        'eurCurrency_louisiana_egg': eurCurrency_louisiana_egg,
        'gbpCurrency_louisiana_embryo': gbpCurrency_louisiana_embryo,
        'usdCurrency_louisiana_embryo': usdCurrency_louisiana_embryo,
        'eurCurrency_louisiana_embryo': eurCurrency_louisiana_embryo,
        'gbpCurrency_louisiana_sperm': gbpCurrency_louisiana_sperm,
        'usdCurrency_louisiana_sperm': usdCurrency_louisiana_sperm,
        'eurCurrency_louisiana_sperm': eurCurrency_louisiana_sperm,
        'gbpCurrency_louisiana_icsi': gbpCurrency_louisiana_icsi,
        'usdCurrency_louisiana_icsi': usdCurrency_louisiana_icsi,
        'eurCurrency_louisiana_icsi': eurCurrency_louisiana_icsi,
        'gbpCurrency_louisiana_iui': gbpCurrency_louisiana_iui,
        'usdCurrency_louisiana_iui': usdCurrency_louisiana_iui,
        'eurCurrency_louisiana_iui': eurCurrency_louisiana_iui,

        'gbpCurrency_maine_ivf': gbpCurrency_maine_ivf,
        'usdCurrency_maine_ivf': usdCurrency_maine_ivf,
        'eurCurrency_maine_ivf': eurCurrency_maine_ivf,
        'gbpCurrency_maine_egg': gbpCurrency_maine_egg,
        'usdCurrency_maine_egg': usdCurrency_maine_egg,
        'eurCurrency_maine_egg': eurCurrency_maine_egg,
        'gbpCurrency_maine_embryo': gbpCurrency_maine_embryo,
        'usdCurrency_maine_embryo': usdCurrency_maine_embryo,
        'eurCurrency_maine_embryo': eurCurrency_maine_embryo,
        'gbpCurrency_maine_sperm': gbpCurrency_maine_sperm,
        'usdCurrency_maine_sperm': usdCurrency_maine_sperm,
        'eurCurrency_maine_sperm': eurCurrency_maine_sperm,
        'gbpCurrency_maine_icsi': gbpCurrency_maine_icsi,
        'usdCurrency_maine_icsi': usdCurrency_maine_icsi,
        'eurCurrency_maine_icsi': eurCurrency_maine_icsi,
        'gbpCurrency_maine_iui': gbpCurrency_maine_iui,
        'usdCurrency_maine_iui': usdCurrency_maine_iui,
        'eurCurrency_maine_iui': eurCurrency_maine_iui,

        'gbpCurrency_maryland_ivf': gbpCurrency_maryland_ivf,
        'usdCurrency_maryland_ivf': usdCurrency_maryland_ivf,
        'eurCurrency_maryland_ivf': eurCurrency_maryland_ivf,
        'gbpCurrency_maryland_egg': gbpCurrency_maryland_egg,
        'usdCurrency_maryland_egg': usdCurrency_maryland_egg,
        'eurCurrency_maryland_egg': eurCurrency_maryland_egg,
        'gbpCurrency_maryland_embryo': gbpCurrency_maryland_embryo,
        'usdCurrency_maryland_embryo': usdCurrency_maryland_embryo,
        'eurCurrency_maryland_embryo': eurCurrency_maryland_embryo,
        'gbpCurrency_maryland_sperm': gbpCurrency_maryland_sperm,
        'usdCurrency_maryland_sperm': usdCurrency_maryland_sperm,
        'eurCurrency_maryland_sperm': eurCurrency_maryland_sperm,
        'gbpCurrency_maryland_icsi': gbpCurrency_maryland_icsi,
        'usdCurrency_maryland_icsi': usdCurrency_maryland_icsi,
        'eurCurrency_maryland_icsi': eurCurrency_maryland_icsi,
        'gbpCurrency_maryland_iui': gbpCurrency_maryland_iui,
        'usdCurrency_maryland_iui': usdCurrency_maryland_iui,
        'eurCurrency_maryland_iui': eurCurrency_maryland_iui,

        'gbpCurrency_massachusetts_ivf': gbpCurrency_massachusetts_ivf,
        'usdCurrency_massachusetts_ivf': usdCurrency_massachusetts_ivf,
        'eurCurrency_massachusetts_ivf': eurCurrency_massachusetts_ivf,
        'gbpCurrency_massachusetts_egg': gbpCurrency_massachusetts_egg,
        'usdCurrency_massachusetts_egg': usdCurrency_massachusetts_egg,
        'eurCurrency_massachusetts_egg': eurCurrency_massachusetts_egg,
        'gbpCurrency_massachusetts_embryo': gbpCurrency_massachusetts_embryo,
        'usdCurrency_massachusetts_embryo': usdCurrency_massachusetts_embryo,
        'eurCurrency_massachusetts_embryo': eurCurrency_massachusetts_embryo,
        'gbpCurrency_massachusetts_sperm': gbpCurrency_massachusetts_sperm,
        'usdCurrency_massachusetts_sperm': usdCurrency_massachusetts_sperm,
        'eurCurrency_massachusetts_sperm': eurCurrency_massachusetts_sperm,
        'gbpCurrency_massachusetts_icsi': gbpCurrency_massachusetts_icsi,
        'usdCurrency_massachusetts_icsi': usdCurrency_massachusetts_icsi,
        'eurCurrency_massachusetts_icsi': eurCurrency_massachusetts_icsi,
        'gbpCurrency_massachusetts_iui': gbpCurrency_massachusetts_iui,
        'usdCurrency_massachusetts_iui': usdCurrency_massachusetts_iui,
        'eurCurrency_massachusetts_iui': eurCurrency_massachusetts_iui,

        'gbpCurrency_michigan_ivf': gbpCurrency_michigan_ivf,
        'usdCurrency_michigan_ivf': usdCurrency_michigan_ivf,
        'eurCurrency_michigan_ivf': eurCurrency_michigan_ivf,
        'gbpCurrency_michigan_egg': gbpCurrency_michigan_egg,
        'usdCurrency_michigan_egg': usdCurrency_michigan_egg,
        'eurCurrency_michigan_egg': eurCurrency_michigan_egg,
        'gbpCurrency_michigan_embryo': gbpCurrency_michigan_embryo,
        'usdCurrency_michigan_embryo': usdCurrency_michigan_embryo,
        'eurCurrency_michigan_embryo': eurCurrency_michigan_embryo,
        'gbpCurrency_michigan_sperm': gbpCurrency_michigan_sperm,
        'usdCurrency_michigan_sperm': usdCurrency_michigan_sperm,
        'eurCurrency_michigan_sperm': eurCurrency_michigan_sperm,
        'gbpCurrency_michigan_icsi': gbpCurrency_michigan_icsi,
        'usdCurrency_michigan_icsi': usdCurrency_michigan_icsi,
        'eurCurrency_michigan_icsi': eurCurrency_michigan_icsi,
        'gbpCurrency_michigan_iui': gbpCurrency_michigan_iui,
        'usdCurrency_michigan_iui': usdCurrency_michigan_iui,
        'eurCurrency_michigan_iui': eurCurrency_michigan_iui,

        'gbpCurrency_minnesota_ivf': gbpCurrency_minnesota_ivf,
        'usdCurrency_minnesota_ivf': usdCurrency_minnesota_ivf,
        'eurCurrency_minnesota_ivf': eurCurrency_minnesota_ivf,
        'gbpCurrency_minnesota_egg': gbpCurrency_minnesota_egg,
        'usdCurrency_minnesota_egg': usdCurrency_minnesota_egg,
        'eurCurrency_minnesota_egg': eurCurrency_minnesota_egg,
        'gbpCurrency_minnesota_embryo': gbpCurrency_minnesota_embryo,
        'usdCurrency_minnesota_embryo': usdCurrency_minnesota_embryo,
        'eurCurrency_minnesota_embryo': eurCurrency_minnesota_embryo,
        'gbpCurrency_minnesota_sperm': gbpCurrency_minnesota_sperm,
        'usdCurrency_minnesota_sperm': usdCurrency_minnesota_sperm,
        'eurCurrency_minnesota_sperm': eurCurrency_minnesota_sperm,
        'gbpCurrency_minnesota_icsi': gbpCurrency_minnesota_icsi,
        'usdCurrency_minnesota_icsi': usdCurrency_minnesota_icsi,
        'eurCurrency_minnesota_icsi': eurCurrency_minnesota_icsi,
        'gbpCurrency_minnesota_iui': gbpCurrency_minnesota_iui,
        'usdCurrency_minnesota_iui': usdCurrency_minnesota_iui,
        'eurCurrency_minnesota_iui': eurCurrency_minnesota_iui,

        'gbpCurrency_mississippi_ivf': gbpCurrency_mississippi_ivf,
        'usdCurrency_mississippi_ivf': usdCurrency_mississippi_ivf,
        'eurCurrency_mississippi_ivf': eurCurrency_mississippi_ivf,
        'gbpCurrency_mississippi_egg': gbpCurrency_mississippi_egg,
        'usdCurrency_mississippi_egg': usdCurrency_mississippi_egg,
        'eurCurrency_mississippi_egg': eurCurrency_mississippi_egg,
        'gbpCurrency_mississippi_embryo': gbpCurrency_mississippi_embryo,
        'usdCurrency_mississippi_embryo': usdCurrency_mississippi_embryo,
        'eurCurrency_mississippi_embryo': eurCurrency_mississippi_embryo,
        'gbpCurrency_mississippi_sperm': gbpCurrency_mississippi_sperm,
        'usdCurrency_mississippi_sperm': usdCurrency_mississippi_sperm,
        'eurCurrency_mississippi_sperm': eurCurrency_mississippi_sperm,
        'gbpCurrency_mississippi_icsi': gbpCurrency_mississippi_icsi,
        'usdCurrency_mississippi_icsi': usdCurrency_mississippi_icsi,
        'eurCurrency_mississippi_icsi': eurCurrency_mississippi_icsi,
        'gbpCurrency_mississippi_iui': gbpCurrency_mississippi_iui,
        'usdCurrency_mississippi_iui': usdCurrency_mississippi_iui,
        'eurCurrency_mississippi_iui': eurCurrency_mississippi_iui,

        'gbpCurrency_missouri_ivf': gbpCurrency_missouri_ivf,
        'usdCurrency_missouri_ivf': usdCurrency_missouri_ivf,
        'eurCurrency_missouri_ivf': eurCurrency_missouri_ivf,
        'gbpCurrency_missouri_egg': gbpCurrency_missouri_egg,
        'usdCurrency_missouri_egg': usdCurrency_missouri_egg,
        'eurCurrency_missouri_egg': eurCurrency_missouri_egg,
        'gbpCurrency_missouri_embryo': gbpCurrency_missouri_embryo,
        'usdCurrency_missouri_embryo': usdCurrency_missouri_embryo,
        'eurCurrency_missouri_embryo': eurCurrency_missouri_embryo,
        'gbpCurrency_missouri_sperm': gbpCurrency_missouri_sperm,
        'usdCurrency_missouri_sperm': usdCurrency_missouri_sperm,
        'eurCurrency_missouri_sperm': eurCurrency_missouri_sperm,
        'gbpCurrency_missouri_icsi': gbpCurrency_missouri_icsi,
        'usdCurrency_missouri_icsi': usdCurrency_missouri_icsi,
        'eurCurrency_missouri_icsi': eurCurrency_missouri_icsi,
        'gbpCurrency_missouri_iui': gbpCurrency_missouri_iui,
        'usdCurrency_missouri_iui': usdCurrency_missouri_iui,
        'eurCurrency_missouri_iui': eurCurrency_missouri_iui,

        'gbpCurrency_nebraska_ivf': gbpCurrency_nebraska_ivf,
        'usdCurrency_nebraska_ivf': usdCurrency_nebraska_ivf,
        'eurCurrency_nebraska_ivf': eurCurrency_nebraska_ivf,
        'gbpCurrency_nebraska_egg': gbpCurrency_nebraska_egg,
        'usdCurrency_nebraska_egg': usdCurrency_nebraska_egg,
        'eurCurrency_nebraska_egg': eurCurrency_nebraska_egg,
        'gbpCurrency_nebraska_embryo': gbpCurrency_nebraska_embryo,
        'usdCurrency_nebraska_embryo': usdCurrency_nebraska_embryo,
        'eurCurrency_nebraska_embryo': eurCurrency_nebraska_embryo,
        'gbpCurrency_nebraska_sperm': gbpCurrency_nebraska_sperm,
        'usdCurrency_nebraska_sperm': usdCurrency_nebraska_sperm,
        'eurCurrency_nebraska_sperm': eurCurrency_nebraska_sperm,
        'gbpCurrency_nebraska_icsi': gbpCurrency_nebraska_icsi,
        'usdCurrency_nebraska_icsi': usdCurrency_nebraska_icsi,
        'eurCurrency_nebraska_icsi': eurCurrency_nebraska_icsi,
        'gbpCurrency_nebraska_iui': gbpCurrency_nebraska_iui,
        'usdCurrency_nebraska_iui': usdCurrency_nebraska_iui,
        'eurCurrency_nebraska_iui': eurCurrency_nebraska_iui,

        'gbpCurrency_newhampshire_ivf': gbpCurrency_newhampshire_ivf,
        'usdCurrency_newhampshire_ivf': usdCurrency_newhampshire_ivf,
        'eurCurrency_newhampshire_ivf': eurCurrency_newhampshire_ivf,
        'gbpCurrency_newhampshire_egg': gbpCurrency_newhampshire_egg,
        'usdCurrency_newhampshire_egg': usdCurrency_newhampshire_egg,
        'eurCurrency_newhampshire_egg': eurCurrency_newhampshire_egg,
        'gbpCurrency_newhampshire_embryo': gbpCurrency_newhampshire_embryo,
        'usdCurrency_newhampshire_embryo': usdCurrency_newhampshire_embryo,
        'eurCurrency_newhampshire_embryo': eurCurrency_newhampshire_embryo,
        'gbpCurrency_newhampshire_sperm': gbpCurrency_newhampshire_sperm,
        'usdCurrency_newhampshire_sperm': usdCurrency_newhampshire_sperm,
        'eurCurrency_newhampshire_sperm': eurCurrency_newhampshire_sperm,
        'gbpCurrency_newhampshire_icsi': gbpCurrency_newhampshire_icsi,
        'usdCurrency_newhampshire_icsi': usdCurrency_newhampshire_icsi,
        'eurCurrency_newhampshire_icsi': eurCurrency_newhampshire_icsi,
        'gbpCurrency_newhampshire_iui': gbpCurrency_newhampshire_iui,
        'usdCurrency_newhampshire_iui': usdCurrency_newhampshire_iui,
        'eurCurrency_newhampshire_iui': eurCurrency_newhampshire_iui,

        'gbpCurrency_newjersey_ivf': gbpCurrency_newjersey_ivf,
        'usdCurrency_newjersey_ivf': usdCurrency_newjersey_ivf,
        'eurCurrency_newjersey_ivf': eurCurrency_newjersey_ivf,
        'gbpCurrency_newjersey_egg': gbpCurrency_newjersey_egg,
        'usdCurrency_newjersey_egg': usdCurrency_newjersey_egg,
        'eurCurrency_newjersey_egg': eurCurrency_newjersey_egg,
        'gbpCurrency_newjersey_embryo': gbpCurrency_newjersey_embryo,
        'usdCurrency_newjersey_embryo': usdCurrency_newjersey_embryo,
        'eurCurrency_newjersey_embryo': eurCurrency_newjersey_embryo,
        'gbpCurrency_newjersey_sperm': gbpCurrency_newjersey_sperm,
        'usdCurrency_newjersey_sperm': usdCurrency_newjersey_sperm,
        'eurCurrency_newjersey_sperm': eurCurrency_newjersey_sperm,
        'gbpCurrency_newjersey_icsi': gbpCurrency_newjersey_icsi,
        'usdCurrency_newjersey_icsi': usdCurrency_newjersey_icsi,
        'eurCurrency_newjersey_icsi': eurCurrency_newjersey_icsi,
        'gbpCurrency_newjersey_iui': gbpCurrency_newjersey_iui,
        'usdCurrency_newjersey_iui': usdCurrency_newjersey_iui,
        'eurCurrency_newjersey_iui': eurCurrency_newjersey_iui,

        'gbpCurrency_newmexico_ivf': gbpCurrency_newmexico_ivf,
        'usdCurrency_newmexico_ivf': usdCurrency_newmexico_ivf,
        'eurCurrency_newmexico_ivf': eurCurrency_newmexico_ivf,
        'gbpCurrency_newmexico_egg': gbpCurrency_newmexico_egg,
        'usdCurrency_newmexico_egg': usdCurrency_newmexico_egg,
        'eurCurrency_newmexico_egg': eurCurrency_newmexico_egg,
        'gbpCurrency_newmexico_embryo': gbpCurrency_newmexico_embryo,
        'usdCurrency_newmexico_embryo': usdCurrency_newmexico_embryo,
        'eurCurrency_newmexico_embryo': eurCurrency_newmexico_embryo,
        'gbpCurrency_newmexico_sperm': gbpCurrency_newmexico_sperm,
        'usdCurrency_newmexico_sperm': usdCurrency_newmexico_sperm,
        'eurCurrency_newmexico_sperm': eurCurrency_newmexico_sperm,
        'gbpCurrency_newmexico_icsi': gbpCurrency_newmexico_icsi,
        'usdCurrency_newmexico_icsi': usdCurrency_newmexico_icsi,
        'eurCurrency_newmexico_icsi': eurCurrency_newmexico_icsi,
        'gbpCurrency_newmexico_iui': gbpCurrency_newmexico_iui,
        'usdCurrency_newmexico_iui': usdCurrency_newmexico_iui,
        'eurCurrency_newmexico_iui': eurCurrency_newmexico_iui,

        'gbpCurrency_newyork_ivf': gbpCurrency_newyork_ivf,
        'usdCurrency_newyork_ivf': usdCurrency_newyork_ivf,
        'eurCurrency_newyork_ivf': eurCurrency_newyork_ivf,
        'gbpCurrency_newyork_egg': gbpCurrency_newyork_egg,
        'usdCurrency_newyork_egg': usdCurrency_newyork_egg,
        'eurCurrency_newyork_egg': eurCurrency_newyork_egg,
        'gbpCurrency_newyork_embryo': gbpCurrency_newyork_embryo,
        'usdCurrency_newyork_embryo': usdCurrency_newyork_embryo,
        'eurCurrency_newyork_embryo': eurCurrency_newyork_embryo,
        'gbpCurrency_newyork_sperm': gbpCurrency_newyork_sperm,
        'usdCurrency_newyork_sperm': usdCurrency_newyork_sperm,
        'eurCurrency_newyork_sperm': eurCurrency_newyork_sperm,
        'gbpCurrency_newyork_icsi': gbpCurrency_newyork_icsi,
        'usdCurrency_newyork_icsi': usdCurrency_newyork_icsi,
        'eurCurrency_newyork_icsi': eurCurrency_newyork_icsi,
        'gbpCurrency_newyork_iui': gbpCurrency_newyork_iui,
        'usdCurrency_newyork_iui': usdCurrency_newyork_iui,
        'eurCurrency_newyork_iui': eurCurrency_newyork_iui,
        }

    return render(request, 'main/us-regions.html', context)
