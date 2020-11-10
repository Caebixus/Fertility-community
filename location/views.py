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

eurToGbp = 0.91
eurToUsd = 1.10

def locationsStandardIVF(request):
    queryset_list_uk = BasicClinic.objects.all()
    queryset_list_uk = queryset_list_uk.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()
    queryset_list_uk_ivf = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_uk_ivf.items():
        gbpCurrency_uk_ivf = val
        if gbpCurrency_uk_ivf is not None:
            usdCurrency_uk_ivf = val * gbpToUsd
            eurCurrency_uk_ivf = val * gbpToEur
        else:
            usdCurrency_uk_ivf = None
            eurCurrency_uk_ivf = None

#-------------------------------------------------------------------------------
    queryset_list_us = BasicClinic.objects.all()
    queryset_list_us = queryset_list_us.filter(clinicState__iexact='United States')
    my_total_clinic_count_us = queryset_list_us.count()
    queryset_list_us_ivf = queryset_list_us.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_us_ivf.items():
        usdCurrency_us_ivf = val
        if usdCurrency_us_ivf is not None:
            gbpCurrency_us_ivf = val * usdToGbp
            eurCurrency_us_ivf = val * usdToEur
        else:
            gbpCurrency_us_ivf = None
            eurCurrency_us_ivf = None

#-------------------------------------------------------------------------------
    queryset_list_cz = BasicClinic.objects.all()
    queryset_list_cz = queryset_list_cz.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()
    queryset_list_cz_ivf = queryset_list_cz.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cz_ivf.items():
        eurCurrency_cz_ivf = val
        if eurCurrency_cz_ivf is not None:
            gbpCurrency_cz_ivf = val * eurToGbp
            usdCurrency_cz_ivf = val * eurToUsd
        else:
            gbpCurrency_cz_ivf = None
            usdCurrency_cz_ivf = None

#-------------------------------------------------------------------------------
    queryset_list_sp = BasicClinic.objects.all()
    queryset_list_sp = queryset_list_sp.filter(clinicState__iexact='Spain')
    my_total_clinic_count_sp = queryset_list_sp.count()
    queryset_list_sp_ivf = queryset_list_sp.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_sp_ivf.items():
        eurCurrency_sp_ivf = val
        if eurCurrency_sp_ivf is not None:
            gbpCurrency_sp_ivf = val * eurToGbp
            usdCurrency_sp_ivf = val * eurToUsd
        else:
            gbpCurrency_sp_ivf = None
            usdCurrency_sp_ivf = None

    context = {
        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'gbpCurrency_uk_ivf': gbpCurrency_uk_ivf,
        'usdCurrency_uk_ivf': usdCurrency_uk_ivf,
        'eurCurrency_uk_ivf': eurCurrency_uk_ivf,

        'my_total_clinic_count_us': my_total_clinic_count_us,
        'gbpCurrency_us_ivf': gbpCurrency_us_ivf,
        'usdCurrency_us_ivf': usdCurrency_us_ivf,
        'eurCurrency_us_ivf': eurCurrency_us_ivf,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'gbpCurrency_cz_ivf': gbpCurrency_cz_ivf,
        'usdCurrency_cz_ivf': usdCurrency_cz_ivf,
        'eurCurrency_cz_ivf': eurCurrency_cz_ivf,

        'my_total_clinic_count_sp': my_total_clinic_count_sp,
        'gbpCurrency_sp_ivf': gbpCurrency_sp_ivf,
        'usdCurrency_sp_ivf': usdCurrency_sp_ivf,
        'eurCurrency_sp_ivf': eurCurrency_sp_ivf,
        }

    return render(request, 'main/Locations/locations-standard-ivf.html', context)

def locationsIVFwithEggDonation(request):
    queryset_list_uk = BasicClinic.objects.all()
    queryset_list_uk = queryset_list_uk.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()

    queryset_list_uk_egg = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_uk_egg.items():
        gbpCurrency_uk_egg = val
        if gbpCurrency_uk_egg is not None:
            usdCurrency_uk_egg = val * gbpToUsd
            eurCurrency_uk_egg = val * gbpToEur
        else:
            usdCurrency_uk_egg = None
            eurCurrency_uk_egg = None

#-------------------------------------------------------------------------------
    queryset_list_us = BasicClinic.objects.all()
    queryset_list_us = queryset_list_us.filter(clinicState__iexact='United States')
    my_total_clinic_count_us = queryset_list_us.count()

    queryset_list_us_egg = queryset_list_us.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_us_egg.items():
        usdCurrency_us_egg = val
        if usdCurrency_us_egg is not None:
            gbpCurrency_us_egg = val * usdToGbp
            eurCurrency_us_egg = val * usdToEur
        else:
            gbpCurrency_us_egg = None
            eurCurrency_us_egg = None

#-------------------------------------------------------------------------------
    queryset_list_cz = BasicClinic.objects.all()
    queryset_list_cz = queryset_list_cz.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()

    queryset_list_cz_egg = queryset_list_cz.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cz_egg.items():
        eurCurrency_cz_egg = val
        if eurCurrency_cz_egg is not None:
            gbpCurrency_cz_egg = val * eurToGbp
            usdCurrency_cz_egg = val * eurToUsd
        else:
            gbpCurrency_cz_egg = None
            usdCurrency_cz_egg = None

#-------------------------------------------------------------------------------
    queryset_list_es = BasicClinic.objects.all()
    queryset_list_es = queryset_list_es.filter(clinicState__iexact='Spain')
    my_total_clinic_count_es = queryset_list_es.count()

    queryset_list_es_egg = queryset_list_es.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_es_egg.items():
        eurCurrency_es_egg = val
        if eurCurrency_es_egg is not None:
            gbpCurrency_es_egg = val * eurToGbp
            usdCurrency_es_egg = val * eurToUsd
        else:
            gbpCurrency_es_egg = None
            usdCurrency_es_egg = None

    context = {
        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'gbpCurrency_uk_egg': gbpCurrency_uk_egg,
        'usdCurrency_uk_egg': usdCurrency_uk_egg,
        'eurCurrency_uk_egg': eurCurrency_uk_egg,

        'my_total_clinic_count_us': my_total_clinic_count_us,
        'gbpCurrency_us_egg': gbpCurrency_us_egg,
        'usdCurrency_us_egg': usdCurrency_us_egg,
        'eurCurrency_us_egg': eurCurrency_us_egg,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'gbpCurrency_cz_egg': gbpCurrency_cz_egg,
        'usdCurrency_cz_egg': usdCurrency_cz_egg,
        'eurCurrency_cz_egg': eurCurrency_cz_egg,

        'my_total_clinic_count_es': my_total_clinic_count_es,
        'gbpCurrency_es_egg': gbpCurrency_es_egg,
        'usdCurrency_es_egg': usdCurrency_es_egg,
        'eurCurrency_es_egg': eurCurrency_es_egg,
        }

    return render(request, 'main/Locations/locations-ivf-with-egg-donors.html', context)

def locationsIVFwithEmbryoDonation(request):
    queryset_list_uk = BasicClinic.objects.all()
    queryset_list_uk = queryset_list_uk.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()

    queryset_list_uk_embryo = queryset_list_uk.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_uk_embryo.items():
        gbpCurrency_uk_embryo = val
        if gbpCurrency_uk_embryo is not None:
            usdCurrency_uk_embryo = val * gbpToUsd
            eurCurrency_uk_embryo = val * gbpToEur
        else:
            usdCurrency_uk_embryo = None
            eurCurrency_uk_embryo = None

#-------------------------------------------------------------------------------
    queryset_list_us = BasicClinic.objects.all()
    queryset_list_us = queryset_list_us.filter(clinicState__iexact='United States')
    my_total_clinic_count_us = queryset_list_us.count()

    queryset_list_us_embryo = queryset_list_us.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_us_embryo.items():
        usdCurrency_us_embryo = val
        if usdCurrency_us_embryo is not None:
            gbpCurrency_us_embryo = val * usdToGbp
            eurCurrency_us_embryo = val * usdToEur
        else:
            gbpCurrency_us_embryo = None
            eurCurrency_us_embryo = None

#-------------------------------------------------------------------------------
    queryset_list_cz = BasicClinic.objects.all()
    queryset_list_cz = queryset_list_cz.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()

    queryset_list_cz_embryo = queryset_list_cz.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cz_embryo.items():
        eurCurrency_cz_embryo = val
        if eurCurrency_cz_embryo is not None:
            gbpCurrency_cz_embryo = val * eurToGbp
            usdCurrency_cz_embryo = val * eurToUsd
        else:
            gbpCurrency_cz_embryo = None
            usdCurrency_cz_embryo = None

#-------------------------------------------------------------------------------
    queryset_list_es = BasicClinic.objects.all()
    queryset_list_es = queryset_list_es.filter(clinicState__iexact='Spain')
    my_total_clinic_count_es = queryset_list_es.count()

    queryset_list_es_embryo = queryset_list_es.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_es_embryo.items():
        eurCurrency_es_embryo = val
        if eurCurrency_es_embryo is not None:
            gbpCurrency_es_embryo = val * eurToGbp
            usdCurrency_es_embryo = val * eurToUsd
        else:
            gbpCurrency_es_embryo = None
            usdCurrency_es_embryo = None

    context = {
        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'gbpCurrency_uk_embryo': gbpCurrency_uk_embryo,
        'usdCurrency_uk_embryo': usdCurrency_uk_embryo,
        'eurCurrency_uk_embryo': eurCurrency_uk_embryo,

        'my_total_clinic_count_us': my_total_clinic_count_us,
        'gbpCurrency_us_embryo': gbpCurrency_us_embryo,
        'usdCurrency_us_embryo': usdCurrency_us_embryo,
        'eurCurrency_us_embryo': eurCurrency_us_embryo,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'gbpCurrency_cz_embryo': gbpCurrency_cz_embryo,
        'usdCurrency_cz_embryo': usdCurrency_cz_embryo,
        'eurCurrency_cz_embryo': eurCurrency_cz_embryo,

        'my_total_clinic_count_es': my_total_clinic_count_es,
        'gbpCurrency_es_embryo': gbpCurrency_es_embryo,
        'usdCurrency_es_embryo': usdCurrency_es_embryo,
        'eurCurrency_es_embryo': eurCurrency_es_embryo,

        }

    return render(request, 'main/Locations/locations-ivf-with-embryo-donors.html', context)

def locationsIUI(request):
    queryset_list_uk = BasicClinic.objects.all()
    queryset_list_uk = queryset_list_uk.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()

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
    my_total_clinic_count_us = queryset_list_us.count()

    queryset_list_us_iui = queryset_list_us.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_us_iui.items():
        usdCurrency_us_iui = val
        if usdCurrency_us_iui is not None:
            gbpCurrency_us_iui = val * usdToGbp
            eurCurrency_us_iui = val * usdToEur
        else:
            gbpCurrency_us_iui = None
            eurCurrency_us_iui = None

#-------------------------------------------------------------------------------
    queryset_list_cz = BasicClinic.objects.all()
    queryset_list_cz = queryset_list_cz.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()

    queryset_list_cz_iui = queryset_list_cz.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cz_iui.items():
        eurCurrency_cz_iui = val
        if eurCurrency_cz_iui is not None:
            gbpCurrency_cz_iui = val * eurToGbp
            usdCurrency_cz_iui = val * eurToUsd
        else:
            gbpCurrency_cz_iui = None
            usdCurrency_cz_iui = None

#-------------------------------------------------------------------------------
    queryset_list_es = BasicClinic.objects.all()
    queryset_list_es = queryset_list_es.filter(clinicState__iexact='Spain')
    my_total_clinic_count_es = queryset_list_es.count()

    queryset_list_es_iui = queryset_list_es.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_es_iui.items():
        eurCurrency_es_iui = val
        if eurCurrency_es_iui is not None:
            gbpCurrency_es_iui = val * eurToGbp
            usdCurrency_es_iui = val * eurToUsd
        else:
            gbpCurrency_es_iui = None
            usdCurrency_es_iui = None

    context = {
        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'gbpCurrency_uk_iui': gbpCurrency_uk_iui,
        'usdCurrency_uk_iui': usdCurrency_uk_iui,
        'eurCurrency_uk_iui': eurCurrency_uk_iui,

        'my_total_clinic_count_us': my_total_clinic_count_us,
        'gbpCurrency_us_iui': gbpCurrency_us_iui,
        'usdCurrency_us_iui': usdCurrency_us_iui,
        'eurCurrency_us_iui': eurCurrency_us_iui,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'gbpCurrency_cz_iui': gbpCurrency_cz_iui,
        'usdCurrency_cz_iui': usdCurrency_cz_iui,
        'eurCurrency_cz_iui': eurCurrency_cz_iui,

        'my_total_clinic_count_es': my_total_clinic_count_es,
        'gbpCurrency_es_iui': gbpCurrency_es_iui,
        'usdCurrency_es_iui': usdCurrency_es_iui,
        'eurCurrency_es_iui': eurCurrency_es_iui,

        }

    return render(request, 'main/Locations/locations-iui.html', context)












