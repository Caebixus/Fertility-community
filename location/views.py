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


def locationsRegions(request):
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
        }

    return render(request, 'main/us-regions.html', context)
