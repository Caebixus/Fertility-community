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
        }

    return render(request, 'main/locations.html', context)