def locationsUSRegions(request):
    queryset_list_us = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_alabama = queryset_list_us.filter(clinicRegion__iexact='Alabama')
    my_total_count_alabama = queryset_list_alabama.count()
    queryset_list_alabama_ivf = queryset_list_alabama.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_alaska = queryset_list_alaska.count()
    queryset_list_alaska_ivf = queryset_list_alaska.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_arizona = queryset_list_arizona.count()
    queryset_list_arizona_ivf = queryset_list_arizona.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_arkansas = queryset_list_arkansas.count()
    queryset_list_arkansas_ivf = queryset_list_arkansas.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_california = queryset_list_california.count()
    queryset_list_california_ivf = queryset_list_california.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_colorado = queryset_list_colorado.count()
    queryset_list_colorado_ivf = queryset_list_colorado.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_connecticut = queryset_list_connecticut.count()
    queryset_list_connecticut_ivf = queryset_list_connecticut.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_delaware = queryset_list_delaware.count()
    queryset_list_delaware_ivf = queryset_list_delaware.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_florida = queryset_list_florida.count()
    queryset_list_florida_ivf = queryset_list_florida.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    my_total_count_florida_ovarian_ivf_treatment = queryset_list_florida.filter(ovarian_ivf_treatment=True).count()
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
    my_total_count_georgia = queryset_list_georgia.count()
    queryset_list_georgia_ivf = queryset_list_georgia.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_hawaii = queryset_list_hawaii.count()
    queryset_list_hawaii_ivf = queryset_list_hawaii.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_idaho = queryset_list_idaho.count()
    queryset_list_idaho_ivf = queryset_list_idaho.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_illinois = queryset_list_illinois.count()
    queryset_list_illinois_ivf = queryset_list_illinois.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_indiana = queryset_list_indiana.count()
    queryset_list_indiana_ivf = queryset_list_indiana.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_iowa = queryset_list_iowa.count()
    queryset_list_iowa_ivf = queryset_list_iowa.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_kansas = queryset_list_kansas.count()
    queryset_list_kansas_ivf = queryset_list_kansas.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_kentucky = queryset_list_kentucky.count()
    queryset_list_kentucky_ivf = queryset_list_kentucky.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_louisiana = queryset_list_louisiana.count()
    queryset_list_louisiana_ivf = queryset_list_louisiana.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_maine = queryset_list_maine.count()
    queryset_list_maine_ivf = queryset_list_maine.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_maryland = queryset_list_maryland.count()
    queryset_list_maryland_ivf = queryset_list_maryland.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_massachusetts = queryset_list_massachusetts.count()
    queryset_list_massachusetts_ivf = queryset_list_massachusetts.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_michigan = queryset_list_michigan.count()
    queryset_list_michigan_ivf = queryset_list_michigan.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_minnesota = queryset_list_minnesota.count()
    queryset_list_minnesota_ivf = queryset_list_minnesota.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_mississippi = queryset_list_mississippi.count()
    queryset_list_mississippi_ivf = queryset_list_mississippi.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_missouri = queryset_list_missouri.count()
    queryset_list_missouri_ivf = queryset_list_missouri.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    queryset_list_montana = queryset_list_us.filter(clinicRegion__iexact='Montana')
    my_total_count_montana = queryset_list_montana.count()
    queryset_list_montana_ivf = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_missouri_ivf.items():
        usdCurrency_montana_ivf = val
        if usdCurrency_montana_ivf is not None:
            gbpCurrency_montana_ivf = val * usdToGbp
            eurCurrency_montana_ivf = val * usdToEur
        else:
            gbpCurrency_montana_ivf = None
            eurCurrency_montana_ivf = None

    queryset_list_montana_egg = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_montana_egg.items():
        usdCurrency_montana_egg = val
        if usdCurrency_montana_egg is not None:
            gbpCurrency_montana_egg = val * usdToGbp
            eurCurrency_montana_egg = val * usdToEur
        else:
            gbpCurrency_montana_egg = None
            eurCurrency_montana_egg = None

    queryset_list_montana_embryo = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_montana_embryo.items():
        usdCurrency_montana_embryo = val
        if usdCurrency_montana_embryo is not None:
            gbpCurrency_montana_embryo = val * usdToGbp
            eurCurrency_montana_embryo = val * usdToEur
        else:
            gbpCurrency_montana_embryo = None
            eurCurrency_montana_embryo = None

    queryset_list_montana_sperm = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_montana_sperm.items():
        usdCurrency_montana_sperm = val
        if usdCurrency_montana_sperm is not None:
            gbpCurrency_montana_sperm = val * usdToGbp
            eurCurrency_montana_sperm = val * usdToEur
        else:
            gbpCurrency_montana_sperm = None
            eurCurrency_montana_sperm = None

    queryset_list_montana_icsi = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_montana_icsi.items():
        usdCurrency_montana_icsi = val
        if usdCurrency_montana_icsi is not None:
            gbpCurrency_montana_icsi = val * usdToGbp
            eurCurrency_montana_icsi = val * usdToEur
        else:
            gbpCurrency_montana_icsi = None
            eurCurrency_montana_icsi = None

    queryset_list_montana_iui = queryset_list_montana.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_montana_iui.items():
        usdCurrency_montana_iui = val
        if usdCurrency_montana_iui is not None:
            gbpCurrency_montana_iui = val * usdToGbp
            eurCurrency_montana_iui = val * usdToEur
        else:
            gbpCurrency_montana_iui = None
            eurCurrency_montana_iui = None

    #--------------------------------------------------------------------------
    queryset_list_nebraska = queryset_list_us.filter(clinicRegion__iexact='Nebraska')
    my_total_count_nebraska = queryset_list_nebraska.count()
    queryset_list_nebraska_ivf = queryset_list_nebraska.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_newhampshire = queryset_list_newhampshire.count()
    queryset_list_newhampshire_ivf = queryset_list_newhampshire.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_newjersey = queryset_list_newjersey.count()
    queryset_list_newjersey_ivf = queryset_list_newjersey.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_newmexico = queryset_list_newmexico.count()
    queryset_list_newmexico_ivf = queryset_list_newmexico.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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
    my_total_count_newyork = queryset_list_newyork.count()
    queryset_list_newyork_ivf = queryset_list_newyork.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
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

    #--------------------------------------------------------------------------
    queryset_list_northcarolina = queryset_list_us.filter(clinicRegion__iexact='North Carolina')
    my_total_count_northcarolina = queryset_list_northcarolina.count()
    queryset_list_northcarolina_ivf = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_northcarolina_ivf.items():
        usdCurrency_northcarolina_ivf = val
        if usdCurrency_northcarolina_ivf is not None:
            gbpCurrency_northcarolina_ivf = val * usdToGbp
            eurCurrency_northcarolina_ivf = val * usdToEur
        else:
            gbpCurrency_northcarolina_ivf = None
            eurCurrency_northcarolina_ivf = None

    queryset_list_northcarolina_egg = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_egg.items():
        usdCurrency_northcarolina_egg = val
        if usdCurrency_northcarolina_egg is not None:
            gbpCurrency_northcarolina_egg = val * usdToGbp
            eurCurrency_northcarolina_egg = val * usdToEur
        else:
            gbpCurrency_northcarolina_egg = None
            eurCurrency_northcarolina_egg = None

    queryset_list_northcarolina_embryo = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_embryo.items():
        usdCurrency_northcarolina_embryo = val
        if usdCurrency_northcarolina_embryo is not None:
            gbpCurrency_northcarolina_embryo = val * usdToGbp
            eurCurrency_northcarolina_embryo = val * usdToEur
        else:
            gbpCurrency_northcarolina_embryo = None
            eurCurrency_northcarolina_embryo = None

    queryset_list_northcarolina_sperm = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_sperm.items():
        usdCurrency_northcarolina_sperm = val
        if usdCurrency_northcarolina_sperm is not None:
            gbpCurrency_northcarolina_sperm = val * usdToGbp
            eurCurrency_northcarolina_sperm = val * usdToEur
        else:
            gbpCurrency_northcarolina_sperm = None
            eurCurrency_northcarolina_sperm = None

    queryset_list_northcarolina_icsi = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_northcarolina_icsi.items():
        usdCurrency_northcarolina_icsi = val
        if usdCurrency_northcarolina_icsi is not None:
            gbpCurrency_northcarolina_icsi = val * usdToGbp
            eurCurrency_northcarolina_icsi = val * usdToEur
        else:
            gbpCurrency_northcarolina_icsi = None
            eurCurrency_northcarolina_icsi = None

    queryset_list_northcarolina_iui = queryset_list_northcarolina.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_northcarolina_iui.items():
        usdCurrency_northcarolina_iui = val
        if usdCurrency_northcarolina_iui is not None:
            gbpCurrency_northcarolina_iui = val * usdToGbp
            eurCurrency_northcarolina_iui = val * usdToEur
        else:
            gbpCurrency_northcarolina_iui = None
            eurCurrency_northcarolina_iui = None

    #--------------------------------------------------------------------------
    queryset_list_northdakota = queryset_list_us.filter(clinicRegion__iexact='North Dakota')
    my_total_count_northdakota = queryset_list_northdakota.count()
    queryset_list_northdakota_ivf = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_northdakota_ivf.items():
        usdCurrency_northdakota_ivf = val
        if usdCurrency_northdakota_ivf is not None:
            gbpCurrency_northdakota_ivf = val * usdToGbp
            eurCurrency_northdakota_ivf = val * usdToEur
        else:
            gbpCurrency_northdakota_ivf = None
            eurCurrency_northdakota_ivf = None

    queryset_list_northdakota_egg = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_egg.items():
        usdCurrency_northdakota_egg = val
        if usdCurrency_northdakota_egg is not None:
            gbpCurrency_northdakota_egg = val * usdToGbp
            eurCurrency_northdakota_egg = val * usdToEur
        else:
            gbpCurrency_northdakota_egg = None
            eurCurrency_northdakota_egg = None

    queryset_list_northdakota_embryo = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_embryo.items():
        usdCurrency_northdakota_embryo = val
        if usdCurrency_northdakota_embryo is not None:
            gbpCurrency_northdakota_embryo = val * usdToGbp
            eurCurrency_northdakota_embryo = val * usdToEur
        else:
            gbpCurrency_northdakota_embryo = None
            eurCurrency_northdakota_embryo = None

    queryset_list_northdakota_sperm = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_sperm.items():
        usdCurrency_northdakota_sperm = val
        if usdCurrency_northdakota_sperm is not None:
            gbpCurrency_northdakota_sperm = val * usdToGbp
            eurCurrency_northdakota_sperm = val * usdToEur
        else:
            gbpCurrency_northdakota_sperm = None
            eurCurrency_northdakota_sperm = None

    queryset_list_northdakota_icsi = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_northdakota_icsi.items():
        usdCurrency_northdakota_icsi = val
        if usdCurrency_northdakota_icsi is not None:
            gbpCurrency_northdakota_icsi = val * usdToGbp
            eurCurrency_northdakota_icsi = val * usdToEur
        else:
            gbpCurrency_northdakota_icsi = None
            eurCurrency_northdakota_icsi = None

    queryset_list_northdakota_iui = queryset_list_northdakota.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_northdakota_iui.items():
        usdCurrency_northdakota_iui = val
        if usdCurrency_northdakota_iui is not None:
            gbpCurrency_northdakota_iui = val * usdToGbp
            eurCurrency_northdakota_iui = val * usdToEur
        else:
            gbpCurrency_northdakota_iui = None
            eurCurrency_northdakota_iui = None

    #--------------------------------------------------------------------------
    queryset_list_nevada = queryset_list_us.filter(clinicRegion__iexact='Nevada')
    my_total_count_nevada = queryset_list_nevada.count()
    queryset_list_nevada_ivf = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nevada_ivf.items():
        usdCurrency_nevada_ivf = val
        if usdCurrency_nevada_ivf is not None:
            gbpCurrency_nevada_ivf = val * usdToGbp
            eurCurrency_nevada_ivf = val * usdToEur
        else:
            gbpCurrency_nevada_ivf = None
            eurCurrency_nevada_ivf = None

    queryset_list_nevada_egg = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nevada_egg.items():
        usdCurrency_nevada_egg = val
        if usdCurrency_nevada_egg is not None:
            gbpCurrency_nevada_egg = val * usdToGbp
            eurCurrency_nevada_egg = val * usdToEur
        else:
            gbpCurrency_nevada_egg = None
            eurCurrency_nevada_egg = None

    queryset_list_nevada_embryo = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nevada_embryo.items():
        usdCurrency_nevada_embryo = val
        if usdCurrency_nevada_embryo is not None:
            gbpCurrency_nevada_embryo = val * usdToGbp
            eurCurrency_nevada_embryo = val * usdToEur
        else:
            gbpCurrency_nevada_embryo = None
            eurCurrency_nevada_embryo = None

    queryset_list_nevada_sperm = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nevada_sperm.items():
        usdCurrency_nevada_sperm = val
        if usdCurrency_nevada_sperm is not None:
            gbpCurrency_nevada_sperm = val * usdToGbp
            eurCurrency_nevada_sperm = val * usdToEur
        else:
            gbpCurrency_nevada_sperm = None
            eurCurrency_nevada_sperm = None

    queryset_list_nevada_icsi = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nevada_icsi.items():
        usdCurrency_nevada_icsi = val
        if usdCurrency_nevada_icsi is not None:
            gbpCurrency_nevada_icsi = val * usdToGbp
            eurCurrency_nevada_icsi = val * usdToEur
        else:
            gbpCurrency_nevada_icsi = None
            eurCurrency_nevada_icsi = None

    queryset_list_nevada_iui = queryset_list_nevada.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nevada_iui.items():
        usdCurrency_nevada_iui = val
        if usdCurrency_nevada_iui is not None:
            gbpCurrency_nevada_iui = val * usdToGbp
            eurCurrency_nevada_iui = val * usdToEur
        else:
            gbpCurrency_nevada_iui = None
            eurCurrency_nevada_iui = None

    #--------------------------------------------------------------------------
    queryset_list_ohio = queryset_list_us.filter(clinicRegion__iexact='Ohio')
    my_total_count_ohio = queryset_list_ohio.count()
    queryset_list_ohio_ivf = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_ohio_ivf.items():
        usdCurrency_ohio_ivf = val
        if usdCurrency_ohio_ivf is not None:
            gbpCurrency_ohio_ivf = val * usdToGbp
            eurCurrency_ohio_ivf = val * usdToEur
        else:
            gbpCurrency_ohio_ivf = None
            eurCurrency_ohio_ivf = None

    queryset_list_ohio_egg = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_ohio_egg.items():
        usdCurrency_ohio_egg = val
        if usdCurrency_ohio_egg is not None:
            gbpCurrency_ohio_egg = val * usdToGbp
            eurCurrency_ohio_egg = val * usdToEur
        else:
            gbpCurrency_ohio_egg = None
            eurCurrency_ohio_egg = None

    queryset_list_ohio_embryo = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_ohio_embryo.items():
        usdCurrency_ohio_embryo = val
        if usdCurrency_ohio_embryo is not None:
            gbpCurrency_ohio_embryo = val * usdToGbp
            eurCurrency_ohio_embryo = val * usdToEur
        else:
            gbpCurrency_ohio_embryo = None
            eurCurrency_ohio_embryo = None

    queryset_list_ohio_sperm = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_ohio_sperm.items():
        usdCurrency_ohio_sperm = val
        if usdCurrency_ohio_sperm is not None:
            gbpCurrency_ohio_sperm = val * usdToGbp
            eurCurrency_ohio_sperm = val * usdToEur
        else:
            gbpCurrency_ohio_sperm = None
            eurCurrency_ohio_sperm = None

    queryset_list_ohio_icsi = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_ohio_icsi.items():
        usdCurrency_ohio_icsi = val
        if usdCurrency_ohio_icsi is not None:
            gbpCurrency_ohio_icsi = val * usdToGbp
            eurCurrency_ohio_icsi = val * usdToEur
        else:
            gbpCurrency_ohio_icsi = None
            eurCurrency_ohio_icsi = None

    queryset_list_ohio_iui = queryset_list_ohio.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_ohio_iui.items():
        usdCurrency_ohio_iui = val
        if usdCurrency_ohio_iui is not None:
            gbpCurrency_ohio_iui = val * usdToGbp
            eurCurrency_ohio_iui = val * usdToEur
        else:
            gbpCurrency_ohio_iui = None
            eurCurrency_ohio_iui = None

    #--------------------------------------------------------------------------
    queryset_list_oklahoma = queryset_list_us.filter(clinicRegion__iexact='Oklahoma')
    my_total_count_oklahoma = queryset_list_oklahoma.count()
    queryset_list_oklahoma_ivf = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_oklahoma_ivf.items():
        usdCurrency_oklahoma_ivf = val
        if usdCurrency_oklahoma_ivf is not None:
            gbpCurrency_oklahoma_ivf = val * usdToGbp
            eurCurrency_oklahoma_ivf = val * usdToEur
        else:
            gbpCurrency_oklahoma_ivf = None
            eurCurrency_oklahoma_ivf = None

    queryset_list_oklahoma_egg = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_egg.items():
        usdCurrency_oklahoma_egg = val
        if usdCurrency_oklahoma_egg is not None:
            gbpCurrency_oklahoma_egg = val * usdToGbp
            eurCurrency_oklahoma_egg = val * usdToEur
        else:
            gbpCurrency_oklahoma_egg = None
            eurCurrency_oklahoma_egg = None

    queryset_list_oklahoma_embryo = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_embryo.items():
        usdCurrency_oklahoma_embryo = val
        if usdCurrency_oklahoma_embryo is not None:
            gbpCurrency_oklahoma_embryo = val * usdToGbp
            eurCurrency_oklahoma_embryo = val * usdToEur
        else:
            gbpCurrency_oklahoma_embryo = None
            eurCurrency_oklahoma_embryo = None

    queryset_list_oklahoma_sperm = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_sperm.items():
        usdCurrency_oklahoma_sperm = val
        if usdCurrency_oklahoma_sperm is not None:
            gbpCurrency_oklahoma_sperm = val * usdToGbp
            eurCurrency_oklahoma_sperm = val * usdToEur
        else:
            gbpCurrency_oklahoma_sperm = None
            eurCurrency_oklahoma_sperm = None

    queryset_list_oklahoma_icsi = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_oklahoma_icsi.items():
        usdCurrency_oklahoma_icsi = val
        if usdCurrency_oklahoma_icsi is not None:
            gbpCurrency_oklahoma_icsi = val * usdToGbp
            eurCurrency_oklahoma_icsi = val * usdToEur
        else:
            gbpCurrency_oklahoma_icsi = None
            eurCurrency_oklahoma_icsi = None

    queryset_list_oklahoma_iui = queryset_list_oklahoma.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_oklahoma_iui.items():
        usdCurrency_oklahoma_iui = val
        if usdCurrency_oklahoma_iui is not None:
            gbpCurrency_oklahoma_iui = val * usdToGbp
            eurCurrency_oklahoma_iui = val * usdToEur
        else:
            gbpCurrency_oklahoma_iui = None
            eurCurrency_oklahoma_iui = None

    #--------------------------------------------------------------------------
    queryset_list_oregon = queryset_list_us.filter(clinicRegion__iexact='Oregon')
    my_total_count_oregon = queryset_list_oregon.count()
    queryset_list_oregon_ivf = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_oregon_ivf.items():
        usdCurrency_oregon_ivf = val
        if usdCurrency_oregon_ivf is not None:
            gbpCurrency_oregon_ivf = val * usdToGbp
            eurCurrency_oregon_ivf = val * usdToEur
        else:
            gbpCurrency_oregon_ivf = None
            eurCurrency_oregon_ivf = None

    queryset_list_oregon_egg = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_oregon_egg.items():
        usdCurrency_oregon_egg = val
        if usdCurrency_oregon_egg is not None:
            gbpCurrency_oregon_egg = val * usdToGbp
            eurCurrency_oregon_egg = val * usdToEur
        else:
            gbpCurrency_oregon_egg = None
            eurCurrency_oregon_egg = None

    queryset_list_oregon_embryo = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_oregon_embryo.items():
        usdCurrency_oregon_embryo = val
        if usdCurrency_oregon_embryo is not None:
            gbpCurrency_oregon_embryo = val * usdToGbp
            eurCurrency_oregon_embryo = val * usdToEur
        else:
            gbpCurrency_oregon_embryo = None
            eurCurrency_oregon_embryo = None

    queryset_list_oregon_sperm = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_oregon_sperm.items():
        usdCurrency_oregon_sperm = val
        if usdCurrency_oregon_sperm is not None:
            gbpCurrency_oregon_sperm = val * usdToGbp
            eurCurrency_oregon_sperm = val * usdToEur
        else:
            gbpCurrency_oregon_sperm = None
            eurCurrency_oregon_sperm = None

    queryset_list_oregon_icsi = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_oregon_icsi.items():
        usdCurrency_oregon_icsi = val
        if usdCurrency_oregon_icsi is not None:
            gbpCurrency_oregon_icsi = val * usdToGbp
            eurCurrency_oregon_icsi = val * usdToEur
        else:
            gbpCurrency_oregon_icsi = None
            eurCurrency_oregon_icsi = None

    queryset_list_oregon_iui = queryset_list_oregon.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_oregon_iui.items():
        usdCurrency_oregon_iui = val
        if usdCurrency_oregon_iui is not None:
            gbpCurrency_oregon_iui = val * usdToGbp
            eurCurrency_oregon_iui = val * usdToEur
        else:
            gbpCurrency_oregon_iui = None
            eurCurrency_oregon_iui = None

    #--------------------------------------------------------------------------
    queryset_list_pennsylvania = queryset_list_us.filter(clinicRegion__iexact='Pennsylvania')
    my_total_count_pennsylvania = queryset_list_pennsylvania.count()
    queryset_list_pennsylvania_ivf = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_pennsylvania_ivf.items():
        usdCurrency_pennsylvania_ivf = val
        if usdCurrency_pennsylvania_ivf is not None:
            gbpCurrency_pennsylvania_ivf = val * usdToGbp
            eurCurrency_pennsylvania_ivf = val * usdToEur
        else:
            gbpCurrency_pennsylvania_ivf = None
            eurCurrency_pennsylvania_ivf = None

    queryset_list_pennsylvania_egg = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_egg.items():
        usdCurrency_pennsylvania_egg = val
        if usdCurrency_pennsylvania_egg is not None:
            gbpCurrency_pennsylvania_egg = val * usdToGbp
            eurCurrency_pennsylvania_egg = val * usdToEur
        else:
            gbpCurrency_pennsylvania_egg = None
            eurCurrency_pennsylvania_egg = None

    queryset_list_pennsylvania_embryo = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_embryo.items():
        usdCurrency_pennsylvania_embryo = val
        if usdCurrency_pennsylvania_embryo is not None:
            gbpCurrency_pennsylvania_embryo = val * usdToGbp
            eurCurrency_pennsylvania_embryo = val * usdToEur
        else:
            gbpCurrency_pennsylvania_embryo = None
            eurCurrency_pennsylvania_embryo = None

    queryset_list_pennsylvania_sperm = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_sperm.items():
        usdCurrency_pennsylvania_sperm = val
        if usdCurrency_pennsylvania_sperm is not None:
            gbpCurrency_pennsylvania_sperm = val * usdToGbp
            eurCurrency_pennsylvania_sperm = val * usdToEur
        else:
            gbpCurrency_pennsylvania_sperm = None
            eurCurrency_pennsylvania_sperm = None

    queryset_list_pennsylvania_icsi = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_pennsylvania_icsi.items():
        usdCurrency_pennsylvania_icsi = val
        if usdCurrency_pennsylvania_icsi is not None:
            gbpCurrency_pennsylvania_icsi = val * usdToGbp
            eurCurrency_pennsylvania_icsi = val * usdToEur
        else:
            gbpCurrency_pennsylvania_icsi = None
            eurCurrency_pennsylvania_icsi = None

    queryset_list_pennsylvania_iui = queryset_list_pennsylvania.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_pennsylvania_iui.items():
        usdCurrency_pennsylvania_iui = val
        if usdCurrency_pennsylvania_iui is not None:
            gbpCurrency_pennsylvania_iui = val * usdToGbp
            eurCurrency_pennsylvania_iui = val * usdToEur
        else:
            gbpCurrency_pennsylvania_iui = None
            eurCurrency_pennsylvania_iui = None

    #--------------------------------------------------------------------------
    queryset_list_puertorico = queryset_list_us.filter(clinicRegion__iexact='Puerto Rico')
    my_total_count_puertorico = queryset_list_puertorico.count()
    queryset_list_puertorico_ivf = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_puertorico_ivf.items():
        usdCurrency_puertorico_ivf = val
        if usdCurrency_puertorico_ivf is not None:
            gbpCurrency_puertorico_ivf = val * usdToGbp
            eurCurrency_puertorico_ivf = val * usdToEur
        else:
            gbpCurrency_puertorico_ivf = None
            eurCurrency_puertorico_ivf = None

    queryset_list_puertorico_egg = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_egg.items():
        usdCurrency_puertorico_egg = val
        if usdCurrency_puertorico_egg is not None:
            gbpCurrency_puertorico_egg = val * usdToGbp
            eurCurrency_puertorico_egg = val * usdToEur
        else:
            gbpCurrency_puertorico_egg = None
            eurCurrency_puertorico_egg = None

    queryset_list_puertorico_embryo = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_embryo.items():
        usdCurrency_puertorico_embryo = val
        if usdCurrency_puertorico_embryo is not None:
            gbpCurrency_puertorico_embryo = val * usdToGbp
            eurCurrency_puertorico_embryo = val * usdToEur
        else:
            gbpCurrency_puertorico_embryo = None
            eurCurrency_puertorico_embryo = None

    queryset_list_puertorico_sperm = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_sperm.items():
        usdCurrency_puertorico_sperm = val
        if usdCurrency_puertorico_sperm is not None:
            gbpCurrency_puertorico_sperm = val * usdToGbp
            eurCurrency_puertorico_sperm = val * usdToEur
        else:
            gbpCurrency_puertorico_sperm = None
            eurCurrency_puertorico_sperm = None

    queryset_list_puertorico_icsi = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_puertorico_icsi.items():
        usdCurrency_puertorico_icsi = val
        if usdCurrency_puertorico_icsi is not None:
            gbpCurrency_puertorico_icsi = val * usdToGbp
            eurCurrency_puertorico_icsi = val * usdToEur
        else:
            gbpCurrency_puertorico_icsi = None
            eurCurrency_puertorico_icsi = None

    queryset_list_puertorico_iui = queryset_list_puertorico.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_puertorico_iui.items():
        usdCurrency_puertorico_iui = val
        if usdCurrency_puertorico_iui is not None:
            gbpCurrency_puertorico_iui = val * usdToGbp
            eurCurrency_puertorico_iui = val * usdToEur
        else:
            gbpCurrency_puertorico_iui = None
            eurCurrency_puertorico_iui = None

    #--------------------------------------------------------------------------
    queryset_list_southcarolina = queryset_list_us.filter(clinicRegion__iexact='South Carolina')
    my_total_count_southcarolina = queryset_list_southcarolina.count()
    queryset_list_southcarolina_ivf = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_southcarolina_ivf.items():
        usdCurrency_southcarolina_ivf = val
        if usdCurrency_southcarolina_ivf is not None:
            gbpCurrency_southcarolina_ivf = val * usdToGbp
            eurCurrency_southcarolina_ivf = val * usdToEur
        else:
            gbpCurrency_southcarolina_ivf = None
            eurCurrency_southcarolina_ivf = None

    queryset_list_southcarolina_egg = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_egg.items():
        usdCurrency_southcarolina_egg = val
        if usdCurrency_southcarolina_egg is not None:
            gbpCurrency_southcarolina_egg = val * usdToGbp
            eurCurrency_southcarolina_egg = val * usdToEur
        else:
            gbpCurrency_southcarolina_egg = None
            eurCurrency_southcarolina_egg = None

    queryset_list_southcarolina_embryo = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_embryo.items():
        usdCurrency_southcarolina_embryo = val
        if usdCurrency_southcarolina_embryo is not None:
            gbpCurrency_southcarolina_embryo = val * usdToGbp
            eurCurrency_southcarolina_embryo = val * usdToEur
        else:
            gbpCurrency_southcarolina_embryo = None
            eurCurrency_southcarolina_embryo = None

    queryset_list_southcarolina_sperm = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_sperm.items():
        usdCurrency_southcarolina_sperm = val
        if usdCurrency_southcarolina_sperm is not None:
            gbpCurrency_southcarolina_sperm = val * usdToGbp
            eurCurrency_southcarolina_sperm = val * usdToEur
        else:
            gbpCurrency_southcarolina_sperm = None
            eurCurrency_southcarolina_sperm = None

    queryset_list_southcarolina_icsi = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_southcarolina_icsi.items():
        usdCurrency_southcarolina_icsi = val
        if usdCurrency_southcarolina_icsi is not None:
            gbpCurrency_southcarolina_icsi = val * usdToGbp
            eurCurrency_southcarolina_icsi = val * usdToEur
        else:
            gbpCurrency_southcarolina_icsi = None
            eurCurrency_southcarolina_icsi = None

    queryset_list_southcarolina_iui = queryset_list_southcarolina.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_southcarolina_iui.items():
        usdCurrency_southcarolina_iui = val
        if usdCurrency_southcarolina_iui is not None:
            gbpCurrency_southcarolina_iui = val * usdToGbp
            eurCurrency_southcarolina_iui = val * usdToEur
        else:
            gbpCurrency_southcarolina_iui = None
            eurCurrency_southcarolina_iui = None

    #--------------------------------------------------------------------------
    queryset_list_rhodeisland = queryset_list_us.filter(clinicRegion__iexact='Rhode Island')
    my_total_count_rhodeisland = queryset_list_rhodeisland.count()
    queryset_list_rhodeisland_ivf = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_rhodeisland_ivf.items():
        usdCurrency_rhodeisland_ivf = val
        if usdCurrency_rhodeisland_ivf is not None:
            gbpCurrency_rhodeisland_ivf = val * usdToGbp
            eurCurrency_rhodeisland_ivf = val * usdToEur
        else:
            gbpCurrency_rhodeisland_ivf = None
            eurCurrency_rhodeisland_ivf = None

    queryset_list_rhodeisland_egg = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_egg.items():
        usdCurrency_rhodeisland_egg = val
        if usdCurrency_rhodeisland_egg is not None:
            gbpCurrency_rhodeisland_egg = val * usdToGbp
            eurCurrency_rhodeisland_egg = val * usdToEur
        else:
            gbpCurrency_rhodeisland_egg = None
            eurCurrency_rhodeisland_egg = None

    queryset_list_rhodeisland_embryo = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_embryo.items():
        usdCurrency_rhodeisland_embryo = val
        if usdCurrency_rhodeisland_embryo is not None:
            gbpCurrency_rhodeisland_embryo = val * usdToGbp
            eurCurrency_rhodeisland_embryo = val * usdToEur
        else:
            gbpCurrency_rhodeisland_embryo = None
            eurCurrency_rhodeisland_embryo = None

    queryset_list_rhodeisland_sperm = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_sperm.items():
        usdCurrency_rhodeisland_sperm = val
        if usdCurrency_rhodeisland_sperm is not None:
            gbpCurrency_rhodeisland_sperm = val * usdToGbp
            eurCurrency_rhodeisland_sperm = val * usdToEur
        else:
            gbpCurrency_rhodeisland_sperm = None
            eurCurrency_rhodeisland_sperm = None

    queryset_list_rhodeisland_icsi = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_rhodeisland_icsi.items():
        usdCurrency_rhodeisland_icsi = val
        if usdCurrency_rhodeisland_icsi is not None:
            gbpCurrency_rhodeisland_icsi = val * usdToGbp
            eurCurrency_rhodeisland_icsi = val * usdToEur
        else:
            gbpCurrency_rhodeisland_icsi = None
            eurCurrency_rhodeisland_icsi = None

    queryset_list_rhodeisland_iui = queryset_list_rhodeisland.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_rhodeisland_iui.items():
        usdCurrency_rhodeisland_iui = val
        if usdCurrency_rhodeisland_iui is not None:
            gbpCurrency_rhodeisland_iui = val * usdToGbp
            eurCurrency_rhodeisland_iui = val * usdToEur
        else:
            gbpCurrency_rhodeisland_iui = None
            eurCurrency_rhodeisland_iui = None

    #--------------------------------------------------------------------------
    queryset_list_southdakota = queryset_list_us.filter(clinicRegion__iexact='South Dakota')
    my_total_count_southdakota = queryset_list_southdakota.count()
    queryset_list_southdakota_ivf = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_southdakota_ivf.items():
        usdCurrency_southdakota_ivf = val
        if usdCurrency_southdakota_ivf is not None:
            gbpCurrency_southdakota_ivf = val * usdToGbp
            eurCurrency_southdakota_ivf = val * usdToEur
        else:
            gbpCurrency_southdakota_ivf = None
            eurCurrency_southdakota_ivf = None

    queryset_list_southdakota_egg = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_egg.items():
        usdCurrency_southdakota_egg = val
        if usdCurrency_southdakota_egg is not None:
            gbpCurrency_southdakota_egg = val * usdToGbp
            eurCurrency_southdakota_egg = val * usdToEur
        else:
            gbpCurrency_southdakota_egg = None
            eurCurrency_southdakota_egg = None

    queryset_list_southdakota_embryo = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_embryo.items():
        usdCurrency_southdakota_embryo = val
        if usdCurrency_southdakota_embryo is not None:
            gbpCurrency_southdakota_embryo = val * usdToGbp
            eurCurrency_southdakota_embryo = val * usdToEur
        else:
            gbpCurrency_southdakota_embryo = None
            eurCurrency_southdakota_embryo = None

    queryset_list_southdakota_sperm = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_sperm.items():
        usdCurrency_southdakota_sperm = val
        if usdCurrency_southdakota_sperm is not None:
            gbpCurrency_southdakota_sperm = val * usdToGbp
            eurCurrency_southdakota_sperm = val * usdToEur
        else:
            gbpCurrency_southdakota_sperm = None
            eurCurrency_southdakota_sperm = None

    queryset_list_southdakota_icsi = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_southdakota_icsi.items():
        usdCurrency_southdakota_icsi = val
        if usdCurrency_southdakota_icsi is not None:
            gbpCurrency_southdakota_icsi = val * usdToGbp
            eurCurrency_southdakota_icsi = val * usdToEur
        else:
            gbpCurrency_southdakota_icsi = None
            eurCurrency_southdakota_icsi = None

    queryset_list_southdakota_iui = queryset_list_southdakota.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_southdakota_iui.items():
        usdCurrency_southdakota_iui = val
        if usdCurrency_southdakota_iui is not None:
            gbpCurrency_southdakota_iui = val * usdToGbp
            eurCurrency_southdakota_iui = val * usdToEur
        else:
            gbpCurrency_southdakota_iui = None
            eurCurrency_southdakota_iui = None

    #--------------------------------------------------------------------------
    queryset_list_tennessee = queryset_list_us.filter(clinicRegion__iexact='Tennessee')
    my_total_count_tennessee = queryset_list_tennessee.count()
    queryset_list_tennessee_ivf = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_tennessee_ivf.items():
        usdCurrency_tennessee_ivf = val
        if usdCurrency_tennessee_ivf is not None:
            gbpCurrency_tennessee_ivf = val * usdToGbp
            eurCurrency_tennessee_ivf = val * usdToEur
        else:
            gbpCurrency_tennessee_ivf = None
            eurCurrency_tennessee_ivf = None

    queryset_list_tennessee_egg = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_egg.items():
        usdCurrency_tennessee_egg = val
        if usdCurrency_tennessee_egg is not None:
            gbpCurrency_tennessee_egg = val * usdToGbp
            eurCurrency_tennessee_egg = val * usdToEur
        else:
            gbpCurrency_tennessee_egg = None
            eurCurrency_tennessee_egg = None

    queryset_list_tennessee_embryo = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_embryo.items():
        usdCurrency_tennessee_embryo = val
        if usdCurrency_tennessee_embryo is not None:
            gbpCurrency_tennessee_embryo = val * usdToGbp
            eurCurrency_tennessee_embryo = val * usdToEur
        else:
            gbpCurrency_tennessee_embryo = None
            eurCurrency_tennessee_embryo = None

    queryset_list_tennessee_sperm = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_sperm.items():
        usdCurrency_tennessee_sperm = val
        if usdCurrency_tennessee_sperm is not None:
            gbpCurrency_tennessee_sperm = val * usdToGbp
            eurCurrency_tennessee_sperm = val * usdToEur
        else:
            gbpCurrency_tennessee_sperm = None
            eurCurrency_tennessee_sperm = None

    queryset_list_tennessee_icsi = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_tennessee_icsi.items():
        usdCurrency_tennessee_icsi = val
        if usdCurrency_tennessee_icsi is not None:
            gbpCurrency_tennessee_icsi = val * usdToGbp
            eurCurrency_tennessee_icsi = val * usdToEur
        else:
            gbpCurrency_tennessee_icsi = None
            eurCurrency_tennessee_icsi = None

    queryset_list_tennessee_iui = queryset_list_tennessee.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_tennessee_iui.items():
        usdCurrency_tennessee_iui = val
        if usdCurrency_tennessee_iui is not None:
            gbpCurrency_tennessee_iui = val * usdToGbp
            eurCurrency_tennessee_iui = val * usdToEur
        else:
            gbpCurrency_tennessee_iui = None
            eurCurrency_tennessee_iui = None

    #--------------------------------------------------------------------------
    queryset_list_texas = queryset_list_us.filter(clinicRegion__iexact='Texas')
    my_total_count_texas = queryset_list_texas.count()
    queryset_list_texas_ivf = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_texas_ivf.items():
        usdCurrency_texas_ivf = val
        if usdCurrency_texas_ivf is not None:
            gbpCurrency_texas_ivf = val * usdToGbp
            eurCurrency_texas_ivf = val * usdToEur
        else:
            gbpCurrency_texas_ivf = None
            eurCurrency_texas_ivf = None

    queryset_list_texas_egg = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_texas_egg.items():
        usdCurrency_texas_egg = val
        if usdCurrency_texas_egg is not None:
            gbpCurrency_texas_egg = val * usdToGbp
            eurCurrency_texas_egg = val * usdToEur
        else:
            gbpCurrency_texas_egg = None
            eurCurrency_texas_egg = None

    queryset_list_texas_embryo = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_texas_embryo.items():
        usdCurrency_texas_embryo = val
        if usdCurrency_texas_embryo is not None:
            gbpCurrency_texas_embryo = val * usdToGbp
            eurCurrency_texas_embryo = val * usdToEur
        else:
            gbpCurrency_texas_embryo = None
            eurCurrency_texas_embryo = None

    queryset_list_texas_sperm = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_texas_sperm.items():
        usdCurrency_texas_sperm = val
        if usdCurrency_texas_sperm is not None:
            gbpCurrency_texas_sperm = val * usdToGbp
            eurCurrency_texas_sperm = val * usdToEur
        else:
            gbpCurrency_texas_sperm = None
            eurCurrency_texas_sperm = None

    queryset_list_texas_icsi = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_texas_icsi.items():
        usdCurrency_texas_icsi = val
        if usdCurrency_texas_icsi is not None:
            gbpCurrency_texas_icsi = val * usdToGbp
            eurCurrency_texas_icsi = val * usdToEur
        else:
            gbpCurrency_texas_icsi = None
            eurCurrency_texas_icsi = None

    queryset_list_texas_iui = queryset_list_texas.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_texas_iui.items():
        usdCurrency_texas_iui = val
        if usdCurrency_texas_iui is not None:
            gbpCurrency_texas_iui = val * usdToGbp
            eurCurrency_texas_iui = val * usdToEur
        else:
            gbpCurrency_texas_iui = None
            eurCurrency_texas_iui = None

    #--------------------------------------------------------------------------
    queryset_list_utah = queryset_list_us.filter(clinicRegion__iexact='Utah')
    my_total_count_utah = queryset_list_utah.count()
    queryset_list_utah_ivf = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_utah_ivf.items():
        usdCurrency_utah_ivf = val
        if usdCurrency_utah_ivf is not None:
            gbpCurrency_utah_ivf = val * usdToGbp
            eurCurrency_utah_ivf = val * usdToEur
        else:
            gbpCurrency_utah_ivf = None
            eurCurrency_utah_ivf = None

    queryset_list_utah_egg = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_utah_egg.items():
        usdCurrency_utah_egg = val
        if usdCurrency_utah_egg is not None:
            gbpCurrency_utah_egg = val * usdToGbp
            eurCurrency_utah_egg = val * usdToEur
        else:
            gbpCurrency_utah_egg = None
            eurCurrency_utah_egg = None

    queryset_list_utah_embryo = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_utah_embryo.items():
        usdCurrency_utah_embryo = val
        if usdCurrency_utah_embryo is not None:
            gbpCurrency_utah_embryo = val * usdToGbp
            eurCurrency_utah_embryo = val * usdToEur
        else:
            gbpCurrency_utah_embryo = None
            eurCurrency_utah_embryo = None

    queryset_list_utah_sperm = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_utah_sperm.items():
        usdCurrency_utah_sperm = val
        if usdCurrency_utah_sperm is not None:
            gbpCurrency_utah_sperm = val * usdToGbp
            eurCurrency_utah_sperm = val * usdToEur
        else:
            gbpCurrency_utah_sperm = None
            eurCurrency_utah_sperm = None

    queryset_list_utah_icsi = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_utah_icsi.items():
        usdCurrency_utah_icsi = val
        if usdCurrency_utah_icsi is not None:
            gbpCurrency_utah_icsi = val * usdToGbp
            eurCurrency_utah_icsi = val * usdToEur
        else:
            gbpCurrency_utah_icsi = None
            eurCurrency_utah_icsi = None

    queryset_list_utah_iui = queryset_list_utah.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_utah_iui.items():
        usdCurrency_utah_iui = val
        if usdCurrency_utah_iui is not None:
            gbpCurrency_utah_iui = val * usdToGbp
            eurCurrency_utah_iui = val * usdToEur
        else:
            gbpCurrency_utah_iui = None
            eurCurrency_utah_iui = None

    #--------------------------------------------------------------------------
    queryset_list_vermont = queryset_list_us.filter(clinicRegion__iexact='Vermont')
    my_total_count_vermont = queryset_list_vermont.count()
    queryset_list_vermont_ivf = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_vermont_ivf.items():
        usdCurrency_vermont_ivf = val
        if usdCurrency_vermont_ivf is not None:
            gbpCurrency_vermont_ivf = val * usdToGbp
            eurCurrency_vermont_ivf = val * usdToEur
        else:
            gbpCurrency_vermont_ivf = None
            eurCurrency_vermont_ivf = None

    queryset_list_vermont_egg = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_vermont_egg.items():
        usdCurrency_vermont_egg = val
        if usdCurrency_vermont_egg is not None:
            gbpCurrency_vermont_egg = val * usdToGbp
            eurCurrency_vermont_egg = val * usdToEur
        else:
            gbpCurrency_vermont_egg = None
            eurCurrency_vermont_egg = None

    queryset_list_vermont_embryo = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_vermont_embryo.items():
        usdCurrency_vermont_embryo = val
        if usdCurrency_vermont_embryo is not None:
            gbpCurrency_vermont_embryo = val * usdToGbp
            eurCurrency_vermont_embryo = val * usdToEur
        else:
            gbpCurrency_vermont_embryo = None
            eurCurrency_vermont_embryo = None

    queryset_list_vermont_sperm = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_vermont_sperm.items():
        usdCurrency_vermont_sperm = val
        if usdCurrency_vermont_sperm is not None:
            gbpCurrency_vermont_sperm = val * usdToGbp
            eurCurrency_vermont_sperm = val * usdToEur
        else:
            gbpCurrency_vermont_sperm = None
            eurCurrency_vermont_sperm = None

    queryset_list_vermont_icsi = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_vermont_icsi.items():
        usdCurrency_vermont_icsi = val
        if usdCurrency_vermont_icsi is not None:
            gbpCurrency_vermont_icsi = val * usdToGbp
            eurCurrency_vermont_icsi = val * usdToEur
        else:
            gbpCurrency_vermont_icsi = None
            eurCurrency_vermont_icsi = None

    queryset_list_vermont_iui = queryset_list_vermont.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_vermont_iui.items():
        usdCurrency_vermont_iui = val
        if usdCurrency_vermont_iui is not None:
            gbpCurrency_vermont_iui = val * usdToGbp
            eurCurrency_vermont_iui = val * usdToEur
        else:
            gbpCurrency_vermont_iui = None
            eurCurrency_vermont_iui = None

    #--------------------------------------------------------------------------
    queryset_list_virginia = queryset_list_us.filter(clinicRegion__iexact='Virginia')
    my_total_count_virginia = queryset_list_virginia.count()
    queryset_list_virginia_ivf = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_virginia_ivf.items():
        usdCurrency_virginia_ivf = val
        if usdCurrency_virginia_ivf is not None:
            gbpCurrency_virginia_ivf = val * usdToGbp
            eurCurrency_virginia_ivf = val * usdToEur
        else:
            gbpCurrency_virginia_ivf = None
            eurCurrency_virginia_ivf = None

    queryset_list_virginia_egg = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_virginia_egg.items():
        usdCurrency_virginia_egg = val
        if usdCurrency_virginia_egg is not None:
            gbpCurrency_virginia_egg = val * usdToGbp
            eurCurrency_virginia_egg = val * usdToEur
        else:
            gbpCurrency_virginia_egg = None
            eurCurrency_virginia_egg = None

    queryset_list_virginia_embryo = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_virginia_embryo.items():
        usdCurrency_virginia_embryo = val
        if usdCurrency_virginia_embryo is not None:
            gbpCurrency_virginia_embryo = val * usdToGbp
            eurCurrency_virginia_embryo = val * usdToEur
        else:
            gbpCurrency_virginia_embryo = None
            eurCurrency_virginia_embryo = None

    queryset_list_virginia_sperm = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_virginia_sperm.items():
        usdCurrency_virginia_sperm = val
        if usdCurrency_virginia_sperm is not None:
            gbpCurrency_virginia_sperm = val * usdToGbp
            eurCurrency_virginia_sperm = val * usdToEur
        else:
            gbpCurrency_virginia_sperm = None
            eurCurrency_virginia_sperm = None

    queryset_list_virginia_icsi = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_virginia_icsi.items():
        usdCurrency_virginia_icsi = val
        if usdCurrency_virginia_icsi is not None:
            gbpCurrency_virginia_icsi = val * usdToGbp
            eurCurrency_virginia_icsi = val * usdToEur
        else:
            gbpCurrency_virginia_icsi = None
            eurCurrency_virginia_icsi = None

    queryset_list_virginia_iui = queryset_list_virginia.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_virginia_iui.items():
        usdCurrency_virginia_iui = val
        if usdCurrency_virginia_iui is not None:
            gbpCurrency_virginia_iui = val * usdToGbp
            eurCurrency_virginia_iui = val * usdToEur
        else:
            gbpCurrency_virginia_iui = None
            eurCurrency_virginia_iui = None

    #--------------------------------------------------------------------------
    queryset_list_washington = queryset_list_us.filter(clinicRegion__iexact='Washington')
    my_total_count_washington = queryset_list_washington.count()
    queryset_list_washington_ivf = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_washington_ivf.items():
        usdCurrency_washington_ivf = val
        if usdCurrency_washington_ivf is not None:
            gbpCurrency_washington_ivf = val * usdToGbp
            eurCurrency_washington_ivf = val * usdToEur
        else:
            gbpCurrency_washington_ivf = None
            eurCurrency_washington_ivf = None

    queryset_list_washington_egg = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_washington_egg.items():
        usdCurrency_washington_egg = val
        if usdCurrency_washington_egg is not None:
            gbpCurrency_washington_egg = val * usdToGbp
            eurCurrency_washington_egg = val * usdToEur
        else:
            gbpCurrency_washington_egg = None
            eurCurrency_washington_egg = None

    queryset_list_washington_embryo = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_washington_embryo.items():
        usdCurrency_washington_embryo = val
        if usdCurrency_washington_embryo is not None:
            gbpCurrency_washington_embryo = val * usdToGbp
            eurCurrency_washington_embryo = val * usdToEur
        else:
            gbpCurrency_washington_embryo = None
            eurCurrency_washington_embryo = None

    queryset_list_washington_sperm = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_washington_sperm.items():
        usdCurrency_washington_sperm = val
        if usdCurrency_washington_sperm is not None:
            gbpCurrency_washington_sperm = val * usdToGbp
            eurCurrency_washington_sperm = val * usdToEur
        else:
            gbpCurrency_washington_sperm = None
            eurCurrency_washington_sperm = None

    queryset_list_washington_icsi = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_washington_icsi.items():
        usdCurrency_washington_icsi = val
        if usdCurrency_washington_icsi is not None:
            gbpCurrency_washington_icsi = val * usdToGbp
            eurCurrency_washington_icsi = val * usdToEur
        else:
            gbpCurrency_washington_icsi = None
            eurCurrency_washington_icsi = None

    queryset_list_washington_iui = queryset_list_washington.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_washington_iui.items():
        usdCurrency_washington_iui = val
        if usdCurrency_washington_iui is not None:
            gbpCurrency_washington_iui = val * usdToGbp
            eurCurrency_washington_iui = val * usdToEur
        else:
            gbpCurrency_washington_iui = None
            eurCurrency_washington_iui = None

    #--------------------------------------------------------------------------
    queryset_list_westvirginia = queryset_list_us.filter(clinicRegion__iexact='West Virginia')
    my_total_count_westvirginia = queryset_list_westvirginia.count()
    queryset_list_westvirginia_ivf = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_westvirginia_ivf.items():
        usdCurrency_westvirginia_ivf = val
        if usdCurrency_westvirginia_ivf is not None:
            gbpCurrency_westvirginia_ivf = val * usdToGbp
            eurCurrency_westvirginia_ivf = val * usdToEur
        else:
            gbpCurrency_westvirginia_ivf = None
            eurCurrency_westvirginia_ivf = None

    queryset_list_westvirginia_egg = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_egg.items():
        usdCurrency_westvirginia_egg = val
        if usdCurrency_westvirginia_egg is not None:
            gbpCurrency_westvirginia_egg = val * usdToGbp
            eurCurrency_westvirginia_egg = val * usdToEur
        else:
            gbpCurrency_westvirginia_egg = None
            eurCurrency_westvirginia_egg = None

    queryset_list_westvirginia_embryo = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_embryo.items():
        usdCurrency_westvirginia_embryo = val
        if usdCurrency_westvirginia_embryo is not None:
            gbpCurrency_westvirginia_embryo = val * usdToGbp
            eurCurrency_westvirginia_embryo = val * usdToEur
        else:
            gbpCurrency_westvirginia_embryo = None
            eurCurrency_westvirginia_embryo = None

    queryset_list_westvirginia_sperm = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_sperm.items():
        usdCurrency_westvirginia_sperm = val
        if usdCurrency_westvirginia_sperm is not None:
            gbpCurrency_westvirginia_sperm = val * usdToGbp
            eurCurrency_westvirginia_sperm = val * usdToEur
        else:
            gbpCurrency_westvirginia_sperm = None
            eurCurrency_westvirginia_sperm = None

    queryset_list_westvirginia_icsi = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_westvirginia_icsi.items():
        usdCurrency_westvirginia_icsi = val
        if usdCurrency_westvirginia_icsi is not None:
            gbpCurrency_westvirginia_icsi = val * usdToGbp
            eurCurrency_westvirginia_icsi = val * usdToEur
        else:
            gbpCurrency_westvirginia_icsi = None
            eurCurrency_westvirginia_icsi = None

    queryset_list_westvirginia_iui = queryset_list_westvirginia.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_westvirginia_iui.items():
        usdCurrency_westvirginia_iui = val
        if usdCurrency_westvirginia_iui is not None:
            gbpCurrency_westvirginia_iui = val * usdToGbp
            eurCurrency_westvirginia_iui = val * usdToEur
        else:
            gbpCurrency_westvirginia_iui = None
            eurCurrency_westvirginia_iui = None

    #--------------------------------------------------------------------------
    queryset_list_wisconsin = queryset_list_us.filter(clinicRegion__iexact='Wisconsin')
    my_total_count_wisconsin = queryset_list_wisconsin.count()
    queryset_list_wisconsin_ivf = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_wisconsin_ivf.items():
        usdCurrency_wisconsin_ivf = val
        if usdCurrency_wisconsin_ivf is not None:
            gbpCurrency_wisconsin_ivf = val * usdToGbp
            eurCurrency_wisconsin_ivf = val * usdToEur
        else:
            gbpCurrency_wisconsin_ivf = None
            eurCurrency_wisconsin_ivf = None

    queryset_list_wisconsin_egg = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_egg.items():
        usdCurrency_wisconsin_egg = val
        if usdCurrency_wisconsin_egg is not None:
            gbpCurrency_wisconsin_egg = val * usdToGbp
            eurCurrency_wisconsin_egg = val * usdToEur
        else:
            gbpCurrency_wisconsin_egg = None
            eurCurrency_wisconsin_egg = None

    queryset_list_wisconsin_embryo = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_embryo.items():
        usdCurrency_wisconsin_embryo = val
        if usdCurrency_wisconsin_embryo is not None:
            gbpCurrency_wisconsin_embryo = val * usdToGbp
            eurCurrency_wisconsin_embryo = val * usdToEur
        else:
            gbpCurrency_wisconsin_embryo = None
            eurCurrency_wisconsin_embryo = None

    queryset_list_wisconsin_sperm = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_sperm.items():
        usdCurrency_wisconsin_sperm = val
        if usdCurrency_wisconsin_sperm is not None:
            gbpCurrency_wisconsin_sperm = val * usdToGbp
            eurCurrency_wisconsin_sperm = val * usdToEur
        else:
            gbpCurrency_wisconsin_sperm = None
            eurCurrency_wisconsin_sperm = None

    queryset_list_wisconsin_icsi = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_wisconsin_icsi.items():
        usdCurrency_wisconsin_icsi = val
        if usdCurrency_wisconsin_icsi is not None:
            gbpCurrency_wisconsin_icsi = val * usdToGbp
            eurCurrency_wisconsin_icsi = val * usdToEur
        else:
            gbpCurrency_wisconsin_icsi = None
            eurCurrency_wisconsin_icsi = None

    queryset_list_wisconsin_iui = queryset_list_wisconsin.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_wisconsin_iui.items():
        usdCurrency_wisconsin_iui = val
        if usdCurrency_wisconsin_iui is not None:
            gbpCurrency_wisconsin_iui = val * usdToGbp
            eurCurrency_wisconsin_iui = val * usdToEur
        else:
            gbpCurrency_wisconsin_iui = None
            eurCurrency_wisconsin_iui = None

    #--------------------------------------------------------------------------
    queryset_list_wyoming = queryset_list_us.filter(clinicRegion__iexact='Wyoming')
    my_total_count_wyoming = queryset_list_wyoming.count()
    queryset_list_wyoming_ivf = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_wyoming_ivf.items():
        usdCurrency_wyoming_ivf = val
        if usdCurrency_wyoming_ivf is not None:
            gbpCurrency_wyoming_ivf = val * usdToGbp
            eurCurrency_wyoming_ivf = val * usdToEur
        else:
            gbpCurrency_wyoming_ivf = None
            eurCurrency_wyoming_ivf = None

    queryset_list_wyoming_egg = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_egg.items():
        usdCurrency_wyoming_egg = val
        if usdCurrency_wyoming_egg is not None:
            gbpCurrency_wyoming_egg = val * usdToGbp
            eurCurrency_wyoming_egg = val * usdToEur
        else:
            gbpCurrency_wyoming_egg = None
            eurCurrency_wyoming_egg = None

    queryset_list_wyoming_embryo = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_embryo.items():
        usdCurrency_wyoming_embryo = val
        if usdCurrency_wyoming_embryo is not None:
            gbpCurrency_wyoming_embryo = val * usdToGbp
            eurCurrency_wyoming_embryo = val * usdToEur
        else:
            gbpCurrency_wyoming_embryo = None
            eurCurrency_wyoming_embryo = None

    queryset_list_wyoming_sperm = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_sperm.items():
        usdCurrency_wyoming_sperm = val
        if usdCurrency_wyoming_sperm is not None:
            gbpCurrency_wyoming_sperm = val * usdToGbp
            eurCurrency_wyoming_sperm = val * usdToEur
        else:
            gbpCurrency_wyoming_sperm = None
            eurCurrency_wyoming_sperm = None

    queryset_list_wyoming_icsi = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_wyoming_icsi.items():
        usdCurrency_wyoming_icsi = val
        if usdCurrency_wyoming_icsi is not None:
            gbpCurrency_wyoming_icsi = val * usdToGbp
            eurCurrency_wyoming_icsi = val * usdToEur
        else:
            gbpCurrency_wyoming_icsi = None
            eurCurrency_wyoming_icsi = None

    queryset_list_wyoming_iui = queryset_list_wyoming.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_wyoming_iui.items():
        usdCurrency_wyoming_iui = val
        if usdCurrency_wyoming_iui is not None:
            gbpCurrency_wyoming_iui = val * usdToGbp
            eurCurrency_wyoming_iui = val * usdToEur
        else:
            gbpCurrency_wyoming_iui = None
            eurCurrency_wyoming_iui = None

    #--------------------------------------------------------------------------
    queryset_list_districtofcolumbia = queryset_list_us.filter(clinicRegion__iexact='District of Columbia')
    my_total_count_districtofcolumbia = queryset_list_districtofcolumbia.count()
    queryset_list_districtofcolumbia_ivf = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_ivf.items():
        usdCurrency_districtofcolumbia_ivf = val
        if usdCurrency_districtofcolumbia_ivf is not None:
            gbpCurrency_districtofcolumbia_ivf = val * usdToGbp
            eurCurrency_districtofcolumbia_ivf = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_ivf = None
            eurCurrency_districtofcolumbia_ivf = None

    queryset_list_districtofcolumbia_egg = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_egg.items():
        usdCurrency_districtofcolumbia_egg = val
        if usdCurrency_districtofcolumbia_egg is not None:
            gbpCurrency_districtofcolumbia_egg = val * usdToGbp
            eurCurrency_districtofcolumbia_egg = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_egg = None
            eurCurrency_districtofcolumbia_egg = None

    queryset_list_districtofcolumbia_embryo = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_embryo.items():
        usdCurrency_districtofcolumbia_embryo = val
        if usdCurrency_districtofcolumbia_embryo is not None:
            gbpCurrency_districtofcolumbia_embryo = val * usdToGbp
            eurCurrency_districtofcolumbia_embryo = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_embryo = None
            eurCurrency_districtofcolumbia_embryo = None

    queryset_list_districtofcolumbia_sperm = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_sperm.items():
        usdCurrency_districtofcolumbia_sperm = val
        if usdCurrency_districtofcolumbia_sperm is not None:
            gbpCurrency_districtofcolumbia_sperm = val * usdToGbp
            eurCurrency_districtofcolumbia_sperm = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_sperm = None
            eurCurrency_districtofcolumbia_sperm = None

    queryset_list_districtofcolumbia_icsi = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_icsi.items():
        usdCurrency_districtofcolumbia_icsi = val
        if usdCurrency_districtofcolumbia_icsi is not None:
            gbpCurrency_districtofcolumbia_icsi = val * usdToGbp
            eurCurrency_districtofcolumbia_icsi = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_icsi = None
            eurCurrency_districtofcolumbia_icsi = None

    queryset_list_districtofcolumbia_iui = queryset_list_districtofcolumbia.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_iui.items():
        usdCurrency_districtofcolumbia_iui = val
        if usdCurrency_districtofcolumbia_iui is not None:
            gbpCurrency_districtofcolumbia_iui = val * usdToGbp
            eurCurrency_districtofcolumbia_iui = val * usdToEur
        else:
            gbpCurrency_districtofcolumbia_iui = None
            eurCurrency_districtofcolumbia_iui = None

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

        'gbpCurrency_arizona_ivf': gbpCurrency_arizona_ivf,
        'usdCurrency_arizona_ivf': usdCurrency_arizona_ivf,
        'eurCurrency_arizona_ivf': eurCurrency_arizona_ivf,
        'gbpCurrency_arizona_egg': gbpCurrency_arizona_egg,
        'usdCurrency_arizona_egg': usdCurrency_arizona_egg,
        'eurCurrency_arizona_egg': eurCurrency_arizona_egg,
        'gbpCurrency_arizona_embryo': gbpCurrency_arizona_embryo,
        'usdCurrency_arizona_embryo': usdCurrency_arizona_embryo,
        'eurCurrency_arizona_embryo': eurCurrency_arizona_embryo,
        'gbpCurrency_arizona_sperm': gbpCurrency_arizona_sperm,
        'usdCurrency_arizona_sperm': usdCurrency_arizona_sperm,
        'eurCurrency_arizona_sperm': eurCurrency_arizona_sperm,
        'gbpCurrency_arizona_icsi': gbpCurrency_arizona_icsi,
        'usdCurrency_arizona_icsi': usdCurrency_arizona_icsi,
        'eurCurrency_arizona_icsi': eurCurrency_arizona_icsi,
        'gbpCurrency_arizona_iui': gbpCurrency_arizona_iui,
        'usdCurrency_arizona_iui': usdCurrency_arizona_iui,
        'eurCurrency_arizona_iui': eurCurrency_arizona_iui,

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

        'gbpCurrency_montana_ivf': gbpCurrency_montana_ivf,
        'usdCurrency_montana_ivf': usdCurrency_montana_ivf,
        'eurCurrency_montana_ivf': eurCurrency_montana_ivf,
        'gbpCurrency_montana_egg': gbpCurrency_montana_egg,
        'usdCurrency_montana_egg': usdCurrency_montana_egg,
        'eurCurrency_montana_egg': eurCurrency_montana_egg,
        'gbpCurrency_montana_embryo': gbpCurrency_montana_embryo,
        'usdCurrency_montana_embryo': usdCurrency_montana_embryo,
        'eurCurrency_montana_embryo': eurCurrency_montana_embryo,
        'gbpCurrency_montana_sperm': gbpCurrency_montana_sperm,
        'usdCurrency_montana_sperm': usdCurrency_montana_sperm,
        'eurCurrency_montana_sperm': eurCurrency_montana_sperm,
        'gbpCurrency_montana_icsi': gbpCurrency_montana_icsi,
        'usdCurrency_montana_icsi': usdCurrency_montana_icsi,
        'eurCurrency_montana_icsi': eurCurrency_montana_icsi,
        'gbpCurrency_montana_iui': gbpCurrency_montana_iui,
        'usdCurrency_montana_iui': usdCurrency_montana_iui,
        'eurCurrency_montana_iui': eurCurrency_montana_iui,

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

        'gbpCurrency_northcarolina_ivf': gbpCurrency_northcarolina_ivf,
        'usdCurrency_northcarolina_ivf': usdCurrency_northcarolina_ivf,
        'eurCurrency_northcarolina_ivf': eurCurrency_northcarolina_ivf,
        'gbpCurrency_northcarolina_egg': gbpCurrency_northcarolina_egg,
        'usdCurrency_northcarolina_egg': usdCurrency_northcarolina_egg,
        'eurCurrency_northcarolina_egg': eurCurrency_northcarolina_egg,
        'gbpCurrency_northcarolina_embryo': gbpCurrency_northcarolina_embryo,
        'usdCurrency_northcarolina_embryo': usdCurrency_northcarolina_embryo,
        'eurCurrency_northcarolina_embryo': eurCurrency_northcarolina_embryo,
        'gbpCurrency_northcarolina_sperm': gbpCurrency_northcarolina_sperm,
        'usdCurrency_northcarolina_sperm': usdCurrency_northcarolina_sperm,
        'eurCurrency_northcarolina_sperm': eurCurrency_northcarolina_sperm,
        'gbpCurrency_northcarolina_icsi': gbpCurrency_northcarolina_icsi,
        'usdCurrency_northcarolina_icsi': usdCurrency_northcarolina_icsi,
        'eurCurrency_northcarolina_icsi': eurCurrency_northcarolina_icsi,
        'gbpCurrency_northcarolina_iui': gbpCurrency_northcarolina_iui,
        'usdCurrency_northcarolina_iui': usdCurrency_northcarolina_iui,
        'eurCurrency_northcarolina_iui': eurCurrency_northcarolina_iui,

        'gbpCurrency_northdakota_ivf': gbpCurrency_northdakota_ivf,
        'usdCurrency_northdakota_ivf': usdCurrency_northdakota_ivf,
        'eurCurrency_northdakota_ivf': eurCurrency_northdakota_ivf,
        'gbpCurrency_northdakota_egg': gbpCurrency_northdakota_egg,
        'usdCurrency_northdakota_egg': usdCurrency_northdakota_egg,
        'eurCurrency_northdakota_egg': eurCurrency_northdakota_egg,
        'gbpCurrency_northdakota_embryo': gbpCurrency_northdakota_embryo,
        'usdCurrency_northdakota_embryo': usdCurrency_northdakota_embryo,
        'eurCurrency_northdakota_embryo': eurCurrency_northdakota_embryo,
        'gbpCurrency_northdakota_sperm': gbpCurrency_northdakota_sperm,
        'usdCurrency_northdakota_sperm': usdCurrency_northdakota_sperm,
        'eurCurrency_northdakota_sperm': eurCurrency_northdakota_sperm,
        'gbpCurrency_northdakota_icsi': gbpCurrency_northdakota_icsi,
        'usdCurrency_northdakota_icsi': usdCurrency_northdakota_icsi,
        'eurCurrency_northdakota_icsi': eurCurrency_northdakota_icsi,
        'gbpCurrency_northdakota_iui': gbpCurrency_northdakota_iui,
        'usdCurrency_northdakota_iui': usdCurrency_northdakota_iui,
        'eurCurrency_northdakota_iui': eurCurrency_northdakota_iui,

        'gbpCurrency_nevada_ivf': gbpCurrency_nevada_ivf,
        'usdCurrency_nevada_ivf': usdCurrency_nevada_ivf,
        'eurCurrency_nevada_ivf': eurCurrency_nevada_ivf,
        'gbpCurrency_nevada_egg': gbpCurrency_nevada_egg,
        'usdCurrency_nevada_egg': usdCurrency_nevada_egg,
        'eurCurrency_nevada_egg': eurCurrency_nevada_egg,
        'gbpCurrency_nevada_embryo': gbpCurrency_nevada_embryo,
        'usdCurrency_nevada_embryo': usdCurrency_nevada_embryo,
        'eurCurrency_nevada_embryo': eurCurrency_nevada_embryo,
        'gbpCurrency_nevada_sperm': gbpCurrency_nevada_sperm,
        'usdCurrency_nevada_sperm': usdCurrency_nevada_sperm,
        'eurCurrency_nevada_sperm': eurCurrency_nevada_sperm,
        'gbpCurrency_nevada_icsi': gbpCurrency_nevada_icsi,
        'usdCurrency_nevada_icsi': usdCurrency_nevada_icsi,
        'eurCurrency_nevada_icsi': eurCurrency_nevada_icsi,
        'gbpCurrency_nevada_iui': gbpCurrency_nevada_iui,
        'usdCurrency_nevada_iui': usdCurrency_nevada_iui,
        'eurCurrency_nevada_iui': eurCurrency_nevada_iui,

        'gbpCurrency_ohio_ivf': gbpCurrency_ohio_ivf,
        'usdCurrency_ohio_ivf': usdCurrency_ohio_ivf,
        'eurCurrency_ohio_ivf': eurCurrency_ohio_ivf,
        'gbpCurrency_ohio_egg': gbpCurrency_ohio_egg,
        'usdCurrency_ohio_egg': usdCurrency_ohio_egg,
        'eurCurrency_ohio_egg': eurCurrency_ohio_egg,
        'gbpCurrency_ohio_embryo': gbpCurrency_ohio_embryo,
        'usdCurrency_ohio_embryo': usdCurrency_ohio_embryo,
        'eurCurrency_ohio_embryo': eurCurrency_ohio_embryo,
        'gbpCurrency_ohio_sperm': gbpCurrency_ohio_sperm,
        'usdCurrency_ohio_sperm': usdCurrency_ohio_sperm,
        'eurCurrency_ohio_sperm': eurCurrency_ohio_sperm,
        'gbpCurrency_ohio_icsi': gbpCurrency_ohio_icsi,
        'usdCurrency_ohio_icsi': usdCurrency_ohio_icsi,
        'eurCurrency_ohio_icsi': eurCurrency_ohio_icsi,
        'gbpCurrency_ohio_iui': gbpCurrency_ohio_iui,
        'usdCurrency_ohio_iui': usdCurrency_ohio_iui,
        'eurCurrency_ohio_iui': eurCurrency_ohio_iui,

        'gbpCurrency_oklahoma_ivf': gbpCurrency_oklahoma_ivf,
        'usdCurrency_oklahoma_ivf': usdCurrency_oklahoma_ivf,
        'eurCurrency_oklahoma_ivf': eurCurrency_oklahoma_ivf,
        'gbpCurrency_oklahoma_egg': gbpCurrency_oklahoma_egg,
        'usdCurrency_oklahoma_egg': usdCurrency_oklahoma_egg,
        'eurCurrency_oklahoma_egg': eurCurrency_oklahoma_egg,
        'gbpCurrency_oklahoma_embryo': gbpCurrency_oklahoma_embryo,
        'usdCurrency_oklahoma_embryo': usdCurrency_oklahoma_embryo,
        'eurCurrency_oklahoma_embryo': eurCurrency_oklahoma_embryo,
        'gbpCurrency_oklahoma_sperm': gbpCurrency_oklahoma_sperm,
        'usdCurrency_oklahoma_sperm': usdCurrency_oklahoma_sperm,
        'eurCurrency_oklahoma_sperm': eurCurrency_oklahoma_sperm,
        'gbpCurrency_oklahoma_icsi': gbpCurrency_oklahoma_icsi,
        'usdCurrency_oklahoma_icsi': usdCurrency_oklahoma_icsi,
        'eurCurrency_oklahoma_icsi': eurCurrency_oklahoma_icsi,
        'gbpCurrency_oklahoma_iui': gbpCurrency_oklahoma_iui,
        'usdCurrency_oklahoma_iui': usdCurrency_oklahoma_iui,
        'eurCurrency_oklahoma_iui': eurCurrency_oklahoma_iui,

        'gbpCurrency_oregon_ivf': gbpCurrency_oregon_ivf,
        'usdCurrency_oregon_ivf': usdCurrency_oregon_ivf,
        'eurCurrency_oregon_ivf': eurCurrency_oregon_ivf,
        'gbpCurrency_oregon_egg': gbpCurrency_oregon_egg,
        'usdCurrency_oregon_egg': usdCurrency_oregon_egg,
        'eurCurrency_oregon_egg': eurCurrency_oregon_egg,
        'gbpCurrency_oregon_embryo': gbpCurrency_oregon_embryo,
        'usdCurrency_oregon_embryo': usdCurrency_oregon_embryo,
        'eurCurrency_oregon_embryo': eurCurrency_oregon_embryo,
        'gbpCurrency_oregon_sperm': gbpCurrency_oregon_sperm,
        'usdCurrency_oregon_sperm': usdCurrency_oregon_sperm,
        'eurCurrency_oregon_sperm': eurCurrency_oregon_sperm,
        'gbpCurrency_oregon_icsi': gbpCurrency_oregon_icsi,
        'usdCurrency_oregon_icsi': usdCurrency_oregon_icsi,
        'eurCurrency_oregon_icsi': eurCurrency_oregon_icsi,
        'gbpCurrency_oregon_iui': gbpCurrency_oregon_iui,
        'usdCurrency_oregon_iui': usdCurrency_oregon_iui,
        'eurCurrency_oregon_iui': eurCurrency_oregon_iui,

        'gbpCurrency_pennsylvania_ivf': gbpCurrency_pennsylvania_ivf,
        'usdCurrency_pennsylvania_ivf': usdCurrency_pennsylvania_ivf,
        'eurCurrency_pennsylvania_ivf': eurCurrency_pennsylvania_ivf,
        'gbpCurrency_pennsylvania_egg': gbpCurrency_pennsylvania_egg,
        'usdCurrency_pennsylvania_egg': usdCurrency_pennsylvania_egg,
        'eurCurrency_pennsylvania_egg': eurCurrency_pennsylvania_egg,
        'gbpCurrency_pennsylvania_embryo': gbpCurrency_pennsylvania_embryo,
        'usdCurrency_pennsylvania_embryo': usdCurrency_pennsylvania_embryo,
        'eurCurrency_pennsylvania_embryo': eurCurrency_pennsylvania_embryo,
        'gbpCurrency_pennsylvania_sperm': gbpCurrency_pennsylvania_sperm,
        'usdCurrency_pennsylvania_sperm': usdCurrency_pennsylvania_sperm,
        'eurCurrency_pennsylvania_sperm': eurCurrency_pennsylvania_sperm,
        'gbpCurrency_pennsylvania_icsi': gbpCurrency_pennsylvania_icsi,
        'usdCurrency_pennsylvania_icsi': usdCurrency_pennsylvania_icsi,
        'eurCurrency_pennsylvania_icsi': eurCurrency_pennsylvania_icsi,
        'gbpCurrency_pennsylvania_iui': gbpCurrency_pennsylvania_iui,
        'usdCurrency_pennsylvania_iui': usdCurrency_pennsylvania_iui,
        'eurCurrency_pennsylvania_iui': eurCurrency_pennsylvania_iui,

        'gbpCurrency_puertorico_ivf': gbpCurrency_puertorico_ivf,
        'usdCurrency_puertorico_ivf': usdCurrency_puertorico_ivf,
        'eurCurrency_puertorico_ivf': eurCurrency_puertorico_ivf,
        'gbpCurrency_puertorico_egg': gbpCurrency_puertorico_egg,
        'usdCurrency_puertorico_egg': usdCurrency_puertorico_egg,
        'eurCurrency_puertorico_egg': eurCurrency_puertorico_egg,
        'gbpCurrency_puertorico_embryo': gbpCurrency_puertorico_embryo,
        'usdCurrency_puertorico_embryo': usdCurrency_puertorico_embryo,
        'eurCurrency_puertorico_embryo': eurCurrency_puertorico_embryo,
        'gbpCurrency_puertorico_sperm': gbpCurrency_puertorico_sperm,
        'usdCurrency_puertorico_sperm': usdCurrency_puertorico_sperm,
        'eurCurrency_puertorico_sperm': eurCurrency_puertorico_sperm,
        'gbpCurrency_puertorico_icsi': gbpCurrency_puertorico_icsi,
        'usdCurrency_puertorico_icsi': usdCurrency_puertorico_icsi,
        'eurCurrency_puertorico_icsi': eurCurrency_puertorico_icsi,
        'gbpCurrency_puertorico_iui': gbpCurrency_puertorico_iui,
        'usdCurrency_puertorico_iui': usdCurrency_puertorico_iui,
        'eurCurrency_puertorico_iui': eurCurrency_puertorico_iui,

        'gbpCurrency_rhodeisland_ivf': gbpCurrency_rhodeisland_ivf,
        'usdCurrency_rhodeisland_ivf': usdCurrency_rhodeisland_ivf,
        'eurCurrency_rhodeisland_ivf': eurCurrency_rhodeisland_ivf,
        'gbpCurrency_rhodeisland_egg': gbpCurrency_rhodeisland_egg,
        'usdCurrency_rhodeisland_egg': usdCurrency_rhodeisland_egg,
        'eurCurrency_rhodeisland_egg': eurCurrency_rhodeisland_egg,
        'gbpCurrency_rhodeisland_embryo': gbpCurrency_rhodeisland_embryo,
        'usdCurrency_rhodeisland_embryo': usdCurrency_rhodeisland_embryo,
        'eurCurrency_rhodeisland_embryo': eurCurrency_rhodeisland_embryo,
        'gbpCurrency_rhodeisland_sperm': gbpCurrency_rhodeisland_sperm,
        'usdCurrency_rhodeisland_sperm': usdCurrency_rhodeisland_sperm,
        'eurCurrency_rhodeisland_sperm': eurCurrency_rhodeisland_sperm,
        'gbpCurrency_rhodeisland_icsi': gbpCurrency_rhodeisland_icsi,
        'usdCurrency_rhodeisland_icsi': usdCurrency_rhodeisland_icsi,
        'eurCurrency_rhodeisland_icsi': eurCurrency_rhodeisland_icsi,
        'gbpCurrency_rhodeisland_iui': gbpCurrency_rhodeisland_iui,
        'usdCurrency_rhodeisland_iui': usdCurrency_rhodeisland_iui,
        'eurCurrency_rhodeisland_iui': eurCurrency_rhodeisland_iui,

        'gbpCurrency_southcarolina_ivf': gbpCurrency_southcarolina_ivf,
        'usdCurrency_southcarolina_ivf': usdCurrency_southcarolina_ivf,
        'eurCurrency_southcarolina_ivf': eurCurrency_southcarolina_ivf,
        'gbpCurrency_southcarolina_egg': gbpCurrency_southcarolina_egg,
        'usdCurrency_southcarolina_egg': usdCurrency_southcarolina_egg,
        'eurCurrency_southcarolina_egg': eurCurrency_southcarolina_egg,
        'gbpCurrency_southcarolina_embryo': gbpCurrency_southcarolina_embryo,
        'usdCurrency_southcarolina_embryo': usdCurrency_southcarolina_embryo,
        'eurCurrency_southcarolina_embryo': eurCurrency_southcarolina_embryo,
        'gbpCurrency_southcarolina_sperm': gbpCurrency_southcarolina_sperm,
        'usdCurrency_southcarolina_sperm': usdCurrency_southcarolina_sperm,
        'eurCurrency_southcarolina_sperm': eurCurrency_southcarolina_sperm,
        'gbpCurrency_southcarolina_icsi': gbpCurrency_southcarolina_icsi,
        'usdCurrency_southcarolina_icsi': usdCurrency_southcarolina_icsi,
        'eurCurrency_southcarolina_icsi': eurCurrency_southcarolina_icsi,
        'gbpCurrency_southcarolina_iui': gbpCurrency_southcarolina_iui,
        'usdCurrency_southcarolina_iui': usdCurrency_southcarolina_iui,
        'eurCurrency_southcarolina_iui': eurCurrency_southcarolina_iui,

        'gbpCurrency_southdakota_ivf': gbpCurrency_southdakota_ivf,
        'usdCurrency_southdakota_ivf': usdCurrency_southdakota_ivf,
        'eurCurrency_southdakota_ivf': eurCurrency_southdakota_ivf,
        'gbpCurrency_southdakota_egg': gbpCurrency_southdakota_egg,
        'usdCurrency_southdakota_egg': usdCurrency_southdakota_egg,
        'eurCurrency_southdakota_egg': eurCurrency_southdakota_egg,
        'gbpCurrency_southdakota_embryo': gbpCurrency_southdakota_embryo,
        'usdCurrency_southdakota_embryo': usdCurrency_southdakota_embryo,
        'eurCurrency_southdakota_embryo': eurCurrency_southdakota_embryo,
        'gbpCurrency_southdakota_sperm': gbpCurrency_southdakota_sperm,
        'usdCurrency_southdakota_sperm': usdCurrency_southdakota_sperm,
        'eurCurrency_southdakota_sperm': eurCurrency_southdakota_sperm,
        'gbpCurrency_southdakota_icsi': gbpCurrency_southdakota_icsi,
        'usdCurrency_southdakota_icsi': usdCurrency_southdakota_icsi,
        'eurCurrency_southdakota_icsi': eurCurrency_southdakota_icsi,
        'gbpCurrency_southdakota_iui': gbpCurrency_southdakota_iui,
        'usdCurrency_southdakota_iui': usdCurrency_southdakota_iui,
        'eurCurrency_southdakota_iui': eurCurrency_southdakota_iui,

        'gbpCurrency_tennessee_ivf': gbpCurrency_tennessee_ivf,
        'usdCurrency_tennessee_ivf': usdCurrency_tennessee_ivf,
        'eurCurrency_tennessee_ivf': eurCurrency_tennessee_ivf,
        'gbpCurrency_tennessee_egg': gbpCurrency_tennessee_egg,
        'usdCurrency_tennessee_egg': usdCurrency_tennessee_egg,
        'eurCurrency_tennessee_egg': eurCurrency_tennessee_egg,
        'gbpCurrency_tennessee_embryo': gbpCurrency_tennessee_embryo,
        'usdCurrency_tennessee_embryo': usdCurrency_tennessee_embryo,
        'eurCurrency_tennessee_embryo': eurCurrency_tennessee_embryo,
        'gbpCurrency_tennessee_sperm': gbpCurrency_tennessee_sperm,
        'usdCurrency_tennessee_sperm': usdCurrency_tennessee_sperm,
        'eurCurrency_tennessee_sperm': eurCurrency_tennessee_sperm,
        'gbpCurrency_tennessee_icsi': gbpCurrency_tennessee_icsi,
        'usdCurrency_tennessee_icsi': usdCurrency_tennessee_icsi,
        'eurCurrency_tennessee_icsi': eurCurrency_tennessee_icsi,
        'gbpCurrency_tennessee_iui': gbpCurrency_tennessee_iui,
        'usdCurrency_tennessee_iui': usdCurrency_tennessee_iui,
        'eurCurrency_tennessee_iui': eurCurrency_tennessee_iui,

        'gbpCurrency_texas_ivf': gbpCurrency_texas_ivf,
        'usdCurrency_texas_ivf': usdCurrency_texas_ivf,
        'eurCurrency_texas_ivf': eurCurrency_texas_ivf,
        'gbpCurrency_texas_egg': gbpCurrency_texas_egg,
        'usdCurrency_texas_egg': usdCurrency_texas_egg,
        'eurCurrency_texas_egg': eurCurrency_texas_egg,
        'gbpCurrency_texas_embryo': gbpCurrency_texas_embryo,
        'usdCurrency_texas_embryo': usdCurrency_texas_embryo,
        'eurCurrency_texas_embryo': eurCurrency_texas_embryo,
        'gbpCurrency_texas_sperm': gbpCurrency_texas_sperm,
        'usdCurrency_texas_sperm': usdCurrency_texas_sperm,
        'eurCurrency_texas_sperm': eurCurrency_texas_sperm,
        'gbpCurrency_texas_icsi': gbpCurrency_texas_icsi,
        'usdCurrency_texas_icsi': usdCurrency_texas_icsi,
        'eurCurrency_texas_icsi': eurCurrency_texas_icsi,
        'gbpCurrency_texas_iui': gbpCurrency_texas_iui,
        'usdCurrency_texas_iui': usdCurrency_texas_iui,
        'eurCurrency_texas_iui': eurCurrency_texas_iui,

        'gbpCurrency_utah_ivf': gbpCurrency_utah_ivf,
        'usdCurrency_utah_ivf': usdCurrency_utah_ivf,
        'eurCurrency_utah_ivf': eurCurrency_utah_ivf,
        'gbpCurrency_utah_egg': gbpCurrency_utah_egg,
        'usdCurrency_utah_egg': usdCurrency_utah_egg,
        'eurCurrency_utah_egg': eurCurrency_utah_egg,
        'gbpCurrency_utah_embryo': gbpCurrency_utah_embryo,
        'usdCurrency_utah_embryo': usdCurrency_utah_embryo,
        'eurCurrency_utah_embryo': eurCurrency_utah_embryo,
        'gbpCurrency_utah_sperm': gbpCurrency_utah_sperm,
        'usdCurrency_utah_sperm': usdCurrency_utah_sperm,
        'eurCurrency_utah_sperm': eurCurrency_utah_sperm,
        'gbpCurrency_utah_icsi': gbpCurrency_utah_icsi,
        'usdCurrency_utah_icsi': usdCurrency_utah_icsi,
        'eurCurrency_utah_icsi': eurCurrency_utah_icsi,
        'gbpCurrency_utah_iui': gbpCurrency_utah_iui,
        'usdCurrency_utah_iui': usdCurrency_utah_iui,
        'eurCurrency_utah_iui': eurCurrency_utah_iui,

        'gbpCurrency_vermont_ivf': gbpCurrency_vermont_ivf,
        'usdCurrency_vermont_ivf': usdCurrency_vermont_ivf,
        'eurCurrency_vermont_ivf': eurCurrency_vermont_ivf,
        'gbpCurrency_vermont_egg': gbpCurrency_vermont_egg,
        'usdCurrency_vermont_egg': usdCurrency_vermont_egg,
        'eurCurrency_vermont_egg': eurCurrency_vermont_egg,
        'gbpCurrency_vermont_embryo': gbpCurrency_vermont_embryo,
        'usdCurrency_vermont_embryo': usdCurrency_vermont_embryo,
        'eurCurrency_vermont_embryo': eurCurrency_vermont_embryo,
        'gbpCurrency_vermont_sperm': gbpCurrency_vermont_sperm,
        'usdCurrency_vermont_sperm': usdCurrency_vermont_sperm,
        'eurCurrency_vermont_sperm': eurCurrency_vermont_sperm,
        'gbpCurrency_vermont_icsi': gbpCurrency_vermont_icsi,
        'usdCurrency_vermont_icsi': usdCurrency_vermont_icsi,
        'eurCurrency_vermont_icsi': eurCurrency_vermont_icsi,
        'gbpCurrency_vermont_iui': gbpCurrency_vermont_iui,
        'usdCurrency_vermont_iui': usdCurrency_vermont_iui,
        'eurCurrency_vermont_iui': eurCurrency_vermont_iui,

        'gbpCurrency_virginia_ivf': gbpCurrency_virginia_ivf,
        'usdCurrency_virginia_ivf': usdCurrency_virginia_ivf,
        'eurCurrency_virginia_ivf': eurCurrency_virginia_ivf,
        'gbpCurrency_virginia_egg': gbpCurrency_virginia_egg,
        'usdCurrency_virginia_egg': usdCurrency_virginia_egg,
        'eurCurrency_virginia_egg': eurCurrency_virginia_egg,
        'gbpCurrency_virginia_embryo': gbpCurrency_virginia_embryo,
        'usdCurrency_virginia_embryo': usdCurrency_virginia_embryo,
        'eurCurrency_virginia_embryo': eurCurrency_virginia_embryo,
        'gbpCurrency_virginia_sperm': gbpCurrency_virginia_sperm,
        'usdCurrency_virginia_sperm': usdCurrency_virginia_sperm,
        'eurCurrency_virginia_sperm': eurCurrency_virginia_sperm,
        'gbpCurrency_virginia_icsi': gbpCurrency_virginia_icsi,
        'usdCurrency_virginia_icsi': usdCurrency_virginia_icsi,
        'eurCurrency_virginia_icsi': eurCurrency_virginia_icsi,
        'gbpCurrency_virginia_iui': gbpCurrency_virginia_iui,
        'usdCurrency_virginia_iui': usdCurrency_virginia_iui,
        'eurCurrency_virginia_iui': eurCurrency_virginia_iui,

        'gbpCurrency_washington_ivf': gbpCurrency_washington_ivf,
        'usdCurrency_washington_ivf': usdCurrency_washington_ivf,
        'eurCurrency_washington_ivf': eurCurrency_washington_ivf,
        'gbpCurrency_washington_egg': gbpCurrency_washington_egg,
        'usdCurrency_washington_egg': usdCurrency_washington_egg,
        'eurCurrency_washington_egg': eurCurrency_washington_egg,
        'gbpCurrency_washington_embryo': gbpCurrency_washington_embryo,
        'usdCurrency_washington_embryo': usdCurrency_washington_embryo,
        'eurCurrency_washington_embryo': eurCurrency_washington_embryo,
        'gbpCurrency_washington_sperm': gbpCurrency_washington_sperm,
        'usdCurrency_washington_sperm': usdCurrency_washington_sperm,
        'eurCurrency_washington_sperm': eurCurrency_washington_sperm,
        'gbpCurrency_washington_icsi': gbpCurrency_washington_icsi,
        'usdCurrency_washington_icsi': usdCurrency_washington_icsi,
        'eurCurrency_washington_icsi': eurCurrency_washington_icsi,
        'gbpCurrency_washington_iui': gbpCurrency_washington_iui,
        'usdCurrency_washington_iui': usdCurrency_washington_iui,
        'eurCurrency_washington_iui': eurCurrency_washington_iui,

        'gbpCurrency_westvirginia_ivf': gbpCurrency_westvirginia_ivf,
        'usdCurrency_westvirginia_ivf': usdCurrency_westvirginia_ivf,
        'eurCurrency_westvirginia_ivf': eurCurrency_westvirginia_ivf,
        'gbpCurrency_westvirginia_egg': gbpCurrency_westvirginia_egg,
        'usdCurrency_westvirginia_egg': usdCurrency_westvirginia_egg,
        'eurCurrency_westvirginia_egg': eurCurrency_westvirginia_egg,
        'gbpCurrency_westvirginia_embryo': gbpCurrency_westvirginia_embryo,
        'usdCurrency_westvirginia_embryo': usdCurrency_westvirginia_embryo,
        'eurCurrency_westvirginia_embryo': eurCurrency_westvirginia_embryo,
        'gbpCurrency_westvirginia_sperm': gbpCurrency_westvirginia_sperm,
        'usdCurrency_westvirginia_sperm': usdCurrency_westvirginia_sperm,
        'eurCurrency_westvirginia_sperm': eurCurrency_westvirginia_sperm,
        'gbpCurrency_westvirginia_icsi': gbpCurrency_westvirginia_icsi,
        'usdCurrency_westvirginia_icsi': usdCurrency_westvirginia_icsi,
        'eurCurrency_westvirginia_icsi': eurCurrency_westvirginia_icsi,
        'gbpCurrency_westvirginia_iui': gbpCurrency_westvirginia_iui,
        'usdCurrency_westvirginia_iui': usdCurrency_westvirginia_iui,
        'eurCurrency_westvirginia_iui': eurCurrency_westvirginia_iui,

        'gbpCurrency_wisconsin_ivf': gbpCurrency_wisconsin_ivf,
        'usdCurrency_wisconsin_ivf': usdCurrency_wisconsin_ivf,
        'eurCurrency_wisconsin_ivf': eurCurrency_wisconsin_ivf,
        'gbpCurrency_wisconsin_egg': gbpCurrency_wisconsin_egg,
        'usdCurrency_wisconsin_egg': usdCurrency_wisconsin_egg,
        'eurCurrency_wisconsin_egg': eurCurrency_wisconsin_egg,
        'gbpCurrency_wisconsin_embryo': gbpCurrency_wisconsin_embryo,
        'usdCurrency_wisconsin_embryo': usdCurrency_wisconsin_embryo,
        'eurCurrency_wisconsin_embryo': eurCurrency_wisconsin_embryo,
        'gbpCurrency_wisconsin_sperm': gbpCurrency_wisconsin_sperm,
        'usdCurrency_wisconsin_sperm': usdCurrency_wisconsin_sperm,
        'eurCurrency_wisconsin_sperm': eurCurrency_wisconsin_sperm,
        'gbpCurrency_wisconsin_icsi': gbpCurrency_wisconsin_icsi,
        'usdCurrency_wisconsin_icsi': usdCurrency_wisconsin_icsi,
        'eurCurrency_wisconsin_icsi': eurCurrency_wisconsin_icsi,
        'gbpCurrency_wisconsin_iui': gbpCurrency_wisconsin_iui,
        'usdCurrency_wisconsin_iui': usdCurrency_wisconsin_iui,
        'eurCurrency_wisconsin_iui': eurCurrency_wisconsin_iui,

        'gbpCurrency_wyoming_ivf': gbpCurrency_wyoming_ivf,
        'usdCurrency_wyoming_ivf': usdCurrency_wyoming_ivf,
        'eurCurrency_wyoming_ivf': eurCurrency_wyoming_ivf,
        'gbpCurrency_wyoming_egg': gbpCurrency_wyoming_egg,
        'usdCurrency_wyoming_egg': usdCurrency_wyoming_egg,
        'eurCurrency_wyoming_egg': eurCurrency_wyoming_egg,
        'gbpCurrency_wyoming_embryo': gbpCurrency_wyoming_embryo,
        'usdCurrency_wyoming_embryo': usdCurrency_wyoming_embryo,
        'eurCurrency_wyoming_embryo': eurCurrency_wyoming_embryo,
        'gbpCurrency_wyoming_sperm': gbpCurrency_wyoming_sperm,
        'usdCurrency_wyoming_sperm': usdCurrency_wyoming_sperm,
        'eurCurrency_wyoming_sperm': eurCurrency_wyoming_sperm,
        'gbpCurrency_wyoming_icsi': gbpCurrency_wyoming_icsi,
        'usdCurrency_wyoming_icsi': usdCurrency_wyoming_icsi,
        'eurCurrency_wyoming_icsi': eurCurrency_wyoming_icsi,
        'gbpCurrency_wyoming_iui': gbpCurrency_wyoming_iui,
        'usdCurrency_wyoming_iui': usdCurrency_wyoming_iui,
        'eurCurrency_wyoming_iui': eurCurrency_wyoming_iui,

        'gbpCurrency_districtofcolumbia_ivf': gbpCurrency_districtofcolumbia_ivf,
        'usdCurrency_districtofcolumbia_ivf': usdCurrency_districtofcolumbia_ivf,
        'eurCurrency_districtofcolumbia_ivf': eurCurrency_districtofcolumbia_ivf,
        'gbpCurrency_districtofcolumbia_egg': gbpCurrency_districtofcolumbia_egg,
        'usdCurrency_districtofcolumbia_egg': usdCurrency_districtofcolumbia_egg,
        'eurCurrency_districtofcolumbia_egg': eurCurrency_districtofcolumbia_egg,
        'gbpCurrency_districtofcolumbia_embryo': gbpCurrency_districtofcolumbia_embryo,
        'usdCurrency_districtofcolumbia_embryo': usdCurrency_districtofcolumbia_embryo,
        'eurCurrency_districtofcolumbia_embryo': eurCurrency_districtofcolumbia_embryo,
        'gbpCurrency_districtofcolumbia_sperm': gbpCurrency_districtofcolumbia_sperm,
        'usdCurrency_districtofcolumbia_sperm': usdCurrency_districtofcolumbia_sperm,
        'eurCurrency_districtofcolumbia_sperm': eurCurrency_districtofcolumbia_sperm,
        'gbpCurrency_districtofcolumbia_icsi': gbpCurrency_districtofcolumbia_icsi,
        'usdCurrency_districtofcolumbia_icsi': usdCurrency_districtofcolumbia_icsi,
        'eurCurrency_districtofcolumbia_icsi': eurCurrency_districtofcolumbia_icsi,
        'gbpCurrency_districtofcolumbia_iui': gbpCurrency_districtofcolumbia_iui,
        'usdCurrency_districtofcolumbia_iui': usdCurrency_districtofcolumbia_iui,
        'eurCurrency_districtofcolumbia_iui': eurCurrency_districtofcolumbia_iui,

        'my_total_count_alabama': my_total_count_alabama,
        'my_total_count_alaska': my_total_count_alaska,
        'my_total_count_arizona': my_total_count_arizona,
        'my_total_count_arkansas': my_total_count_arkansas,
        'my_total_count_california': my_total_count_california,
        'my_total_count_colorado': my_total_count_colorado,
        'my_total_count_connecticut': my_total_count_connecticut,
        'my_total_count_delaware': my_total_count_delaware,
        'my_total_count_florida': my_total_count_florida,
        'my_total_count_florida_ovarian_ivf_treatment': my_total_count_florida_ovarian_ivf_treatment,
        'my_total_count_georgia': my_total_count_georgia,
        'my_total_count_hawaii': my_total_count_hawaii,
        'my_total_count_idaho': my_total_count_idaho,
        'my_total_count_illinois': my_total_count_illinois,
        'my_total_count_indiana': my_total_count_indiana,
        'my_total_count_iowa': my_total_count_iowa,
        'my_total_count_kansas': my_total_count_kansas,
        'my_total_count_kentucky': my_total_count_kentucky,
        'my_total_count_louisiana': my_total_count_louisiana,
        'my_total_count_maine': my_total_count_maine,
        'my_total_count_maryland': my_total_count_maryland,
        'my_total_count_massachusetts': my_total_count_massachusetts,
        'my_total_count_michigan': my_total_count_michigan,
        'my_total_count_minnesota': my_total_count_minnesota,
        'my_total_count_mississippi': my_total_count_mississippi,
        'my_total_count_missouri': my_total_count_missouri,
        'my_total_count_montana': my_total_count_montana,
        'my_total_count_nebraska': my_total_count_nebraska,
        'my_total_count_newhampshire': my_total_count_newhampshire,
        'my_total_count_newjersey': my_total_count_newjersey,
        'my_total_count_newmexico': my_total_count_newmexico,
        'my_total_count_newyork': my_total_count_newyork,
        'my_total_count_northcarolina': my_total_count_northcarolina,
        'my_total_count_northdakota': my_total_count_northdakota,
        'my_total_count_nevada': my_total_count_nevada,
        'my_total_count_ohio': my_total_count_ohio,
        'my_total_count_oklahoma': my_total_count_oklahoma,
        'my_total_count_oregon': my_total_count_oregon,
        'my_total_count_pennsylvania': my_total_count_pennsylvania,
        'my_total_count_puertorico': my_total_count_puertorico,
        'my_total_count_rhodeisland': my_total_count_rhodeisland,
        'my_total_count_southcarolina': my_total_count_southcarolina,
        'my_total_count_southdakota': my_total_count_southdakota,
        'my_total_count_tennessee': my_total_count_tennessee,
        'my_total_count_texas': my_total_count_texas,
        'my_total_count_utah': my_total_count_utah,
        'my_total_count_vermont': my_total_count_vermont,
        'my_total_count_virginia': my_total_count_virginia,
        'my_total_count_washington': my_total_count_washington,
        'my_total_count_westvirginia': my_total_count_westvirginia,
        'my_total_count_wisconsin': my_total_count_wisconsin,
        'my_total_count_wyoming': my_total_count_wyoming,
        'my_total_count_districtofcolumbia': my_total_count_districtofcolumbia,
        }

    return render(request, 'main/Locations/USLocations/us-regions-ivf.html', context)

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------



def locationsUKRegions(request):
    queryset_list_uk = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_aberdeen = queryset_list_uk.filter(clinicRegion__iexact='Aberdeen')
    my_total_count_aberdeen = queryset_list_aberdeen.count()
    queryset_list_aberdeen_ivf = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_aberdeen_ivf.items():
        gbpCurrency_aberdeen_ivf = val
        if gbpCurrency_aberdeen_ivf is not None:
            usdCurrency_aberdeen_ivf = val * gbpToUsd
            eurCurrency_aberdeen_ivf = val * gbpToEur
        else:
            usdCurrency_aberdeen_ivf = None
            eurCurrency_aberdeen_ivf = None

    queryset_list_aberdeen_egg = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_egg.items():
        gbpCurrency_aberdeen_egg = val
        if gbpCurrency_aberdeen_egg is not None:
            usdCurrency_aberdeen_egg = val * gbpToUsd
            eurCurrency_aberdeen_egg = val * gbpToEur
        else:
            usdCurrency_aberdeen_egg = None
            eurCurrency_aberdeen_egg = None

    queryset_list_aberdeen_embryo = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_embryo.items():
        gbpCurrency_aberdeen_embryo = val
        if gbpCurrency_aberdeen_embryo is not None:
            usdCurrency_aberdeen_embryo = val * gbpToUsd
            eurCurrency_aberdeen_embryo = val * gbpToEur
        else:
            usdCurrency_aberdeen_embryo = None
            eurCurrency_aberdeen_embryo = None

    queryset_list_aberdeen_sperm = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_sperm.items():
        gbpCurrency_aberdeen_sperm = val
        if gbpCurrency_aberdeen_sperm is not None:
            usdCurrency_aberdeen_sperm = val * gbpToUsd
            eurCurrency_aberdeen_sperm = val * gbpToEur
        else:
            usdCurrency_aberdeen_sperm = None
            eurCurrency_aberdeen_sperm = None

    queryset_list_aberdeen_icsi = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_aberdeen_icsi.items():
        gbpCurrency_aberdeen_icsi = val
        if gbpCurrency_aberdeen_icsi is not None:
            usdCurrency_aberdeen_icsi = val * gbpToUsd
            eurCurrency_aberdeen_icsi = val * gbpToEur
        else:
            usdCurrency_aberdeen_icsi = None
            eurCurrency_aberdeen_icsi = None

    queryset_list_aberdeen_iui = queryset_list_aberdeen.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_aberdeen_iui.items():
        gbpCurrency_aberdeen_iui = val
        if gbpCurrency_aberdeen_iui is not None:
            usdCurrency_aberdeen_iui = val * gbpToUsd
            eurCurrency_aberdeen_iui = val * gbpToEur
        else:
            usdCurrency_aberdeen_iui = None
            eurCurrency_aberdeen_iui = None

    #--------------------------------------------------------------------------
    queryset_list_bath = queryset_list_uk.filter(clinicRegion__iexact='Bath')
    my_total_count_bath = queryset_list_bath.count()
    queryset_list_bath_ivf = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bath_ivf.items():
        gbpCurrency_bath_ivf = val
        if gbpCurrency_bath_ivf is not None:
            usdCurrency_bath_ivf = val * gbpToUsd
            eurCurrency_bath_ivf = val * gbpToEur
        else:
            usdCurrency_bath_ivf = None
            eurCurrency_bath_ivf = None

    queryset_list_bath_egg = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bath_egg.items():
        gbpCurrency_bath_egg = val
        if gbpCurrency_bath_egg is not None:
            usdCurrency_bath_egg = val * gbpToUsd
            eurCurrency_bath_egg = val * gbpToEur
        else:
            usdCurrency_bath_egg = None
            eurCurrency_bath_egg = None

    queryset_list_bath_embryo = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bath_embryo.items():
        gbpCurrency_bath_embryo = val
        if gbpCurrency_bath_embryo is not None:
            usdCurrency_bath_embryo = val * gbpToUsd
            eurCurrency_bath_embryo = val * gbpToEur
        else:
            usdCurrency_bath_embryo = None
            eurCurrency_bath_embryo = None

    queryset_list_bath_sperm = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bath_sperm.items():
        gbpCurrency_bath_sperm = val
        if gbpCurrency_bath_sperm is not None:
            usdCurrency_bath_sperm = val * gbpToUsd
            eurCurrency_bath_sperm = val * gbpToEur
        else:
            usdCurrency_bath_sperm = None
            eurCurrency_bath_sperm = None

    queryset_list_bath_icsi = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bath_icsi.items():
        gbpCurrency_bath_icsi = val
        if gbpCurrency_bath_icsi is not None:
            usdCurrency_bath_icsi = val * gbpToUsd
            eurCurrency_bath_icsi = val * gbpToEur
        else:
            usdCurrency_bath_icsi = None
            eurCurrency_bath_icsi = None

    queryset_list_bath_iui = queryset_list_bath.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bath_iui.items():
        gbpCurrency_bath_iui = val
        if gbpCurrency_bath_iui is not None:
            usdCurrency_bath_iui = val * gbpToUsd
            eurCurrency_bath_iui = val * gbpToEur
        else:
            usdCurrency_bath_iui = None
            eurCurrency_bath_iui = None

    #--------------------------------------------------------------------------
    queryset_list_belfast = queryset_list_uk.filter(clinicRegion__iexact='Belfast')
    my_total_count_belfast = queryset_list_belfast.count()
    queryset_list_belfast_ivf = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_belfast_ivf.items():
      gbpCurrency_belfast_ivf = val
      if gbpCurrency_belfast_ivf is not None:
          usdCurrency_belfast_ivf = val * gbpToUsd
          eurCurrency_belfast_ivf = val * gbpToEur
      else:
          usdCurrency_belfast_ivf = None
          eurCurrency_belfast_ivf = None

    queryset_list_belfast_egg = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_belfast_egg.items():
      gbpCurrency_belfast_egg = val
      if gbpCurrency_belfast_egg is not None:
          usdCurrency_belfast_egg = val * gbpToUsd
          eurCurrency_belfast_egg = val * gbpToEur
      else:
          usdCurrency_belfast_egg = None
          eurCurrency_belfast_egg = None

    queryset_list_belfast_embryo = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_belfast_embryo.items():
      gbpCurrency_belfast_embryo = val
      if gbpCurrency_belfast_embryo is not None:
          usdCurrency_belfast_embryo = val * gbpToUsd
          eurCurrency_belfast_embryo = val * gbpToEur
      else:
          usdCurrency_belfast_embryo = None
          eurCurrency_belfast_embryo = None

    queryset_list_belfast_sperm = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_belfast_sperm.items():
      gbpCurrency_belfast_sperm = val
      if gbpCurrency_belfast_sperm is not None:
          usdCurrency_belfast_sperm = val * gbpToUsd
          eurCurrency_belfast_sperm = val * gbpToEur
      else:
          usdCurrency_belfast_sperm = None
          eurCurrency_belfast_sperm = None

    queryset_list_belfast_icsi = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_belfast_icsi.items():
      gbpCurrency_belfast_icsi = val
      if gbpCurrency_belfast_icsi is not None:
          usdCurrency_belfast_icsi = val * gbpToUsd
          eurCurrency_belfast_icsi = val * gbpToEur
      else:
          usdCurrency_belfast_icsi = None
          eurCurrency_belfast_icsi = None

    queryset_list_belfast_iui = queryset_list_belfast.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_belfast_iui.items():
      gbpCurrency_belfast_iui = val
      if gbpCurrency_belfast_iui is not None:
          usdCurrency_belfast_iui = val * gbpToUsd
          eurCurrency_belfast_iui = val * gbpToEur
      else:
          usdCurrency_belfast_iui = None
          eurCurrency_belfast_iui = None

    #--------------------------------------------------------------------------
    queryset_list_birmingham = queryset_list_uk.filter(clinicRegion__iexact='Birmingham')
    my_total_count_birmingham = queryset_list_birmingham.count()
    queryset_list_birmingham_ivf = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_birmingham_ivf.items():
      gbpCurrency_birmingham_ivf = val
      if gbpCurrency_birmingham_ivf is not None:
          usdCurrency_birmingham_ivf = val * gbpToUsd
          eurCurrency_birmingham_ivf = val * gbpToEur
      else:
          usdCurrency_birmingham_ivf = None
          eurCurrency_birmingham_ivf = None

    queryset_list_birmingham_egg = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_egg.items():
      gbpCurrency_birmingham_egg = val
      if gbpCurrency_birmingham_egg is not None:
          usdCurrency_birmingham_egg = val * gbpToUsd
          eurCurrency_birmingham_egg = val * gbpToEur
      else:
          usdCurrency_birmingham_egg = None
          eurCurrency_birmingham_egg = None

    queryset_list_birmingham_embryo = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_embryo.items():
      gbpCurrency_birmingham_embryo = val
      if gbpCurrency_birmingham_embryo is not None:
          usdCurrency_birmingham_embryo = val * gbpToUsd
          eurCurrency_birmingham_embryo = val * gbpToEur
      else:
          usdCurrency_birmingham_embryo = None
          eurCurrency_birmingham_embryo = None

    queryset_list_birmingham_sperm = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_sperm.items():
      gbpCurrency_birmingham_sperm = val
      if gbpCurrency_birmingham_sperm is not None:
          usdCurrency_birmingham_sperm = val * gbpToUsd
          eurCurrency_birmingham_sperm = val * gbpToEur
      else:
          usdCurrency_birmingham_sperm = None
          eurCurrency_birmingham_sperm = None

    queryset_list_birmingham_icsi = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_birmingham_icsi.items():
      gbpCurrency_birmingham_icsi = val
      if gbpCurrency_birmingham_icsi is not None:
          usdCurrency_birmingham_icsi = val * gbpToUsd
          eurCurrency_birmingham_icsi = val * gbpToEur
      else:
          usdCurrency_birmingham_icsi = None
          eurCurrency_birmingham_icsi = None

    queryset_list_birmingham_iui = queryset_list_birmingham.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_birmingham_iui.items():
      gbpCurrency_birmingham_iui = val
      if gbpCurrency_birmingham_iui is not None:
          usdCurrency_birmingham_iui = val * gbpToUsd
          eurCurrency_birmingham_iui = val * gbpToEur
      else:
          usdCurrency_birmingham_iui = None
          eurCurrency_birmingham_iui = None

    #--------------------------------------------------------------------------
    queryset_list_bournemouth = queryset_list_uk.filter(clinicRegion__iexact='Bournemouth')
    my_total_count_bournemouth = queryset_list_bournemouth.count()
    queryset_list_bournemouth_ivf = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bournemouth_ivf.items():
      gbpCurrency_bournemouth_ivf = val
      if gbpCurrency_bournemouth_ivf is not None:
          usdCurrency_bournemouth_ivf = val * gbpToUsd
          eurCurrency_bournemouth_ivf = val * gbpToEur
      else:
          usdCurrency_bournemouth_ivf = None
          eurCurrency_bournemouth_ivf = None

    queryset_list_bournemouth_egg = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_egg.items():
      gbpCurrency_bournemouth_egg = val
      if gbpCurrency_bournemouth_egg is not None:
          usdCurrency_bournemouth_egg = val * gbpToUsd
          eurCurrency_bournemouth_egg = val * gbpToEur
      else:
          usdCurrency_bournemouth_egg = None
          eurCurrency_bournemouth_egg = None

    queryset_list_bournemouth_embryo = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_embryo.items():
      gbpCurrency_bournemouth_embryo = val
      if gbpCurrency_bournemouth_embryo is not None:
          usdCurrency_bournemouth_embryo = val * gbpToUsd
          eurCurrency_bournemouth_embryo = val * gbpToEur
      else:
          usdCurrency_bournemouth_embryo = None
          eurCurrency_bournemouth_embryo = None

    queryset_list_bournemouth_sperm = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_sperm.items():
      gbpCurrency_bournemouth_sperm = val
      if gbpCurrency_bournemouth_sperm is not None:
          usdCurrency_bournemouth_sperm = val * gbpToUsd
          eurCurrency_bournemouth_sperm = val * gbpToEur
      else:
          usdCurrency_bournemouth_sperm = None
          eurCurrency_bournemouth_sperm = None

    queryset_list_bournemouth_icsi = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bournemouth_icsi.items():
      gbpCurrency_bournemouth_icsi = val
      if gbpCurrency_bournemouth_icsi is not None:
          usdCurrency_bournemouth_icsi = val * gbpToUsd
          eurCurrency_bournemouth_icsi = val * gbpToEur
      else:
          usdCurrency_bournemouth_icsi = None
          eurCurrency_bournemouth_icsi = None

    queryset_list_bournemouth_iui = queryset_list_bournemouth.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bournemouth_iui.items():
      gbpCurrency_bournemouth_iui = val
      if gbpCurrency_bournemouth_iui is not None:
          usdCurrency_bournemouth_iui = val * gbpToUsd
          eurCurrency_bournemouth_iui = val * gbpToEur
      else:
          usdCurrency_bournemouth_iui = None
          eurCurrency_bournemouth_iui = None

      #--------------------------------------------------------------------------
      queryset_list_brightonhove = queryset_list_uk.filter(clinicRegion__iexact='BrightonHove')
      my_total_count_brightonhove = queryset_list_brightonhove.count()
      queryset_list_brightonhove_ivf = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_brightonhove_ivf.items():
          gbpCurrency_brightonhove_ivf = val
          if gbpCurrency_brightonhove_ivf is not None:
              usdCurrency_brightonhove_ivf = val * gbpToUsd
              eurCurrency_brightonhove_ivf = val * gbpToEur
          else:
              usdCurrency_brightonhove_ivf = None
              eurCurrency_brightonhove_ivf = None

      queryset_list_brightonhove_egg = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_brightonhove_egg.items():
          gbpCurrency_brightonhove_egg = val
          if gbpCurrency_brightonhove_egg is not None:
              usdCurrency_brightonhove_egg = val * gbpToUsd
              eurCurrency_brightonhove_egg = val * gbpToEur
          else:
              usdCurrency_brightonhove_egg = None
              eurCurrency_brightonhove_egg = None

      queryset_list_brightonhove_embryo = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_brightonhove_embryo.items():
          gbpCurrency_brightonhove_embryo = val
          if gbpCurrency_brightonhove_embryo is not None:
              usdCurrency_brightonhove_embryo = val * gbpToUsd
              eurCurrency_brightonhove_embryo = val * gbpToEur
          else:
              usdCurrency_brightonhove_embryo = None
              eurCurrency_brightonhove_embryo = None

      queryset_list_brightonhove_sperm = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_brightonhove_sperm.items():
          gbpCurrency_brightonhove_sperm = val
          if gbpCurrency_brightonhove_sperm is not None:
              usdCurrency_brightonhove_sperm = val * gbpToUsd
              eurCurrency_brightonhove_sperm = val * gbpToEur
          else:
              usdCurrency_brightonhove_sperm = None
              eurCurrency_brightonhove_sperm = None

      queryset_list_brightonhove_icsi = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_brightonhove_icsi.items():
          gbpCurrency_brightonhove_icsi = val
          if gbpCurrency_brightonhove_icsi is not None:
              usdCurrency_brightonhove_icsi = val * gbpToUsd
              eurCurrency_brightonhove_icsi = val * gbpToEur
          else:
              usdCurrency_brightonhove_icsi = None
              eurCurrency_brightonhove_icsi = None

      queryset_list_brightonhove_iui = queryset_list_brightonhove.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_brightonhove_iui.items():
          gbpCurrency_brightonhove_iui = val
          if gbpCurrency_brightonhove_iui is not None:
              usdCurrency_brightonhove_iui = val * gbpToUsd
              eurCurrency_brightonhove_iui = val * gbpToEur
          else:
              usdCurrency_brightonhove_iui = None
              eurCurrency_brightonhove_iui = None

      #--------------------------------------------------------------------------
      queryset_list_bristol = queryset_list_uk.filter(clinicRegion__iexact='Bristol')
      my_total_count_bristol = queryset_list_bristol.count()
      queryset_list_bristol_ivf = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_bristol_ivf.items():
          gbpCurrency_bristol_ivf = val
          if gbpCurrency_bristol_ivf is not None:
              usdCurrency_bristol_ivf = val * gbpToUsd
              eurCurrency_bristol_ivf = val * gbpToEur
          else:
              usdCurrency_bristol_ivf = None
              eurCurrency_bristol_ivf = None

      queryset_list_bristol_egg = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_bristol_egg.items():
          gbpCurrency_bristol_egg = val
          if gbpCurrency_bristol_egg is not None:
              usdCurrency_bristol_egg = val * gbpToUsd
              eurCurrency_bristol_egg = val * gbpToEur
          else:
              usdCurrency_bristol_egg = None
              eurCurrency_bristol_egg = None

      queryset_list_bristol_embryo = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_bristol_embryo.items():
          gbpCurrency_bristol_embryo = val
          if gbpCurrency_bristol_embryo is not None:
              usdCurrency_bristol_embryo = val * gbpToUsd
              eurCurrency_bristol_embryo = val * gbpToEur
          else:
              usdCurrency_bristol_embryo = None
              eurCurrency_bristol_embryo = None

      queryset_list_bristol_sperm = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_bristol_sperm.items():
          gbpCurrency_bristol_sperm = val
          if gbpCurrency_bristol_sperm is not None:
              usdCurrency_bristol_sperm = val * gbpToUsd
              eurCurrency_bristol_sperm = val * gbpToEur
          else:
              usdCurrency_bristol_sperm = None
              eurCurrency_bristol_sperm = None

      queryset_list_bristol_icsi = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_bristol_icsi.items():
          gbpCurrency_bristol_icsi = val
          if gbpCurrency_bristol_icsi is not None:
              usdCurrency_bristol_icsi = val * gbpToUsd
              eurCurrency_bristol_icsi = val * gbpToEur
          else:
              usdCurrency_bristol_icsi = None
              eurCurrency_bristol_icsi = None

      queryset_list_bristol_iui = queryset_list_bristol.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_bristol_iui.items():
          gbpCurrency_bristol_iui = val
          if gbpCurrency_bristol_iui is not None:
              usdCurrency_bristol_iui = val * gbpToUsd
              eurCurrency_bristol_iui = val * gbpToEur
          else:
              usdCurrency_bristol_iui = None
              eurCurrency_bristol_iui = None

    #--------------------------------------------------------------------------
      queryset_list_cambridge = queryset_list_uk.filter(clinicRegion__iexact='Cambridge')
      my_total_count_cambridge = queryset_list_cambridge.count()
      queryset_list_cambridge_ivf = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_cambridge_ivf.items():
          gbpCurrency_cambridge_ivf = val
          if gbpCurrency_cambridge_ivf is not None:
              usdCurrency_cambridge_ivf = val * gbpToUsd
              eurCurrency_cambridge_ivf = val * gbpToEur
          else:
              usdCurrency_cambridge_ivf = None
              eurCurrency_cambridge_ivf = None

      queryset_list_cambridge_egg = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_cambridge_egg.items():
          gbpCurrency_cambridge_egg = val
          if gbpCurrency_cambridge_egg is not None:
              usdCurrency_cambridge_egg = val * gbpToUsd
              eurCurrency_cambridge_egg = val * gbpToEur
          else:
              usdCurrency_cambridge_egg = None
              eurCurrency_cambridge_egg = None

      queryset_list_cambridge_embryo = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_cambridge_embryo.items():
          gbpCurrency_cambridge_embryo = val
          if gbpCurrency_cambridge_embryo is not None:
              usdCurrency_cambridge_embryo = val * gbpToUsd
              eurCurrency_cambridge_embryo = val * gbpToEur
          else:
              usdCurrency_cambridge_embryo = None
              eurCurrency_cambridge_embryo = None

      queryset_list_cambridge_sperm = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_cambridge_sperm.items():
          gbpCurrency_cambridge_sperm = val
          if gbpCurrency_cambridge_sperm is not None:
              usdCurrency_cambridge_sperm = val * gbpToUsd
              eurCurrency_cambridge_sperm = val * gbpToEur
          else:
              usdCurrency_cambridge_sperm = None
              eurCurrency_cambridge_sperm = None

      queryset_list_cambridge_icsi = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_cambridge_icsi.items():
          gbpCurrency_cambridge_icsi = val
          if gbpCurrency_cambridge_icsi is not None:
              usdCurrency_cambridge_icsi = val * gbpToUsd
              eurCurrency_cambridge_icsi = val * gbpToEur
          else:
              usdCurrency_cambridge_icsi = None
              eurCurrency_cambridge_icsi = None

      queryset_list_cambridge_iui = queryset_list_cambridge.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_cambridge_iui.items():
          gbpCurrency_cambridge_iui = val
          if gbpCurrency_cambridge_iui is not None:
              usdCurrency_cambridge_iui = val * gbpToUsd
              eurCurrency_cambridge_iui = val * gbpToEur
          else:
              usdCurrency_cambridge_iui = None
              eurCurrency_cambridge_iui = None

    #--------------------------------------------------------------------------
      queryset_list_cardiff = queryset_list_uk.filter(clinicRegion__iexact='Cardiff')
      my_total_count_cardiff = queryset_list_cardiff.count()
      queryset_list_cardiff_ivf = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_cardiff_ivf.items():
          gbpCurrency_cardiff_ivf = val
          if gbpCurrency_cardiff_ivf is not None:
              usdCurrency_cardiff_ivf = val * gbpToUsd
              eurCurrency_cardiff_ivf = val * gbpToEur
          else:
              usdCurrency_cardiff_ivf = None
              eurCurrency_cardiff_ivf = None

      queryset_list_cardiff_egg = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_cardiff_egg.items():
          gbpCurrency_cardiff_egg = val
          if gbpCurrency_cardiff_egg is not None:
              usdCurrency_cardiff_egg = val * gbpToUsd
              eurCurrency_cardiff_egg = val * gbpToEur
          else:
              usdCurrency_cardiff_egg = None
              eurCurrency_cardiff_egg = None

      queryset_list_cardiff_embryo = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_cardiff_embryo.items():
          gbpCurrency_cardiff_embryo = val
          if gbpCurrency_cardiff_embryo is not None:
              usdCurrency_cardiff_embryo = val * gbpToUsd
              eurCurrency_cardiff_embryo = val * gbpToEur
          else:
              usdCurrency_cardiff_embryo = None
              eurCurrency_cardiff_embryo = None

      queryset_list_cardiff_sperm = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_cardiff_sperm.items():
          gbpCurrency_cardiff_sperm = val
          if gbpCurrency_cardiff_sperm is not None:
              usdCurrency_cardiff_sperm = val * gbpToUsd
              eurCurrency_cardiff_sperm = val * gbpToEur
          else:
              usdCurrency_cardiff_sperm = None
              eurCurrency_cardiff_sperm = None

      queryset_list_cardiff_icsi = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_cardiff_icsi.items():
          gbpCurrency_cardiff_icsi = val
          if gbpCurrency_cardiff_icsi is not None:
              usdCurrency_cardiff_icsi = val * gbpToUsd
              eurCurrency_cardiff_icsi = val * gbpToEur
          else:
              usdCurrency_cardiff_icsi = None
              eurCurrency_cardiff_icsi = None

      queryset_list_cardiff_iui = queryset_list_cardiff.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_cardiff_iui.items():
          gbpCurrency_cardiff_iui = val
          if gbpCurrency_cardiff_iui is not None:
              usdCurrency_cardiff_iui = val * gbpToUsd
              eurCurrency_cardiff_iui = val * gbpToEur
          else:
              usdCurrency_cardiff_iui = None
              eurCurrency_cardiff_iui = None

    #--------------------------------------------------------------------------
      queryset_list_colchester = queryset_list_uk.filter(clinicRegion__iexact='Colchester')
      my_total_count_colchester = queryset_list_colchester.count()
      queryset_list_colchester_ivf = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_colchester_ivf.items():
          gbpCurrency_colchester_ivf = val
          if gbpCurrency_colchester_ivf is not None:
              usdCurrency_colchester_ivf = val * gbpToUsd
              eurCurrency_colchester_ivf = val * gbpToEur
          else:
              usdCurrency_colchester_ivf = None
              eurCurrency_colchester_ivf = None

      queryset_list_colchester_egg = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_colchester_egg.items():
          gbpCurrency_colchester_egg = val
          if gbpCurrency_colchester_egg is not None:
              usdCurrency_colchester_egg = val * gbpToUsd
              eurCurrency_colchester_egg = val * gbpToEur
          else:
              usdCurrency_colchester_egg = None
              eurCurrency_colchester_egg = None

      queryset_list_colchester_embryo = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_colchester_embryo.items():
          gbpCurrency_colchester_embryo = val
          if gbpCurrency_colchester_embryo is not None:
              usdCurrency_colchester_embryo = val * gbpToUsd
              eurCurrency_colchester_embryo = val * gbpToEur
          else:
              usdCurrency_colchester_embryo = None
              eurCurrency_colchester_embryo = None

      queryset_list_colchester_sperm = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_colchester_sperm.items():
          gbpCurrency_colchester_sperm = val
          if gbpCurrency_colchester_sperm is not None:
              usdCurrency_colchester_sperm = val * gbpToUsd
              eurCurrency_colchester_sperm = val * gbpToEur
          else:
              usdCurrency_colchester_sperm = None
              eurCurrency_colchester_sperm = None

      queryset_list_colchester_icsi = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_colchester_icsi.items():
          gbpCurrency_colchester_icsi = val
          if gbpCurrency_colchester_icsi is not None:
              usdCurrency_colchester_icsi = val * gbpToUsd
              eurCurrency_colchester_icsi = val * gbpToEur
          else:
              usdCurrency_colchester_icsi = None
              eurCurrency_colchester_icsi = None

      queryset_list_colchester_iui = queryset_list_colchester.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_colchester_iui.items():
          gbpCurrency_colchester_iui = val
          if gbpCurrency_colchester_iui is not None:
              usdCurrency_colchester_iui = val * gbpToUsd
              eurCurrency_colchester_iui = val * gbpToEur
          else:
              usdCurrency_colchester_iui = None
              eurCurrency_colchester_iui = None

    #--------------------------------------------------------------------------
      queryset_list_derby = queryset_list_uk.filter(clinicRegion__iexact='Derby')
      my_total_count_derby = queryset_list_derby.count()
      queryset_list_derby_ivf = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_derby_ivf.items():
          gbpCurrency_derby_ivf = val
          if gbpCurrency_derby_ivf is not None:
              usdCurrency_derby_ivf = val * gbpToUsd
              eurCurrency_derby_ivf = val * gbpToEur
          else:
              usdCurrency_derby_ivf = None
              eurCurrency_derby_ivf = None

      queryset_list_derby_egg = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_derby_egg.items():
          gbpCurrency_derby_egg = val
          if gbpCurrency_derby_egg is not None:
              usdCurrency_derby_egg = val * gbpToUsd
              eurCurrency_derby_egg = val * gbpToEur
          else:
              usdCurrency_derby_egg = None
              eurCurrency_derby_egg = None

      queryset_list_derby_embryo = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_derby_embryo.items():
          gbpCurrency_derby_embryo = val
          if gbpCurrency_derby_embryo is not None:
              usdCurrency_derby_embryo = val * gbpToUsd
              eurCurrency_derby_embryo = val * gbpToEur
          else:
              usdCurrency_derby_embryo = None
              eurCurrency_derby_embryo = None

      queryset_list_derby_sperm = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_derby_sperm.items():
          gbpCurrency_derby_sperm = val
          if gbpCurrency_derby_sperm is not None:
              usdCurrency_derby_sperm = val * gbpToUsd
              eurCurrency_derby_sperm = val * gbpToEur
          else:
              usdCurrency_derby_sperm = None
              eurCurrency_derby_sperm = None

      queryset_list_derby_icsi = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_derby_icsi.items():
          gbpCurrency_derby_icsi = val
          if gbpCurrency_derby_icsi is not None:
              usdCurrency_derby_icsi = val * gbpToUsd
              eurCurrency_derby_icsi = val * gbpToEur
          else:
              usdCurrency_derby_icsi = None
              eurCurrency_derby_icsi = None

      queryset_list_derby_iui = queryset_list_derby.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_derby_iui.items():
          gbpCurrency_derby_iui = val
          if gbpCurrency_derby_iui is not None:
              usdCurrency_derby_iui = val * gbpToUsd
              eurCurrency_derby_iui = val * gbpToEur
          else:
              usdCurrency_derby_iui = None
              eurCurrency_derby_iui = None

    #--------------------------------------------------------------------------
      queryset_list_exeter = queryset_list_uk.filter(clinicRegion__iexact='Exeter')
      my_total_count_exeter = queryset_list_exeter.count()
      queryset_list_exeter_ivf = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_exeter_ivf.items():
          gbpCurrency_exeter_ivf = val
          if gbpCurrency_exeter_ivf is not None:
              usdCurrency_exeter_ivf = val * gbpToUsd
              eurCurrency_exeter_ivf = val * gbpToEur
          else:
              usdCurrency_exeter_ivf = None
              eurCurrency_exeter_ivf = None

      queryset_list_exeter_egg = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_exeter_egg.items():
          gbpCurrency_exeter_egg = val
          if gbpCurrency_exeter_egg is not None:
              usdCurrency_exeter_egg = val * gbpToUsd
              eurCurrency_exeter_egg = val * gbpToEur
          else:
              usdCurrency_exeter_egg = None
              eurCurrency_exeter_egg = None

      queryset_list_exeter_embryo = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_exeter_embryo.items():
          gbpCurrency_exeter_embryo = val
          if gbpCurrency_exeter_embryo is not None:
              usdCurrency_exeter_embryo = val * gbpToUsd
              eurCurrency_exeter_embryo = val * gbpToEur
          else:
              usdCurrency_exeter_embryo = None
              eurCurrency_exeter_embryo = None

      queryset_list_exeter_sperm = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_exeter_sperm.items():
          gbpCurrency_exeter_sperm = val
          if gbpCurrency_exeter_sperm is not None:
              usdCurrency_exeter_sperm = val * gbpToUsd
              eurCurrency_exeter_sperm = val * gbpToEur
          else:
              usdCurrency_exeter_sperm = None
              eurCurrency_exeter_sperm = None

      queryset_list_exeter_icsi = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_exeter_icsi.items():
          gbpCurrency_exeter_icsi = val
          if gbpCurrency_exeter_icsi is not None:
              usdCurrency_exeter_icsi = val * gbpToUsd
              eurCurrency_exeter_icsi = val * gbpToEur
          else:
              usdCurrency_exeter_icsi = None
              eurCurrency_exeter_icsi = None

      queryset_list_exeter_iui = queryset_list_exeter.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_exeter_iui.items():
          gbpCurrency_exeter_iui = val
          if gbpCurrency_exeter_iui is not None:
              usdCurrency_exeter_iui = val * gbpToUsd
              eurCurrency_exeter_iui = val * gbpToEur
          else:
              usdCurrency_exeter_iui = None
              eurCurrency_exeter_iui = None

    #--------------------------------------------------------------------------
      queryset_list_glasgow = queryset_list_uk.filter(clinicRegion__iexact='Glasgow')
      my_total_count_glasgow = queryset_list_glasgow.count()
      queryset_list_glasgow_ivf = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_glasgow_ivf.items():
          gbpCurrency_glasgow_ivf = val
          if gbpCurrency_glasgow_ivf is not None:
              usdCurrency_glasgow_ivf = val * gbpToUsd
              eurCurrency_glasgow_ivf = val * gbpToEur
          else:
              usdCurrency_glasgow_ivf = None
              eurCurrency_glasgow_ivf = None

      queryset_list_glasgow_egg = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_glasgow_egg.items():
          gbpCurrency_glasgow_egg = val
          if gbpCurrency_glasgow_egg is not None:
              usdCurrency_glasgow_egg = val * gbpToUsd
              eurCurrency_glasgow_egg = val * gbpToEur
          else:
              usdCurrency_glasgow_egg = None
              eurCurrency_glasgow_egg = None

      queryset_list_glasgow_embryo = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_glasgow_embryo.items():
          gbpCurrency_glasgow_embryo = val
          if gbpCurrency_glasgow_embryo is not None:
              usdCurrency_glasgow_embryo = val * gbpToUsd
              eurCurrency_glasgow_embryo = val * gbpToEur
          else:
              usdCurrency_glasgow_embryo = None
              eurCurrency_glasgow_embryo = None

      queryset_list_glasgow_sperm = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_glasgow_sperm.items():
          gbpCurrency_glasgow_sperm = val
          if gbpCurrency_glasgow_sperm is not None:
              usdCurrency_glasgow_sperm = val * gbpToUsd
              eurCurrency_glasgow_sperm = val * gbpToEur
          else:
              usdCurrency_glasgow_sperm = None
              eurCurrency_glasgow_sperm = None

      queryset_list_glasgow_icsi = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_glasgow_icsi.items():
          gbpCurrency_glasgow_icsi = val
          if gbpCurrency_glasgow_icsi is not None:
              usdCurrency_glasgow_icsi = val * gbpToUsd
              eurCurrency_glasgow_icsi = val * gbpToEur
          else:
              usdCurrency_glasgow_icsi = None
              eurCurrency_glasgow_icsi = None

      queryset_list_glasgow_iui = queryset_list_glasgow.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_glasgow_iui.items():
          gbpCurrency_glasgow_iui = val
          if gbpCurrency_glasgow_iui is not None:
              usdCurrency_glasgow_iui = val * gbpToUsd
              eurCurrency_glasgow_iui = val * gbpToEur
          else:
              usdCurrency_glasgow_iui = None
              eurCurrency_glasgow_iui = None

    #--------------------------------------------------------------------------
      queryset_list_hull = queryset_list_uk.filter(clinicRegion__iexact='Hull')
      my_total_count_hull = queryset_list_hull.count()
      queryset_list_hull_ivf = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_hull_ivf.items():
          gbpCurrency_hull_ivf = val
          if gbpCurrency_hull_ivf is not None:
              usdCurrency_hull_ivf = val * gbpToUsd
              eurCurrency_hull_ivf = val * gbpToEur
          else:
              usdCurrency_hull_ivf = None
              eurCurrency_hull_ivf = None

      queryset_list_hull_egg = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_hull_egg.items():
          gbpCurrency_hull_egg = val
          if gbpCurrency_hull_egg is not None:
              usdCurrency_hull_egg = val * gbpToUsd
              eurCurrency_hull_egg = val * gbpToEur
          else:
              usdCurrency_hull_egg = None
              eurCurrency_hull_egg = None

      queryset_list_hull_embryo = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_hull_embryo.items():
          gbpCurrency_hull_embryo = val
          if gbpCurrency_hull_embryo is not None:
              usdCurrency_hull_embryo = val * gbpToUsd
              eurCurrency_hull_embryo = val * gbpToEur
          else:
              usdCurrency_hull_embryo = None
              eurCurrency_hull_embryo = None

      queryset_list_hull_sperm = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_hull_sperm.items():
          gbpCurrency_hull_sperm = val
          if gbpCurrency_hull_sperm is not None:
              usdCurrency_hull_sperm = val * gbpToUsd
              eurCurrency_hull_sperm = val * gbpToEur
          else:
              usdCurrency_hull_sperm = None
              eurCurrency_hull_sperm = None

      queryset_list_hull_icsi = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_hull_icsi.items():
          gbpCurrency_hull_icsi = val
          if gbpCurrency_hull_icsi is not None:
              usdCurrency_hull_icsi = val * gbpToUsd
              eurCurrency_hull_icsi = val * gbpToEur
          else:
              usdCurrency_hull_icsi = None
              eurCurrency_hull_icsi = None

      queryset_list_hull_iui = queryset_list_hull.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_hull_iui.items():
          gbpCurrency_hull_iui = val
          if gbpCurrency_hull_iui is not None:
              usdCurrency_hull_iui = val * gbpToUsd
              eurCurrency_hull_iui = val * gbpToEur
          else:
              usdCurrency_hull_iui = None
              eurCurrency_hull_iui = None

    #--------------------------------------------------------------------------
      queryset_list_chelmsford = queryset_list_uk.filter(clinicRegion__iexact='Chelmsford')
      my_total_count_chelmsford = queryset_list_chelmsford.count()
      queryset_list_chelmsford_ivf = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_chelmsford_ivf.items():
          gbpCurrency_chelmsford_ivf = val
          if gbpCurrency_chelmsford_ivf is not None:
              usdCurrency_chelmsford_ivf = val * gbpToUsd
              eurCurrency_chelmsford_ivf = val * gbpToEur
          else:
              usdCurrency_chelmsford_ivf = None
              eurCurrency_chelmsford_ivf = None

      queryset_list_chelmsford_egg = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_chelmsford_egg.items():
          gbpCurrency_chelmsford_egg = val
          if gbpCurrency_chelmsford_egg is not None:
              usdCurrency_chelmsford_egg = val * gbpToUsd
              eurCurrency_chelmsford_egg = val * gbpToEur
          else:
              usdCurrency_chelmsford_egg = None
              eurCurrency_chelmsford_egg = None

      queryset_list_chelmsford_embryo = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_chelmsford_embryo.items():
          gbpCurrency_chelmsford_embryo = val
          if gbpCurrency_chelmsford_embryo is not None:
              usdCurrency_chelmsford_embryo = val * gbpToUsd
              eurCurrency_chelmsford_embryo = val * gbpToEur
          else:
              usdCurrency_chelmsford_embryo = None
              eurCurrency_chelmsford_embryo = None

      queryset_list_chelmsford_sperm = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_chelmsford_sperm.items():
          gbpCurrency_chelmsford_sperm = val
          if gbpCurrency_chelmsford_sperm is not None:
              usdCurrency_chelmsford_sperm = val * gbpToUsd
              eurCurrency_chelmsford_sperm = val * gbpToEur
          else:
              usdCurrency_chelmsford_sperm = None
              eurCurrency_chelmsford_sperm = None

      queryset_list_chelmsford_icsi = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_chelmsford_icsi.items():
          gbpCurrency_chelmsford_icsi = val
          if gbpCurrency_chelmsford_icsi is not None:
              usdCurrency_chelmsford_icsi = val * gbpToUsd
              eurCurrency_chelmsford_icsi = val * gbpToEur
          else:
              usdCurrency_chelmsford_icsi = None
              eurCurrency_chelmsford_icsi = None

      queryset_list_chelmsford_iui = queryset_list_chelmsford.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_chelmsford_iui.items():
          gbpCurrency_chelmsford_iui = val
          if gbpCurrency_chelmsford_iui is not None:
              usdCurrency_chelmsford_iui = val * gbpToUsd
              eurCurrency_chelmsford_iui = val * gbpToEur
          else:
              usdCurrency_chelmsford_iui = None
              eurCurrency_chelmsford_iui = None

    #--------------------------------------------------------------------------
      queryset_list_leeds = queryset_list_uk.filter(clinicRegion__iexact='Leeds')
      my_total_count_leeds = queryset_list_leeds.count()
      queryset_list_leeds_ivf = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_leeds_ivf.items():
          gbpCurrency_leeds_ivf = val
          if gbpCurrency_leeds_ivf is not None:
              usdCurrency_leeds_ivf = val * gbpToUsd
              eurCurrency_leeds_ivf = val * gbpToEur
          else:
              usdCurrency_leeds_ivf = None
              eurCurrency_leeds_ivf = None

      queryset_list_leeds_egg = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_leeds_egg.items():
          gbpCurrency_leeds_egg = val
          if gbpCurrency_leeds_egg is not None:
              usdCurrency_leeds_egg = val * gbpToUsd
              eurCurrency_leeds_egg = val * gbpToEur
          else:
              usdCurrency_leeds_egg = None
              eurCurrency_leeds_egg = None

      queryset_list_leeds_embryo = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_leeds_embryo.items():
          gbpCurrency_leeds_embryo = val
          if gbpCurrency_leeds_embryo is not None:
              usdCurrency_leeds_embryo = val * gbpToUsd
              eurCurrency_leeds_embryo = val * gbpToEur
          else:
              usdCurrency_leeds_embryo = None
              eurCurrency_leeds_embryo = None

      queryset_list_leeds_sperm = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_leeds_sperm.items():
          gbpCurrency_leeds_sperm = val
          if gbpCurrency_leeds_sperm is not None:
              usdCurrency_leeds_sperm = val * gbpToUsd
              eurCurrency_leeds_sperm = val * gbpToEur
          else:
              usdCurrency_leeds_sperm = None
              eurCurrency_leeds_sperm = None

      queryset_list_leeds_icsi = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_leeds_icsi.items():
          gbpCurrency_leeds_icsi = val
          if gbpCurrency_leeds_icsi is not None:
              usdCurrency_leeds_icsi = val * gbpToUsd
              eurCurrency_leeds_icsi = val * gbpToEur
          else:
              usdCurrency_leeds_icsi = None
              eurCurrency_leeds_icsi = None

      queryset_list_leeds_iui = queryset_list_leeds.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_leeds_iui.items():
          gbpCurrency_leeds_iui = val
          if gbpCurrency_leeds_iui is not None:
              usdCurrency_leeds_iui = val * gbpToUsd
              eurCurrency_leeds_iui = val * gbpToEur
          else:
              usdCurrency_leeds_iui = None
              eurCurrency_leeds_iui = None

    #--------------------------------------------------------------------------
      queryset_list_leicester = queryset_list_uk.filter(clinicRegion__iexact='Leicester')
      my_total_count_leicester = queryset_list_leicester.count()
      queryset_list_leicester_ivf = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_leicester_ivf.items():
          gbpCurrency_leicester_ivf = val
          if gbpCurrency_leicester_ivf is not None:
              usdCurrency_leicester_ivf = val * gbpToUsd
              eurCurrency_leicester_ivf = val * gbpToEur
          else:
              usdCurrency_leicester_ivf = None
              eurCurrency_leicester_ivf = None

      queryset_list_leicester_egg = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_leicester_egg.items():
          gbpCurrency_leicester_egg = val
          if gbpCurrency_leicester_egg is not None:
              usdCurrency_leicester_egg = val * gbpToUsd
              eurCurrency_leicester_egg = val * gbpToEur
          else:
              usdCurrency_leicester_egg = None
              eurCurrency_leicester_egg = None

      queryset_list_leicester_embryo = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_leicester_embryo.items():
          gbpCurrency_leicester_embryo = val
          if gbpCurrency_leicester_embryo is not None:
              usdCurrency_leicester_embryo = val * gbpToUsd
              eurCurrency_leicester_embryo = val * gbpToEur
          else:
              usdCurrency_leicester_embryo = None
              eurCurrency_leicester_embryo = None

      queryset_list_leicester_sperm = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_leicester_sperm.items():
          gbpCurrency_leicester_sperm = val
          if gbpCurrency_leicester_sperm is not None:
              usdCurrency_leicester_sperm = val * gbpToUsd
              eurCurrency_leicester_sperm = val * gbpToEur
          else:
              usdCurrency_leicester_sperm = None
              eurCurrency_leicester_sperm = None

      queryset_list_leicester_icsi = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_leicester_icsi.items():
          gbpCurrency_leicester_icsi = val
          if gbpCurrency_leicester_icsi is not None:
              usdCurrency_leicester_icsi = val * gbpToUsd
              eurCurrency_leicester_icsi = val * gbpToEur
          else:
              usdCurrency_leicester_icsi = None
              eurCurrency_leicester_icsi = None

      queryset_list_leicester_iui = queryset_list_leicester.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_leicester_iui.items():
          gbpCurrency_leicester_iui = val
          if gbpCurrency_leicester_iui is not None:
              usdCurrency_leicester_iui = val * gbpToUsd
              eurCurrency_leicester_iui = val * gbpToEur
          else:
              usdCurrency_leicester_iui = None
              eurCurrency_leicester_iui = None

    #--------------------------------------------------------------------------
      queryset_list_liverpool = queryset_list_uk.filter(clinicRegion__iexact='Liverpool')
      my_total_count_liverpool = queryset_list_liverpool.count()
      queryset_list_liverpool_ivf = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_liverpool_ivf.items():
          gbpCurrency_liverpool_ivf = val
          if gbpCurrency_liverpool_ivf is not None:
              usdCurrency_liverpool_ivf = val * gbpToUsd
              eurCurrency_liverpool_ivf = val * gbpToEur
          else:
              usdCurrency_liverpool_ivf = None
              eurCurrency_liverpool_ivf = None

      queryset_list_liverpool_egg = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_liverpool_egg.items():
          gbpCurrency_liverpool_egg = val
          if gbpCurrency_liverpool_egg is not None:
              usdCurrency_liverpool_egg = val * gbpToUsd
              eurCurrency_liverpool_egg = val * gbpToEur
          else:
              usdCurrency_liverpool_egg = None
              eurCurrency_liverpool_egg = None

      queryset_list_liverpool_embryo = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_liverpool_embryo.items():
          gbpCurrency_liverpool_embryo = val
          if gbpCurrency_liverpool_embryo is not None:
              usdCurrency_liverpool_embryo = val * gbpToUsd
              eurCurrency_liverpool_embryo = val * gbpToEur
          else:
              usdCurrency_liverpool_embryo = None
              eurCurrency_liverpool_embryo = None

      queryset_list_liverpool_sperm = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_liverpool_sperm.items():
          gbpCurrency_liverpool_sperm = val
          if gbpCurrency_liverpool_sperm is not None:
              usdCurrency_liverpool_sperm = val * gbpToUsd
              eurCurrency_liverpool_sperm = val * gbpToEur
          else:
              usdCurrency_liverpool_sperm = None
              eurCurrency_liverpool_sperm = None

      queryset_list_liverpool_icsi = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_liverpool_icsi.items():
          gbpCurrency_liverpool_icsi = val
          if gbpCurrency_liverpool_icsi is not None:
              usdCurrency_liverpool_icsi = val * gbpToUsd
              eurCurrency_liverpool_icsi = val * gbpToEur
          else:
              usdCurrency_liverpool_icsi = None
              eurCurrency_liverpool_icsi = None

      queryset_list_liverpool_iui = queryset_list_liverpool.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_liverpool_iui.items():
          gbpCurrency_liverpool_iui = val
          if gbpCurrency_liverpool_iui is not None:
              usdCurrency_liverpool_iui = val * gbpToUsd
              eurCurrency_liverpool_iui = val * gbpToEur
          else:
              usdCurrency_liverpool_iui = None
              eurCurrency_liverpool_iui = None

    #--------------------------------------------------------------------------
      queryset_list_london = queryset_list_uk.filter(clinicRegion__iexact='London')
      my_total_count_london = queryset_list_london.count()
      queryset_list_london_ivf = queryset_list_london.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_london_ivf.items():
          gbpCurrency_london_ivf = val
          if gbpCurrency_london_ivf is not None:
              usdCurrency_london_ivf = val * gbpToUsd
              eurCurrency_london_ivf = val * gbpToEur
          else:
              usdCurrency_london_ivf = None
              eurCurrency_london_ivf = None

      queryset_list_london_egg = queryset_list_london.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_london_egg.items():
          gbpCurrency_london_egg = val
          if gbpCurrency_london_egg is not None:
              usdCurrency_london_egg = val * gbpToUsd
              eurCurrency_london_egg = val * gbpToEur
          else:
              usdCurrency_london_egg = None
              eurCurrency_london_egg = None

      queryset_list_london_embryo = queryset_list_london.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_london_embryo.items():
          gbpCurrency_london_embryo = val
          if gbpCurrency_london_embryo is not None:
              usdCurrency_london_embryo = val * gbpToUsd
              eurCurrency_london_embryo = val * gbpToEur
          else:
              usdCurrency_london_embryo = None
              eurCurrency_london_embryo = None

      queryset_list_london_sperm = queryset_list_london.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_london_sperm.items():
          gbpCurrency_london_sperm = val
          if gbpCurrency_london_sperm is not None:
              usdCurrency_london_sperm = val * gbpToUsd
              eurCurrency_london_sperm = val * gbpToEur
          else:
              usdCurrency_london_sperm = None
              eurCurrency_london_sperm = None

      queryset_list_london_icsi = queryset_list_london.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_london_icsi.items():
          gbpCurrency_london_icsi = val
          if gbpCurrency_london_icsi is not None:
              usdCurrency_london_icsi = val * gbpToUsd
              eurCurrency_london_icsi = val * gbpToEur
          else:
              usdCurrency_london_icsi = None
              eurCurrency_london_icsi = None

      queryset_list_london_iui = queryset_list_london.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_london_iui.items():
          gbpCurrency_london_iui = val
          if gbpCurrency_london_iui is not None:
              usdCurrency_london_iui = val * gbpToUsd
              eurCurrency_london_iui = val * gbpToEur
          else:
              usdCurrency_london_iui = None
              eurCurrency_london_iui = None

    #--------------------------------------------------------------------------
      queryset_list_manchester = queryset_list_uk.filter(clinicRegion__iexact='Manchester')
      my_total_count_manchester = queryset_list_manchester.count()
      queryset_list_manchester_ivf = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_manchester_ivf.items():
          gbpCurrency_manchester_ivf = val
          if gbpCurrency_manchester_ivf is not None:
              usdCurrency_manchester_ivf = val * gbpToUsd
              eurCurrency_manchester_ivf = val * gbpToEur
          else:
              usdCurrency_manchester_ivf = None
              eurCurrency_manchester_ivf = None

      queryset_list_manchester_egg = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_manchester_egg.items():
          gbpCurrency_manchester_egg = val
          if gbpCurrency_manchester_egg is not None:
              usdCurrency_manchester_egg = val * gbpToUsd
              eurCurrency_manchester_egg = val * gbpToEur
          else:
              usdCurrency_manchester_egg = None
              eurCurrency_manchester_egg = None

      queryset_list_manchester_embryo = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_manchester_embryo.items():
          gbpCurrency_manchester_embryo = val
          if gbpCurrency_manchester_embryo is not None:
              usdCurrency_manchester_embryo = val * gbpToUsd
              eurCurrency_manchester_embryo = val * gbpToEur
          else:
              usdCurrency_manchester_embryo = None
              eurCurrency_manchester_embryo = None

      queryset_list_manchester_sperm = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_manchester_sperm.items():
          gbpCurrency_manchester_sperm = val
          if gbpCurrency_manchester_sperm is not None:
              usdCurrency_manchester_sperm = val * gbpToUsd
              eurCurrency_manchester_sperm = val * gbpToEur
          else:
              usdCurrency_manchester_sperm = None
              eurCurrency_manchester_sperm = None

      queryset_list_manchester_icsi = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_manchester_icsi.items():
          gbpCurrency_manchester_icsi = val
          if gbpCurrency_manchester_icsi is not None:
              usdCurrency_manchester_icsi = val * gbpToUsd
              eurCurrency_manchester_icsi = val * gbpToEur
          else:
              usdCurrency_manchester_icsi = None
              eurCurrency_manchester_icsi = None

      queryset_list_manchester_iui = queryset_list_manchester.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_manchester_iui.items():
          gbpCurrency_manchester_iui = val
          if gbpCurrency_manchester_iui is not None:
              usdCurrency_manchester_iui = val * gbpToUsd
              eurCurrency_manchester_iui = val * gbpToEur
          else:
              usdCurrency_manchester_iui = None
              eurCurrency_manchester_iui = None

    #--------------------------------------------------------------------------
      queryset_list_middlesbrough = queryset_list_uk.filter(clinicRegion__iexact='Middlesbrough')
      my_total_count_middlesbrough = queryset_list_middlesbrough.count()
      queryset_list_middlesbrough_ivf = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_middlesbrough_ivf.items():
          gbpCurrency_middlesbrough_ivf = val
          if gbpCurrency_middlesbrough_ivf is not None:
              usdCurrency_middlesbrough_ivf = val * gbpToUsd
              eurCurrency_middlesbrough_ivf = val * gbpToEur
          else:
              usdCurrency_middlesbrough_ivf = None
              eurCurrency_middlesbrough_ivf = None

      queryset_list_middlesbrough_egg = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_middlesbrough_egg.items():
          gbpCurrency_middlesbrough_egg = val
          if gbpCurrency_middlesbrough_egg is not None:
              usdCurrency_middlesbrough_egg = val * gbpToUsd
              eurCurrency_middlesbrough_egg = val * gbpToEur
          else:
              usdCurrency_middlesbrough_egg = None
              eurCurrency_middlesbrough_egg = None

      queryset_list_middlesbrough_embryo = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_middlesbrough_embryo.items():
          gbpCurrency_middlesbrough_embryo = val
          if gbpCurrency_middlesbrough_embryo is not None:
              usdCurrency_middlesbrough_embryo = val * gbpToUsd
              eurCurrency_middlesbrough_embryo = val * gbpToEur
          else:
              usdCurrency_middlesbrough_embryo = None
              eurCurrency_middlesbrough_embryo = None

      queryset_list_middlesbrough_sperm = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_middlesbrough_sperm.items():
          gbpCurrency_middlesbrough_sperm = val
          if gbpCurrency_middlesbrough_sperm is not None:
              usdCurrency_middlesbrough_sperm = val * gbpToUsd
              eurCurrency_middlesbrough_sperm = val * gbpToEur
          else:
              usdCurrency_middlesbrough_sperm = None
              eurCurrency_middlesbrough_sperm = None

      queryset_list_middlesbrough_icsi = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_middlesbrough_icsi.items():
          gbpCurrency_middlesbrough_icsi = val
          if gbpCurrency_middlesbrough_icsi is not None:
              usdCurrency_middlesbrough_icsi = val * gbpToUsd
              eurCurrency_middlesbrough_icsi = val * gbpToEur
          else:
              usdCurrency_middlesbrough_icsi = None
              eurCurrency_middlesbrough_icsi = None

      queryset_list_middlesbrough_iui = queryset_list_middlesbrough.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_middlesbrough_iui.items():
          gbpCurrency_middlesbrough_iui = val
          if gbpCurrency_middlesbrough_iui is not None:
              usdCurrency_middlesbrough_iui = val * gbpToUsd
              eurCurrency_middlesbrough_iui = val * gbpToEur
          else:
              usdCurrency_middlesbrough_iui = None
              eurCurrency_middlesbrough_iui = None

    #--------------------------------------------------------------------------
      queryset_list_newcastle = queryset_list_uk.filter(clinicRegion__iexact='Newcastle')
      my_total_count_newcastle = queryset_list_newcastle.count()
      queryset_list_newcastle_ivf = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_newcastle_ivf.items():
          gbpCurrency_newcastle_ivf = val
          if gbpCurrency_newcastle_ivf is not None:
              usdCurrency_newcastle_ivf = val * gbpToUsd
              eurCurrency_newcastle_ivf = val * gbpToEur
          else:
              usdCurrency_newcastle_ivf = None
              eurCurrency_newcastle_ivf = None

      queryset_list_newcastle_egg = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_newcastle_egg.items():
          gbpCurrency_newcastle_egg = val
          if gbpCurrency_newcastle_egg is not None:
              usdCurrency_newcastle_egg = val * gbpToUsd
              eurCurrency_newcastle_egg = val * gbpToEur
          else:
              usdCurrency_newcastle_egg = None
              eurCurrency_newcastle_egg = None

      queryset_list_newcastle_embryo = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_newcastle_embryo.items():
          gbpCurrency_newcastle_embryo = val
          if gbpCurrency_newcastle_embryo is not None:
              usdCurrency_newcastle_embryo = val * gbpToUsd
              eurCurrency_newcastle_embryo = val * gbpToEur
          else:
              usdCurrency_newcastle_embryo = None
              eurCurrency_newcastle_embryo = None

      queryset_list_newcastle_sperm = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_newcastle_sperm.items():
          gbpCurrency_newcastle_sperm = val
          if gbpCurrency_newcastle_sperm is not None:
              usdCurrency_newcastle_sperm = val * gbpToUsd
              eurCurrency_newcastle_sperm = val * gbpToEur
          else:
              usdCurrency_newcastle_sperm = None
              eurCurrency_newcastle_sperm = None

      queryset_list_newcastle_icsi = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_newcastle_icsi.items():
          gbpCurrency_newcastle_icsi = val
          if gbpCurrency_newcastle_icsi is not None:
              usdCurrency_newcastle_icsi = val * gbpToUsd
              eurCurrency_newcastle_icsi = val * gbpToEur
          else:
              usdCurrency_newcastle_icsi = None
              eurCurrency_newcastle_icsi = None

      queryset_list_newcastle_iui = queryset_list_newcastle.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_newcastle_iui.items():
          gbpCurrency_newcastle_iui = val
          if gbpCurrency_newcastle_iui is not None:
              usdCurrency_newcastle_iui = val * gbpToUsd
              eurCurrency_newcastle_iui = val * gbpToEur
          else:
              usdCurrency_newcastle_iui = None
              eurCurrency_newcastle_iui = None

    #--------------------------------------------------------------------------
      queryset_list_norwich = queryset_list_uk.filter(clinicRegion__iexact='Norwich')
      my_total_count_norwich = queryset_list_norwich.count()
      queryset_list_norwich_ivf = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_norwich_ivf.items():
          gbpCurrency_norwich_ivf = val
          if gbpCurrency_norwich_ivf is not None:
              usdCurrency_norwich_ivf = val * gbpToUsd
              eurCurrency_norwich_ivf = val * gbpToEur
          else:
              usdCurrency_norwich_ivf = None
              eurCurrency_norwich_ivf = None

      queryset_list_norwich_egg = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_norwich_egg.items():
          gbpCurrency_norwich_egg = val
          if gbpCurrency_norwich_egg is not None:
              usdCurrency_norwich_egg = val * gbpToUsd
              eurCurrency_norwich_egg = val * gbpToEur
          else:
              usdCurrency_norwich_egg = None
              eurCurrency_norwich_egg = None

      queryset_list_norwich_embryo = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_norwich_embryo.items():
          gbpCurrency_norwich_embryo = val
          if gbpCurrency_norwich_embryo is not None:
              usdCurrency_norwich_embryo = val * gbpToUsd
              eurCurrency_norwich_embryo = val * gbpToEur
          else:
              usdCurrency_norwich_embryo = None
              eurCurrency_norwich_embryo = None

      queryset_list_norwich_sperm = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_norwich_sperm.items():
          gbpCurrency_norwich_sperm = val
          if gbpCurrency_norwich_sperm is not None:
              usdCurrency_norwich_sperm = val * gbpToUsd
              eurCurrency_norwich_sperm = val * gbpToEur
          else:
              usdCurrency_norwich_sperm = None
              eurCurrency_norwich_sperm = None

      queryset_list_norwich_icsi = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_norwich_icsi.items():
          gbpCurrency_norwich_icsi = val
          if gbpCurrency_norwich_icsi is not None:
              usdCurrency_norwich_icsi = val * gbpToUsd
              eurCurrency_norwich_icsi = val * gbpToEur
          else:
              usdCurrency_norwich_icsi = None
              eurCurrency_norwich_icsi = None

      queryset_list_norwich_iui = queryset_list_norwich.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_norwich_iui.items():
          gbpCurrency_norwich_iui = val
          if gbpCurrency_norwich_iui is not None:
              usdCurrency_norwich_iui = val * gbpToUsd
              eurCurrency_norwich_iui = val * gbpToEur
          else:
              usdCurrency_norwich_iui = None
              eurCurrency_norwich_iui = None

    #--------------------------------------------------------------------------
      queryset_list_nottingham = queryset_list_uk.filter(clinicRegion__iexact='Nottingham')
      my_total_count_nottingham = queryset_list_nottingham.count()
      queryset_list_nottingham_ivf = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_nottingham_ivf.items():
          gbpCurrency_nottingham_ivf = val
          if gbpCurrency_nottingham_ivf is not None:
              usdCurrency_nottingham_ivf = val * gbpToUsd
              eurCurrency_nottingham_ivf = val * gbpToEur
          else:
              usdCurrency_nottingham_ivf = None
              eurCurrency_nottingham_ivf = None

      queryset_list_nottingham_egg = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_nottingham_egg.items():
          gbpCurrency_nottingham_egg = val
          if gbpCurrency_nottingham_egg is not None:
              usdCurrency_nottingham_egg = val * gbpToUsd
              eurCurrency_nottingham_egg = val * gbpToEur
          else:
              usdCurrency_nottingham_egg = None
              eurCurrency_nottingham_egg = None

      queryset_list_nottingham_embryo = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_nottingham_embryo.items():
          gbpCurrency_nottingham_embryo = val
          if gbpCurrency_nottingham_embryo is not None:
              usdCurrency_nottingham_embryo = val * gbpToUsd
              eurCurrency_nottingham_embryo = val * gbpToEur
          else:
              usdCurrency_nottingham_embryo = None
              eurCurrency_nottingham_embryo = None

      queryset_list_nottingham_sperm = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_nottingham_sperm.items():
          gbpCurrency_nottingham_sperm = val
          if gbpCurrency_nottingham_sperm is not None:
              usdCurrency_nottingham_sperm = val * gbpToUsd
              eurCurrency_nottingham_sperm = val * gbpToEur
          else:
              usdCurrency_nottingham_sperm = None
              eurCurrency_nottingham_sperm = None

      queryset_list_nottingham_icsi = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_nottingham_icsi.items():
          gbpCurrency_nottingham_icsi = val
          if gbpCurrency_nottingham_icsi is not None:
              usdCurrency_nottingham_icsi = val * gbpToUsd
              eurCurrency_nottingham_icsi = val * gbpToEur
          else:
              usdCurrency_nottingham_icsi = None
              eurCurrency_nottingham_icsi = None

      queryset_list_nottingham_iui = queryset_list_nottingham.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_nottingham_iui.items():
          gbpCurrency_nottingham_iui = val
          if gbpCurrency_nottingham_iui is not None:
              usdCurrency_nottingham_iui = val * gbpToUsd
              eurCurrency_nottingham_iui = val * gbpToEur
          else:
              usdCurrency_nottingham_iui = None
              eurCurrency_nottingham_iui = None

    #--------------------------------------------------------------------------
      queryset_list_oxford = queryset_list_uk.filter(clinicRegion__iexact='Oxford')
      my_total_count_oxford = queryset_list_oxford.count()
      queryset_list_oxford_ivf = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_oxford_ivf.items():
          gbpCurrency_oxford_ivf = val
          if gbpCurrency_oxford_ivf is not None:
              usdCurrency_oxford_ivf = val * gbpToUsd
              eurCurrency_oxford_ivf = val * gbpToEur
          else:
              usdCurrency_oxford_ivf = None
              eurCurrency_oxford_ivf = None

      queryset_list_oxford_egg = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_oxford_egg.items():
          gbpCurrency_oxford_egg = val
          if gbpCurrency_oxford_egg is not None:
              usdCurrency_oxford_egg = val * gbpToUsd
              eurCurrency_oxford_egg = val * gbpToEur
          else:
              usdCurrency_oxford_egg = None
              eurCurrency_oxford_egg = None

      queryset_list_oxford_embryo = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_oxford_embryo.items():
          gbpCurrency_oxford_embryo = val
          if gbpCurrency_oxford_embryo is not None:
              usdCurrency_oxford_embryo = val * gbpToUsd
              eurCurrency_oxford_embryo = val * gbpToEur
          else:
              usdCurrency_oxford_embryo = None
              eurCurrency_oxford_embryo = None

      queryset_list_oxford_sperm = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_oxford_sperm.items():
          gbpCurrency_oxford_sperm = val
          if gbpCurrency_oxford_sperm is not None:
              usdCurrency_oxford_sperm = val * gbpToUsd
              eurCurrency_oxford_sperm = val * gbpToEur
          else:
              usdCurrency_oxford_sperm = None
              eurCurrency_oxford_sperm = None

      queryset_list_oxford_icsi = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_oxford_icsi.items():
          gbpCurrency_oxford_icsi = val
          if gbpCurrency_oxford_icsi is not None:
              usdCurrency_oxford_icsi = val * gbpToUsd
              eurCurrency_oxford_icsi = val * gbpToEur
          else:
              usdCurrency_oxford_icsi = None
              eurCurrency_oxford_icsi = None

      queryset_list_oxford_iui = queryset_list_oxford.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_oxford_iui.items():
          gbpCurrency_oxford_iui = val
          if gbpCurrency_oxford_iui is not None:
              usdCurrency_oxford_iui = val * gbpToUsd
              eurCurrency_oxford_iui = val * gbpToEur
          else:
              usdCurrency_oxford_iui = None
              eurCurrency_oxford_iui = None

    #--------------------------------------------------------------------------
      queryset_list_peterborough = queryset_list_uk.filter(clinicRegion__iexact='Peterborough')
      my_total_count_peterborough = queryset_list_peterborough.count()
      queryset_list_peterborough_ivf = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_peterborough_ivf.items():
          gbpCurrency_peterborough_ivf = val
          if gbpCurrency_peterborough_ivf is not None:
              usdCurrency_peterborough_ivf = val * gbpToUsd
              eurCurrency_peterborough_ivf = val * gbpToEur
          else:
              usdCurrency_peterborough_ivf = None
              eurCurrency_peterborough_ivf = None

      queryset_list_peterborough_egg = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_peterborough_egg.items():
          gbpCurrency_peterborough_egg = val
          if gbpCurrency_peterborough_egg is not None:
              usdCurrency_peterborough_egg = val * gbpToUsd
              eurCurrency_peterborough_egg = val * gbpToEur
          else:
              usdCurrency_peterborough_egg = None
              eurCurrency_peterborough_egg = None

      queryset_list_peterborough_embryo = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_peterborough_embryo.items():
          gbpCurrency_peterborough_embryo = val
          if gbpCurrency_peterborough_embryo is not None:
              usdCurrency_peterborough_embryo = val * gbpToUsd
              eurCurrency_peterborough_embryo = val * gbpToEur
          else:
              usdCurrency_peterborough_embryo = None
              eurCurrency_peterborough_embryo = None

      queryset_list_peterborough_sperm = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_peterborough_sperm.items():
          gbpCurrency_peterborough_sperm = val
          if gbpCurrency_peterborough_sperm is not None:
              usdCurrency_peterborough_sperm = val * gbpToUsd
              eurCurrency_peterborough_sperm = val * gbpToEur
          else:
              usdCurrency_peterborough_sperm = None
              eurCurrency_peterborough_sperm = None

      queryset_list_peterborough_icsi = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_peterborough_icsi.items():
          gbpCurrency_peterborough_icsi = val
          if gbpCurrency_peterborough_icsi is not None:
              usdCurrency_peterborough_icsi = val * gbpToUsd
              eurCurrency_peterborough_icsi = val * gbpToEur
          else:
              usdCurrency_peterborough_icsi = None
              eurCurrency_peterborough_icsi = None

      queryset_list_peterborough_iui = queryset_list_peterborough.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_peterborough_iui.items():
          gbpCurrency_peterborough_iui = val
          if gbpCurrency_peterborough_iui is not None:
              usdCurrency_peterborough_iui = val * gbpToUsd
              eurCurrency_peterborough_iui = val * gbpToEur
          else:
              usdCurrency_peterborough_iui = None
              eurCurrency_peterborough_iui = None

    #--------------------------------------------------------------------------
      queryset_list_plymouth = queryset_list_uk.filter(clinicRegion__iexact='Plymouth')
      my_total_count_plymouth = queryset_list_plymouth.count()
      queryset_list_plymouth_ivf = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_plymouth_ivf.items():
          gbpCurrency_plymouth_ivf = val
          if gbpCurrency_plymouth_ivf is not None:
              usdCurrency_plymouth_ivf = val * gbpToUsd
              eurCurrency_plymouth_ivf = val * gbpToEur
          else:
              usdCurrency_plymouth_ivf = None
              eurCurrency_plymouth_ivf = None

      queryset_list_plymouth_egg = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_plymouth_egg.items():
          gbpCurrency_plymouth_egg = val
          if gbpCurrency_plymouth_egg is not None:
              usdCurrency_plymouth_egg = val * gbpToUsd
              eurCurrency_plymouth_egg = val * gbpToEur
          else:
              usdCurrency_plymouth_egg = None
              eurCurrency_plymouth_egg = None

      queryset_list_plymouth_embryo = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_plymouth_embryo.items():
          gbpCurrency_plymouth_embryo = val
          if gbpCurrency_plymouth_embryo is not None:
              usdCurrency_plymouth_embryo = val * gbpToUsd
              eurCurrency_plymouth_embryo = val * gbpToEur
          else:
              usdCurrency_plymouth_embryo = None
              eurCurrency_plymouth_embryo = None

      queryset_list_plymouth_sperm = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_plymouth_sperm.items():
          gbpCurrency_plymouth_sperm = val
          if gbpCurrency_plymouth_sperm is not None:
              usdCurrency_plymouth_sperm = val * gbpToUsd
              eurCurrency_plymouth_sperm = val * gbpToEur
          else:
              usdCurrency_plymouth_sperm = None
              eurCurrency_plymouth_sperm = None

      queryset_list_plymouth_icsi = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_plymouth_icsi.items():
          gbpCurrency_plymouth_icsi = val
          if gbpCurrency_plymouth_icsi is not None:
              usdCurrency_plymouth_icsi = val * gbpToUsd
              eurCurrency_plymouth_icsi = val * gbpToEur
          else:
              usdCurrency_plymouth_icsi = None
              eurCurrency_plymouth_icsi = None

      queryset_list_plymouth_iui = queryset_list_plymouth.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_plymouth_iui.items():
          gbpCurrency_plymouth_iui = val
          if gbpCurrency_plymouth_iui is not None:
              usdCurrency_plymouth_iui = val * gbpToUsd
              eurCurrency_plymouth_iui = val * gbpToEur
          else:
              usdCurrency_plymouth_iui = None
              eurCurrency_plymouth_iui = None

    #--------------------------------------------------------------------------
      queryset_list_portsmouth = queryset_list_uk.filter(clinicRegion__iexact='Portsmouth')
      my_total_count_portsmouth = queryset_list_portsmouth.count()
      queryset_list_portsmouth_ivf = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_portsmouth_ivf.items():
          gbpCurrency_portsmouth_ivf = val
          if gbpCurrency_portsmouth_ivf is not None:
              usdCurrency_portsmouth_ivf = val * gbpToUsd
              eurCurrency_portsmouth_ivf = val * gbpToEur
          else:
              usdCurrency_portsmouth_ivf = None
              eurCurrency_portsmouth_ivf = None

      queryset_list_portsmouth_egg = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_portsmouth_egg.items():
          gbpCurrency_portsmouth_egg = val
          if gbpCurrency_portsmouth_egg is not None:
              usdCurrency_portsmouth_egg = val * gbpToUsd
              eurCurrency_portsmouth_egg = val * gbpToEur
          else:
              usdCurrency_portsmouth_egg = None
              eurCurrency_portsmouth_egg = None

      queryset_list_portsmouth_embryo = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_portsmouth_embryo.items():
          gbpCurrency_portsmouth_embryo = val
          if gbpCurrency_portsmouth_embryo is not None:
              usdCurrency_portsmouth_embryo = val * gbpToUsd
              eurCurrency_portsmouth_embryo = val * gbpToEur
          else:
              usdCurrency_portsmouth_embryo = None
              eurCurrency_portsmouth_embryo = None

      queryset_list_portsmouth_sperm = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_portsmouth_sperm.items():
          gbpCurrency_portsmouth_sperm = val
          if gbpCurrency_portsmouth_sperm is not None:
              usdCurrency_portsmouth_sperm = val * gbpToUsd
              eurCurrency_portsmouth_sperm = val * gbpToEur
          else:
              usdCurrency_portsmouth_sperm = None
              eurCurrency_portsmouth_sperm = None

      queryset_list_portsmouth_icsi = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_portsmouth_icsi.items():
          gbpCurrency_portsmouth_icsi = val
          if gbpCurrency_portsmouth_icsi is not None:
              usdCurrency_portsmouth_icsi = val * gbpToUsd
              eurCurrency_portsmouth_icsi = val * gbpToEur
          else:
              usdCurrency_portsmouth_icsi = None
              eurCurrency_portsmouth_icsi = None

      queryset_list_portsmouth_iui = queryset_list_portsmouth.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_portsmouth_iui.items():
          gbpCurrency_portsmouth_iui = val
          if gbpCurrency_portsmouth_iui is not None:
              usdCurrency_portsmouth_iui = val * gbpToUsd
              eurCurrency_portsmouth_iui = val * gbpToEur
          else:
              usdCurrency_portsmouth_iui = None
              eurCurrency_portsmouth_iui = None

    #--------------------------------------------------------------------------
      queryset_list_salisbury = queryset_list_uk.filter(clinicRegion__iexact='Salisbury')
      my_total_count_salisbury = queryset_list_salisbury.count()
      queryset_list_salisbury_ivf = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_salisbury_ivf.items():
          gbpCurrency_salisbury_ivf = val
          if gbpCurrency_salisbury_ivf is not None:
              usdCurrency_salisbury_ivf = val * gbpToUsd
              eurCurrency_salisbury_ivf = val * gbpToEur
          else:
              usdCurrency_salisbury_ivf = None
              eurCurrency_salisbury_ivf = None

      queryset_list_salisbury_egg = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_salisbury_egg.items():
          gbpCurrency_salisbury_egg = val
          if gbpCurrency_salisbury_egg is not None:
              usdCurrency_salisbury_egg = val * gbpToUsd
              eurCurrency_salisbury_egg = val * gbpToEur
          else:
              usdCurrency_salisbury_egg = None
              eurCurrency_salisbury_egg = None

      queryset_list_salisbury_embryo = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_salisbury_embryo.items():
          gbpCurrency_salisbury_embryo = val
          if gbpCurrency_salisbury_embryo is not None:
              usdCurrency_salisbury_embryo = val * gbpToUsd
              eurCurrency_salisbury_embryo = val * gbpToEur
          else:
              usdCurrency_salisbury_embryo = None
              eurCurrency_salisbury_embryo = None

      queryset_list_salisbury_sperm = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_salisbury_sperm.items():
          gbpCurrency_salisbury_sperm = val
          if gbpCurrency_salisbury_sperm is not None:
              usdCurrency_salisbury_sperm = val * gbpToUsd
              eurCurrency_salisbury_sperm = val * gbpToEur
          else:
              usdCurrency_salisbury_sperm = None
              eurCurrency_salisbury_sperm = None

      queryset_list_salisbury_icsi = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_salisbury_icsi.items():
          gbpCurrency_salisbury_icsi = val
          if gbpCurrency_salisbury_icsi is not None:
              usdCurrency_salisbury_icsi = val * gbpToUsd
              eurCurrency_salisbury_icsi = val * gbpToEur
          else:
              usdCurrency_salisbury_icsi = None
              eurCurrency_salisbury_icsi = None

      queryset_list_salisbury_iui = queryset_list_salisbury.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_salisbury_iui.items():
          gbpCurrency_salisbury_iui = val
          if gbpCurrency_salisbury_iui is not None:
              usdCurrency_salisbury_iui = val * gbpToUsd
              eurCurrency_salisbury_iui = val * gbpToEur
          else:
              usdCurrency_salisbury_iui = None
              eurCurrency_salisbury_iui = None

    #--------------------------------------------------------------------------
      queryset_list_sheffield = queryset_list_uk.filter(clinicRegion__iexact='Sheffield')
      my_total_count_sheffield = queryset_list_sheffield.count()
      queryset_list_sheffield_ivf = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_sheffield_ivf.items():
          gbpCurrency_sheffield_ivf = val
          if gbpCurrency_sheffield_ivf is not None:
              usdCurrency_sheffield_ivf = val * gbpToUsd
              eurCurrency_sheffield_ivf = val * gbpToEur
          else:
              usdCurrency_sheffield_ivf = None
              eurCurrency_sheffield_ivf = None

      queryset_list_sheffield_egg = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_sheffield_egg.items():
          gbpCurrency_sheffield_egg = val
          if gbpCurrency_sheffield_egg is not None:
              usdCurrency_sheffield_egg = val * gbpToUsd
              eurCurrency_sheffield_egg = val * gbpToEur
          else:
              usdCurrency_sheffield_egg = None
              eurCurrency_sheffield_egg = None

      queryset_list_sheffield_embryo = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_sheffield_embryo.items():
          gbpCurrency_sheffield_embryo = val
          if gbpCurrency_sheffield_embryo is not None:
              usdCurrency_sheffield_embryo = val * gbpToUsd
              eurCurrency_sheffield_embryo = val * gbpToEur
          else:
              usdCurrency_sheffield_embryo = None
              eurCurrency_sheffield_embryo = None

      queryset_list_sheffield_sperm = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_sheffield_sperm.items():
          gbpCurrency_sheffield_sperm = val
          if gbpCurrency_sheffield_sperm is not None:
              usdCurrency_sheffield_sperm = val * gbpToUsd
              eurCurrency_sheffield_sperm = val * gbpToEur
          else:
              usdCurrency_sheffield_sperm = None
              eurCurrency_sheffield_sperm = None

      queryset_list_sheffield_icsi = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_sheffield_icsi.items():
          gbpCurrency_sheffield_icsi = val
          if gbpCurrency_sheffield_icsi is not None:
              usdCurrency_sheffield_icsi = val * gbpToUsd
              eurCurrency_sheffield_icsi = val * gbpToEur
          else:
              usdCurrency_sheffield_icsi = None
              eurCurrency_sheffield_icsi = None

      queryset_list_sheffield_iui = queryset_list_sheffield.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_sheffield_iui.items():
          gbpCurrency_sheffield_iui = val
          if gbpCurrency_sheffield_iui is not None:
              usdCurrency_sheffield_iui = val * gbpToUsd
              eurCurrency_sheffield_iui = val * gbpToEur
          else:
              usdCurrency_sheffield_iui = None
              eurCurrency_sheffield_iui = None

    #--------------------------------------------------------------------------
      queryset_list_southampton = queryset_list_uk.filter(clinicRegion__iexact='Southampton')
      my_total_count_southampton = queryset_list_southampton.count()
      queryset_list_southampton_ivf = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_southampton_ivf.items():
          gbpCurrency_southampton_ivf = val
          if gbpCurrency_southampton_ivf is not None:
              usdCurrency_southampton_ivf = val * gbpToUsd
              eurCurrency_southampton_ivf = val * gbpToEur
          else:
              usdCurrency_southampton_ivf = None
              eurCurrency_southampton_ivf = None

      queryset_list_southampton_egg = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_southampton_egg.items():
          gbpCurrency_southampton_egg = val
          if gbpCurrency_southampton_egg is not None:
              usdCurrency_southampton_egg = val * gbpToUsd
              eurCurrency_southampton_egg = val * gbpToEur
          else:
              usdCurrency_southampton_egg = None
              eurCurrency_southampton_egg = None

      queryset_list_southampton_embryo = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_southampton_embryo.items():
          gbpCurrency_southampton_embryo = val
          if gbpCurrency_southampton_embryo is not None:
              usdCurrency_southampton_embryo = val * gbpToUsd
              eurCurrency_southampton_embryo = val * gbpToEur
          else:
              usdCurrency_southampton_embryo = None
              eurCurrency_southampton_embryo = None

      queryset_list_southampton_sperm = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_southampton_sperm.items():
          gbpCurrency_southampton_sperm = val
          if gbpCurrency_southampton_sperm is not None:
              usdCurrency_southampton_sperm = val * gbpToUsd
              eurCurrency_southampton_sperm = val * gbpToEur
          else:
              usdCurrency_southampton_sperm = None
              eurCurrency_southampton_sperm = None

      queryset_list_southampton_icsi = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_southampton_icsi.items():
          gbpCurrency_southampton_icsi = val
          if gbpCurrency_southampton_icsi is not None:
              usdCurrency_southampton_icsi = val * gbpToUsd
              eurCurrency_southampton_icsi = val * gbpToEur
          else:
              usdCurrency_southampton_icsi = None
              eurCurrency_southampton_icsi = None

      queryset_list_southampton_iui = queryset_list_southampton.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_southampton_iui.items():
          gbpCurrency_southampton_iui = val
          if gbpCurrency_southampton_iui is not None:
              usdCurrency_southampton_iui = val * gbpToUsd
              eurCurrency_southampton_iui = val * gbpToEur
          else:
              usdCurrency_southampton_iui = None
              eurCurrency_southampton_iui = None

        #--------------------------------------------------------------------------
      queryset_list_swansea = queryset_list_uk.filter(clinicRegion__iexact='Swansea')
      my_total_count_swansea = queryset_list_swansea.count()
      queryset_list_swansea_ivf = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
      for key,val in queryset_list_swansea_ivf.items():
          gbpCurrency_swansea_ivf = val
          if gbpCurrency_swansea_ivf is not None:
              usdCurrency_swansea_ivf = val * gbpToUsd
              eurCurrency_swansea_ivf = val * gbpToEur
          else:
              usdCurrency_swansea_ivf = None
              eurCurrency_swansea_ivf = None

      queryset_list_swansea_egg = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
      for key,val in queryset_list_swansea_egg.items():
          gbpCurrency_swansea_egg = val
          if gbpCurrency_swansea_egg is not None:
              usdCurrency_swansea_egg = val * gbpToUsd
              eurCurrency_swansea_egg = val * gbpToEur
          else:
              usdCurrency_swansea_egg = None
              eurCurrency_swansea_egg = None

      queryset_list_swansea_embryo = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
      for key,val in queryset_list_swansea_embryo.items():
          gbpCurrency_swansea_embryo = val
          if gbpCurrency_swansea_embryo is not None:
              usdCurrency_swansea_embryo = val * gbpToUsd
              eurCurrency_swansea_embryo = val * gbpToEur
          else:
              usdCurrency_swansea_embryo = None
              eurCurrency_swansea_embryo = None

      queryset_list_swansea_sperm = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
      for key,val in queryset_list_swansea_sperm.items():
          gbpCurrency_swansea_sperm = val
          if gbpCurrency_swansea_sperm is not None:
              usdCurrency_swansea_sperm = val * gbpToUsd
              eurCurrency_swansea_sperm = val * gbpToEur
          else:
              usdCurrency_swansea_sperm = None
              eurCurrency_swansea_sperm = None

      queryset_list_swansea_icsi = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
      for key,val in queryset_list_swansea_icsi.items():
          gbpCurrency_swansea_icsi = val
          if gbpCurrency_swansea_icsi is not None:
              usdCurrency_swansea_icsi = val * gbpToUsd
              eurCurrency_swansea_icsi = val * gbpToEur
          else:
              usdCurrency_swansea_icsi = None
              eurCurrency_swansea_icsi = None

      queryset_list_swansea_iui = queryset_list_swansea.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
      for key,val in queryset_list_swansea_iui.items():
          gbpCurrency_swansea_iui = val
          if gbpCurrency_swansea_iui is not None:
              usdCurrency_swansea_iui = val * gbpToUsd
              eurCurrency_swansea_iui = val * gbpToEur
          else:
              usdCurrency_swansea_iui = None
              eurCurrency_swansea_iui = None

    context = {
        'gbpCurrency_aberdeen_ivf': gbpCurrency_aberdeen_ivf,
        'usdCurrency_aberdeen_ivf': usdCurrency_aberdeen_ivf,
        'eurCurrency_aberdeen_ivf': eurCurrency_aberdeen_ivf,
        'gbpCurrency_aberdeen_egg': gbpCurrency_aberdeen_egg,
        'usdCurrency_aberdeen_egg': usdCurrency_aberdeen_egg,
        'eurCurrency_aberdeen_egg': eurCurrency_aberdeen_egg,
        'gbpCurrency_aberdeen_embryo': gbpCurrency_aberdeen_embryo,
        'usdCurrency_aberdeen_embryo': usdCurrency_aberdeen_embryo,
        'eurCurrency_aberdeen_embryo': eurCurrency_aberdeen_embryo,
        'gbpCurrency_aberdeen_sperm': gbpCurrency_aberdeen_sperm,
        'usdCurrency_aberdeen_sperm': usdCurrency_aberdeen_sperm,
        'eurCurrency_aberdeen_sperm': eurCurrency_aberdeen_sperm,
        'gbpCurrency_aberdeen_icsi': gbpCurrency_aberdeen_icsi,
        'usdCurrency_aberdeen_icsi': usdCurrency_aberdeen_icsi,
        'eurCurrency_aberdeen_icsi': eurCurrency_aberdeen_icsi,
        'gbpCurrency_aberdeen_iui': gbpCurrency_aberdeen_iui,
        'usdCurrency_aberdeen_iui': usdCurrency_aberdeen_iui,
        'eurCurrency_aberdeen_iui': eurCurrency_aberdeen_iui,
        'my_total_count_aberdeen': my_total_count_aberdeen,

        'gbpCurrency_bath_ivf': gbpCurrency_bath_ivf,
        'usdCurrency_bath_ivf': usdCurrency_bath_ivf,
        'eurCurrency_bath_ivf': eurCurrency_bath_ivf,
        'gbpCurrency_bath_egg': gbpCurrency_bath_egg,
        'usdCurrency_bath_egg': usdCurrency_bath_egg,
        'eurCurrency_bath_egg': eurCurrency_bath_egg,
        'gbpCurrency_bath_embryo': gbpCurrency_bath_embryo,
        'usdCurrency_bath_embryo': usdCurrency_bath_embryo,
        'eurCurrency_bath_embryo': eurCurrency_bath_embryo,
        'gbpCurrency_bath_sperm': gbpCurrency_bath_sperm,
        'usdCurrency_bath_sperm': usdCurrency_bath_sperm,
        'eurCurrency_bath_sperm': eurCurrency_bath_sperm,
        'gbpCurrency_bath_icsi': gbpCurrency_bath_icsi,
        'usdCurrency_bath_icsi': usdCurrency_bath_icsi,
        'eurCurrency_bath_icsi': eurCurrency_bath_icsi,
        'gbpCurrency_bath_iui': gbpCurrency_bath_iui,
        'usdCurrency_bath_iui': usdCurrency_bath_iui,
        'eurCurrency_bath_iui': eurCurrency_bath_iui,
        'my_total_count_bath': my_total_count_bath,

        'gbpCurrency_belfast_ivf': gbpCurrency_belfast_ivf,
        'usdCurrency_belfast_ivf': usdCurrency_belfast_ivf,
        'eurCurrency_belfast_ivf': eurCurrency_belfast_ivf,
        'gbpCurrency_belfast_egg': gbpCurrency_belfast_egg,
        'usdCurrency_belfast_egg': usdCurrency_belfast_egg,
        'eurCurrency_belfast_egg': eurCurrency_belfast_egg,
        'gbpCurrency_belfast_embryo': gbpCurrency_belfast_embryo,
        'usdCurrency_belfast_embryo': usdCurrency_belfast_embryo,
        'eurCurrency_belfast_embryo': eurCurrency_belfast_embryo,
        'gbpCurrency_belfast_sperm': gbpCurrency_belfast_sperm,
        'usdCurrency_belfast_sperm': usdCurrency_belfast_sperm,
        'eurCurrency_belfast_sperm': eurCurrency_belfast_sperm,
        'gbpCurrency_belfast_icsi': gbpCurrency_belfast_icsi,
        'usdCurrency_belfast_icsi': usdCurrency_belfast_icsi,
        'eurCurrency_belfast_icsi': eurCurrency_belfast_icsi,
        'gbpCurrency_belfast_iui': gbpCurrency_belfast_iui,
        'usdCurrency_belfast_iui': usdCurrency_belfast_iui,
        'eurCurrency_belfast_iui': eurCurrency_belfast_iui,
        'my_total_count_belfast': my_total_count_belfast,

        'gbpCurrency_birmingham_ivf': gbpCurrency_birmingham_ivf,
        'usdCurrency_birmingham_ivf': usdCurrency_birmingham_ivf,
        'eurCurrency_birmingham_ivf': eurCurrency_birmingham_ivf,
        'gbpCurrency_birmingham_egg': gbpCurrency_birmingham_egg,
        'usdCurrency_birmingham_egg': usdCurrency_birmingham_egg,
        'eurCurrency_birmingham_egg': eurCurrency_birmingham_egg,
        'gbpCurrency_birmingham_embryo': gbpCurrency_birmingham_embryo,
        'usdCurrency_birmingham_embryo': usdCurrency_birmingham_embryo,
        'eurCurrency_birmingham_embryo': eurCurrency_birmingham_embryo,
        'gbpCurrency_birmingham_sperm': gbpCurrency_birmingham_sperm,
        'usdCurrency_birmingham_sperm': usdCurrency_birmingham_sperm,
        'eurCurrency_birmingham_sperm': eurCurrency_birmingham_sperm,
        'gbpCurrency_birmingham_icsi': gbpCurrency_birmingham_icsi,
        'usdCurrency_birmingham_icsi': usdCurrency_birmingham_icsi,
        'eurCurrency_birmingham_icsi': eurCurrency_birmingham_icsi,
        'gbpCurrency_birmingham_iui': gbpCurrency_birmingham_iui,
        'usdCurrency_birmingham_iui': usdCurrency_birmingham_iui,
        'eurCurrency_birmingham_iui': eurCurrency_birmingham_iui,
        'my_total_count_birmingham': my_total_count_birmingham,

        'gbpCurrency_bournemouth_ivf': gbpCurrency_bournemouth_ivf,
        'usdCurrency_bournemouth_ivf': usdCurrency_bournemouth_ivf,
        'eurCurrency_bournemouth_ivf': eurCurrency_bournemouth_ivf,
        'gbpCurrency_bournemouth_egg': gbpCurrency_bournemouth_egg,
        'usdCurrency_bournemouth_egg': usdCurrency_bournemouth_egg,
        'eurCurrency_bournemouth_egg': eurCurrency_bournemouth_egg,
        'gbpCurrency_bournemouth_embryo': gbpCurrency_bournemouth_embryo,
        'usdCurrency_bournemouth_embryo': usdCurrency_bournemouth_embryo,
        'eurCurrency_bournemouth_embryo': eurCurrency_bournemouth_embryo,
        'gbpCurrency_bournemouth_sperm': gbpCurrency_bournemouth_sperm,
        'usdCurrency_bournemouth_sperm': usdCurrency_bournemouth_sperm,
        'eurCurrency_bournemouth_sperm': eurCurrency_bournemouth_sperm,
        'gbpCurrency_bournemouth_icsi': gbpCurrency_bournemouth_icsi,
        'usdCurrency_bournemouth_icsi': usdCurrency_bournemouth_icsi,
        'eurCurrency_bournemouth_icsi': eurCurrency_bournemouth_icsi,
        'gbpCurrency_bournemouth_iui': gbpCurrency_bournemouth_iui,
        'usdCurrency_bournemouth_iui': usdCurrency_bournemouth_iui,
        'eurCurrency_bournemouth_iui': eurCurrency_bournemouth_iui,
        'my_total_count_bournemouth': my_total_count_bournemouth,

        'gbpCurrency_brightonhove_ivf': gbpCurrency_brightonhove_ivf,
        'usdCurrency_brightonhove_ivf': usdCurrency_brightonhove_ivf,
        'eurCurrency_brightonhove_ivf': eurCurrency_brightonhove_ivf,
        'gbpCurrency_brightonhove_egg': gbpCurrency_brightonhove_egg,
        'usdCurrency_brightonhove_egg': usdCurrency_brightonhove_egg,
        'eurCurrency_brightonhove_egg': eurCurrency_brightonhove_egg,
        'gbpCurrency_brightonhove_embryo': gbpCurrency_brightonhove_embryo,
        'usdCurrency_brightonhove_embryo': usdCurrency_brightonhove_embryo,
        'eurCurrency_brightonhove_embryo': eurCurrency_brightonhove_embryo,
        'gbpCurrency_brightonhove_sperm': gbpCurrency_brightonhove_sperm,
        'usdCurrency_brightonhove_sperm': usdCurrency_brightonhove_sperm,
        'eurCurrency_brightonhove_sperm': eurCurrency_brightonhove_sperm,
        'gbpCurrency_brightonhove_icsi': gbpCurrency_brightonhove_icsi,
        'usdCurrency_brightonhove_icsi': usdCurrency_brightonhove_icsi,
        'eurCurrency_brightonhove_icsi': eurCurrency_brightonhove_icsi,
        'gbpCurrency_brightonhove_iui': gbpCurrency_brightonhove_iui,
        'usdCurrency_brightonhove_iui': usdCurrency_brightonhove_iui,
        'eurCurrency_brightonhove_iui': eurCurrency_brightonhove_iui,
        'my_total_count_brightonhove': my_total_count_brightonhove,

        'gbpCurrency_bristol_ivf': gbpCurrency_bristol_ivf,
        'usdCurrency_bristol_ivf': usdCurrency_bristol_ivf,
        'eurCurrency_bristol_ivf': eurCurrency_bristol_ivf,
        'gbpCurrency_bristol_egg': gbpCurrency_bristol_egg,
        'usdCurrency_bristol_egg': usdCurrency_bristol_egg,
        'eurCurrency_bristol_egg': eurCurrency_bristol_egg,
        'gbpCurrency_bristol_embryo': gbpCurrency_bristol_embryo,
        'usdCurrency_bristol_embryo': usdCurrency_bristol_embryo,
        'eurCurrency_bristol_embryo': eurCurrency_bristol_embryo,
        'gbpCurrency_bristol_sperm': gbpCurrency_bristol_sperm,
        'usdCurrency_bristol_sperm': usdCurrency_bristol_sperm,
        'eurCurrency_bristol_sperm': eurCurrency_bristol_sperm,
        'gbpCurrency_bristol_icsi': gbpCurrency_bristol_icsi,
        'usdCurrency_bristol_icsi': usdCurrency_bristol_icsi,
        'eurCurrency_bristol_icsi': eurCurrency_bristol_icsi,
        'gbpCurrency_bristol_iui': gbpCurrency_bristol_iui,
        'usdCurrency_bristol_iui': usdCurrency_bristol_iui,
        'eurCurrency_bristol_iui': eurCurrency_bristol_iui,
        'my_total_count_bristol': my_total_count_bristol,

        'gbpCurrency_cambridge_ivf': gbpCurrency_cambridge_ivf,
        'usdCurrency_cambridge_ivf': usdCurrency_cambridge_ivf,
        'eurCurrency_cambridge_ivf': eurCurrency_cambridge_ivf,
        'gbpCurrency_cambridge_egg': gbpCurrency_cambridge_egg,
        'usdCurrency_cambridge_egg': usdCurrency_cambridge_egg,
        'eurCurrency_cambridge_egg': eurCurrency_cambridge_egg,
        'gbpCurrency_cambridge_embryo': gbpCurrency_cambridge_embryo,
        'usdCurrency_cambridge_embryo': usdCurrency_cambridge_embryo,
        'eurCurrency_cambridge_embryo': eurCurrency_cambridge_embryo,
        'gbpCurrency_cambridge_sperm': gbpCurrency_cambridge_sperm,
        'usdCurrency_cambridge_sperm': usdCurrency_cambridge_sperm,
        'eurCurrency_cambridge_sperm': eurCurrency_cambridge_sperm,
        'gbpCurrency_cambridge_icsi': gbpCurrency_cambridge_icsi,
        'usdCurrency_cambridge_icsi': usdCurrency_cambridge_icsi,
        'eurCurrency_cambridge_icsi': eurCurrency_cambridge_icsi,
        'gbpCurrency_cambridge_iui': gbpCurrency_cambridge_iui,
        'usdCurrency_cambridge_iui': usdCurrency_cambridge_iui,
        'eurCurrency_cambridge_iui': eurCurrency_cambridge_iui,
        'my_total_count_cambridge': my_total_count_cambridge,

        'gbpCurrency_cardiff_ivf': gbpCurrency_cardiff_ivf,
        'usdCurrency_cardiff_ivf': usdCurrency_cardiff_ivf,
        'eurCurrency_cardiff_ivf': eurCurrency_cardiff_ivf,
        'gbpCurrency_cardiff_egg': gbpCurrency_cardiff_egg,
        'usdCurrency_cardiff_egg': usdCurrency_cardiff_egg,
        'eurCurrency_cardiff_egg': eurCurrency_cardiff_egg,
        'gbpCurrency_cardiff_embryo': gbpCurrency_cardiff_embryo,
        'usdCurrency_cardiff_embryo': usdCurrency_cardiff_embryo,
        'eurCurrency_cardiff_embryo': eurCurrency_cardiff_embryo,
        'gbpCurrency_cardiff_sperm': gbpCurrency_cardiff_sperm,
        'usdCurrency_cardiff_sperm': usdCurrency_cardiff_sperm,
        'eurCurrency_cardiff_sperm': eurCurrency_cardiff_sperm,
        'gbpCurrency_cardiff_icsi': gbpCurrency_cardiff_icsi,
        'usdCurrency_cardiff_icsi': usdCurrency_cardiff_icsi,
        'eurCurrency_cardiff_icsi': eurCurrency_cardiff_icsi,
        'gbpCurrency_cardiff_iui': gbpCurrency_cardiff_iui,
        'usdCurrency_cardiff_iui': usdCurrency_cardiff_iui,
        'eurCurrency_cardiff_iui': eurCurrency_cardiff_iui,
        'my_total_count_cardiff': my_total_count_cardiff,

        'gbpCurrency_colchester_ivf': gbpCurrency_colchester_ivf,
        'usdCurrency_colchester_ivf': usdCurrency_colchester_ivf,
        'eurCurrency_colchester_ivf': eurCurrency_colchester_ivf,
        'gbpCurrency_colchester_egg': gbpCurrency_colchester_egg,
        'usdCurrency_colchester_egg': usdCurrency_colchester_egg,
        'eurCurrency_colchester_egg': eurCurrency_colchester_egg,
        'gbpCurrency_colchester_embryo': gbpCurrency_colchester_embryo,
        'usdCurrency_colchester_embryo': usdCurrency_colchester_embryo,
        'eurCurrency_colchester_embryo': eurCurrency_colchester_embryo,
        'gbpCurrency_colchester_sperm': gbpCurrency_colchester_sperm,
        'usdCurrency_colchester_sperm': usdCurrency_colchester_sperm,
        'eurCurrency_colchester_sperm': eurCurrency_colchester_sperm,
        'gbpCurrency_colchester_icsi': gbpCurrency_colchester_icsi,
        'usdCurrency_colchester_icsi': usdCurrency_colchester_icsi,
        'eurCurrency_colchester_icsi': eurCurrency_colchester_icsi,
        'gbpCurrency_colchester_iui': gbpCurrency_colchester_iui,
        'usdCurrency_colchester_iui': usdCurrency_colchester_iui,
        'eurCurrency_colchester_iui': eurCurrency_colchester_iui,
        'my_total_count_colchester': my_total_count_colchester,

        'gbpCurrency_derby_ivf': gbpCurrency_derby_ivf,
        'usdCurrency_derby_ivf': usdCurrency_derby_ivf,
        'eurCurrency_derby_ivf': eurCurrency_derby_ivf,
        'gbpCurrency_derby_egg': gbpCurrency_derby_egg,
        'usdCurrency_derby_egg': usdCurrency_derby_egg,
        'eurCurrency_derby_egg': eurCurrency_derby_egg,
        'gbpCurrency_derby_embryo': gbpCurrency_derby_embryo,
        'usdCurrency_derby_embryo': usdCurrency_derby_embryo,
        'eurCurrency_derby_embryo': eurCurrency_derby_embryo,
        'gbpCurrency_derby_sperm': gbpCurrency_derby_sperm,
        'usdCurrency_derby_sperm': usdCurrency_derby_sperm,
        'eurCurrency_derby_sperm': eurCurrency_derby_sperm,
        'gbpCurrency_derby_icsi': gbpCurrency_derby_icsi,
        'usdCurrency_derby_icsi': usdCurrency_derby_icsi,
        'eurCurrency_derby_icsi': eurCurrency_derby_icsi,
        'gbpCurrency_derby_iui': gbpCurrency_derby_iui,
        'usdCurrency_derby_iui': usdCurrency_derby_iui,
        'eurCurrency_derby_iui': eurCurrency_derby_iui,
        'my_total_count_derby': my_total_count_derby,

        'gbpCurrency_exeter_ivf': gbpCurrency_exeter_ivf,
        'usdCurrency_exeter_ivf': usdCurrency_exeter_ivf,
        'eurCurrency_exeter_ivf': eurCurrency_exeter_ivf,
        'gbpCurrency_exeter_egg': gbpCurrency_exeter_egg,
        'usdCurrency_exeter_egg': usdCurrency_exeter_egg,
        'eurCurrency_exeter_egg': eurCurrency_exeter_egg,
        'gbpCurrency_exeter_embryo': gbpCurrency_exeter_embryo,
        'usdCurrency_exeter_embryo': usdCurrency_exeter_embryo,
        'eurCurrency_exeter_embryo': eurCurrency_exeter_embryo,
        'gbpCurrency_exeter_sperm': gbpCurrency_exeter_sperm,
        'usdCurrency_exeter_sperm': usdCurrency_exeter_sperm,
        'eurCurrency_exeter_sperm': eurCurrency_exeter_sperm,
        'gbpCurrency_exeter_icsi': gbpCurrency_exeter_icsi,
        'usdCurrency_exeter_icsi': usdCurrency_exeter_icsi,
        'eurCurrency_exeter_icsi': eurCurrency_exeter_icsi,
        'gbpCurrency_exeter_iui': gbpCurrency_exeter_iui,
        'usdCurrency_exeter_iui': usdCurrency_exeter_iui,
        'eurCurrency_exeter_iui': eurCurrency_exeter_iui,
        'my_total_count_exeter': my_total_count_exeter,

        'gbpCurrency_glasgow_ivf': gbpCurrency_glasgow_ivf,
        'usdCurrency_glasgow_ivf': usdCurrency_glasgow_ivf,
        'eurCurrency_glasgow_ivf': eurCurrency_glasgow_ivf,
        'gbpCurrency_glasgow_egg': gbpCurrency_glasgow_egg,
        'usdCurrency_glasgow_egg': usdCurrency_glasgow_egg,
        'eurCurrency_glasgow_egg': eurCurrency_glasgow_egg,
        'gbpCurrency_glasgow_embryo': gbpCurrency_glasgow_embryo,
        'usdCurrency_glasgow_embryo': usdCurrency_glasgow_embryo,
        'eurCurrency_glasgow_embryo': eurCurrency_glasgow_embryo,
        'gbpCurrency_glasgow_sperm': gbpCurrency_glasgow_sperm,
        'usdCurrency_glasgow_sperm': usdCurrency_glasgow_sperm,
        'eurCurrency_glasgow_sperm': eurCurrency_glasgow_sperm,
        'gbpCurrency_glasgow_icsi': gbpCurrency_glasgow_icsi,
        'usdCurrency_glasgow_icsi': usdCurrency_glasgow_icsi,
        'eurCurrency_glasgow_icsi': eurCurrency_glasgow_icsi,
        'gbpCurrency_glasgow_iui': gbpCurrency_glasgow_iui,
        'usdCurrency_glasgow_iui': usdCurrency_glasgow_iui,
        'eurCurrency_glasgow_iui': eurCurrency_glasgow_iui,
        'my_total_count_glasgow': my_total_count_glasgow,

        'gbpCurrency_hull_ivf': gbpCurrency_hull_ivf,
        'usdCurrency_hull_ivf': usdCurrency_hull_ivf,
        'eurCurrency_hull_ivf': eurCurrency_hull_ivf,
        'gbpCurrency_hull_egg': gbpCurrency_hull_egg,
        'usdCurrency_hull_egg': usdCurrency_hull_egg,
        'eurCurrency_hull_egg': eurCurrency_hull_egg,
        'gbpCurrency_hull_embryo': gbpCurrency_hull_embryo,
        'usdCurrency_hull_embryo': usdCurrency_hull_embryo,
        'eurCurrency_hull_embryo': eurCurrency_hull_embryo,
        'gbpCurrency_hull_sperm': gbpCurrency_hull_sperm,
        'usdCurrency_hull_sperm': usdCurrency_hull_sperm,
        'eurCurrency_hull_sperm': eurCurrency_hull_sperm,
        'gbpCurrency_hull_icsi': gbpCurrency_hull_icsi,
        'usdCurrency_hull_icsi': usdCurrency_hull_icsi,
        'eurCurrency_hull_icsi': eurCurrency_hull_icsi,
        'gbpCurrency_hull_iui': gbpCurrency_hull_iui,
        'usdCurrency_hull_iui': usdCurrency_hull_iui,
        'eurCurrency_hull_iui': eurCurrency_hull_iui,
        'my_total_count_hull': my_total_count_hull,

        'gbpCurrency_chelmsford_ivf': gbpCurrency_chelmsford_ivf,
        'usdCurrency_chelmsford_ivf': usdCurrency_chelmsford_ivf,
        'eurCurrency_chelmsford_ivf': eurCurrency_chelmsford_ivf,
        'gbpCurrency_chelmsford_egg': gbpCurrency_chelmsford_egg,
        'usdCurrency_chelmsford_egg': usdCurrency_chelmsford_egg,
        'eurCurrency_chelmsford_egg': eurCurrency_chelmsford_egg,
        'gbpCurrency_chelmsford_embryo': gbpCurrency_chelmsford_embryo,
        'usdCurrency_chelmsford_embryo': usdCurrency_chelmsford_embryo,
        'eurCurrency_chelmsford_embryo': eurCurrency_chelmsford_embryo,
        'gbpCurrency_chelmsford_sperm': gbpCurrency_chelmsford_sperm,
        'usdCurrency_chelmsford_sperm': usdCurrency_chelmsford_sperm,
        'eurCurrency_chelmsford_sperm': eurCurrency_chelmsford_sperm,
        'gbpCurrency_chelmsford_icsi': gbpCurrency_chelmsford_icsi,
        'usdCurrency_chelmsford_icsi': usdCurrency_chelmsford_icsi,
        'eurCurrency_chelmsford_icsi': eurCurrency_chelmsford_icsi,
        'gbpCurrency_chelmsford_iui': gbpCurrency_chelmsford_iui,
        'usdCurrency_chelmsford_iui': usdCurrency_chelmsford_iui,
        'eurCurrency_chelmsford_iui': eurCurrency_chelmsford_iui,
        'my_total_count_chelmsford': my_total_count_chelmsford,

        'gbpCurrency_leeds_ivf': gbpCurrency_leeds_ivf,
        'usdCurrency_leeds_ivf': usdCurrency_leeds_ivf,
        'eurCurrency_leeds_ivf': eurCurrency_leeds_ivf,
        'gbpCurrency_leeds_egg': gbpCurrency_leeds_egg,
        'usdCurrency_leeds_egg': usdCurrency_leeds_egg,
        'eurCurrency_leeds_egg': eurCurrency_leeds_egg,
        'gbpCurrency_leeds_embryo': gbpCurrency_leeds_embryo,
        'usdCurrency_leeds_embryo': usdCurrency_leeds_embryo,
        'eurCurrency_leeds_embryo': eurCurrency_leeds_embryo,
        'gbpCurrency_leeds_sperm': gbpCurrency_leeds_sperm,
        'usdCurrency_leeds_sperm': usdCurrency_leeds_sperm,
        'eurCurrency_leeds_sperm': eurCurrency_leeds_sperm,
        'gbpCurrency_leeds_icsi': gbpCurrency_leeds_icsi,
        'usdCurrency_leeds_icsi': usdCurrency_leeds_icsi,
        'eurCurrency_leeds_icsi': eurCurrency_leeds_icsi,
        'gbpCurrency_leeds_iui': gbpCurrency_leeds_iui,
        'usdCurrency_leeds_iui': usdCurrency_leeds_iui,
        'eurCurrency_leeds_iui': eurCurrency_leeds_iui,
        'my_total_count_leeds': my_total_count_leeds,

        'gbpCurrency_leicester_ivf': gbpCurrency_leicester_ivf,
        'usdCurrency_leicester_ivf': usdCurrency_leicester_ivf,
        'eurCurrency_leicester_ivf': eurCurrency_leicester_ivf,
        'gbpCurrency_leicester_egg': gbpCurrency_leicester_egg,
        'usdCurrency_leicester_egg': usdCurrency_leicester_egg,
        'eurCurrency_leicester_egg': eurCurrency_leicester_egg,
        'gbpCurrency_leicester_embryo': gbpCurrency_leicester_embryo,
        'usdCurrency_leicester_embryo': usdCurrency_leicester_embryo,
        'eurCurrency_leicester_embryo': eurCurrency_leicester_embryo,
        'gbpCurrency_leicester_sperm': gbpCurrency_leicester_sperm,
        'usdCurrency_leicester_sperm': usdCurrency_leicester_sperm,
        'eurCurrency_leicester_sperm': eurCurrency_leicester_sperm,
        'gbpCurrency_leicester_icsi': gbpCurrency_leicester_icsi,
        'usdCurrency_leicester_icsi': usdCurrency_leicester_icsi,
        'eurCurrency_leicester_icsi': eurCurrency_leicester_icsi,
        'gbpCurrency_leicester_iui': gbpCurrency_leicester_iui,
        'usdCurrency_leicester_iui': usdCurrency_leicester_iui,
        'eurCurrency_leicester_iui': eurCurrency_leicester_iui,
        'my_total_count_leicester': my_total_count_leicester,

        'gbpCurrency_liverpool_ivf': gbpCurrency_liverpool_ivf,
        'usdCurrency_liverpool_ivf': usdCurrency_liverpool_ivf,
        'eurCurrency_liverpool_ivf': eurCurrency_liverpool_ivf,
        'gbpCurrency_liverpool_egg': gbpCurrency_liverpool_egg,
        'usdCurrency_liverpool_egg': usdCurrency_liverpool_egg,
        'eurCurrency_liverpool_egg': eurCurrency_liverpool_egg,
        'gbpCurrency_liverpool_embryo': gbpCurrency_liverpool_embryo,
        'usdCurrency_liverpool_embryo': usdCurrency_liverpool_embryo,
        'eurCurrency_liverpool_embryo': eurCurrency_liverpool_embryo,
        'gbpCurrency_liverpool_sperm': gbpCurrency_liverpool_sperm,
        'usdCurrency_liverpool_sperm': usdCurrency_liverpool_sperm,
        'eurCurrency_liverpool_sperm': eurCurrency_liverpool_sperm,
        'gbpCurrency_liverpool_icsi': gbpCurrency_liverpool_icsi,
        'usdCurrency_liverpool_icsi': usdCurrency_liverpool_icsi,
        'eurCurrency_liverpool_icsi': eurCurrency_liverpool_icsi,
        'gbpCurrency_liverpool_iui': gbpCurrency_liverpool_iui,
        'usdCurrency_liverpool_iui': usdCurrency_liverpool_iui,
        'eurCurrency_liverpool_iui': eurCurrency_liverpool_iui,
        'my_total_count_liverpool': my_total_count_liverpool,

        'gbpCurrency_london_ivf': gbpCurrency_london_ivf,
        'usdCurrency_london_ivf': usdCurrency_london_ivf,
        'eurCurrency_london_ivf': eurCurrency_london_ivf,
        'gbpCurrency_london_egg': gbpCurrency_london_egg,
        'usdCurrency_london_egg': usdCurrency_london_egg,
        'eurCurrency_london_egg': eurCurrency_london_egg,
        'gbpCurrency_london_embryo': gbpCurrency_london_embryo,
        'usdCurrency_london_embryo': usdCurrency_london_embryo,
        'eurCurrency_london_embryo': eurCurrency_london_embryo,
        'gbpCurrency_london_sperm': gbpCurrency_london_sperm,
        'usdCurrency_london_sperm': usdCurrency_london_sperm,
        'eurCurrency_london_sperm': eurCurrency_london_sperm,
        'gbpCurrency_london_icsi': gbpCurrency_london_icsi,
        'usdCurrency_london_icsi': usdCurrency_london_icsi,
        'eurCurrency_london_icsi': eurCurrency_london_icsi,
        'gbpCurrency_london_iui': gbpCurrency_london_iui,
        'usdCurrency_london_iui': usdCurrency_london_iui,
        'eurCurrency_london_iui': eurCurrency_london_iui,
        'my_total_count_london': my_total_count_london,

        'gbpCurrency_manchester_ivf': gbpCurrency_manchester_ivf,
        'usdCurrency_manchester_ivf': usdCurrency_manchester_ivf,
        'eurCurrency_manchester_ivf': eurCurrency_manchester_ivf,
        'gbpCurrency_manchester_egg': gbpCurrency_manchester_egg,
        'usdCurrency_manchester_egg': usdCurrency_manchester_egg,
        'eurCurrency_manchester_egg': eurCurrency_manchester_egg,
        'gbpCurrency_manchester_embryo': gbpCurrency_manchester_embryo,
        'usdCurrency_manchester_embryo': usdCurrency_manchester_embryo,
        'eurCurrency_manchester_embryo': eurCurrency_manchester_embryo,
        'gbpCurrency_manchester_sperm': gbpCurrency_manchester_sperm,
        'usdCurrency_manchester_sperm': usdCurrency_manchester_sperm,
        'eurCurrency_manchester_sperm': eurCurrency_manchester_sperm,
        'gbpCurrency_manchester_icsi': gbpCurrency_manchester_icsi,
        'usdCurrency_manchester_icsi': usdCurrency_manchester_icsi,
        'eurCurrency_manchester_icsi': eurCurrency_manchester_icsi,
        'gbpCurrency_manchester_iui': gbpCurrency_manchester_iui,
        'usdCurrency_manchester_iui': usdCurrency_manchester_iui,
        'eurCurrency_manchester_iui': eurCurrency_manchester_iui,
        'my_total_count_manchester': my_total_count_manchester,

        'gbpCurrency_middlesbrough_ivf': gbpCurrency_middlesbrough_ivf,
        'usdCurrency_middlesbrough_ivf': usdCurrency_middlesbrough_ivf,
        'eurCurrency_middlesbrough_ivf': eurCurrency_middlesbrough_ivf,
        'gbpCurrency_middlesbrough_egg': gbpCurrency_middlesbrough_egg,
        'usdCurrency_middlesbrough_egg': usdCurrency_middlesbrough_egg,
        'eurCurrency_middlesbrough_egg': eurCurrency_middlesbrough_egg,
        'gbpCurrency_middlesbrough_embryo': gbpCurrency_middlesbrough_embryo,
        'usdCurrency_middlesbrough_embryo': usdCurrency_middlesbrough_embryo,
        'eurCurrency_middlesbrough_embryo': eurCurrency_middlesbrough_embryo,
        'gbpCurrency_middlesbrough_sperm': gbpCurrency_middlesbrough_sperm,
        'usdCurrency_middlesbrough_sperm': usdCurrency_middlesbrough_sperm,
        'eurCurrency_middlesbrough_sperm': eurCurrency_middlesbrough_sperm,
        'gbpCurrency_middlesbrough_icsi': gbpCurrency_middlesbrough_icsi,
        'usdCurrency_middlesbrough_icsi': usdCurrency_middlesbrough_icsi,
        'eurCurrency_middlesbrough_icsi': eurCurrency_middlesbrough_icsi,
        'gbpCurrency_middlesbrough_iui': gbpCurrency_middlesbrough_iui,
        'usdCurrency_middlesbrough_iui': usdCurrency_middlesbrough_iui,
        'eurCurrency_middlesbrough_iui': eurCurrency_middlesbrough_iui,
        'my_total_count_middlesbrough': my_total_count_middlesbrough,

        'gbpCurrency_newcastle_ivf': gbpCurrency_newcastle_ivf,
        'usdCurrency_newcastle_ivf': usdCurrency_newcastle_ivf,
        'eurCurrency_newcastle_ivf': eurCurrency_newcastle_ivf,
        'gbpCurrency_newcastle_egg': gbpCurrency_newcastle_egg,
        'usdCurrency_newcastle_egg': usdCurrency_newcastle_egg,
        'eurCurrency_newcastle_egg': eurCurrency_newcastle_egg,
        'gbpCurrency_newcastle_embryo': gbpCurrency_newcastle_embryo,
        'usdCurrency_newcastle_embryo': usdCurrency_newcastle_embryo,
        'eurCurrency_newcastle_embryo': eurCurrency_newcastle_embryo,
        'gbpCurrency_newcastle_sperm': gbpCurrency_newcastle_sperm,
        'usdCurrency_newcastle_sperm': usdCurrency_newcastle_sperm,
        'eurCurrency_newcastle_sperm': eurCurrency_newcastle_sperm,
        'gbpCurrency_newcastle_icsi': gbpCurrency_newcastle_icsi,
        'usdCurrency_newcastle_icsi': usdCurrency_newcastle_icsi,
        'eurCurrency_newcastle_icsi': eurCurrency_newcastle_icsi,
        'gbpCurrency_newcastle_iui': gbpCurrency_newcastle_iui,
        'usdCurrency_newcastle_iui': usdCurrency_newcastle_iui,
        'eurCurrency_newcastle_iui': eurCurrency_newcastle_iui,
        'my_total_count_newcastle': my_total_count_newcastle,

        'gbpCurrency_norwich_ivf': gbpCurrency_norwich_ivf,
        'usdCurrency_norwich_ivf': usdCurrency_norwich_ivf,
        'eurCurrency_norwich_ivf': eurCurrency_norwich_ivf,
        'gbpCurrency_norwich_egg': gbpCurrency_norwich_egg,
        'usdCurrency_norwich_egg': usdCurrency_norwich_egg,
        'eurCurrency_norwich_egg': eurCurrency_norwich_egg,
        'gbpCurrency_norwich_embryo': gbpCurrency_norwich_embryo,
        'usdCurrency_norwich_embryo': usdCurrency_norwich_embryo,
        'eurCurrency_norwich_embryo': eurCurrency_norwich_embryo,
        'gbpCurrency_norwich_sperm': gbpCurrency_norwich_sperm,
        'usdCurrency_norwich_sperm': usdCurrency_norwich_sperm,
        'eurCurrency_norwich_sperm': eurCurrency_norwich_sperm,
        'gbpCurrency_norwich_icsi': gbpCurrency_norwich_icsi,
        'usdCurrency_norwich_icsi': usdCurrency_norwich_icsi,
        'eurCurrency_norwich_icsi': eurCurrency_norwich_icsi,
        'gbpCurrency_norwich_iui': gbpCurrency_norwich_iui,
        'usdCurrency_norwich_iui': usdCurrency_norwich_iui,
        'eurCurrency_norwich_iui': eurCurrency_norwich_iui,
        'my_total_count_norwich': my_total_count_norwich,

        'gbpCurrency_nottingham_ivf': gbpCurrency_nottingham_ivf,
        'usdCurrency_nottingham_ivf': usdCurrency_nottingham_ivf,
        'eurCurrency_nottingham_ivf': eurCurrency_nottingham_ivf,
        'gbpCurrency_nottingham_egg': gbpCurrency_nottingham_egg,
        'usdCurrency_nottingham_egg': usdCurrency_nottingham_egg,
        'eurCurrency_nottingham_egg': eurCurrency_nottingham_egg,
        'gbpCurrency_nottingham_embryo': gbpCurrency_nottingham_embryo,
        'usdCurrency_nottingham_embryo': usdCurrency_nottingham_embryo,
        'eurCurrency_nottingham_embryo': eurCurrency_nottingham_embryo,
        'gbpCurrency_nottingham_sperm': gbpCurrency_nottingham_sperm,
        'usdCurrency_nottingham_sperm': usdCurrency_nottingham_sperm,
        'eurCurrency_nottingham_sperm': eurCurrency_nottingham_sperm,
        'gbpCurrency_nottingham_icsi': gbpCurrency_nottingham_icsi,
        'usdCurrency_nottingham_icsi': usdCurrency_nottingham_icsi,
        'eurCurrency_nottingham_icsi': eurCurrency_nottingham_icsi,
        'gbpCurrency_nottingham_iui': gbpCurrency_nottingham_iui,
        'usdCurrency_nottingham_iui': usdCurrency_nottingham_iui,
        'eurCurrency_nottingham_iui': eurCurrency_nottingham_iui,
        'my_total_count_nottingham': my_total_count_nottingham,

        'gbpCurrency_oxford_ivf': gbpCurrency_oxford_ivf,
        'usdCurrency_oxford_ivf': usdCurrency_oxford_ivf,
        'eurCurrency_oxford_ivf': eurCurrency_oxford_ivf,
        'gbpCurrency_oxford_egg': gbpCurrency_oxford_egg,
        'usdCurrency_oxford_egg': usdCurrency_oxford_egg,
        'eurCurrency_oxford_egg': eurCurrency_oxford_egg,
        'gbpCurrency_oxford_embryo': gbpCurrency_oxford_embryo,
        'usdCurrency_oxford_embryo': usdCurrency_oxford_embryo,
        'eurCurrency_oxford_embryo': eurCurrency_oxford_embryo,
        'gbpCurrency_oxford_sperm': gbpCurrency_oxford_sperm,
        'usdCurrency_oxford_sperm': usdCurrency_oxford_sperm,
        'eurCurrency_oxford_sperm': eurCurrency_oxford_sperm,
        'gbpCurrency_oxford_icsi': gbpCurrency_oxford_icsi,
        'usdCurrency_oxford_icsi': usdCurrency_oxford_icsi,
        'eurCurrency_oxford_icsi': eurCurrency_oxford_icsi,
        'gbpCurrency_oxford_iui': gbpCurrency_oxford_iui,
        'usdCurrency_oxford_iui': usdCurrency_oxford_iui,
        'eurCurrency_oxford_iui': eurCurrency_oxford_iui,
        'my_total_count_oxford': my_total_count_oxford,

        'gbpCurrency_peterborough_ivf': gbpCurrency_peterborough_ivf,
        'usdCurrency_peterborough_ivf': usdCurrency_peterborough_ivf,
        'eurCurrency_peterborough_ivf': eurCurrency_peterborough_ivf,
        'gbpCurrency_peterborough_egg': gbpCurrency_peterborough_egg,
        'usdCurrency_peterborough_egg': usdCurrency_peterborough_egg,
        'eurCurrency_peterborough_egg': eurCurrency_peterborough_egg,
        'gbpCurrency_peterborough_embryo': gbpCurrency_peterborough_embryo,
        'usdCurrency_peterborough_embryo': usdCurrency_peterborough_embryo,
        'eurCurrency_peterborough_embryo': eurCurrency_peterborough_embryo,
        'gbpCurrency_peterborough_sperm': gbpCurrency_peterborough_sperm,
        'usdCurrency_peterborough_sperm': usdCurrency_peterborough_sperm,
        'eurCurrency_peterborough_sperm': eurCurrency_peterborough_sperm,
        'gbpCurrency_peterborough_icsi': gbpCurrency_peterborough_icsi,
        'usdCurrency_peterborough_icsi': usdCurrency_peterborough_icsi,
        'eurCurrency_peterborough_icsi': eurCurrency_peterborough_icsi,
        'gbpCurrency_peterborough_iui': gbpCurrency_peterborough_iui,
        'usdCurrency_peterborough_iui': usdCurrency_peterborough_iui,
        'eurCurrency_peterborough_iui': eurCurrency_peterborough_iui,
        'my_total_count_peterborough': my_total_count_peterborough,

        'gbpCurrency_plymouth_ivf': gbpCurrency_plymouth_ivf,
        'usdCurrency_plymouth_ivf': usdCurrency_plymouth_ivf,
        'eurCurrency_plymouth_ivf': eurCurrency_plymouth_ivf,
        'gbpCurrency_plymouth_egg': gbpCurrency_plymouth_egg,
        'usdCurrency_plymouth_egg': usdCurrency_plymouth_egg,
        'eurCurrency_plymouth_egg': eurCurrency_plymouth_egg,
        'gbpCurrency_plymouth_embryo': gbpCurrency_plymouth_embryo,
        'usdCurrency_plymouth_embryo': usdCurrency_plymouth_embryo,
        'eurCurrency_plymouth_embryo': eurCurrency_plymouth_embryo,
        'gbpCurrency_plymouth_sperm': gbpCurrency_plymouth_sperm,
        'usdCurrency_plymouth_sperm': usdCurrency_plymouth_sperm,
        'eurCurrency_plymouth_sperm': eurCurrency_plymouth_sperm,
        'gbpCurrency_plymouth_icsi': gbpCurrency_plymouth_icsi,
        'usdCurrency_plymouth_icsi': usdCurrency_plymouth_icsi,
        'eurCurrency_plymouth_icsi': eurCurrency_plymouth_icsi,
        'gbpCurrency_plymouth_iui': gbpCurrency_plymouth_iui,
        'usdCurrency_plymouth_iui': usdCurrency_plymouth_iui,
        'eurCurrency_plymouth_iui': eurCurrency_plymouth_iui,
        'my_total_count_plymouth': my_total_count_plymouth,

        'gbpCurrency_portsmouth_ivf': gbpCurrency_portsmouth_ivf,
        'usdCurrency_portsmouth_ivf': usdCurrency_portsmouth_ivf,
        'eurCurrency_portsmouth_ivf': eurCurrency_portsmouth_ivf,
        'gbpCurrency_portsmouth_egg': gbpCurrency_portsmouth_egg,
        'usdCurrency_portsmouth_egg': usdCurrency_portsmouth_egg,
        'eurCurrency_portsmouth_egg': eurCurrency_portsmouth_egg,
        'gbpCurrency_portsmouth_embryo': gbpCurrency_portsmouth_embryo,
        'usdCurrency_portsmouth_embryo': usdCurrency_portsmouth_embryo,
        'eurCurrency_portsmouth_embryo': eurCurrency_portsmouth_embryo,
        'gbpCurrency_portsmouth_sperm': gbpCurrency_portsmouth_sperm,
        'usdCurrency_portsmouth_sperm': usdCurrency_portsmouth_sperm,
        'eurCurrency_portsmouth_sperm': eurCurrency_portsmouth_sperm,
        'gbpCurrency_portsmouth_icsi': gbpCurrency_portsmouth_icsi,
        'usdCurrency_portsmouth_icsi': usdCurrency_portsmouth_icsi,
        'eurCurrency_portsmouth_icsi': eurCurrency_portsmouth_icsi,
        'gbpCurrency_portsmouth_iui': gbpCurrency_portsmouth_iui,
        'usdCurrency_portsmouth_iui': usdCurrency_portsmouth_iui,
        'eurCurrency_portsmouth_iui': eurCurrency_portsmouth_iui,
        'my_total_count_portsmouth': my_total_count_portsmouth,

        'gbpCurrency_salisbury_ivf': gbpCurrency_salisbury_ivf,
        'usdCurrency_salisbury_ivf': usdCurrency_salisbury_ivf,
        'eurCurrency_salisbury_ivf': eurCurrency_salisbury_ivf,
        'gbpCurrency_salisbury_egg': gbpCurrency_salisbury_egg,
        'usdCurrency_salisbury_egg': usdCurrency_salisbury_egg,
        'eurCurrency_salisbury_egg': eurCurrency_salisbury_egg,
        'gbpCurrency_salisbury_embryo': gbpCurrency_salisbury_embryo,
        'usdCurrency_salisbury_embryo': usdCurrency_salisbury_embryo,
        'eurCurrency_salisbury_embryo': eurCurrency_salisbury_embryo,
        'gbpCurrency_salisbury_sperm': gbpCurrency_salisbury_sperm,
        'usdCurrency_salisbury_sperm': usdCurrency_salisbury_sperm,
        'eurCurrency_salisbury_sperm': eurCurrency_salisbury_sperm,
        'gbpCurrency_salisbury_icsi': gbpCurrency_salisbury_icsi,
        'usdCurrency_salisbury_icsi': usdCurrency_salisbury_icsi,
        'eurCurrency_salisbury_icsi': eurCurrency_salisbury_icsi,
        'gbpCurrency_salisbury_iui': gbpCurrency_salisbury_iui,
        'usdCurrency_salisbury_iui': usdCurrency_salisbury_iui,
        'eurCurrency_salisbury_iui': eurCurrency_salisbury_iui,
        'my_total_count_salisbury': my_total_count_salisbury,

        'gbpCurrency_sheffield_ivf': gbpCurrency_sheffield_ivf,
        'usdCurrency_sheffield_ivf': usdCurrency_sheffield_ivf,
        'eurCurrency_sheffield_ivf': eurCurrency_sheffield_ivf,
        'gbpCurrency_sheffield_egg': gbpCurrency_sheffield_egg,
        'usdCurrency_sheffield_egg': usdCurrency_sheffield_egg,
        'eurCurrency_sheffield_egg': eurCurrency_sheffield_egg,
        'gbpCurrency_sheffield_embryo': gbpCurrency_sheffield_embryo,
        'usdCurrency_sheffield_embryo': usdCurrency_sheffield_embryo,
        'eurCurrency_sheffield_embryo': eurCurrency_sheffield_embryo,
        'gbpCurrency_sheffield_sperm': gbpCurrency_sheffield_sperm,
        'usdCurrency_sheffield_sperm': usdCurrency_sheffield_sperm,
        'eurCurrency_sheffield_sperm': eurCurrency_sheffield_sperm,
        'gbpCurrency_sheffield_icsi': gbpCurrency_sheffield_icsi,
        'usdCurrency_sheffield_icsi': usdCurrency_sheffield_icsi,
        'eurCurrency_sheffield_icsi': eurCurrency_sheffield_icsi,
        'gbpCurrency_sheffield_iui': gbpCurrency_sheffield_iui,
        'usdCurrency_sheffield_iui': usdCurrency_sheffield_iui,
        'eurCurrency_sheffield_iui': eurCurrency_sheffield_iui,
        'my_total_count_sheffield': my_total_count_sheffield,

        'gbpCurrency_southampton_ivf': gbpCurrency_southampton_ivf,
        'usdCurrency_southampton_ivf': usdCurrency_southampton_ivf,
        'eurCurrency_southampton_ivf': eurCurrency_southampton_ivf,
        'gbpCurrency_southampton_egg': gbpCurrency_southampton_egg,
        'usdCurrency_southampton_egg': usdCurrency_southampton_egg,
        'eurCurrency_southampton_egg': eurCurrency_southampton_egg,
        'gbpCurrency_southampton_embryo': gbpCurrency_southampton_embryo,
        'usdCurrency_southampton_embryo': usdCurrency_southampton_embryo,
        'eurCurrency_southampton_embryo': eurCurrency_southampton_embryo,
        'gbpCurrency_southampton_sperm': gbpCurrency_southampton_sperm,
        'usdCurrency_southampton_sperm': usdCurrency_southampton_sperm,
        'eurCurrency_southampton_sperm': eurCurrency_southampton_sperm,
        'gbpCurrency_southampton_icsi': gbpCurrency_southampton_icsi,
        'usdCurrency_southampton_icsi': usdCurrency_southampton_icsi,
        'eurCurrency_southampton_icsi': eurCurrency_southampton_icsi,
        'gbpCurrency_southampton_iui': gbpCurrency_southampton_iui,
        'usdCurrency_southampton_iui': usdCurrency_southampton_iui,
        'eurCurrency_southampton_iui': eurCurrency_southampton_iui,
        'my_total_count_southampton': my_total_count_southampton,

        'gbpCurrency_swansea_ivf': gbpCurrency_swansea_ivf,
        'usdCurrency_swansea_ivf': usdCurrency_swansea_ivf,
        'eurCurrency_swansea_ivf': eurCurrency_swansea_ivf,
        'gbpCurrency_swansea_egg': gbpCurrency_swansea_egg,
        'usdCurrency_swansea_egg': usdCurrency_swansea_egg,
        'eurCurrency_swansea_egg': eurCurrency_swansea_egg,
        'gbpCurrency_swansea_embryo': gbpCurrency_swansea_embryo,
        'usdCurrency_swansea_embryo': usdCurrency_swansea_embryo,
        'eurCurrency_swansea_embryo': eurCurrency_swansea_embryo,
        'gbpCurrency_swansea_sperm': gbpCurrency_swansea_sperm,
        'usdCurrency_swansea_sperm': usdCurrency_swansea_sperm,
        'eurCurrency_swansea_sperm': eurCurrency_swansea_sperm,
        'gbpCurrency_swansea_icsi': gbpCurrency_swansea_icsi,
        'usdCurrency_swansea_icsi': usdCurrency_swansea_icsi,
        'eurCurrency_swansea_icsi': eurCurrency_swansea_icsi,
        'gbpCurrency_swansea_iui': gbpCurrency_swansea_iui,
        'usdCurrency_swansea_iui': usdCurrency_swansea_iui,
        'eurCurrency_swansea_iui': eurCurrency_swansea_iui,
        'my_total_count_swansea': my_total_count_swansea,
        }


    return render(request, 'main/Locations/UKLocations/uk-regions-ivf.html', context)


def locationsCZRegions(request):
    queryset_list_cz = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_prague = queryset_list_cz.filter(clinicRegion__iexact='Prague')
    my_total_count_prague = queryset_list_prague.count()
    queryset_list_prague_ivf = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_prague_ivf.items():
        eurCurrency_prague_ivf = val
        if eurCurrency_prague_ivf is not None:
            usdCurrency_prague_ivf = val * eurToUsd
            gbpCurrency_prague_ivf = val * eurToGbp
        else:
            usdCurrency_prague_ivf = None
            gbpCurrency_prague_ivf = None

    queryset_list_prague_egg = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_prague_egg.items():
        eurCurrency_prague_egg = val
        if eurCurrency_prague_egg is not None:
            usdCurrency_prague_egg = val * eurToUsd
            gbpCurrency_prague_egg = val * eurToGbp
        else:
            usdCurrency_prague_egg = None
            gbpCurrency_prague_egg = None

    queryset_list_prague_embryo = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_prague_embryo.items():
        eurCurrency_prague_embryo = val
        if eurCurrency_prague_embryo is not None:
            usdCurrency_prague_embryo = val * eurToUsd
            gbpCurrency_prague_embryo = val * eurToGbp
        else:
            usdCurrency_prague_embryo = None
            gbpCurrency_prague_embryo = None

    queryset_list_prague_sperm = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_prague_sperm.items():
        eurCurrency_prague_sperm = val
        if eurCurrency_prague_sperm is not None:
            usdCurrency_prague_sperm = val * eurToUsd
            gbpCurrency_prague_sperm = val * eurToGbp
        else:
            usdCurrency_prague_sperm = None
            gbpCurrency_prague_sperm = None

    queryset_list_prague_icsi = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_prague_icsi.items():
        eurCurrency_prague_icsi = val
        if eurCurrency_prague_icsi is not None:
            usdCurrency_prague_icsi = val * eurToUsd
            gbpCurrency_prague_icsi = val * eurToGbp
        else:
            usdCurrency_prague_icsi = None
            gbpCurrency_prague_icsi = None

    queryset_list_prague_iui = queryset_list_prague.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_prague_iui.items():
        eurCurrency_prague_iui = val
        if eurCurrency_prague_iui is not None:
            usdCurrency_prague_iui = val * eurToUsd
            gbpCurrency_prague_iui = val * eurToGbp
        else:
            usdCurrency_prague_iui = None
            gbpCurrency_prague_iui = None

    #--------------------------------------------------------------------------
    queryset_list_brno = queryset_list_cz.filter(clinicRegion__iexact='Brno')
    my_total_count_brno = queryset_list_brno.count()
    queryset_list_brno_ivf = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_brno_ivf.items():
        eurCurrency_brno_ivf = val
        if eurCurrency_brno_ivf is not None:
            usdCurrency_brno_ivf = val * eurToUsd
            gbpCurrency_brno_ivf = val * eurToGbp
        else:
            usdCurrency_brno_ivf = None
            gbpCurrency_brno_ivf = None

    queryset_list_brno_egg = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_brno_egg.items():
        eurCurrency_brno_egg = val
        if eurCurrency_brno_egg is not None:
            usdCurrency_brno_egg = val * eurToUsd
            gbpCurrency_brno_egg = val * eurToGbp
        else:
            usdCurrency_brno_egg = None
            gbpCurrency_brno_egg = None

    queryset_list_brno_embryo = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_brno_embryo.items():
        eurCurrency_brno_embryo = val
        if eurCurrency_brno_embryo is not None:
            usdCurrency_brno_embryo = val * eurToUsd
            gbpCurrency_brno_embryo = val * eurToGbp
        else:
            usdCurrency_brno_embryo = None
            gbpCurrency_brno_embryo = None

    queryset_list_brno_sperm = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_brno_sperm.items():
        eurCurrency_brno_sperm = val
        if eurCurrency_brno_sperm is not None:
            usdCurrency_brno_sperm = val * eurToUsd
            gbpCurrency_brno_sperm = val * eurToGbp
        else:
            usdCurrency_brno_sperm = None
            gbpCurrency_brno_sperm = None

    queryset_list_brno_icsi = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_brno_icsi.items():
        eurCurrency_brno_icsi = val
        if eurCurrency_brno_icsi is not None:
            usdCurrency_brno_icsi = val * eurToUsd
            gbpCurrency_brno_icsi = val * eurToGbp
        else:
            usdCurrency_brno_icsi = None
            gbpCurrency_brno_icsi = None

    queryset_list_brno_iui = queryset_list_brno.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_brno_iui.items():
        eurCurrency_brno_iui = val
        if eurCurrency_brno_iui is not None:
            usdCurrency_brno_iui = val * eurToUsd
            gbpCurrency_brno_iui = val * eurToGbp
        else:
            usdCurrency_brno_iui = None
            gbpCurrency_brno_iui = None

    context = {
        'gbpCurrency_prague_ivf': gbpCurrency_prague_ivf,
        'usdCurrency_prague_ivf': usdCurrency_prague_ivf,
        'eurCurrency_prague_ivf': eurCurrency_prague_ivf,
        'gbpCurrency_prague_egg': gbpCurrency_prague_egg,
        'usdCurrency_prague_egg': usdCurrency_prague_egg,
        'eurCurrency_prague_egg': eurCurrency_prague_egg,
        'gbpCurrency_prague_embryo': gbpCurrency_prague_embryo,
        'usdCurrency_prague_embryo': usdCurrency_prague_embryo,
        'eurCurrency_prague_embryo': eurCurrency_prague_embryo,
        'gbpCurrency_prague_sperm': gbpCurrency_prague_sperm,
        'usdCurrency_prague_sperm': usdCurrency_prague_sperm,
        'eurCurrency_prague_sperm': eurCurrency_prague_sperm,
        'gbpCurrency_prague_icsi': gbpCurrency_prague_icsi,
        'usdCurrency_prague_icsi': usdCurrency_prague_icsi,
        'eurCurrency_prague_icsi': eurCurrency_prague_icsi,
        'gbpCurrency_prague_iui': gbpCurrency_prague_iui,
        'usdCurrency_prague_iui': usdCurrency_prague_iui,
        'eurCurrency_prague_iui': eurCurrency_prague_iui,
        'my_total_count_prague': my_total_count_prague,

        'gbpCurrency_brno_ivf': gbpCurrency_brno_ivf,
        'usdCurrency_brno_ivf': usdCurrency_brno_ivf,
        'eurCurrency_brno_ivf': eurCurrency_brno_ivf,
        'gbpCurrency_brno_egg': gbpCurrency_brno_egg,
        'usdCurrency_brno_egg': usdCurrency_brno_egg,
        'eurCurrency_brno_egg': eurCurrency_brno_egg,
        'gbpCurrency_brno_embryo': gbpCurrency_brno_embryo,
        'usdCurrency_brno_embryo': usdCurrency_brno_embryo,
        'eurCurrency_brno_embryo': eurCurrency_brno_embryo,
        'gbpCurrency_brno_sperm': gbpCurrency_brno_sperm,
        'usdCurrency_brno_sperm': usdCurrency_brno_sperm,
        'eurCurrency_brno_sperm': eurCurrency_brno_sperm,
        'gbpCurrency_brno_icsi': gbpCurrency_brno_icsi,
        'usdCurrency_brno_icsi': usdCurrency_brno_icsi,
        'eurCurrency_brno_icsi': eurCurrency_brno_icsi,
        'gbpCurrency_brno_iui': gbpCurrency_brno_iui,
        'usdCurrency_brno_iui': usdCurrency_brno_iui,
        'eurCurrency_brno_iui': eurCurrency_brno_iui,
        'my_total_count_brno': my_total_count_brno,
        }
    return render(request, 'main/Locations/CZLocations/cz-regions-ivf.html', context)

def locationsSPRegions(request):
    queryset_list_sp = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_alicante = queryset_list_sp.filter(clinicRegion__iexact='Alicante')
    my_total_count_alicante = queryset_list_alicante.count()
    queryset_list_alicante_ivf = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_alicante_ivf.items():
        eurCurrency_alicante_ivf = val
        if eurCurrency_alicante_ivf is not None:
            usdCurrency_alicante_ivf = val * eurToUsd
            gbpCurrency_alicante_ivf = val * eurToGbp
        else:
            usdCurrency_alicante_ivf = None
            gbpCurrency_alicante_ivf = None

    queryset_list_alicante_egg = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alicante_egg.items():
        eurCurrency_alicante_egg = val
        if eurCurrency_alicante_egg is not None:
            usdCurrency_alicante_egg = val * eurToUsd
            gbpCurrency_alicante_egg = val * eurToGbp
        else:
            usdCurrency_alicante_egg = None
            gbpCurrency_alicante_egg = None

    queryset_list_alicante_embryo = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alicante_embryo.items():
        eurCurrency_alicante_embryo = val
        if eurCurrency_alicante_embryo is not None:
            usdCurrency_alicante_embryo = val * eurToUsd
            gbpCurrency_alicante_embryo = val * eurToGbp
        else:
            usdCurrency_alicante_embryo = None
            gbpCurrency_alicante_embryo = None

    queryset_list_alicante_sperm = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alicante_sperm.items():
        eurCurrency_alicante_sperm = val
        if eurCurrency_alicante_sperm is not None:
            usdCurrency_alicante_sperm = val * eurToUsd
            gbpCurrency_alicante_sperm = val * eurToGbp
        else:
            usdCurrency_alicante_sperm = None
            gbpCurrency_alicante_sperm = None

    queryset_list_alicante_icsi = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alicante_icsi.items():
        eurCurrency_alicante_icsi = val
        if eurCurrency_alicante_icsi is not None:
            usdCurrency_alicante_icsi = val * eurToUsd
            gbpCurrency_alicante_icsi = val * eurToGbp
        else:
            usdCurrency_alicante_icsi = None
            gbpCurrency_alicante_icsi = None

    queryset_list_alicante_iui = queryset_list_alicante.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alicante_iui.items():
        eurCurrency_alicante_iui = val
        if eurCurrency_alicante_iui is not None:
            usdCurrency_alicante_iui = val * eurToUsd
            gbpCurrency_alicante_iui = val * eurToGbp
        else:
            usdCurrency_alicante_iui = None
            gbpCurrency_alicante_iui = None

    #--------------------------------------------------------------------------
    queryset_list_barcelona = queryset_list_sp.filter(clinicRegion__iexact='Barcelona')
    my_total_count_barcelona = queryset_list_barcelona.count()
    queryset_list_barcelona_ivf = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_barcelona_ivf.items():
        eurCurrency_barcelona_ivf = val
        if eurCurrency_barcelona_ivf is not None:
            usdCurrency_barcelona_ivf = val * eurToUsd
            gbpCurrency_barcelona_ivf = val * eurToGbp
        else:
            usdCurrency_barcelona_ivf = None
            gbpCurrency_barcelona_ivf = None

    queryset_list_barcelona_egg = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_egg.items():
        eurCurrency_barcelona_egg = val
        if eurCurrency_barcelona_egg is not None:
            usdCurrency_barcelona_egg = val * eurToUsd
            gbpCurrency_barcelona_egg = val * eurToGbp
        else:
            usdCurrency_barcelona_egg = None
            gbpCurrency_barcelona_egg = None

    queryset_list_barcelona_embryo = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_embryo.items():
        eurCurrency_barcelona_embryo = val
        if eurCurrency_barcelona_embryo is not None:
            usdCurrency_barcelona_embryo = val * eurToUsd
            gbpCurrency_barcelona_embryo = val * eurToGbp
        else:
            usdCurrency_barcelona_embryo = None
            gbpCurrency_barcelona_embryo = None

    queryset_list_barcelona_sperm = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_sperm.items():
        eurCurrency_barcelona_sperm = val
        if eurCurrency_barcelona_sperm is not None:
            usdCurrency_barcelona_sperm = val * eurToUsd
            gbpCurrency_barcelona_sperm = val * eurToGbp
        else:
            usdCurrency_barcelona_sperm = None
            gbpCurrency_barcelona_sperm = None

    queryset_list_barcelona_icsi = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_barcelona_icsi.items():
        eurCurrency_barcelona_icsi = val
        if eurCurrency_barcelona_icsi is not None:
            usdCurrency_barcelona_icsi = val * eurToUsd
            gbpCurrency_barcelona_icsi = val * eurToGbp
        else:
            usdCurrency_barcelona_icsi = None
            gbpCurrency_barcelona_icsi = None

    queryset_list_barcelona_iui = queryset_list_barcelona.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_barcelona_iui.items():
        eurCurrency_barcelona_iui = val
        if eurCurrency_barcelona_iui is not None:
            usdCurrency_barcelona_iui = val * eurToUsd
            gbpCurrency_barcelona_iui = val * eurToGbp
        else:
            usdCurrency_barcelona_iui = None
            gbpCurrency_barcelona_iui = None

    #--------------------------------------------------------------------------
    queryset_list_madrid = queryset_list_sp.filter(clinicRegion__iexact='Madrid')
    my_total_count_madrid = queryset_list_madrid.count()
    queryset_list_madrid_ivf = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_madrid_ivf.items():
        eurCurrency_madrid_ivf = val
        if eurCurrency_madrid_ivf is not None:
            usdCurrency_madrid_ivf = val * eurToUsd
            gbpCurrency_madrid_ivf = val * eurToGbp
        else:
            usdCurrency_madrid_ivf = None
            gbpCurrency_madrid_ivf = None

    queryset_list_madrid_egg = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_madrid_egg.items():
        eurCurrency_madrid_egg = val
        if eurCurrency_madrid_egg is not None:
            usdCurrency_madrid_egg = val * eurToUsd
            gbpCurrency_madrid_egg = val * eurToGbp
        else:
            usdCurrency_madrid_egg = None
            gbpCurrency_madrid_egg = None

    queryset_list_madrid_embryo = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_madrid_embryo.items():
        eurCurrency_madrid_embryo = val
        if eurCurrency_madrid_embryo is not None:
            usdCurrency_madrid_embryo = val * eurToUsd
            gbpCurrency_madrid_embryo = val * eurToGbp
        else:
            usdCurrency_madrid_embryo = None
            gbpCurrency_madrid_embryo = None

    queryset_list_madrid_sperm = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_madrid_sperm.items():
        eurCurrency_madrid_sperm = val
        if eurCurrency_madrid_sperm is not None:
            usdCurrency_madrid_sperm = val * eurToUsd
            gbpCurrency_madrid_sperm = val * eurToGbp
        else:
            usdCurrency_madrid_sperm = None
            gbpCurrency_madrid_sperm = None

    queryset_list_madrid_icsi = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_madrid_icsi.items():
        eurCurrency_madrid_icsi = val
        if eurCurrency_madrid_icsi is not None:
            usdCurrency_madrid_icsi = val * eurToUsd
            gbpCurrency_madrid_icsi = val * eurToGbp
        else:
            usdCurrency_madrid_icsi = None
            gbpCurrency_madrid_icsi = None

    queryset_list_madrid_iui = queryset_list_madrid.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_madrid_iui.items():
        eurCurrency_madrid_iui = val
        if eurCurrency_madrid_iui is not None:
            usdCurrency_madrid_iui = val * eurToUsd
            gbpCurrency_madrid_iui = val * eurToGbp
        else:
            usdCurrency_madrid_iui = None
            gbpCurrency_madrid_iui = None

    #--------------------------------------------------------------------------
    queryset_list_malaga = queryset_list_sp.filter(clinicRegion__iexact='Malaga')
    my_total_count_malaga = queryset_list_malaga.count()
    queryset_list_malaga_ivf = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_malaga_ivf.items():
        eurCurrency_malaga_ivf = val
        if eurCurrency_malaga_ivf is not None:
            usdCurrency_malaga_ivf = val * eurToUsd
            gbpCurrency_malaga_ivf = val * eurToGbp
        else:
            usdCurrency_malaga_ivf = None
            gbpCurrency_malaga_ivf = None

    queryset_list_malaga_egg = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_malaga_egg.items():
        eurCurrency_malaga_egg = val
        if eurCurrency_malaga_egg is not None:
            usdCurrency_malaga_egg = val * eurToUsd
            gbpCurrency_malaga_egg = val * eurToGbp
        else:
            usdCurrency_malaga_egg = None
            gbpCurrency_malaga_egg = None

    queryset_list_malaga_embryo = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_malaga_embryo.items():
        eurCurrency_malaga_embryo = val
        if eurCurrency_malaga_embryo is not None:
            usdCurrency_malaga_embryo = val * eurToUsd
            gbpCurrency_malaga_embryo = val * eurToGbp
        else:
            usdCurrency_malaga_embryo = None
            gbpCurrency_malaga_embryo = None

    queryset_list_malaga_sperm = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_malaga_sperm.items():
        eurCurrency_malaga_sperm = val
        if eurCurrency_malaga_sperm is not None:
            usdCurrency_malaga_sperm = val * eurToUsd
            gbpCurrency_malaga_sperm = val * eurToGbp
        else:
            usdCurrency_malaga_sperm = None
            gbpCurrency_malaga_sperm = None

    queryset_list_malaga_icsi = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_malaga_icsi.items():
        eurCurrency_malaga_icsi = val
        if eurCurrency_malaga_icsi is not None:
            usdCurrency_malaga_icsi = val * eurToUsd
            gbpCurrency_malaga_icsi = val * eurToGbp
        else:
            usdCurrency_malaga_icsi = None
            gbpCurrency_malaga_icsi = None

    queryset_list_malaga_iui = queryset_list_malaga.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_malaga_iui.items():
        eurCurrency_malaga_iui = val
        if eurCurrency_malaga_iui is not None:
            usdCurrency_malaga_iui = val * eurToUsd
            gbpCurrency_malaga_iui = val * eurToGbp
        else:
            usdCurrency_malaga_iui = None
            gbpCurrency_malaga_iui = None

    #--------------------------------------------------------------------------
    queryset_list_sevilla = queryset_list_sp.filter(clinicRegion__iexact='Sevilla')
    my_total_count_sevilla = queryset_list_sevilla.count()
    queryset_list_sevilla_ivf = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_sevilla_ivf.items():
        eurCurrency_sevilla_ivf = val
        if eurCurrency_sevilla_ivf is not None:
            usdCurrency_sevilla_ivf = val * eurToUsd
            gbpCurrency_sevilla_ivf = val * eurToGbp
        else:
            usdCurrency_sevilla_ivf = None
            gbpCurrency_sevilla_ivf = None

    queryset_list_sevilla_egg = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_egg.items():
        eurCurrency_sevilla_egg = val
        if eurCurrency_sevilla_egg is not None:
            usdCurrency_sevilla_egg = val * eurToUsd
            gbpCurrency_sevilla_egg = val * eurToGbp
        else:
            usdCurrency_sevilla_egg = None
            gbpCurrency_sevilla_egg = None

    queryset_list_sevilla_embryo = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_embryo.items():
        eurCurrency_sevilla_embryo = val
        if eurCurrency_sevilla_embryo is not None:
            usdCurrency_sevilla_embryo = val * eurToUsd
            gbpCurrency_sevilla_embryo = val * eurToGbp
        else:
            usdCurrency_sevilla_embryo = None
            gbpCurrency_sevilla_embryo = None

    queryset_list_sevilla_sperm = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_sperm.items():
        eurCurrency_sevilla_sperm = val
        if eurCurrency_sevilla_sperm is not None:
            usdCurrency_sevilla_sperm = val * eurToUsd
            gbpCurrency_sevilla_sperm = val * eurToGbp
        else:
            usdCurrency_sevilla_sperm = None
            gbpCurrency_sevilla_sperm = None

    queryset_list_sevilla_icsi = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_sevilla_icsi.items():
        eurCurrency_sevilla_icsi = val
        if eurCurrency_sevilla_icsi is not None:
            usdCurrency_sevilla_icsi = val * eurToUsd
            gbpCurrency_sevilla_icsi = val * eurToGbp
        else:
            usdCurrency_sevilla_icsi = None
            gbpCurrency_sevilla_icsi = None

    queryset_list_sevilla_iui = queryset_list_sevilla.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_sevilla_iui.items():
        eurCurrency_sevilla_iui = val
        if eurCurrency_sevilla_iui is not None:
            usdCurrency_sevilla_iui = val * eurToUsd
            gbpCurrency_sevilla_iui = val * eurToGbp
        else:
            usdCurrency_sevilla_iui = None
            gbpCurrency_sevilla_iui = None

    #--------------------------------------------------------------------------
    queryset_list_valencia = queryset_list_sp.filter(clinicRegion__iexact='Valencia')
    my_total_count_valencia = queryset_list_valencia.count()
    queryset_list_valencia_ivf = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_valencia_ivf.items():
        eurCurrency_valencia_ivf = val
        if eurCurrency_valencia_ivf is not None:
            usdCurrency_valencia_ivf = val * eurToUsd
            gbpCurrency_valencia_ivf = val * eurToGbp
        else:
            usdCurrency_valencia_ivf = None
            gbpCurrency_valencia_ivf = None

    queryset_list_valencia_egg = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_valencia_egg.items():
        eurCurrency_valencia_egg = val
        if eurCurrency_valencia_egg is not None:
            usdCurrency_valencia_egg = val * eurToUsd
            gbpCurrency_valencia_egg = val * eurToGbp
        else:
            usdCurrency_valencia_egg = None
            gbpCurrency_valencia_egg = None

    queryset_list_valencia_embryo = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_valencia_embryo.items():
        eurCurrency_valencia_embryo = val
        if eurCurrency_valencia_embryo is not None:
            usdCurrency_valencia_embryo = val * eurToUsd
            gbpCurrency_valencia_embryo = val * eurToGbp
        else:
            usdCurrency_valencia_embryo = None
            gbpCurrency_valencia_embryo = None

    queryset_list_valencia_sperm = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_valencia_sperm.items():
        eurCurrency_valencia_sperm = val
        if eurCurrency_valencia_sperm is not None:
            usdCurrency_valencia_sperm = val * eurToUsd
            gbpCurrency_valencia_sperm = val * eurToGbp
        else:
            usdCurrency_valencia_sperm = None
            gbpCurrency_valencia_sperm = None

    queryset_list_valencia_icsi = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_valencia_icsi.items():
        eurCurrency_valencia_icsi = val
        if eurCurrency_valencia_icsi is not None:
            usdCurrency_valencia_icsi = val * eurToUsd
            gbpCurrency_valencia_icsi = val * eurToGbp
        else:
            usdCurrency_valencia_icsi = None
            gbpCurrency_valencia_icsi = None

    queryset_list_valencia_iui = queryset_list_valencia.filter(is_published=True).aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_valencia_iui.items():
        eurCurrency_valencia_iui = val
        if eurCurrency_valencia_iui is not None:
            usdCurrency_valencia_iui = val * eurToUsd
            gbpCurrency_valencia_iui = val * eurToGbp
        else:
            usdCurrency_valencia_iui = None
            gbpCurrency_valencia_iui = None



    context = {
        'gbpCurrency_alicante_ivf': gbpCurrency_alicante_ivf,
        'usdCurrency_alicante_ivf': usdCurrency_alicante_ivf,
        'eurCurrency_alicante_ivf': eurCurrency_alicante_ivf,
        'gbpCurrency_alicante_egg': gbpCurrency_alicante_egg,
        'usdCurrency_alicante_egg': usdCurrency_alicante_egg,
        'eurCurrency_alicante_egg': eurCurrency_alicante_egg,
        'gbpCurrency_alicante_embryo': gbpCurrency_alicante_embryo,
        'usdCurrency_alicante_embryo': usdCurrency_alicante_embryo,
        'eurCurrency_alicante_embryo': eurCurrency_alicante_embryo,
        'gbpCurrency_alicante_sperm': gbpCurrency_alicante_sperm,
        'usdCurrency_alicante_sperm': usdCurrency_alicante_sperm,
        'eurCurrency_alicante_sperm': eurCurrency_alicante_sperm,
        'gbpCurrency_alicante_icsi': gbpCurrency_alicante_icsi,
        'usdCurrency_alicante_icsi': usdCurrency_alicante_icsi,
        'eurCurrency_alicante_icsi': eurCurrency_alicante_icsi,
        'gbpCurrency_alicante_iui': gbpCurrency_alicante_iui,
        'usdCurrency_alicante_iui': usdCurrency_alicante_iui,
        'eurCurrency_alicante_iui': eurCurrency_alicante_iui,
        'my_total_count_alicante': my_total_count_alicante,

        'gbpCurrency_madrid_ivf': gbpCurrency_madrid_ivf,
        'usdCurrency_madrid_ivf': usdCurrency_madrid_ivf,
        'eurCurrency_madrid_ivf': eurCurrency_madrid_ivf,
        'gbpCurrency_madrid_egg': gbpCurrency_madrid_egg,
        'usdCurrency_madrid_egg': usdCurrency_madrid_egg,
        'eurCurrency_madrid_egg': eurCurrency_madrid_egg,
        'gbpCurrency_madrid_embryo': gbpCurrency_madrid_embryo,
        'usdCurrency_madrid_embryo': usdCurrency_madrid_embryo,
        'eurCurrency_madrid_embryo': eurCurrency_madrid_embryo,
        'gbpCurrency_madrid_sperm': gbpCurrency_madrid_sperm,
        'usdCurrency_madrid_sperm': usdCurrency_madrid_sperm,
        'eurCurrency_madrid_sperm': eurCurrency_madrid_sperm,
        'gbpCurrency_madrid_icsi': gbpCurrency_madrid_icsi,
        'usdCurrency_madrid_icsi': usdCurrency_madrid_icsi,
        'eurCurrency_madrid_icsi': eurCurrency_madrid_icsi,
        'gbpCurrency_madrid_iui': gbpCurrency_madrid_iui,
        'usdCurrency_madrid_iui': usdCurrency_madrid_iui,
        'eurCurrency_madrid_iui': eurCurrency_madrid_iui,
        'my_total_count_madrid': my_total_count_madrid,

        'gbpCurrency_barcelona_ivf': gbpCurrency_barcelona_ivf,
        'usdCurrency_barcelona_ivf': usdCurrency_barcelona_ivf,
        'eurCurrency_barcelona_ivf': eurCurrency_barcelona_ivf,
        'gbpCurrency_barcelona_egg': gbpCurrency_barcelona_egg,
        'usdCurrency_barcelona_egg': usdCurrency_barcelona_egg,
        'eurCurrency_barcelona_egg': eurCurrency_barcelona_egg,
        'gbpCurrency_barcelona_embryo': gbpCurrency_barcelona_embryo,
        'usdCurrency_barcelona_embryo': usdCurrency_barcelona_embryo,
        'eurCurrency_barcelona_embryo': eurCurrency_barcelona_embryo,
        'gbpCurrency_barcelona_sperm': gbpCurrency_barcelona_sperm,
        'usdCurrency_barcelona_sperm': usdCurrency_barcelona_sperm,
        'eurCurrency_barcelona_sperm': eurCurrency_barcelona_sperm,
        'gbpCurrency_barcelona_icsi': gbpCurrency_barcelona_icsi,
        'usdCurrency_barcelona_icsi': usdCurrency_barcelona_icsi,
        'eurCurrency_barcelona_icsi': eurCurrency_barcelona_icsi,
        'gbpCurrency_barcelona_iui': gbpCurrency_barcelona_iui,
        'usdCurrency_barcelona_iui': usdCurrency_barcelona_iui,
        'eurCurrency_barcelona_iui': eurCurrency_barcelona_iui,
        'my_total_count_barcelona': my_total_count_barcelona,

        'gbpCurrency_malaga_ivf': gbpCurrency_malaga_ivf,
        'usdCurrency_malaga_ivf': usdCurrency_malaga_ivf,
        'eurCurrency_malaga_ivf': eurCurrency_malaga_ivf,
        'gbpCurrency_malaga_egg': gbpCurrency_malaga_egg,
        'usdCurrency_malaga_egg': usdCurrency_malaga_egg,
        'eurCurrency_malaga_egg': eurCurrency_malaga_egg,
        'gbpCurrency_malaga_embryo': gbpCurrency_malaga_embryo,
        'usdCurrency_malaga_embryo': usdCurrency_malaga_embryo,
        'eurCurrency_malaga_embryo': eurCurrency_malaga_embryo,
        'gbpCurrency_malaga_sperm': gbpCurrency_malaga_sperm,
        'usdCurrency_malaga_sperm': usdCurrency_malaga_sperm,
        'eurCurrency_malaga_sperm': eurCurrency_malaga_sperm,
        'gbpCurrency_malaga_icsi': gbpCurrency_malaga_icsi,
        'usdCurrency_malaga_icsi': usdCurrency_malaga_icsi,
        'eurCurrency_malaga_icsi': eurCurrency_malaga_icsi,
        'gbpCurrency_malaga_iui': gbpCurrency_malaga_iui,
        'usdCurrency_malaga_iui': usdCurrency_malaga_iui,
        'eurCurrency_malaga_iui': eurCurrency_malaga_iui,
        'my_total_count_malaga': my_total_count_malaga,

        'gbpCurrency_sevilla_ivf': gbpCurrency_sevilla_ivf,
        'usdCurrency_sevilla_ivf': usdCurrency_sevilla_ivf,
        'eurCurrency_sevilla_ivf': eurCurrency_sevilla_ivf,
        'gbpCurrency_sevilla_egg': gbpCurrency_sevilla_egg,
        'usdCurrency_sevilla_egg': usdCurrency_sevilla_egg,
        'eurCurrency_sevilla_egg': eurCurrency_sevilla_egg,
        'gbpCurrency_sevilla_embryo': gbpCurrency_sevilla_embryo,
        'usdCurrency_sevilla_embryo': usdCurrency_sevilla_embryo,
        'eurCurrency_sevilla_embryo': eurCurrency_sevilla_embryo,
        'gbpCurrency_sevilla_sperm': gbpCurrency_sevilla_sperm,
        'usdCurrency_sevilla_sperm': usdCurrency_sevilla_sperm,
        'eurCurrency_sevilla_sperm': eurCurrency_sevilla_sperm,
        'gbpCurrency_sevilla_icsi': gbpCurrency_sevilla_icsi,
        'usdCurrency_sevilla_icsi': usdCurrency_sevilla_icsi,
        'eurCurrency_sevilla_icsi': eurCurrency_sevilla_icsi,
        'gbpCurrency_sevilla_iui': gbpCurrency_sevilla_iui,
        'usdCurrency_sevilla_iui': usdCurrency_sevilla_iui,
        'eurCurrency_sevilla_iui': eurCurrency_sevilla_iui,
        'my_total_count_sevilla': my_total_count_sevilla,

        'gbpCurrency_valencia_ivf': gbpCurrency_valencia_ivf,
        'usdCurrency_valencia_ivf': usdCurrency_valencia_ivf,
        'eurCurrency_valencia_ivf': eurCurrency_valencia_ivf,
        'gbpCurrency_valencia_egg': gbpCurrency_valencia_egg,
        'usdCurrency_valencia_egg': usdCurrency_valencia_egg,
        'eurCurrency_valencia_egg': eurCurrency_valencia_egg,
        'gbpCurrency_valencia_embryo': gbpCurrency_valencia_embryo,
        'usdCurrency_valencia_embryo': usdCurrency_valencia_embryo,
        'eurCurrency_valencia_embryo': eurCurrency_valencia_embryo,
        'gbpCurrency_valencia_sperm': gbpCurrency_valencia_sperm,
        'usdCurrency_valencia_sperm': usdCurrency_valencia_sperm,
        'eurCurrency_valencia_sperm': eurCurrency_valencia_sperm,
        'gbpCurrency_valencia_icsi': gbpCurrency_valencia_icsi,
        'usdCurrency_valencia_icsi': usdCurrency_valencia_icsi,
        'eurCurrency_valencia_icsi': eurCurrency_valencia_icsi,
        'gbpCurrency_valencia_iui': gbpCurrency_valencia_iui,
        'usdCurrency_valencia_iui': usdCurrency_valencia_iui,
        'eurCurrency_valencia_iui': eurCurrency_valencia_iui,
        'my_total_count_valencia': my_total_count_valencia,
        }
    return render(request, 'main/Locations/SPLocations/sp-regions-ivf.html', context)


def locationsINRegions(request):
    queryset_list_in = BasicClinic.objects.all()

    #--------------------------------------------------------------------------
    queryset_list_chennai = queryset_list_in.filter(clinicRegion__iexact='Chennai')
    my_total_count_chennai = queryset_list_chennai.count()
    queryset_list_chennai_ivf = queryset_list_chennai.filter(is_published=True).aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_chennai_ivf.items():
        eurCurrency_chennai_ivf = val
        if eurCurrency_chennai_ivf is not None:
            usdCurrency_chennai_ivf = val * eurToUsd
            gbpCurrency_chennai_ivf = val * eurToGbp
        else:
            usdCurrency_chennai_ivf = None
            gbpCurrency_chennai_ivf = None


    context = {
        'gbpCurrency_chennai_ivf': gbpCurrency_chennai_ivf,
        'usdCurrency_chennai_ivf': usdCurrency_chennai_ivf,
        'eurCurrency_chennai_ivf': eurCurrency_chennai_ivf,

        }
    return render(request, 'main/Locations/INLocations/in-regions-ivf.html', context)
