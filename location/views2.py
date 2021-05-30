from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from itertools import chain
from .currencies import gbpToEur, gbpToUsd, gbpToInr, usdToGbp, usdToEur, usdToInr, eurToGbp, eurToUsd, eurToInr, inrToGbp, inrToEur, inrToUsd, mxnToGbp, mxnToEur, mxnToUsd
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def locationsUSRegions(request):
    queryset_list_us = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_alabama = queryset_list_us.filter(clinicRegion__iexact='Alabama')
    my_total_clinic_count_alabama = queryset_list_alabama.count()

    queryset_list_alabama_ivf = queryset_list_alabama.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_alabama_ivf.items():
        queryset_list_alabama_ivf_val = val

    queryset_list_alabama_egg = queryset_list_alabama.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alabama_egg.items():
        queryset_list_alabama_egg_val = val

    queryset_list_alabama_embryo = queryset_list_alabama.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alabama_embryo.items():
        queryset_list_alabama_embryo_val = val

    queryset_list_alabama_sperm = queryset_list_alabama.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alabama_sperm.items():
        queryset_list_alabama_sperm_val = val

    queryset_list_alabama_icsi = queryset_list_alabama.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alabama_icsi.items():
        queryset_list_alabama_icsi_val = val

    queryset_list_alabama_iui = queryset_list_alabama.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alabama_iui.items():
        queryset_list_alabama_iui = val

    #--------------------------------------------------------------------------
    queryset_list_alaska = queryset_list_us.filter(clinicRegion__iexact='Alaska')
    my_total_clinic_count_alaska = queryset_list_alaska.count()

    queryset_list_alaska_ivf = queryset_list_alaska.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_alaska_ivf.items():
        queryset_list_alaska_ivf_val = val

    queryset_list_alaska_egg = queryset_list_alaska.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alaska_egg.items():
        queryset_list_alaska_egg_val = val

    queryset_list_alaska_embryo = queryset_list_alaska.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alaska_embryo.items():
        queryset_list_alaska_embryo_val = val

    queryset_list_alaska_sperm = queryset_list_alaska.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alaska_sperm.items():
        queryset_list_alaska_sperm_val = val

    queryset_list_alaska_icsi = queryset_list_alaska.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alaska_icsi.items():
        queryset_list_alaska_icsi_val = val

    queryset_list_alaska_iui = queryset_list_alaska.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alaska_iui.items():
        queryset_list_alaska_iui = val

    #--------------------------------------------------------------------------
    queryset_list_arizona = queryset_list_us.filter(clinicRegion__iexact='Arizona')
    my_total_clinic_count_arizona = queryset_list_arizona.count()

    queryset_list_arizona_ivf = queryset_list_arizona.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_arizona_ivf.items():
        queryset_list_arizona_ivf_val = val

    queryset_list_arizona_egg = queryset_list_arizona.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_arizona_egg.items():
        queryset_list_arizona_egg_val = val

    queryset_list_arizona_embryo = queryset_list_arizona.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_arizona_embryo.items():
        queryset_list_arizona_embryo_val = val

    queryset_list_arizona_sperm = queryset_list_arizona.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_arizona_sperm.items():
        queryset_list_arizona_sperm_val = val

    queryset_list_arizona_icsi = queryset_list_arizona.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_arizona_icsi.items():
        queryset_list_arizona_icsi_val = val

    queryset_list_arizona_iui = queryset_list_arizona.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_arizona_iui.items():
        queryset_list_arizona_iui = val

    #--------------------------------------------------------------------------
    queryset_list_arkansas = queryset_list_us.filter(clinicRegion__iexact='Arkansas')
    my_total_clinic_count_arkansas = queryset_list_arkansas.count()

    queryset_list_arkansas_ivf = queryset_list_arkansas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_arkansas_ivf.items():
        queryset_list_arkansas_ivf_val = val

    queryset_list_arkansas_egg = queryset_list_arkansas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_egg.items():
        queryset_list_arkansas_egg_val = val

    queryset_list_arkansas_embryo = queryset_list_arkansas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_embryo.items():
        queryset_list_arkansas_embryo_val = val

    queryset_list_arkansas_sperm = queryset_list_arkansas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_arkansas_sperm.items():
        queryset_list_arkansas_sperm_val = val

    queryset_list_arkansas_icsi = queryset_list_arkansas.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_arkansas_icsi.items():
        queryset_list_arkansas_icsi_val = val

    queryset_list_arkansas_iui = queryset_list_arkansas.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_arkansas_iui.items():
        queryset_list_arkansas_iui = val

    #--------------------------------------------------------------------------
    queryset_list_california = queryset_list_us.filter(clinicRegion__iexact='California')
    my_total_clinic_count_california = queryset_list_california.count()

    queryset_list_california_ivf = queryset_list_california.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_california_ivf.items():
        queryset_list_california_ivf_val = val

    queryset_list_california_egg = queryset_list_california.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_california_egg.items():
        queryset_list_california_egg_val = val

    queryset_list_california_embryo = queryset_list_california.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_california_embryo.items():
        queryset_list_california_embryo_val = val

    queryset_list_california_sperm = queryset_list_california.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_california_sperm.items():
        queryset_list_california_sperm_val = val

    queryset_list_california_icsi = queryset_list_california.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_california_icsi.items():
        queryset_list_california_icsi_val = val

    queryset_list_california_iui = queryset_list_california.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_california_iui.items():
        queryset_list_california_iui = val

    #--------------------------------------------------------------------------
    queryset_list_colorado = queryset_list_us.filter(clinicRegion__iexact='Colorado')
    my_total_clinic_count_colorado = queryset_list_colorado.count()

    queryset_list_colorado_ivf = queryset_list_colorado.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_colorado_ivf.items():
        queryset_list_colorado_ivf_val = val

    queryset_list_colorado_egg = queryset_list_colorado.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_colorado_egg.items():
        queryset_list_colorado_egg_val = val

    queryset_list_colorado_embryo = queryset_list_colorado.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_colorado_embryo.items():
        queryset_list_colorado_embryo_val = val

    queryset_list_colorado_sperm = queryset_list_colorado.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_colorado_sperm.items():
        queryset_list_colorado_sperm_val = val

    queryset_list_colorado_icsi = queryset_list_colorado.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_colorado_icsi.items():
        queryset_list_colorado_icsi_val = val

    queryset_list_colorado_iui = queryset_list_colorado.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_colorado_iui.items():
        queryset_list_colorado_iui = val

    #--------------------------------------------------------------------------
    queryset_list_connecticut = queryset_list_us.filter(clinicRegion__iexact='Connecticut')
    my_total_clinic_count_connecticut = queryset_list_connecticut.count()

    queryset_list_connecticut_ivf = queryset_list_connecticut.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_connecticut_ivf.items():
        queryset_list_connecticut_ivf_val = val

    queryset_list_connecticut_egg = queryset_list_connecticut.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_egg.items():
        queryset_list_connecticut_egg_val = val

    queryset_list_connecticut_embryo = queryset_list_connecticut.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_embryo.items():
        queryset_list_connecticut_embryo_val = val

    queryset_list_connecticut_sperm = queryset_list_connecticut.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_connecticut_sperm.items():
        queryset_list_connecticut_sperm_val = val

    queryset_list_connecticut_icsi = queryset_list_connecticut.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_connecticut_icsi.items():
        queryset_list_connecticut_icsi_val = val

    queryset_list_connecticut_iui = queryset_list_connecticut.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_connecticut_iui.items():
        queryset_list_connecticut_iui = val

    #--------------------------------------------------------------------------
    queryset_list_delaware = queryset_list_us.filter(clinicRegion__iexact='Delaware')
    my_total_clinic_count_delaware = queryset_list_delaware.count()

    queryset_list_delaware_ivf = queryset_list_delaware.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_delaware_ivf.items():
        queryset_list_delaware_ivf_val = val

    queryset_list_delaware_egg = queryset_list_delaware.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_delaware_egg.items():
        queryset_list_delaware_egg_val = val

    queryset_list_delaware_embryo = queryset_list_delaware.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_delaware_embryo.items():
        queryset_list_delaware_embryo_val = val

    queryset_list_delaware_sperm = queryset_list_delaware.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_delaware_sperm.items():
        queryset_list_delaware_sperm_val = val

    queryset_list_delaware_icsi = queryset_list_delaware.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_delaware_icsi.items():
        queryset_list_delaware_icsi_val = val

    queryset_list_delaware_iui = queryset_list_delaware.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_delaware_iui.items():
        queryset_list_delaware_iui = val

    #--------------------------------------------------------------------------
    queryset_list_florida = queryset_list_us.filter(clinicRegion__iexact='Florida')
    my_total_clinic_count_florida = queryset_list_florida.count()

    queryset_list_florida_ivf = queryset_list_florida.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_florida_ivf.items():
        queryset_list_florida_ivf_val = val

    queryset_list_florida_egg = queryset_list_florida.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_florida_egg.items():
        queryset_list_florida_egg_val = val

    queryset_list_florida_embryo = queryset_list_florida.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_florida_embryo.items():
        queryset_list_florida_embryo_val = val

    queryset_list_florida_sperm = queryset_list_florida.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_florida_sperm.items():
        queryset_list_florida_sperm_val = val

    queryset_list_florida_icsi = queryset_list_florida.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_florida_icsi.items():
        queryset_list_florida_icsi_val = val

    queryset_list_florida_iui = queryset_list_florida.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_florida_iui.items():
        queryset_list_florida_iui = val

    #--------------------------------------------------------------------------
    queryset_list_georgia = queryset_list_us.filter(clinicRegion__iexact='Georgia')
    my_total_clinic_count_georgia = queryset_list_georgia.count()

    queryset_list_georgia_ivf = queryset_list_georgia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_georgia_ivf.items():
        queryset_list_georgia_ivf_val = val

    queryset_list_georgia_egg = queryset_list_georgia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_georgia_egg.items():
        queryset_list_georgia_egg_val = val

    queryset_list_georgia_embryo = queryset_list_georgia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_georgia_embryo.items():
        queryset_list_georgia_embryo_val = val

    queryset_list_georgia_sperm = queryset_list_georgia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_georgia_sperm.items():
        queryset_list_georgia_sperm_val = val

    queryset_list_georgia_icsi = queryset_list_georgia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_georgia_icsi.items():
        queryset_list_georgia_icsi_val = val

    queryset_list_georgia_iui = queryset_list_georgia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_georgia_iui.items():
        queryset_list_georgia_iui = val

    #--------------------------------------------------------------------------
    queryset_list_hawaii = queryset_list_us.filter(clinicRegion__iexact='Hawaii')
    my_total_clinic_count_hawaii = queryset_list_hawaii.count()

    queryset_list_hawaii_ivf = queryset_list_hawaii.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_hawaii_ivf.items():
        queryset_list_hawaii_ivf_val = val

    queryset_list_hawaii_egg = queryset_list_hawaii.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_egg.items():
        queryset_list_hawaii_egg_val = val

    queryset_list_hawaii_embryo = queryset_list_hawaii.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_embryo.items():
        queryset_list_hawaii_embryo_val = val

    queryset_list_hawaii_sperm = queryset_list_hawaii.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_hawaii_sperm.items():
        queryset_list_hawaii_sperm_val = val

    queryset_list_hawaii_icsi = queryset_list_hawaii.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_hawaii_icsi.items():
        queryset_list_hawaii_icsi_val = val

    queryset_list_hawaii_iui = queryset_list_hawaii.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_hawaii_iui.items():
        queryset_list_hawaii_iui = val

    #--------------------------------------------------------------------------
    queryset_list_idaho = queryset_list_us.filter(clinicRegion__iexact='Idaho')
    my_total_clinic_count_idaho = queryset_list_idaho.count()

    queryset_list_idaho_ivf = queryset_list_idaho.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_idaho_ivf.items():
        queryset_list_idaho_ivf_val = val

    queryset_list_idaho_egg = queryset_list_idaho.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_idaho_egg.items():
        queryset_list_idaho_egg_val = val

    queryset_list_idaho_embryo = queryset_list_idaho.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_idaho_embryo.items():
        queryset_list_idaho_embryo_val = val

    queryset_list_idaho_sperm = queryset_list_idaho.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_idaho_sperm.items():
        queryset_list_idaho_sperm_val = val

    queryset_list_idaho_icsi = queryset_list_idaho.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_idaho_icsi.items():
        queryset_list_idaho_icsi_val = val

    queryset_list_idaho_iui = queryset_list_idaho.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_idaho_iui.items():
        queryset_list_idaho_iui = val

    #--------------------------------------------------------------------------
    queryset_list_illinois = queryset_list_us.filter(clinicRegion__iexact='Illinois')
    my_total_clinic_count_illinois = queryset_list_illinois.count()

    queryset_list_illinois_ivf = queryset_list_illinois.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_illinois_ivf.items():
        queryset_list_illinois_ivf_val = val

    queryset_list_illinois_egg = queryset_list_illinois.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_illinois_egg.items():
        queryset_list_illinois_egg_val = val

    queryset_list_illinois_embryo = queryset_list_illinois.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_illinois_embryo.items():
        queryset_list_illinois_embryo_val = val

    queryset_list_illinois_sperm = queryset_list_illinois.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_illinois_sperm.items():
        queryset_list_illinois_sperm_val = val

    queryset_list_illinois_icsi = queryset_list_illinois.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_illinois_icsi.items():
        queryset_list_illinois_icsi_val = val

    queryset_list_illinois_iui = queryset_list_illinois.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_illinois_iui.items():
        queryset_list_illinois_iui = val

    #--------------------------------------------------------------------------
    queryset_list_indiana = queryset_list_us.filter(clinicRegion__iexact='Indiana')
    my_total_clinic_count_indiana = queryset_list_indiana.count()

    queryset_list_indiana_ivf = queryset_list_indiana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_indiana_ivf.items():
        queryset_list_indiana_ivf_val = val

    queryset_list_indiana_egg = queryset_list_indiana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_indiana_egg.items():
        queryset_list_indiana_egg_val = val

    queryset_list_indiana_embryo = queryset_list_indiana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_indiana_embryo.items():
        queryset_list_indiana_embryo_val = val

    queryset_list_indiana_sperm = queryset_list_indiana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_indiana_sperm.items():
        queryset_list_indiana_sperm_val = val

    queryset_list_indiana_icsi = queryset_list_indiana.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_indiana_icsi.items():
        queryset_list_indiana_icsi_val = val

    queryset_list_indiana_iui = queryset_list_indiana.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_indiana_iui.items():
        queryset_list_indiana_iui = val

    #--------------------------------------------------------------------------
    queryset_list_iowa = queryset_list_us.filter(clinicRegion__iexact='Iowa')
    my_total_clinic_count_iowa = queryset_list_iowa.count()

    queryset_list_iowa_ivf = queryset_list_iowa.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_iowa_ivf.items():
        queryset_list_iowa_ivf_val = val

    queryset_list_iowa_egg = queryset_list_iowa.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_iowa_egg.items():
        queryset_list_iowa_egg_val = val

    queryset_list_iowa_embryo = queryset_list_iowa.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_iowa_embryo.items():
        queryset_list_iowa_embryo_val = val

    queryset_list_iowa_sperm = queryset_list_iowa.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_iowa_sperm.items():
        queryset_list_iowa_sperm_val = val

    queryset_list_iowa_icsi = queryset_list_iowa.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_iowa_icsi.items():
        queryset_list_iowa_icsi_val = val

    queryset_list_iowa_iui = queryset_list_iowa.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_iowa_iui.items():
        queryset_list_iowa_iui = val

    #--------------------------------------------------------------------------
    queryset_list_kansas = queryset_list_us.filter(clinicRegion__iexact='Kansas')
    my_total_clinic_count_kansas = queryset_list_kansas.count()

    queryset_list_kansas_ivf = queryset_list_kansas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_kansas_ivf.items():
        queryset_list_kansas_ivf_val = val

    queryset_list_kansas_egg = queryset_list_kansas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kansas_egg.items():
        queryset_list_kansas_egg_val = val

    queryset_list_kansas_embryo = queryset_list_kansas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kansas_embryo.items():
        queryset_list_kansas_embryo_val = val

    queryset_list_kansas_sperm = queryset_list_kansas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kansas_sperm.items():
        queryset_list_kansas_sperm_val = val

    queryset_list_kansas_icsi = queryset_list_kansas.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kansas_icsi.items():
        queryset_list_kansas_icsi_val = val

    queryset_list_kansas_iui = queryset_list_kansas.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kansas_iui.items():
        queryset_list_kansas_iui = val

    #--------------------------------------------------------------------------
    queryset_list_kentucky = queryset_list_us.filter(clinicRegion__iexact='Kentucky')
    my_total_clinic_count_kentucky = queryset_list_kentucky.count()

    queryset_list_kentucky_ivf = queryset_list_kentucky.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_kentucky_ivf.items():
        queryset_list_kentucky_ivf_val = val

    queryset_list_kentucky_egg = queryset_list_kentucky.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_egg.items():
        queryset_list_kentucky_egg_val = val

    queryset_list_kentucky_embryo = queryset_list_kentucky.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_embryo.items():
        queryset_list_kentucky_embryo_val = val

    queryset_list_kentucky_sperm = queryset_list_kentucky.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kentucky_sperm.items():
        queryset_list_kentucky_sperm_val = val

    queryset_list_kentucky_icsi = queryset_list_kentucky.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kentucky_icsi.items():
        queryset_list_kentucky_icsi_val = val

    queryset_list_kentucky_iui = queryset_list_kentucky.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kentucky_iui.items():
        queryset_list_kentucky_iui = val

    #--------------------------------------------------------------------------
    queryset_list_louisiana = queryset_list_us.filter(clinicRegion__iexact='Louisiana')
    my_total_clinic_count_louisiana = queryset_list_louisiana.count()

    queryset_list_louisiana_ivf = queryset_list_louisiana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_louisiana_ivf.items():
        queryset_list_louisiana_ivf_val = val

    queryset_list_louisiana_egg = queryset_list_louisiana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_egg.items():
        queryset_list_louisiana_egg_val = val

    queryset_list_louisiana_embryo = queryset_list_louisiana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_embryo.items():
        queryset_list_louisiana_embryo_val = val

    queryset_list_louisiana_sperm = queryset_list_louisiana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_louisiana_sperm.items():
        queryset_list_louisiana_sperm_val = val

    queryset_list_louisiana_icsi = queryset_list_louisiana.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_louisiana_icsi.items():
        queryset_list_louisiana_icsi_val = val

    queryset_list_louisiana_iui = queryset_list_louisiana.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_louisiana_iui.items():
        queryset_list_louisiana_iui = val

    #--------------------------------------------------------------------------
    queryset_list_maine = queryset_list_us.filter(clinicRegion__iexact='Maine')
    my_total_clinic_count_maine = queryset_list_maine.count()

    queryset_list_maine_ivf = queryset_list_maine.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_maine_ivf.items():
        queryset_list_maine_ivf_val = val

    queryset_list_maine_egg = queryset_list_maine.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_maine_egg.items():
        queryset_list_maine_egg_val = val

    queryset_list_maine_embryo = queryset_list_maine.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_maine_embryo.items():
        queryset_list_maine_embryo_val = val

    queryset_list_maine_sperm = queryset_list_maine.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_maine_sperm.items():
        queryset_list_maine_sperm_val = val

    queryset_list_maine_icsi = queryset_list_maine.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_maine_icsi.items():
        queryset_list_maine_icsi_val = val

    queryset_list_maine_iui = queryset_list_maine.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_maine_iui.items():
        queryset_list_maine_iui = val

    #--------------------------------------------------------------------------
    queryset_list_maryland = queryset_list_us.filter(clinicRegion__iexact='Maryland')
    my_total_clinic_count_maryland = queryset_list_maryland.count()

    queryset_list_maryland_ivf = queryset_list_maryland.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_maryland_ivf.items():
        queryset_list_maryland_ivf_val = val

    queryset_list_maryland_egg = queryset_list_maryland.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_maryland_egg.items():
        queryset_list_maryland_egg_val = val

    queryset_list_maryland_embryo = queryset_list_maryland.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_maryland_embryo.items():
        queryset_list_maryland_embryo_val = val

    queryset_list_maryland_sperm = queryset_list_maryland.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_maryland_sperm.items():
        queryset_list_maryland_sperm_val = val

    queryset_list_maryland_icsi = queryset_list_maryland.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_maryland_icsi.items():
        queryset_list_maryland_icsi_val = val

    queryset_list_maryland_iui = queryset_list_maryland.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_maryland_iui.items():
        queryset_list_maryland_iui = val

    #--------------------------------------------------------------------------
    queryset_list_massachusetts = queryset_list_us.filter(clinicRegion__iexact='Massachusetts')
    my_total_clinic_count_massachusetts = queryset_list_massachusetts.count()

    queryset_list_massachusetts_ivf = queryset_list_massachusetts.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_massachusetts_ivf.items():
        queryset_list_massachusetts_ivf_val = val

    queryset_list_massachusetts_egg = queryset_list_massachusetts.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_egg.items():
        queryset_list_massachusetts_egg_val = val

    queryset_list_massachusetts_embryo = queryset_list_massachusetts.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_embryo.items():
        queryset_list_massachusetts_embryo_val = val

    queryset_list_massachusetts_sperm = queryset_list_massachusetts.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_massachusetts_sperm.items():
        queryset_list_massachusetts_sperm_val = val

    queryset_list_massachusetts_icsi = queryset_list_massachusetts.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_massachusetts_icsi.items():
        queryset_list_massachusetts_icsi_val = val

    queryset_list_massachusetts_iui = queryset_list_massachusetts.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_massachusetts_iui.items():
        queryset_list_massachusetts_iui = val

    #--------------------------------------------------------------------------
    queryset_list_michigan = queryset_list_us.filter(clinicRegion__iexact='Michigan')
    my_total_clinic_count_michigan = queryset_list_michigan.count()

    queryset_list_michigan_ivf = queryset_list_michigan.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_michigan_ivf.items():
        queryset_list_michigan_ivf_val = val

    queryset_list_michigan_egg = queryset_list_michigan.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_michigan_egg.items():
        queryset_list_michigan_egg_val = val

    queryset_list_michigan_embryo = queryset_list_michigan.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_michigan_embryo.items():
        queryset_list_michigan_embryo_val = val

    queryset_list_michigan_sperm = queryset_list_michigan.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_michigan_sperm.items():
        queryset_list_michigan_sperm_val = val

    queryset_list_michigan_icsi = queryset_list_michigan.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_michigan_icsi.items():
        queryset_list_michigan_icsi_val = val

    queryset_list_michigan_iui = queryset_list_michigan.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_michigan_iui.items():
        queryset_list_michigan_iui = val

    #--------------------------------------------------------------------------
    queryset_list_minnesota = queryset_list_us.filter(clinicRegion__iexact='Minnesota')
    my_total_clinic_count_minnesota = queryset_list_minnesota.count()

    queryset_list_minnesota_ivf = queryset_list_minnesota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_minnesota_ivf.items():
        queryset_list_minnesota_ivf_val = val

    queryset_list_minnesota_egg = queryset_list_minnesota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_egg.items():
        queryset_list_minnesota_egg_val = val

    queryset_list_minnesota_embryo = queryset_list_minnesota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_embryo.items():
        queryset_list_minnesota_embryo_val = val

    queryset_list_minnesota_sperm = queryset_list_minnesota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_minnesota_sperm.items():
        queryset_list_minnesota_sperm_val = val

    queryset_list_minnesota_icsi = queryset_list_minnesota.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_minnesota_icsi.items():
        queryset_list_minnesota_icsi_val = val

    queryset_list_minnesota_iui = queryset_list_minnesota.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_minnesota_iui.items():
        queryset_list_minnesota_iui = val

    #--------------------------------------------------------------------------
    queryset_list_mississippi = queryset_list_us.filter(clinicRegion__iexact='Mississippi')
    my_total_clinic_count_mississippi = queryset_list_mississippi.count()

    queryset_list_mississippi_ivf = queryset_list_mississippi.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_mississippi_ivf.items():
        queryset_list_mississippi_ivf_val = val

    queryset_list_mississippi_egg = queryset_list_mississippi.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_egg.items():
        queryset_list_mississippi_egg_val = val

    queryset_list_mississippi_embryo = queryset_list_mississippi.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_embryo.items():
        queryset_list_mississippi_embryo_val = val

    queryset_list_mississippi_sperm = queryset_list_mississippi.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_mississippi_sperm.items():
        queryset_list_mississippi_sperm_val = val

    queryset_list_mississippi_icsi = queryset_list_mississippi.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_mississippi_icsi.items():
        queryset_list_mississippi_icsi_val = val

    queryset_list_mississippi_iui = queryset_list_mississippi.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_mississippi_iui.items():
        queryset_list_mississippi_iui = val

    #--------------------------------------------------------------------------
    queryset_list_missouri = queryset_list_us.filter(clinicRegion__iexact='Missouri')
    my_total_clinic_count_missouri = queryset_list_missouri.count()

    queryset_list_missouri_ivf = queryset_list_missouri.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_missouri_ivf.items():
        queryset_list_missouri_ivf_val = val

    queryset_list_missouri_egg = queryset_list_missouri.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_missouri_egg.items():
        queryset_list_missouri_egg_val = val

    queryset_list_missouri_embryo = queryset_list_missouri.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_missouri_embryo.items():
        queryset_list_missouri_embryo_val = val

    queryset_list_missouri_sperm = queryset_list_missouri.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_missouri_sperm.items():
        queryset_list_missouri_sperm_val = val

    queryset_list_missouri_icsi = queryset_list_missouri.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_missouri_icsi.items():
        queryset_list_missouri_icsi_val = val

    queryset_list_missouri_iui = queryset_list_missouri.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_missouri_iui.items():
        queryset_list_missouri_iui = val

    #--------------------------------------------------------------------------
    queryset_list_montana = queryset_list_us.filter(clinicRegion__iexact='Montana')
    my_total_clinic_count_montana = queryset_list_montana.count()

    queryset_list_montana_ivf = queryset_list_montana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_montana_ivf.items():
        queryset_list_montana_ivf_val = val

    queryset_list_montana_egg = queryset_list_montana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_montana_egg.items():
        queryset_list_montana_egg_val = val

    queryset_list_montana_embryo = queryset_list_montana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_montana_embryo.items():
        queryset_list_montana_embryo_val = val

    queryset_list_montana_sperm = queryset_list_montana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_montana_sperm.items():
        queryset_list_montana_sperm_val = val

    queryset_list_montana_icsi = queryset_list_montana.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_montana_icsi.items():
        queryset_list_montana_icsi_val = val

    queryset_list_montana_iui = queryset_list_montana.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_montana_iui.items():
        queryset_list_montana_iui = val

    #--------------------------------------------------------------------------
    queryset_list_nebraska = queryset_list_us.filter(clinicRegion__iexact='Nebraska')
    my_total_clinic_count_nebraska = queryset_list_nebraska.count()

    queryset_list_nebraska_ivf = queryset_list_nebraska.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nebraska_ivf.items():
        queryset_list_nebraska_ivf_val = val

    queryset_list_nebraska_egg = queryset_list_nebraska.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_egg.items():
        queryset_list_nebraska_egg_val = val

    queryset_list_nebraska_embryo = queryset_list_nebraska.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_embryo.items():
        queryset_list_nebraska_embryo_val = val

    queryset_list_nebraska_sperm = queryset_list_nebraska.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nebraska_sperm.items():
        queryset_list_nebraska_sperm_val = val

    queryset_list_nebraska_icsi = queryset_list_nebraska.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nebraska_icsi.items():
        queryset_list_nebraska_icsi_val = val

    queryset_list_nebraska_iui = queryset_list_nebraska.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nebraska_iui.items():
        queryset_list_nebraska_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newhampshire = queryset_list_us.filter(clinicRegion__iexact='New Hampshire')
    my_total_clinic_count_newhampshire = queryset_list_newhampshire.count()

    queryset_list_newhampshire_ivf = queryset_list_newhampshire.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newhampshire_ivf.items():
        queryset_list_newhampshire_ivf_val = val

    queryset_list_newhampshire_egg = queryset_list_newhampshire.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_egg.items():
        queryset_list_newhampshire_egg_val = val

    queryset_list_newhampshire_embryo = queryset_list_newhampshire.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_embryo.items():
        queryset_list_newhampshire_embryo_val = val

    queryset_list_newhampshire_sperm = queryset_list_newhampshire.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newhampshire_sperm.items():
        queryset_list_newhampshire_sperm_val = val

    queryset_list_newhampshire_icsi = queryset_list_newhampshire.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newhampshire_icsi.items():
        queryset_list_newhampshire_icsi_val = val

    queryset_list_newhampshire_iui = queryset_list_newhampshire.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newhampshire_iui.items():
        queryset_list_newhampshire_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newjersey = queryset_list_us.filter(clinicRegion__iexact='New Jersey')
    my_total_clinic_count_newjersey = queryset_list_newjersey.count()

    queryset_list_newjersey_ivf = queryset_list_newjersey.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newjersey_ivf.items():
        queryset_list_newjersey_ivf_val = val

    queryset_list_newjersey_egg = queryset_list_newjersey.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_egg.items():
        queryset_list_newjersey_egg_val = val

    queryset_list_newjersey_embryo = queryset_list_newjersey.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_embryo.items():
        queryset_list_newjersey_embryo_val = val

    queryset_list_newjersey_sperm = queryset_list_newjersey.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newjersey_sperm.items():
        queryset_list_newjersey_sperm_val = val

    queryset_list_newjersey_icsi = queryset_list_newjersey.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newjersey_icsi.items():
        queryset_list_newjersey_icsi_val = val

    queryset_list_newjersey_iui = queryset_list_newjersey.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newjersey_iui.items():
        queryset_list_newjersey_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newmexico = queryset_list_us.filter(clinicRegion__iexact='New Mexico')
    my_total_clinic_count_newmexico = queryset_list_newmexico.count()

    queryset_list_newmexico_ivf = queryset_list_newmexico.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newmexico_ivf.items():
        queryset_list_newmexico_ivf_val = val

    queryset_list_newmexico_egg = queryset_list_newmexico.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_egg.items():
        queryset_list_newmexico_egg_val = val

    queryset_list_newmexico_embryo = queryset_list_newmexico.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_embryo.items():
        queryset_list_newmexico_embryo_val = val

    queryset_list_newmexico_sperm = queryset_list_newmexico.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newmexico_sperm.items():
        queryset_list_newmexico_sperm_val = val

    queryset_list_newmexico_icsi = queryset_list_newmexico.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newmexico_icsi.items():
        queryset_list_newmexico_icsi_val = val

    queryset_list_newmexico_iui = queryset_list_newmexico.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newmexico_iui.items():
        queryset_list_newmexico_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newyork = queryset_list_us.filter(clinicRegion__iexact='New York')
    my_total_clinic_count_newyork = queryset_list_newyork.count()

    queryset_list_newyork_ivf = queryset_list_newyork.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newyork_ivf.items():
        queryset_list_newyork_ivf_val = val

    queryset_list_newyork_egg = queryset_list_newyork.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newyork_egg.items():
        queryset_list_newyork_egg_val = val

    queryset_list_newyork_embryo = queryset_list_newyork.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newyork_embryo.items():
        queryset_list_newyork_embryo_val = val

    queryset_list_newyork_sperm = queryset_list_newyork.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newyork_sperm.items():
        queryset_list_newyork_sperm_val = val

    queryset_list_newyork_icsi = queryset_list_newyork.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newyork_icsi.items():
        queryset_list_newyork_icsi_val = val

    queryset_list_newyork_iui = queryset_list_newyork.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newyork_iui.items():
        queryset_list_newyork_iui = val

    #--------------------------------------------------------------------------
    queryset_list_northcarolina = queryset_list_us.filter(clinicRegion__iexact='North Carolina')
    my_total_clinic_count_northcarolina = queryset_list_northcarolina.count()

    queryset_list_northcarolina_ivf = queryset_list_northcarolina.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_northcarolina_ivf.items():
        queryset_list_northcarolina_ivf_val = val

    queryset_list_northcarolina_egg = queryset_list_northcarolina.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_egg.items():
        queryset_list_northcarolina_egg_val = val

    queryset_list_northcarolina_embryo = queryset_list_northcarolina.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_embryo.items():
        queryset_list_northcarolina_embryo_val = val

    queryset_list_northcarolina_sperm = queryset_list_northcarolina.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_northcarolina_sperm.items():
        queryset_list_northcarolina_sperm_val = val

    queryset_list_northcarolina_icsi = queryset_list_northcarolina.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_northcarolina_icsi.items():
        queryset_list_northcarolina_icsi_val = val

    queryset_list_northcarolina_iui = queryset_list_northcarolina.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_northcarolina_iui.items():
        queryset_list_northcarolina_iui = val

    #--------------------------------------------------------------------------
    queryset_list_northdakota = queryset_list_us.filter(clinicRegion__iexact='North Dakota')
    my_total_clinic_count_northdakota = queryset_list_northdakota.count()

    queryset_list_northdakota_ivf = queryset_list_northdakota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_northdakota_ivf.items():
        queryset_list_northdakota_ivf_val = val

    queryset_list_northdakota_egg = queryset_list_northdakota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_egg.items():
        queryset_list_northdakota_egg_val = val

    queryset_list_northdakota_embryo = queryset_list_northdakota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_embryo.items():
        queryset_list_northdakota_embryo_val = val

    queryset_list_northdakota_sperm = queryset_list_northdakota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_northdakota_sperm.items():
        queryset_list_northdakota_sperm_val = val

    queryset_list_northdakota_icsi = queryset_list_northdakota.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_northdakota_icsi.items():
        queryset_list_northdakota_icsi_val = val

    queryset_list_northdakota_iui = queryset_list_northdakota.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_northdakota_iui.items():
        queryset_list_northdakota_iui = val

    #--------------------------------------------------------------------------
    queryset_list_nevada = queryset_list_us.filter(clinicRegion__iexact='Nevada')
    my_total_clinic_count_nevada = queryset_list_nevada.count()

    queryset_list_nevada_ivf = queryset_list_nevada.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nevada_ivf.items():
        queryset_list_nevada_ivf_val = val

    queryset_list_nevada_egg = queryset_list_nevada.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nevada_egg.items():
        queryset_list_nevada_egg_val = val

    queryset_list_nevada_embryo = queryset_list_nevada.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nevada_embryo.items():
        queryset_list_nevada_embryo_val = val

    queryset_list_nevada_sperm = queryset_list_nevada.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nevada_sperm.items():
        queryset_list_nevada_sperm_val = val

    queryset_list_nevada_icsi = queryset_list_nevada.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nevada_icsi.items():
        queryset_list_nevada_icsi_val = val

    queryset_list_nevada_iui = queryset_list_nevada.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nevada_iui.items():
        queryset_list_nevada_iui = val

    #--------------------------------------------------------------------------
    queryset_list_ohio = queryset_list_us.filter(clinicRegion__iexact='Ohio')
    my_total_clinic_count_ohio = queryset_list_ohio.count()

    queryset_list_ohio_ivf = queryset_list_ohio.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_ohio_ivf.items():
        queryset_list_ohio_ivf_val = val

    queryset_list_ohio_egg = queryset_list_ohio.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_ohio_egg.items():
        queryset_list_ohio_egg_val = val

    queryset_list_ohio_embryo = queryset_list_ohio.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_ohio_embryo.items():
        queryset_list_ohio_embryo_val = val

    queryset_list_ohio_sperm = queryset_list_ohio.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_ohio_sperm.items():
        queryset_list_ohio_sperm_val = val

    queryset_list_ohio_icsi = queryset_list_ohio.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_ohio_icsi.items():
        queryset_list_ohio_icsi_val = val

    queryset_list_ohio_iui = queryset_list_ohio.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_ohio_iui.items():
        queryset_list_ohio_iui = val

    #--------------------------------------------------------------------------
    queryset_list_oklahoma = queryset_list_us.filter(clinicRegion__iexact='Oklahoma')
    my_total_clinic_count_oklahoma = queryset_list_oklahoma.count()

    queryset_list_oklahoma_ivf = queryset_list_oklahoma.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_oklahoma_ivf.items():
        queryset_list_oklahoma_ivf_val = val

    queryset_list_oklahoma_egg = queryset_list_oklahoma.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_egg.items():
        queryset_list_oklahoma_egg_val = val

    queryset_list_oklahoma_embryo = queryset_list_oklahoma.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_embryo.items():
        queryset_list_oklahoma_embryo_val = val

    queryset_list_oklahoma_sperm = queryset_list_oklahoma.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_oklahoma_sperm.items():
        queryset_list_oklahoma_sperm_val = val

    queryset_list_oklahoma_icsi = queryset_list_oklahoma.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_oklahoma_icsi.items():
        queryset_list_oklahoma_icsi_val = val

    queryset_list_oklahoma_iui = queryset_list_oklahoma.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_oklahoma_iui.items():
        queryset_list_oklahoma_iui = val

    #--------------------------------------------------------------------------
    queryset_list_oregon = queryset_list_us.filter(clinicRegion__iexact='Oregon')
    my_total_clinic_count_oregon = queryset_list_oregon.count()

    queryset_list_oregon_ivf = queryset_list_oregon.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_oregon_ivf.items():
        queryset_list_oregon_ivf_val = val

    queryset_list_oregon_egg = queryset_list_oregon.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_oregon_egg.items():
        queryset_list_oregon_egg_val = val

    queryset_list_oregon_embryo = queryset_list_oregon.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_oregon_embryo.items():
        queryset_list_oregon_embryo_val = val

    queryset_list_oregon_sperm = queryset_list_oregon.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_oregon_sperm.items():
        queryset_list_oregon_sperm_val = val

    queryset_list_oregon_icsi = queryset_list_oregon.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_oregon_icsi.items():
        queryset_list_oregon_icsi_val = val

    queryset_list_oregon_iui = queryset_list_oregon.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_oregon_iui.items():
        queryset_list_oregon_iui = val

    #--------------------------------------------------------------------------
    queryset_list_pennsylvania = queryset_list_us.filter(clinicRegion__iexact='Pennsylvania')
    my_total_clinic_count_pennsylvania = queryset_list_pennsylvania.count()

    queryset_list_pennsylvania_ivf = queryset_list_pennsylvania.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_pennsylvania_ivf.items():
        queryset_list_pennsylvania_ivf_val = val

    queryset_list_pennsylvania_egg = queryset_list_pennsylvania.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_egg.items():
        queryset_list_pennsylvania_egg_val = val

    queryset_list_pennsylvania_embryo = queryset_list_pennsylvania.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_embryo.items():
        queryset_list_pennsylvania_embryo_val = val

    queryset_list_pennsylvania_sperm = queryset_list_pennsylvania.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_pennsylvania_sperm.items():
        queryset_list_pennsylvania_sperm_val = val

    queryset_list_pennsylvania_icsi = queryset_list_pennsylvania.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_pennsylvania_icsi.items():
        queryset_list_pennsylvania_icsi_val = val

    queryset_list_pennsylvania_iui = queryset_list_pennsylvania.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_pennsylvania_iui.items():
        queryset_list_pennsylvania_iui = val

    #--------------------------------------------------------------------------
    queryset_list_puertorico = queryset_list_us.filter(clinicRegion__iexact='Puerto Rico')
    my_total_clinic_count_puertorico = queryset_list_puertorico.count()

    queryset_list_puertorico_ivf = queryset_list_puertorico.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_puertorico_ivf.items():
        queryset_list_puertorico_ivf_val = val

    queryset_list_puertorico_egg = queryset_list_puertorico.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_egg.items():
        queryset_list_puertorico_egg_val = val

    queryset_list_puertorico_embryo = queryset_list_puertorico.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_embryo.items():
        queryset_list_puertorico_embryo_val = val

    queryset_list_puertorico_sperm = queryset_list_puertorico.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_puertorico_sperm.items():
        queryset_list_puertorico_sperm_val = val

    queryset_list_puertorico_icsi = queryset_list_puertorico.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_puertorico_icsi.items():
        queryset_list_puertorico_icsi_val = val

    queryset_list_puertorico_iui = queryset_list_puertorico.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_puertorico_iui.items():
        queryset_list_puertorico_iui = val

    #--------------------------------------------------------------------------
    queryset_list_southcarolina = queryset_list_us.filter(clinicRegion__iexact='South Carolina')
    my_total_clinic_count_southcarolina = queryset_list_southcarolina.count()

    queryset_list_southcarolina_ivf = queryset_list_southcarolina.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_southcarolina_ivf.items():
        queryset_list_southcarolina_ivf_val = val

    queryset_list_southcarolina_egg = queryset_list_southcarolina.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_egg.items():
        queryset_list_southcarolina_egg_val = val

    queryset_list_southcarolina_embryo = queryset_list_southcarolina.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_embryo.items():
        queryset_list_southcarolina_embryo_val = val

    queryset_list_southcarolina_sperm = queryset_list_southcarolina.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_southcarolina_sperm.items():
        queryset_list_southcarolina_sperm_val = val

    queryset_list_southcarolina_icsi = queryset_list_southcarolina.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_southcarolina_icsi.items():
        queryset_list_southcarolina_icsi_val = val

    queryset_list_southcarolina_iui = queryset_list_southcarolina.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_southcarolina_iui.items():
        queryset_list_southcarolina_iui = val

    #--------------------------------------------------------------------------
    queryset_list_rhodeisland = queryset_list_us.filter(clinicRegion__iexact='Rhode Island')
    my_total_clinic_count_rhodeisland = queryset_list_rhodeisland.count()

    queryset_list_rhodeisland_ivf = queryset_list_rhodeisland.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_rhodeisland_ivf.items():
        queryset_list_rhodeisland_ivf_val = val

    queryset_list_rhodeisland_egg = queryset_list_rhodeisland.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_egg.items():
        queryset_list_rhodeisland_egg_val = val

    queryset_list_rhodeisland_embryo = queryset_list_rhodeisland.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_embryo.items():
        queryset_list_rhodeisland_embryo_val = val

    queryset_list_rhodeisland_sperm = queryset_list_rhodeisland.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_rhodeisland_sperm.items():
        queryset_list_rhodeisland_sperm_val = val

    queryset_list_rhodeisland_icsi = queryset_list_rhodeisland.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_rhodeisland_icsi.items():
        queryset_list_rhodeisland_icsi_val = val

    queryset_list_rhodeisland_iui = queryset_list_rhodeisland.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_rhodeisland_iui.items():
        queryset_list_rhodeisland_iui = val

    #--------------------------------------------------------------------------
    queryset_list_southdakota = queryset_list_us.filter(clinicRegion__iexact='South Dakota')
    my_total_clinic_count_southdakota = queryset_list_southdakota.count()

    queryset_list_southdakota_ivf = queryset_list_southdakota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_southdakota_ivf.items():
        queryset_list_southdakota_ivf_val = val

    queryset_list_southdakota_egg = queryset_list_southdakota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_egg.items():
        queryset_list_southdakota_egg_val = val

    queryset_list_southdakota_embryo = queryset_list_southdakota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_embryo.items():
        queryset_list_southdakota_embryo_val = val

    queryset_list_southdakota_sperm = queryset_list_southdakota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_southdakota_sperm.items():
        queryset_list_southdakota_sperm_val = val

    queryset_list_southdakota_icsi = queryset_list_southdakota.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_southdakota_icsi.items():
        queryset_list_southdakota_icsi_val = val

    queryset_list_southdakota_iui = queryset_list_southdakota.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_southdakota_iui.items():
        queryset_list_southdakota_iui = val

    #--------------------------------------------------------------------------
    queryset_list_tennessee = queryset_list_us.filter(clinicRegion__iexact='Tennessee')
    my_total_clinic_count_tennessee = queryset_list_tennessee.count()

    queryset_list_tennessee_ivf = queryset_list_tennessee.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_tennessee_ivf.items():
        queryset_list_tennessee_ivf_val = val

    queryset_list_tennessee_egg = queryset_list_tennessee.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_egg.items():
        queryset_list_tennessee_egg_val = val

    queryset_list_tennessee_embryo = queryset_list_tennessee.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_embryo.items():
        queryset_list_tennessee_embryo_val = val

    queryset_list_tennessee_sperm = queryset_list_tennessee.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_tennessee_sperm.items():
        queryset_list_tennessee_sperm_val = val

    queryset_list_tennessee_icsi = queryset_list_tennessee.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_tennessee_icsi.items():
        queryset_list_tennessee_icsi_val = val

    queryset_list_tennessee_iui = queryset_list_tennessee.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_tennessee_iui.items():
        queryset_list_tennessee_iui = val

    #--------------------------------------------------------------------------
    queryset_list_texas = queryset_list_us.filter(clinicRegion__iexact='Texas')
    my_total_clinic_count_texas = queryset_list_texas.count()

    queryset_list_texas_ivf = queryset_list_texas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_texas_ivf.items():
        queryset_list_texas_ivf_val = val

    queryset_list_texas_egg = queryset_list_texas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_texas_egg.items():
        queryset_list_texas_egg_val = val

    queryset_list_texas_embryo = queryset_list_texas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_texas_embryo.items():
        queryset_list_texas_embryo_val = val

    queryset_list_texas_sperm = queryset_list_texas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_texas_sperm.items():
        queryset_list_texas_sperm_val = val

    queryset_list_texas_icsi = queryset_list_texas.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_texas_icsi.items():
        queryset_list_texas_icsi_val = val

    queryset_list_texas_iui = queryset_list_texas.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_texas_iui.items():
        queryset_list_texas_iui = val

    #--------------------------------------------------------------------------
    queryset_list_utah = queryset_list_us.filter(clinicRegion__iexact='Utah')
    my_total_clinic_count_utah = queryset_list_utah.count()

    queryset_list_utah_ivf = queryset_list_utah.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_utah_ivf.items():
        queryset_list_utah_ivf_val = val

    queryset_list_utah_egg = queryset_list_utah.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_utah_egg.items():
        queryset_list_utah_egg_val = val

    queryset_list_utah_embryo = queryset_list_utah.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_utah_embryo.items():
        queryset_list_utah_embryo_val = val

    queryset_list_utah_sperm = queryset_list_utah.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_utah_sperm.items():
        queryset_list_utah_sperm_val = val

    queryset_list_utah_icsi = queryset_list_utah.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_utah_icsi.items():
        queryset_list_utah_icsi_val = val

    queryset_list_utah_iui = queryset_list_utah.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_utah_iui.items():
        queryset_list_utah_iui = val

    #--------------------------------------------------------------------------
    queryset_list_vermont = queryset_list_us.filter(clinicRegion__iexact='Vermont')
    my_total_clinic_count_vermont = queryset_list_vermont.count()

    queryset_list_vermont_ivf = queryset_list_vermont.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_vermont_ivf.items():
        queryset_list_vermont_ivf_val = val

    queryset_list_vermont_egg = queryset_list_vermont.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_vermont_egg.items():
        queryset_list_vermont_egg_val = val

    queryset_list_vermont_embryo = queryset_list_vermont.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_vermont_embryo.items():
        queryset_list_vermont_embryo_val = val

    queryset_list_vermont_sperm = queryset_list_vermont.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_vermont_sperm.items():
        queryset_list_vermont_sperm_val = val

    queryset_list_vermont_icsi = queryset_list_vermont.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_vermont_icsi.items():
        queryset_list_vermont_icsi_val = val

    queryset_list_vermont_iui = queryset_list_vermont.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_vermont_iui.items():
        queryset_list_vermont_iui = val

    #--------------------------------------------------------------------------
    queryset_list_virginia = queryset_list_us.filter(clinicRegion__iexact='Virginia')
    my_total_clinic_count_virginia = queryset_list_virginia.count()

    queryset_list_virginia_ivf = queryset_list_virginia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_virginia_ivf.items():
        queryset_list_virginia_ivf_val = val

    queryset_list_virginia_egg = queryset_list_virginia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_virginia_egg.items():
        queryset_list_virginia_egg_val = val

    queryset_list_virginia_embryo = queryset_list_virginia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_virginia_embryo.items():
        queryset_list_virginia_embryo_val = val

    queryset_list_virginia_sperm = queryset_list_virginia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_virginia_sperm.items():
        queryset_list_virginia_sperm_val = val

    queryset_list_virginia_icsi = queryset_list_virginia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_virginia_icsi.items():
        queryset_list_virginia_icsi_val = val

    queryset_list_virginia_iui = queryset_list_virginia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_virginia_iui.items():
        queryset_list_virginia_iui = val

    #--------------------------------------------------------------------------
    queryset_list_washington = queryset_list_us.filter(clinicRegion__iexact='Washington')
    my_total_clinic_count_washington = queryset_list_washington.count()

    queryset_list_washington_ivf = queryset_list_washington.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_washington_ivf.items():
        queryset_list_washington_ivf_val = val

    queryset_list_washington_egg = queryset_list_washington.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_washington_egg.items():
        queryset_list_washington_egg_val = val

    queryset_list_washington_embryo = queryset_list_washington.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_washington_embryo.items():
        queryset_list_washington_embryo_val = val

    queryset_list_washington_sperm = queryset_list_washington.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_washington_sperm.items():
        queryset_list_washington_sperm_val = val

    queryset_list_washington_icsi = queryset_list_washington.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_washington_icsi.items():
        queryset_list_washington_icsi_val = val

    queryset_list_washington_iui = queryset_list_washington.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_washington_iui.items():
        queryset_list_washington_iui = val

    #--------------------------------------------------------------------------
    queryset_list_westvirginia = queryset_list_us.filter(clinicRegion__iexact='West Virginia')
    my_total_clinic_count_westvirginia = queryset_list_westvirginia.count()

    queryset_list_westvirginia_ivf = queryset_list_westvirginia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_westvirginia_ivf.items():
        queryset_list_westvirginia_ivf_val = val

    queryset_list_westvirginia_egg = queryset_list_westvirginia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_egg.items():
        queryset_list_westvirginia_egg_val = val

    queryset_list_westvirginia_embryo = queryset_list_westvirginia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_embryo.items():
        queryset_list_westvirginia_embryo_val = val

    queryset_list_westvirginia_sperm = queryset_list_westvirginia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_westvirginia_sperm.items():
        queryset_list_westvirginia_sperm_val = val

    queryset_list_westvirginia_icsi = queryset_list_westvirginia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_westvirginia_icsi.items():
        queryset_list_westvirginia_icsi_val = val

    queryset_list_westvirginia_iui = queryset_list_westvirginia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_westvirginia_iui.items():
        queryset_list_westvirginia_iui = val

    #--------------------------------------------------------------------------
    queryset_list_wisconsin = queryset_list_us.filter(clinicRegion__iexact='Wisconsin')
    my_total_clinic_count_wisconsin = queryset_list_wisconsin.count()

    queryset_list_wisconsin_ivf = queryset_list_wisconsin.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_wisconsin_ivf.items():
        queryset_list_wisconsin_ivf_val = val

    queryset_list_wisconsin_egg = queryset_list_wisconsin.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_egg.items():
        queryset_list_wisconsin_egg_val = val

    queryset_list_wisconsin_embryo = queryset_list_wisconsin.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_embryo.items():
        queryset_list_wisconsin_embryo_val = val

    queryset_list_wisconsin_sperm = queryset_list_wisconsin.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_wisconsin_sperm.items():
        queryset_list_wisconsin_sperm_val = val

    queryset_list_wisconsin_icsi = queryset_list_wisconsin.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_wisconsin_icsi.items():
        queryset_list_wisconsin_icsi_val = val

    queryset_list_wisconsin_iui = queryset_list_wisconsin.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_wisconsin_iui.items():
        queryset_list_wisconsin_iui = val

    #--------------------------------------------------------------------------
    queryset_list_wyoming = queryset_list_us.filter(clinicRegion__iexact='Wyoming')
    my_total_clinic_count_wyoming = queryset_list_wyoming.count()

    queryset_list_wyoming_ivf = queryset_list_wyoming.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_wyoming_ivf.items():
        queryset_list_wyoming_ivf_val = val

    queryset_list_wyoming_egg = queryset_list_wyoming.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_egg.items():
        queryset_list_wyoming_egg_val = val

    queryset_list_wyoming_embryo = queryset_list_wyoming.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_embryo.items():
        queryset_list_wyoming_embryo_val = val

    queryset_list_wyoming_sperm = queryset_list_wyoming.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_wyoming_sperm.items():
        queryset_list_wyoming_sperm_val = val

    queryset_list_wyoming_icsi = queryset_list_wyoming.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_wyoming_icsi.items():
        queryset_list_wyoming_icsi_val = val

    queryset_list_wyoming_iui = queryset_list_wyoming.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_wyoming_iui.items():
        queryset_list_wyoming_iui = val

    #--------------------------------------------------------------------------
    queryset_list_districtofcolumbia = queryset_list_us.filter(clinicRegion__iexact='District of Columbia')
    my_total_clinic_count_districtofcolumbia = queryset_list_districtofcolumbia.count()

    queryset_list_districtofcolumbia_ivf = queryset_list_districtofcolumbia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_ivf.items():
        queryset_list_districtofcolumbia_ivf_val = val

    queryset_list_districtofcolumbia_egg = queryset_list_districtofcolumbia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_egg.items():
        queryset_list_districtofcolumbia_egg_val = val

    queryset_list_districtofcolumbia_embryo = queryset_list_districtofcolumbia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_embryo.items():
        queryset_list_districtofcolumbia_embryo_val = val

    queryset_list_districtofcolumbia_sperm = queryset_list_districtofcolumbia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_districtofcolumbia_sperm.items():
        queryset_list_districtofcolumbia_sperm_val = val

    queryset_list_districtofcolumbia_icsi = queryset_list_districtofcolumbia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_icsi.items():
        queryset_list_districtofcolumbia_icsi_val = val

    queryset_list_districtofcolumbia_iui = queryset_list_districtofcolumbia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_districtofcolumbia_iui.items():
        queryset_list_districtofcolumbia_iui = val

    context = {
        'queryset_list_alabama_ivf_val': queryset_list_alabama_ivf_val,
        'queryset_list_alabama_egg_val': queryset_list_alabama_egg_val,
        'queryset_list_alabama_embryo_val': queryset_list_alabama_embryo_val,
        'queryset_list_alabama_sperm_val': queryset_list_alabama_sperm_val,
        'queryset_list_alabama_icsi_val': queryset_list_alabama_icsi_val,
        'queryset_list_alabama_iui': queryset_list_alabama_iui,

        'queryset_list_arizona_ivf_val': queryset_list_arizona_ivf_val,
        'queryset_list_arizona_egg_val': queryset_list_arizona_egg_val,
        'queryset_list_arizona_embryo_val': queryset_list_arizona_embryo_val,
        'queryset_list_arizona_sperm_val': queryset_list_arizona_sperm_val,
        'queryset_list_arizona_icsi_val': queryset_list_arizona_icsi_val,
        'queryset_list_arizona_iui': queryset_list_arizona_iui,

        'queryset_list_alaska_ivf_val': queryset_list_alaska_ivf_val,
        'queryset_list_alaska_egg_val': queryset_list_alaska_egg_val,
        'queryset_list_alaska_embryo_val': queryset_list_alaska_embryo_val,
        'queryset_list_alaska_sperm_val': queryset_list_alaska_sperm_val,
        'queryset_list_alaska_icsi_val': queryset_list_alaska_icsi_val,
        'queryset_list_alaska_iui': queryset_list_alaska_iui,

        'queryset_list_arkansas_ivf_val': queryset_list_arkansas_ivf_val,
        'queryset_list_arkansas_egg_val': queryset_list_arkansas_egg_val,
        'queryset_list_arkansas_embryo_val': queryset_list_arkansas_embryo_val,
        'queryset_list_arkansas_sperm_val': queryset_list_arkansas_sperm_val,
        'queryset_list_arkansas_icsi_val': queryset_list_arkansas_icsi_val,
        'queryset_list_arkansas_iui': queryset_list_arkansas_iui,

        'queryset_list_california_ivf_val': queryset_list_california_ivf_val,
        'queryset_list_california_egg_val': queryset_list_california_egg_val,
        'queryset_list_california_embryo_val': queryset_list_california_embryo_val,
        'queryset_list_california_sperm_val': queryset_list_california_sperm_val,
        'queryset_list_california_icsi_val': queryset_list_california_icsi_val,
        'queryset_list_california_iui': queryset_list_california_iui,

        'queryset_list_colorado_ivf_val': queryset_list_colorado_ivf_val,
        'queryset_list_colorado_egg_val': queryset_list_colorado_egg_val,
        'queryset_list_colorado_embryo_val': queryset_list_colorado_embryo_val,
        'queryset_list_colorado_sperm_val': queryset_list_colorado_sperm_val,
        'queryset_list_colorado_icsi_val': queryset_list_colorado_icsi_val,
        'queryset_list_colorado_iui': queryset_list_colorado_iui,

        'queryset_list_connecticut_ivf_val': queryset_list_connecticut_ivf_val,
        'queryset_list_connecticut_egg_val': queryset_list_connecticut_egg_val,
        'queryset_list_connecticut_embryo_val': queryset_list_connecticut_embryo_val,
        'queryset_list_connecticut_sperm_val': queryset_list_connecticut_sperm_val,
        'queryset_list_connecticut_icsi_val': queryset_list_connecticut_icsi_val,
        'queryset_list_connecticut_iui': queryset_list_connecticut_iui,

        'queryset_list_delaware_ivf_val': queryset_list_delaware_ivf_val,
        'queryset_list_delaware_egg_val': queryset_list_delaware_egg_val,
        'queryset_list_delaware_embryo_val': queryset_list_delaware_embryo_val,
        'queryset_list_delaware_sperm_val': queryset_list_delaware_sperm_val,
        'queryset_list_delaware_icsi_val': queryset_list_delaware_icsi_val,
        'queryset_list_delaware_iui': queryset_list_delaware_iui,

        'queryset_list_florida_ivf_val': queryset_list_florida_ivf_val,
        'queryset_list_florida_egg_val': queryset_list_florida_egg_val,
        'queryset_list_florida_embryo_val': queryset_list_florida_embryo_val,
        'queryset_list_florida_sperm_val': queryset_list_florida_sperm_val,
        'queryset_list_florida_icsi_val': queryset_list_florida_icsi_val,
        'queryset_list_florida_iui': queryset_list_florida_iui,

        'queryset_list_georgia_ivf_val': queryset_list_georgia_ivf_val,
        'queryset_list_georgia_egg_val': queryset_list_georgia_egg_val,
        'queryset_list_georgia_embryo_val': queryset_list_georgia_embryo_val,
        'queryset_list_georgia_sperm_val': queryset_list_georgia_sperm_val,
        'queryset_list_georgia_icsi_val': queryset_list_georgia_icsi_val,
        'queryset_list_georgia_iui': queryset_list_georgia_iui,

        'queryset_list_hawaii_ivf_val': queryset_list_hawaii_ivf_val,
        'queryset_list_hawaii_egg_val': queryset_list_hawaii_egg_val,
        'queryset_list_hawaii_embryo_val': queryset_list_hawaii_embryo_val,
        'queryset_list_hawaii_sperm_val': queryset_list_hawaii_sperm_val,
        'queryset_list_hawaii_icsi_val': queryset_list_hawaii_icsi_val,
        'queryset_list_hawaii_iui': queryset_list_hawaii_iui,

        'queryset_list_idaho_ivf_val': queryset_list_idaho_ivf_val,
        'queryset_list_idaho_egg_val': queryset_list_idaho_egg_val,
        'queryset_list_idaho_embryo_val': queryset_list_idaho_embryo_val,
        'queryset_list_idaho_sperm_val': queryset_list_idaho_sperm_val,
        'queryset_list_idaho_icsi_val': queryset_list_idaho_icsi_val,
        'queryset_list_idaho_iui': queryset_list_idaho_iui,

        'queryset_list_illinois_ivf_val': queryset_list_illinois_ivf_val,
        'queryset_list_illinois_egg_val': queryset_list_illinois_egg_val,
        'queryset_list_illinois_embryo_val': queryset_list_illinois_embryo_val,
        'queryset_list_illinois_sperm_val': queryset_list_illinois_sperm_val,
        'queryset_list_illinois_icsi_val': queryset_list_illinois_icsi_val,
        'queryset_list_illinois_iui': queryset_list_illinois_iui,

        'queryset_list_indiana_ivf_val': queryset_list_indiana_ivf_val,
        'queryset_list_indiana_egg_val': queryset_list_indiana_egg_val,
        'queryset_list_indiana_embryo_val': queryset_list_indiana_embryo_val,
        'queryset_list_indiana_sperm_val': queryset_list_indiana_sperm_val,
        'queryset_list_indiana_icsi_val': queryset_list_indiana_icsi_val,
        'queryset_list_indiana_iui': queryset_list_indiana_iui,

        'queryset_list_iowa_ivf_val': queryset_list_iowa_ivf_val,
        'queryset_list_iowa_egg_val': queryset_list_iowa_egg_val,
        'queryset_list_iowa_embryo_val': queryset_list_iowa_embryo_val,
        'queryset_list_iowa_sperm_val': queryset_list_iowa_sperm_val,
        'queryset_list_iowa_icsi_val': queryset_list_iowa_icsi_val,
        'queryset_list_iowa_iui': queryset_list_iowa_iui,

        'queryset_list_kansas_ivf_val': queryset_list_kansas_ivf_val,
        'queryset_list_kansas_egg_val': queryset_list_kansas_egg_val,
        'queryset_list_kansas_embryo_val': queryset_list_kansas_embryo_val,
        'queryset_list_kansas_sperm_val': queryset_list_kansas_sperm_val,
        'queryset_list_kansas_icsi_val': queryset_list_kansas_icsi_val,
        'queryset_list_kansas_iui': queryset_list_kansas_iui,

        'queryset_list_kentucky_ivf_val': queryset_list_kentucky_ivf_val,
        'queryset_list_kentucky_egg_val': queryset_list_kentucky_egg_val,
        'queryset_list_kentucky_embryo_val': queryset_list_kentucky_embryo_val,
        'queryset_list_kentucky_sperm_val': queryset_list_kentucky_sperm_val,
        'queryset_list_kentucky_icsi_val': queryset_list_kentucky_icsi_val,
        'queryset_list_kentucky_iui': queryset_list_kentucky_iui,

        'queryset_list_louisiana_ivf_val': queryset_list_louisiana_ivf_val,
        'queryset_list_louisiana_egg_val': queryset_list_louisiana_egg_val,
        'queryset_list_louisiana_embryo_val': queryset_list_louisiana_embryo_val,
        'queryset_list_louisiana_sperm_val': queryset_list_louisiana_sperm_val,
        'queryset_list_louisiana_icsi_val': queryset_list_louisiana_icsi_val,
        'queryset_list_louisiana_iui': queryset_list_louisiana_iui,

        'queryset_list_maine_ivf_val': queryset_list_maine_ivf_val,
        'queryset_list_maine_egg_val': queryset_list_maine_egg_val,
        'queryset_list_maine_embryo_val': queryset_list_maine_embryo_val,
        'queryset_list_maine_sperm_val': queryset_list_maine_sperm_val,
        'queryset_list_maine_icsi_val': queryset_list_maine_icsi_val,
        'queryset_list_maine_iui': queryset_list_maine_iui,

        'queryset_list_maryland_ivf_val': queryset_list_maryland_ivf_val,
        'queryset_list_maryland_egg_val': queryset_list_maryland_egg_val,
        'queryset_list_maryland_embryo_val': queryset_list_maryland_embryo_val,
        'queryset_list_maryland_sperm_val': queryset_list_maryland_sperm_val,
        'queryset_list_maryland_icsi_val': queryset_list_maryland_icsi_val,
        'queryset_list_maryland_iui': queryset_list_maryland_iui,

        'queryset_list_massachusetts_ivf_val': queryset_list_massachusetts_ivf_val,
        'queryset_list_massachusetts_egg_val': queryset_list_massachusetts_egg_val,
        'queryset_list_massachusetts_embryo_val': queryset_list_massachusetts_embryo_val,
        'queryset_list_massachusetts_sperm_val': queryset_list_massachusetts_sperm_val,
        'queryset_list_massachusetts_icsi_val': queryset_list_massachusetts_icsi_val,
        'queryset_list_massachusetts_iui': queryset_list_massachusetts_iui,

        'queryset_list_michigan_ivf_val': queryset_list_michigan_ivf_val,
        'queryset_list_michigan_egg_val': queryset_list_michigan_egg_val,
        'queryset_list_michigan_embryo_val': queryset_list_michigan_embryo_val,
        'queryset_list_michigan_sperm_val': queryset_list_michigan_sperm_val,
        'queryset_list_michigan_icsi_val': queryset_list_michigan_icsi_val,
        'queryset_list_michigan_iui': queryset_list_michigan_iui,

        'queryset_list_minnesota_ivf_val': queryset_list_minnesota_ivf_val,
        'queryset_list_minnesota_egg_val': queryset_list_minnesota_egg_val,
        'queryset_list_minnesota_embryo_val': queryset_list_minnesota_embryo_val,
        'queryset_list_minnesota_sperm_val': queryset_list_minnesota_sperm_val,
        'queryset_list_minnesota_icsi_val': queryset_list_minnesota_icsi_val,
        'queryset_list_minnesota_iui': queryset_list_minnesota_iui,

        'queryset_list_mississippi_ivf_val': queryset_list_mississippi_ivf_val,
        'queryset_list_mississippi_egg_val': queryset_list_mississippi_egg_val,
        'queryset_list_mississippi_embryo_val': queryset_list_mississippi_embryo_val,
        'queryset_list_mississippi_sperm_val': queryset_list_mississippi_sperm_val,
        'queryset_list_mississippi_icsi_val': queryset_list_mississippi_icsi_val,
        'queryset_list_mississippi_iui': queryset_list_mississippi_iui,

        'queryset_list_missouri_ivf_val': queryset_list_missouri_ivf_val,
        'queryset_list_missouri_egg_val': queryset_list_missouri_egg_val,
        'queryset_list_missouri_embryo_val': queryset_list_missouri_embryo_val,
        'queryset_list_missouri_sperm_val': queryset_list_missouri_sperm_val,
        'queryset_list_missouri_icsi_val': queryset_list_missouri_icsi_val,
        'queryset_list_missouri_iui': queryset_list_missouri_iui,

        'queryset_list_montana_ivf_val': queryset_list_montana_ivf_val,
        'queryset_list_montana_egg_val': queryset_list_montana_egg_val,
        'queryset_list_montana_embryo_val': queryset_list_montana_embryo_val,
        'queryset_list_montana_sperm_val': queryset_list_montana_sperm_val,
        'queryset_list_montana_icsi_val': queryset_list_montana_icsi_val,
        'queryset_list_montana_iui': queryset_list_montana_iui,

        'queryset_list_nebraska_ivf_val': queryset_list_nebraska_ivf_val,
        'queryset_list_nebraska_egg_val': queryset_list_nebraska_egg_val,
        'queryset_list_nebraska_embryo_val': queryset_list_nebraska_embryo_val,
        'queryset_list_nebraska_sperm_val': queryset_list_nebraska_sperm_val,
        'queryset_list_nebraska_icsi_val': queryset_list_nebraska_icsi_val,
        'queryset_list_nebraska_iui': queryset_list_nebraska_iui,

        'queryset_list_newhampshire_ivf_val': queryset_list_newhampshire_ivf_val,
        'queryset_list_newhampshire_egg_val': queryset_list_newhampshire_egg_val,
        'queryset_list_newhampshire_embryo_val': queryset_list_newhampshire_embryo_val,
        'queryset_list_newhampshire_sperm_val': queryset_list_newhampshire_sperm_val,
        'queryset_list_newhampshire_icsi_val': queryset_list_newhampshire_icsi_val,
        'queryset_list_newhampshire_iui': queryset_list_newhampshire_iui,

        'queryset_list_newjersey_ivf_val': queryset_list_newjersey_ivf_val,
        'queryset_list_newjersey_egg_val': queryset_list_newjersey_egg_val,
        'queryset_list_newjersey_embryo_val': queryset_list_newjersey_embryo_val,
        'queryset_list_newjersey_sperm_val': queryset_list_newjersey_sperm_val,
        'queryset_list_newjersey_icsi_val': queryset_list_newjersey_icsi_val,
        'queryset_list_newjersey_iui': queryset_list_newjersey_iui,

        'queryset_list_newmexico_ivf_val': queryset_list_newmexico_ivf_val,
        'queryset_list_newmexico_egg_val': queryset_list_newmexico_egg_val,
        'queryset_list_newmexico_embryo_val': queryset_list_newmexico_embryo_val,
        'queryset_list_newmexico_sperm_val': queryset_list_newmexico_sperm_val,
        'queryset_list_newmexico_icsi_val': queryset_list_newmexico_icsi_val,
        'queryset_list_newmexico_iui': queryset_list_newmexico_iui,

        'queryset_list_newyork_ivf_val': queryset_list_newyork_ivf_val,
        'queryset_list_newyork_egg_val': queryset_list_newyork_egg_val,
        'queryset_list_newyork_embryo_val': queryset_list_newyork_embryo_val,
        'queryset_list_newyork_sperm_val': queryset_list_newyork_sperm_val,
        'queryset_list_newyork_icsi_val': queryset_list_newyork_icsi_val,
        'queryset_list_newyork_iui': queryset_list_newyork_iui,

        'queryset_list_northcarolina_ivf_val': queryset_list_northcarolina_ivf_val,
        'queryset_list_northcarolina_egg_val': queryset_list_northcarolina_egg_val,
        'queryset_list_northcarolina_embryo_val': queryset_list_northcarolina_embryo_val,
        'queryset_list_northcarolina_sperm_val': queryset_list_northcarolina_sperm_val,
        'queryset_list_northcarolina_icsi_val': queryset_list_northcarolina_icsi_val,
        'queryset_list_northcarolina_iui': queryset_list_northcarolina_iui,

        'queryset_list_northdakota_ivf_val': queryset_list_northdakota_ivf_val,
        'queryset_list_northdakota_egg_val': queryset_list_northdakota_egg_val,
        'queryset_list_northdakota_embryo_val': queryset_list_northdakota_embryo_val,
        'queryset_list_northdakota_sperm_val': queryset_list_northdakota_sperm_val,
        'queryset_list_northdakota_icsi_val': queryset_list_northdakota_icsi_val,
        'queryset_list_northdakota_iui': queryset_list_northdakota_iui,

        'queryset_list_nevada_ivf_val': queryset_list_nevada_ivf_val,
        'queryset_list_nevada_egg_val': queryset_list_nevada_egg_val,
        'queryset_list_nevada_embryo_val': queryset_list_nevada_embryo_val,
        'queryset_list_nevada_sperm_val': queryset_list_nevada_sperm_val,
        'queryset_list_nevada_icsi_val': queryset_list_nevada_icsi_val,
        'queryset_list_nevada_iui': queryset_list_nevada_iui,

        'queryset_list_ohio_ivf_val': queryset_list_ohio_ivf_val,
        'queryset_list_ohio_egg_val': queryset_list_ohio_egg_val,
        'queryset_list_ohio_embryo_val': queryset_list_ohio_embryo_val,
        'queryset_list_ohio_sperm_val': queryset_list_ohio_sperm_val,
        'queryset_list_ohio_icsi_val': queryset_list_ohio_icsi_val,
        'queryset_list_ohio_iui': queryset_list_ohio_iui,

        'queryset_list_oklahoma_ivf_val': queryset_list_oklahoma_ivf_val,
        'queryset_list_oklahoma_egg_val': queryset_list_oklahoma_egg_val,
        'queryset_list_oklahoma_embryo_val': queryset_list_oklahoma_embryo_val,
        'queryset_list_oklahoma_sperm_val': queryset_list_oklahoma_sperm_val,
        'queryset_list_oklahoma_icsi_val': queryset_list_oklahoma_icsi_val,
        'queryset_list_oklahoma_iui': queryset_list_oklahoma_iui,

        'queryset_list_oregon_ivf_val': queryset_list_oregon_ivf_val,
        'queryset_list_oregon_egg_val': queryset_list_oregon_egg_val,
        'queryset_list_oregon_embryo_val': queryset_list_oregon_embryo_val,
        'queryset_list_oregon_sperm_val': queryset_list_oregon_sperm_val,
        'queryset_list_oregon_icsi_val': queryset_list_oregon_icsi_val,
        'queryset_list_oregon_iui': queryset_list_oregon_iui,

        'queryset_list_pennsylvania_ivf_val': queryset_list_pennsylvania_ivf_val,
        'queryset_list_pennsylvania_egg_val': queryset_list_pennsylvania_egg_val,
        'queryset_list_pennsylvania_embryo_val': queryset_list_pennsylvania_embryo_val,
        'queryset_list_pennsylvania_sperm_val': queryset_list_pennsylvania_sperm_val,
        'queryset_list_pennsylvania_icsi_val': queryset_list_pennsylvania_icsi_val,
        'queryset_list_pennsylvania_iui': queryset_list_pennsylvania_iui,

        'queryset_list_puertorico_ivf_val': queryset_list_puertorico_ivf_val,
        'queryset_list_puertorico_egg_val': queryset_list_puertorico_egg_val,
        'queryset_list_puertorico_embryo_val': queryset_list_puertorico_embryo_val,
        'queryset_list_puertorico_sperm_val': queryset_list_puertorico_sperm_val,
        'queryset_list_puertorico_icsi_val': queryset_list_puertorico_icsi_val,
        'queryset_list_puertorico_iui': queryset_list_puertorico_iui,

        'queryset_list_rhodeisland_ivf_val': queryset_list_rhodeisland_ivf_val,
        'queryset_list_rhodeisland_egg_val': queryset_list_rhodeisland_egg_val,
        'queryset_list_rhodeisland_embryo_val': queryset_list_rhodeisland_embryo_val,
        'queryset_list_rhodeisland_sperm_val': queryset_list_rhodeisland_sperm_val,
        'queryset_list_rhodeisland_icsi_val': queryset_list_rhodeisland_icsi_val,
        'queryset_list_rhodeisland_iui': queryset_list_rhodeisland_iui,

        'queryset_list_southcarolina_ivf_val': queryset_list_southcarolina_ivf_val,
        'queryset_list_southcarolina_egg_val': queryset_list_southcarolina_egg_val,
        'queryset_list_southcarolina_embryo_val': queryset_list_southcarolina_embryo_val,
        'queryset_list_southcarolina_sperm_val': queryset_list_southcarolina_sperm_val,
        'queryset_list_southcarolina_icsi_val': queryset_list_southcarolina_icsi_val,
        'queryset_list_southcarolina_iui': queryset_list_southcarolina_iui,

        'queryset_list_southdakota_ivf_val': queryset_list_southdakota_ivf_val,
        'queryset_list_southdakota_egg_val': queryset_list_southdakota_egg_val,
        'queryset_list_southdakota_embryo_val': queryset_list_southdakota_embryo_val,
        'queryset_list_southdakota_sperm_val': queryset_list_southdakota_sperm_val,
        'queryset_list_southdakota_icsi_val': queryset_list_southdakota_icsi_val,
        'queryset_list_southdakota_iui': queryset_list_southdakota_iui,

        'queryset_list_tennessee_ivf_val': queryset_list_tennessee_ivf_val,
        'queryset_list_tennessee_egg_val': queryset_list_tennessee_egg_val,
        'queryset_list_tennessee_embryo_val': queryset_list_tennessee_embryo_val,
        'queryset_list_tennessee_sperm_val': queryset_list_tennessee_sperm_val,
        'queryset_list_tennessee_icsi_val': queryset_list_tennessee_icsi_val,
        'queryset_list_tennessee_iui': queryset_list_tennessee_iui,

        'queryset_list_texas_ivf_val': queryset_list_texas_ivf_val,
        'queryset_list_texas_egg_val': queryset_list_texas_egg_val,
        'queryset_list_texas_embryo_val': queryset_list_texas_embryo_val,
        'queryset_list_texas_sperm_val': queryset_list_texas_sperm_val,
        'queryset_list_texas_icsi_val': queryset_list_texas_icsi_val,
        'queryset_list_texas_iui': queryset_list_texas_iui,

        'queryset_list_utah_ivf_val': queryset_list_utah_ivf_val,
        'queryset_list_utah_egg_val': queryset_list_utah_egg_val,
        'queryset_list_utah_embryo_val': queryset_list_utah_embryo_val,
        'queryset_list_utah_sperm_val': queryset_list_utah_sperm_val,
        'queryset_list_utah_icsi_val': queryset_list_utah_icsi_val,
        'queryset_list_utah_iui': queryset_list_utah_iui,

        'queryset_list_vermont_ivf_val': queryset_list_vermont_ivf_val,
        'queryset_list_vermont_egg_val': queryset_list_vermont_egg_val,
        'queryset_list_vermont_embryo_val': queryset_list_vermont_embryo_val,
        'queryset_list_vermont_sperm_val': queryset_list_vermont_sperm_val,
        'queryset_list_vermont_icsi_val': queryset_list_vermont_icsi_val,
        'queryset_list_vermont_iui': queryset_list_vermont_iui,

        'queryset_list_virginia_ivf_val': queryset_list_virginia_ivf_val,
        'queryset_list_virginia_egg_val': queryset_list_virginia_egg_val,
        'queryset_list_virginia_embryo_val': queryset_list_virginia_embryo_val,
        'queryset_list_virginia_sperm_val': queryset_list_virginia_sperm_val,
        'queryset_list_virginia_icsi_val': queryset_list_virginia_icsi_val,
        'queryset_list_virginia_iui': queryset_list_virginia_iui,

        'queryset_list_washington_ivf_val': queryset_list_washington_ivf_val,
        'queryset_list_washington_egg_val': queryset_list_washington_egg_val,
        'queryset_list_washington_embryo_val': queryset_list_washington_embryo_val,
        'queryset_list_washington_sperm_val': queryset_list_washington_sperm_val,
        'queryset_list_washington_icsi_val': queryset_list_washington_icsi_val,
        'queryset_list_washington_iui': queryset_list_washington_iui,

        'queryset_list_westvirginia_ivf_val': queryset_list_westvirginia_ivf_val,
        'queryset_list_westvirginia_egg_val': queryset_list_westvirginia_egg_val,
        'queryset_list_westvirginia_embryo_val': queryset_list_westvirginia_embryo_val,
        'queryset_list_westvirginia_sperm_val': queryset_list_westvirginia_sperm_val,
        'queryset_list_westvirginia_icsi_val': queryset_list_westvirginia_icsi_val,
        'queryset_list_westvirginia_iui': queryset_list_westvirginia_iui,

        'queryset_list_wisconsin_ivf_val': queryset_list_wisconsin_ivf_val,
        'queryset_list_wisconsin_egg_val': queryset_list_wisconsin_egg_val,
        'queryset_list_wisconsin_embryo_val': queryset_list_wisconsin_embryo_val,
        'queryset_list_wisconsin_sperm_val': queryset_list_wisconsin_sperm_val,
        'queryset_list_wisconsin_icsi_val': queryset_list_wisconsin_icsi_val,
        'queryset_list_wisconsin_iui': queryset_list_wisconsin_iui,

        'queryset_list_wyoming_ivf_val': queryset_list_wyoming_ivf_val,
        'queryset_list_wyoming_egg_val': queryset_list_wyoming_egg_val,
        'queryset_list_wyoming_embryo_val': queryset_list_wyoming_embryo_val,
        'queryset_list_wyoming_sperm_val': queryset_list_wyoming_sperm_val,
        'queryset_list_wyoming_icsi_val': queryset_list_wyoming_icsi_val,
        'queryset_list_wyoming_iui': queryset_list_wyoming_iui,

        'queryset_list_districtofcolumbia_ivf_val': queryset_list_districtofcolumbia_ivf_val,
        'queryset_list_districtofcolumbia_egg_val': queryset_list_districtofcolumbia_egg_val,
        'queryset_list_districtofcolumbia_embryo_val': queryset_list_districtofcolumbia_embryo_val,
        'queryset_list_districtofcolumbia_sperm_val': queryset_list_districtofcolumbia_sperm_val,
        'queryset_list_districtofcolumbia_icsi_val': queryset_list_districtofcolumbia_icsi_val,
        'queryset_list_districtofcolumbia_iui': queryset_list_districtofcolumbia_iui,

        'my_total_clinic_count_alabama': my_total_clinic_count_alabama,
        'my_total_clinic_count_alaska': my_total_clinic_count_alaska,
        'my_total_clinic_count_arizona': my_total_clinic_count_arizona,
        'my_total_clinic_count_arkansas': my_total_clinic_count_arkansas,
        'my_total_clinic_count_california': my_total_clinic_count_california,
        'my_total_clinic_count_colorado': my_total_clinic_count_colorado,
        'my_total_clinic_count_connecticut': my_total_clinic_count_connecticut,
        'my_total_clinic_count_delaware': my_total_clinic_count_delaware,
        'my_total_clinic_count_florida': my_total_clinic_count_florida,
        'my_total_clinic_count_georgia': my_total_clinic_count_georgia,
        'my_total_clinic_count_hawaii': my_total_clinic_count_hawaii,
        'my_total_clinic_count_idaho': my_total_clinic_count_idaho,
        'my_total_clinic_count_illinois': my_total_clinic_count_illinois,
        'my_total_clinic_count_indiana': my_total_clinic_count_indiana,
        'my_total_clinic_count_iowa': my_total_clinic_count_iowa,
        'my_total_clinic_count_kansas': my_total_clinic_count_kansas,
        'my_total_clinic_count_kentucky': my_total_clinic_count_kentucky,
        'my_total_clinic_count_louisiana': my_total_clinic_count_louisiana,
        'my_total_clinic_count_maine': my_total_clinic_count_maine,
        'my_total_clinic_count_maryland': my_total_clinic_count_maryland,
        'my_total_clinic_count_massachusetts': my_total_clinic_count_massachusetts,
        'my_total_clinic_count_michigan': my_total_clinic_count_michigan,
        'my_total_clinic_count_minnesota': my_total_clinic_count_minnesota,
        'my_total_clinic_count_mississippi': my_total_clinic_count_mississippi,
        'my_total_clinic_count_missouri': my_total_clinic_count_missouri,
        'my_total_clinic_count_montana': my_total_clinic_count_montana,
        'my_total_clinic_count_nebraska': my_total_clinic_count_nebraska,
        'my_total_clinic_count_newhampshire': my_total_clinic_count_newhampshire,
        'my_total_clinic_count_newjersey': my_total_clinic_count_newjersey,
        'my_total_clinic_count_newmexico': my_total_clinic_count_newmexico,
        'my_total_clinic_count_newyork': my_total_clinic_count_newyork,
        'my_total_clinic_count_northcarolina': my_total_clinic_count_northcarolina,
        'my_total_clinic_count_northdakota': my_total_clinic_count_northdakota,
        'my_total_clinic_count_nevada': my_total_clinic_count_nevada,
        'my_total_clinic_count_ohio': my_total_clinic_count_ohio,
        'my_total_clinic_count_oklahoma': my_total_clinic_count_oklahoma,
        'my_total_clinic_count_oregon': my_total_clinic_count_oregon,
        'my_total_clinic_count_pennsylvania': my_total_clinic_count_pennsylvania,
        'my_total_clinic_count_puertorico': my_total_clinic_count_puertorico,
        'my_total_clinic_count_rhodeisland': my_total_clinic_count_rhodeisland,
        'my_total_clinic_count_southcarolina': my_total_clinic_count_southcarolina,
        'my_total_clinic_count_southdakota': my_total_clinic_count_southdakota,
        'my_total_clinic_count_tennessee': my_total_clinic_count_tennessee,
        'my_total_clinic_count_texas': my_total_clinic_count_texas,
        'my_total_clinic_count_utah': my_total_clinic_count_utah,
        'my_total_clinic_count_vermont': my_total_clinic_count_vermont,
        'my_total_clinic_count_virginia': my_total_clinic_count_virginia,
        'my_total_clinic_count_washington': my_total_clinic_count_washington,
        'my_total_clinic_count_westvirginia': my_total_clinic_count_westvirginia,
        'my_total_clinic_count_wisconsin': my_total_clinic_count_wisconsin,
        'my_total_clinic_count_wyoming': my_total_clinic_count_wyoming,
        'my_total_clinic_count_districtofcolumbia': my_total_clinic_count_districtofcolumbia,
        }

    return render(request, 'main/Locations/USLocations/us-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsUKRegions(request):
    queryset_list_uk = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_aberdeen = queryset_list_uk.filter(clinicRegion__iexact='Aberdeen')
    my_total_clinic_count_aberdeen = queryset_list_aberdeen.count()

    queryset_list_aberdeen_ivf = queryset_list_aberdeen.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_aberdeen_ivf.items():
        queryset_list_aberdeen_ivf_val = val

    queryset_list_aberdeen_egg = queryset_list_aberdeen.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_egg.items():
        queryset_list_aberdeen_egg_val = val

    queryset_list_aberdeen_embryo = queryset_list_aberdeen.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_embryo.items():
        queryset_list_aberdeen_embryo_val = val

    queryset_list_aberdeen_sperm = queryset_list_aberdeen.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_aberdeen_sperm.items():
        queryset_list_aberdeen_sperm_val = val

    queryset_list_aberdeen_icsi = queryset_list_aberdeen.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_aberdeen_icsi.items():
        queryset_list_aberdeen_icsi_val = val

    queryset_list_aberdeen_iui = queryset_list_aberdeen.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_aberdeen_iui.items():
        queryset_list_aberdeen_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bath = queryset_list_uk.filter(clinicRegion__iexact='Bath')
    my_total_clinic_count_bath = queryset_list_bath.count()

    queryset_list_bath_ivf = queryset_list_bath.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bath_ivf.items():
        queryset_list_bath_ivf_val = val

    queryset_list_bath_egg = queryset_list_bath.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bath_egg.items():
        queryset_list_bath_egg_val = val

    queryset_list_bath_embryo = queryset_list_bath.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bath_embryo.items():
        queryset_list_bath_embryo_val = val

    queryset_list_bath_sperm = queryset_list_bath.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bath_sperm.items():
        queryset_list_bath_sperm_val = val

    queryset_list_bath_icsi = queryset_list_bath.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bath_icsi.items():
        queryset_list_bath_icsi_val = val

    queryset_list_bath_iui = queryset_list_bath.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bath_iui.items():
        queryset_list_bath_iui = val

    #--------------------------------------------------------------------------
    queryset_list_belfast = queryset_list_uk.filter(clinicRegion__iexact='Belfast')
    my_total_clinic_count_belfast = queryset_list_belfast.count()

    queryset_list_belfast_ivf = queryset_list_belfast.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_belfast_ivf.items():
        queryset_list_belfast_ivf_val = val

    queryset_list_belfast_egg = queryset_list_belfast.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_belfast_egg.items():
        queryset_list_belfast_egg_val = val

    queryset_list_belfast_embryo = queryset_list_belfast.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_belfast_embryo.items():
        queryset_list_belfast_embryo_val = val

    queryset_list_belfast_sperm = queryset_list_belfast.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_belfast_sperm.items():
        queryset_list_belfast_sperm_val = val

    queryset_list_belfast_icsi = queryset_list_belfast.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_belfast_icsi.items():
        queryset_list_belfast_icsi_val = val

    queryset_list_belfast_iui = queryset_list_belfast.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_belfast_iui.items():
        queryset_list_belfast_iui = val

    #--------------------------------------------------------------------------
    queryset_list_birmingham = queryset_list_uk.filter(clinicRegion__iexact='Birmingham')
    my_total_clinic_count_birmingham = queryset_list_birmingham.count()

    queryset_list_birmingham_ivf = queryset_list_birmingham.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_birmingham_ivf.items():
        queryset_list_birmingham_ivf_val = val

    queryset_list_birmingham_egg = queryset_list_birmingham.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_egg.items():
        queryset_list_birmingham_egg_val = val

    queryset_list_birmingham_embryo = queryset_list_birmingham.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_embryo.items():
        queryset_list_birmingham_embryo_val = val

    queryset_list_birmingham_sperm = queryset_list_birmingham.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_birmingham_sperm.items():
        queryset_list_birmingham_sperm_val = val

    queryset_list_birmingham_icsi = queryset_list_birmingham.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_birmingham_icsi.items():
        queryset_list_birmingham_icsi_val = val

    queryset_list_birmingham_iui = queryset_list_birmingham.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_birmingham_iui.items():
        queryset_list_birmingham_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bournemouth = queryset_list_uk.filter(clinicRegion__iexact='Bournemouth')
    my_total_clinic_count_bournemouth = queryset_list_bournemouth.count()

    queryset_list_bournemouth_ivf = queryset_list_bournemouth.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bournemouth_ivf.items():
        queryset_list_bournemouth_ivf_val = val

    queryset_list_bournemouth_egg = queryset_list_bournemouth.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_egg.items():
        queryset_list_bournemouth_egg_val = val

    queryset_list_bournemouth_embryo = queryset_list_bournemouth.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_embryo.items():
        queryset_list_bournemouth_embryo_val = val

    queryset_list_bournemouth_sperm = queryset_list_bournemouth.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bournemouth_sperm.items():
        queryset_list_bournemouth_sperm_val = val

    queryset_list_bournemouth_icsi = queryset_list_bournemouth.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bournemouth_icsi.items():
        queryset_list_bournemouth_icsi_val = val

    queryset_list_bournemouth_iui = queryset_list_bournemouth.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bournemouth_iui.items():
        queryset_list_bournemouth_iui = val

    #--------------------------------------------------------------------------
    queryset_list_brighton = queryset_list_uk.filter(clinicRegion__iexact='Brighton')
    my_total_clinic_count_brighton = queryset_list_brighton.count()

    queryset_list_brighton_ivf = queryset_list_brighton.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_brighton_ivf.items():
        queryset_list_brighton_ivf_val = val

    queryset_list_brighton_egg = queryset_list_brighton.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_brighton_egg.items():
        queryset_list_brighton_egg_val = val

    queryset_list_brighton_embryo = queryset_list_brighton.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_brighton_embryo.items():
        queryset_list_brighton_embryo_val = val

    queryset_list_brighton_sperm = queryset_list_brighton.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_brighton_sperm.items():
        queryset_list_brighton_sperm_val = val

    queryset_list_brighton_icsi = queryset_list_brighton.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_brighton_icsi.items():
        queryset_list_brighton_icsi_val = val

    queryset_list_brighton_iui = queryset_list_brighton.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_brighton_iui.items():
        queryset_list_brighton_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bristol = queryset_list_uk.filter(clinicRegion__iexact='Bristol')
    my_total_clinic_count_bristol = queryset_list_bristol.count()

    queryset_list_bristol_ivf = queryset_list_bristol.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bristol_ivf.items():
        queryset_list_bristol_ivf_val = val

    queryset_list_bristol_egg = queryset_list_bristol.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bristol_egg.items():
        queryset_list_bristol_egg_val = val

    queryset_list_bristol_embryo = queryset_list_bristol.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bristol_embryo.items():
        queryset_list_bristol_embryo_val = val

    queryset_list_bristol_sperm = queryset_list_bristol.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bristol_sperm.items():
        queryset_list_bristol_sperm_val = val

    queryset_list_bristol_icsi = queryset_list_bristol.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bristol_icsi.items():
        queryset_list_bristol_icsi_val = val

    queryset_list_bristol_iui = queryset_list_bristol.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bristol_iui.items():
        queryset_list_bristol_iui = val

    #--------------------------------------------------------------------------
    queryset_list_cambridge = queryset_list_uk.filter(clinicRegion__iexact='Cambridge')
    my_total_clinic_count_cambridge = queryset_list_cambridge.count()

    queryset_list_cambridge_ivf = queryset_list_cambridge.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cambridge_ivf.items():
        queryset_list_cambridge_ivf_val = val

    queryset_list_cambridge_egg = queryset_list_cambridge.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cambridge_egg.items():
        queryset_list_cambridge_egg_val = val

    queryset_list_cambridge_embryo = queryset_list_cambridge.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cambridge_embryo.items():
        queryset_list_cambridge_embryo_val = val

    queryset_list_cambridge_sperm = queryset_list_cambridge.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_cambridge_sperm.items():
        queryset_list_cambridge_sperm_val = val

    queryset_list_cambridge_icsi = queryset_list_cambridge.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_cambridge_icsi.items():
        queryset_list_cambridge_icsi_val = val

    queryset_list_cambridge_iui = queryset_list_cambridge.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cambridge_iui.items():
        queryset_list_cambridge_iui = val

    #--------------------------------------------------------------------------
    queryset_list_cardiff = queryset_list_uk.filter(clinicRegion__iexact='Cardiff')
    my_total_clinic_count_cardiff = queryset_list_cardiff.count()

    queryset_list_cardiff_ivf = queryset_list_cardiff.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cardiff_ivf.items():
        queryset_list_cardiff_ivf_val = val

    queryset_list_cardiff_egg = queryset_list_cardiff.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cardiff_egg.items():
        queryset_list_cardiff_egg_val = val

    queryset_list_cardiff_embryo = queryset_list_cardiff.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cardiff_embryo.items():
        queryset_list_cardiff_embryo_val = val

    queryset_list_cardiff_sperm = queryset_list_cardiff.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_cardiff_sperm.items():
        queryset_list_cardiff_sperm_val = val

    queryset_list_cardiff_icsi = queryset_list_cardiff.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_cardiff_icsi.items():
        queryset_list_cardiff_icsi_val = val

    queryset_list_cardiff_iui = queryset_list_cardiff.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cardiff_iui.items():
        queryset_list_cardiff_iui = val

    #--------------------------------------------------------------------------
    queryset_list_colchester = queryset_list_uk.filter(clinicRegion__iexact='Colchester')
    my_total_clinic_count_colchester = queryset_list_colchester.count()

    queryset_list_colchester_ivf = queryset_list_colchester.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_colchester_ivf.items():
        queryset_list_colchester_ivf_val = val

    queryset_list_colchester_egg = queryset_list_colchester.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_colchester_egg.items():
        queryset_list_colchester_egg_val = val

    queryset_list_colchester_embryo = queryset_list_colchester.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_colchester_embryo.items():
        queryset_list_colchester_embryo_val = val

    queryset_list_colchester_sperm = queryset_list_colchester.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_colchester_sperm.items():
        queryset_list_colchester_sperm_val = val

    queryset_list_colchester_icsi = queryset_list_colchester.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_colchester_icsi.items():
        queryset_list_colchester_icsi_val = val

    queryset_list_colchester_iui = queryset_list_colchester.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_colchester_iui.items():
        queryset_list_colchester_iui = val

    #--------------------------------------------------------------------------
    queryset_list_derby = queryset_list_uk.filter(clinicRegion__iexact='Derby')
    my_total_clinic_count_derby = queryset_list_derby.count()

    queryset_list_derby_ivf = queryset_list_derby.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_derby_ivf.items():
        queryset_list_derby_ivf_val = val

    queryset_list_derby_egg = queryset_list_derby.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_derby_egg.items():
        queryset_list_derby_egg_val = val

    queryset_list_derby_embryo = queryset_list_derby.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_derby_embryo.items():
        queryset_list_derby_embryo_val = val

    queryset_list_derby_sperm = queryset_list_derby.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_derby_sperm.items():
        queryset_list_derby_sperm_val = val

    queryset_list_derby_icsi = queryset_list_derby.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_derby_icsi.items():
        queryset_list_derby_icsi_val = val

    queryset_list_derby_iui = queryset_list_derby.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_derby_iui.items():
        queryset_list_derby_iui = val

    #--------------------------------------------------------------------------
    queryset_list_derby = queryset_list_uk.filter(clinicRegion__iexact='Derby')
    my_total_clinic_count_derby = queryset_list_derby.count()

    queryset_list_derby_ivf = queryset_list_derby.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_derby_ivf.items():
        queryset_list_derby_ivf_val = val

    queryset_list_derby_egg = queryset_list_derby.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_derby_egg.items():
        queryset_list_derby_egg_val = val

    queryset_list_derby_embryo = queryset_list_derby.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_derby_embryo.items():
        queryset_list_derby_embryo_val = val

    queryset_list_derby_sperm = queryset_list_derby.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_derby_sperm.items():
        queryset_list_derby_sperm_val = val

    queryset_list_derby_icsi = queryset_list_derby.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_derby_icsi.items():
        queryset_list_derby_icsi_val = val

    queryset_list_derby_iui = queryset_list_derby.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_derby_iui.items():
        queryset_list_derby_iui = val

    #--------------------------------------------------------------------------
    queryset_list_exeter = queryset_list_uk.filter(clinicRegion__iexact='Exeter')
    my_total_clinic_count_exeter = queryset_list_exeter.count()

    queryset_list_exeter_ivf = queryset_list_exeter.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_exeter_ivf.items():
        queryset_list_exeter_ivf_val = val

    queryset_list_exeter_egg = queryset_list_exeter.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_exeter_egg.items():
        queryset_list_exeter_egg_val = val

    queryset_list_exeter_embryo = queryset_list_exeter.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_exeter_embryo.items():
        queryset_list_exeter_embryo_val = val

    queryset_list_exeter_sperm = queryset_list_exeter.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_exeter_sperm.items():
        queryset_list_exeter_sperm_val = val

    queryset_list_exeter_icsi = queryset_list_exeter.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_exeter_icsi.items():
        queryset_list_exeter_icsi_val = val

    queryset_list_exeter_iui = queryset_list_exeter.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_exeter_iui.items():
        queryset_list_exeter_iui = val

    #--------------------------------------------------------------------------
    queryset_list_glasgow = queryset_list_uk.filter(clinicRegion__iexact='Glasgow')
    my_total_clinic_count_glasgow = queryset_list_glasgow.count()

    queryset_list_glasgow_ivf = queryset_list_glasgow.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_glasgow_ivf.items():
        queryset_list_glasgow_ivf_val = val

    queryset_list_glasgow_egg = queryset_list_glasgow.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_glasgow_egg.items():
        queryset_list_glasgow_egg_val = val

    queryset_list_glasgow_embryo = queryset_list_glasgow.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_glasgow_embryo.items():
        queryset_list_glasgow_embryo_val = val

    queryset_list_glasgow_sperm = queryset_list_glasgow.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_glasgow_sperm.items():
        queryset_list_glasgow_sperm_val = val

    queryset_list_glasgow_icsi = queryset_list_glasgow.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_glasgow_icsi.items():
        queryset_list_glasgow_icsi_val = val

    queryset_list_glasgow_iui = queryset_list_glasgow.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_glasgow_iui.items():
        queryset_list_glasgow_iui = val

    #--------------------------------------------------------------------------
    queryset_list_hull = queryset_list_uk.filter(clinicRegion__iexact='Hull')
    my_total_clinic_count_hull = queryset_list_hull.count()

    queryset_list_hull_ivf = queryset_list_hull.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_hull_ivf.items():
        queryset_list_hull_ivf_val = val

    queryset_list_hull_egg = queryset_list_hull.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_hull_egg.items():
        queryset_list_hull_egg_val = val

    queryset_list_hull_embryo = queryset_list_hull.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_hull_embryo.items():
        queryset_list_hull_embryo_val = val

    queryset_list_hull_sperm = queryset_list_hull.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_hull_sperm.items():
        queryset_list_hull_sperm_val = val

    queryset_list_hull_icsi = queryset_list_hull.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_hull_icsi.items():
        queryset_list_hull_icsi_val = val

    queryset_list_hull_iui = queryset_list_hull.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_hull_iui.items():
        queryset_list_hull_iui = val

    #--------------------------------------------------------------------------
    queryset_list_chelmsford = queryset_list_uk.filter(clinicRegion__iexact='Chelmsford')
    my_total_clinic_count_chelmsford = queryset_list_chelmsford.count()

    queryset_list_chelmsford_ivf = queryset_list_chelmsford.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_chelmsford_ivf.items():
        queryset_list_chelmsford_ivf_val = val

    queryset_list_chelmsford_egg = queryset_list_chelmsford.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_chelmsford_egg.items():
        queryset_list_chelmsford_egg_val = val

    queryset_list_chelmsford_embryo = queryset_list_chelmsford.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_chelmsford_embryo.items():
        queryset_list_chelmsford_embryo_val = val

    queryset_list_chelmsford_sperm = queryset_list_chelmsford.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_chelmsford_sperm.items():
        queryset_list_chelmsford_sperm_val = val

    queryset_list_chelmsford_icsi = queryset_list_chelmsford.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_chelmsford_icsi.items():
        queryset_list_chelmsford_icsi_val = val

    queryset_list_chelmsford_iui = queryset_list_chelmsford.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_chelmsford_iui.items():
        queryset_list_chelmsford_iui = val

    #--------------------------------------------------------------------------
    queryset_list_leeds = queryset_list_uk.filter(clinicRegion__iexact='Leeds')
    my_total_clinic_count_leeds = queryset_list_leeds.count()

    queryset_list_leeds_ivf = queryset_list_leeds.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_leeds_ivf.items():
        queryset_list_leeds_ivf_val = val

    queryset_list_leeds_egg = queryset_list_leeds.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_leeds_egg.items():
        queryset_list_leeds_egg_val = val

    queryset_list_leeds_embryo = queryset_list_leeds.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_leeds_embryo.items():
        queryset_list_leeds_embryo_val = val

    queryset_list_leeds_sperm = queryset_list_leeds.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_leeds_sperm.items():
        queryset_list_leeds_sperm_val = val

    queryset_list_leeds_icsi = queryset_list_leeds.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_leeds_icsi.items():
        queryset_list_leeds_icsi_val = val

    queryset_list_leeds_iui = queryset_list_leeds.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_leeds_iui.items():
        queryset_list_leeds_iui = val

    #--------------------------------------------------------------------------
    queryset_list_leicester = queryset_list_uk.filter(clinicRegion__iexact='Leicester')
    my_total_clinic_count_leicester = queryset_list_leicester.count()

    queryset_list_leicester_ivf = queryset_list_leicester.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_leicester_ivf.items():
        queryset_list_leicester_ivf_val = val

    queryset_list_leicester_egg = queryset_list_leicester.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_leicester_egg.items():
        queryset_list_leicester_egg_val = val

    queryset_list_leicester_embryo = queryset_list_leicester.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_leicester_embryo.items():
        queryset_list_leicester_embryo_val = val

    queryset_list_leicester_sperm = queryset_list_leicester.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_leicester_sperm.items():
        queryset_list_leicester_sperm_val = val

    queryset_list_leicester_icsi = queryset_list_leicester.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_leicester_icsi.items():
        queryset_list_leicester_icsi_val = val

    queryset_list_leicester_iui = queryset_list_leicester.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_leicester_iui.items():
        queryset_list_leicester_iui = val

    #--------------------------------------------------------------------------
    queryset_list_liverpool = queryset_list_uk.filter(clinicRegion__iexact='Liverpool')
    my_total_clinic_count_liverpool = queryset_list_liverpool.count()

    queryset_list_liverpool_ivf = queryset_list_liverpool.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_liverpool_ivf.items():
        queryset_list_liverpool_ivf_val = val

    queryset_list_liverpool_egg = queryset_list_liverpool.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_liverpool_egg.items():
        queryset_list_liverpool_egg_val = val

    queryset_list_liverpool_embryo = queryset_list_liverpool.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_liverpool_embryo.items():
        queryset_list_liverpool_embryo_val = val

    queryset_list_liverpool_sperm = queryset_list_liverpool.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_liverpool_sperm.items():
        queryset_list_liverpool_sperm_val = val

    queryset_list_liverpool_icsi = queryset_list_liverpool.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_liverpool_icsi.items():
        queryset_list_liverpool_icsi_val = val

    queryset_list_liverpool_iui = queryset_list_liverpool.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_liverpool_iui.items():
        queryset_list_liverpool_iui = val

    #--------------------------------------------------------------------------
    queryset_list_london = queryset_list_uk.filter(clinicRegion__iexact='London')
    my_total_clinic_count_london = queryset_list_london.count()

    queryset_list_london_ivf = queryset_list_london.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_london_ivf.items():
        queryset_list_london_ivf_val = val

    queryset_list_london_egg = queryset_list_london.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_london_egg.items():
        queryset_list_london_egg_val = val

    queryset_list_london_embryo = queryset_list_london.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_london_embryo.items():
        queryset_list_london_embryo_val = val

    queryset_list_london_sperm = queryset_list_london.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_london_sperm.items():
        queryset_list_london_sperm_val = val

    queryset_list_london_icsi = queryset_list_london.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_london_icsi.items():
        queryset_list_london_icsi_val = val

    queryset_list_london_iui = queryset_list_london.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_london_iui.items():
        queryset_list_london_iui = val

    #--------------------------------------------------------------------------
    queryset_list_manchester = queryset_list_uk.filter(clinicRegion__iexact='Manchester')
    my_total_clinic_count_manchester = queryset_list_manchester.count()

    queryset_list_manchester_ivf = queryset_list_manchester.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_manchester_ivf.items():
        queryset_list_manchester_ivf_val = val

    queryset_list_manchester_egg = queryset_list_manchester.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_manchester_egg.items():
        queryset_list_manchester_egg_val = val

    queryset_list_manchester_embryo = queryset_list_manchester.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_manchester_embryo.items():
        queryset_list_manchester_embryo_val = val

    queryset_list_manchester_sperm = queryset_list_manchester.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_manchester_sperm.items():
        queryset_list_manchester_sperm_val = val

    queryset_list_manchester_icsi = queryset_list_manchester.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_manchester_icsi.items():
        queryset_list_manchester_icsi_val = val

    queryset_list_manchester_iui = queryset_list_manchester.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_manchester_iui.items():
        queryset_list_manchester_iui = val

    #--------------------------------------------------------------------------
    queryset_list_middlesbrough = queryset_list_uk.filter(clinicRegion__iexact='Middlesbrough')
    my_total_clinic_count_middlesbrough = queryset_list_middlesbrough.count()

    queryset_list_middlesbrough_ivf = queryset_list_middlesbrough.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_middlesbrough_ivf.items():
        queryset_list_middlesbrough_ivf_val = val

    queryset_list_middlesbrough_egg = queryset_list_middlesbrough.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_middlesbrough_egg.items():
        queryset_list_middlesbrough_egg_val = val

    queryset_list_middlesbrough_embryo = queryset_list_middlesbrough.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_middlesbrough_embryo.items():
        queryset_list_middlesbrough_embryo_val = val

    queryset_list_middlesbrough_sperm = queryset_list_middlesbrough.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_middlesbrough_sperm.items():
        queryset_list_middlesbrough_sperm_val = val

    queryset_list_middlesbrough_icsi = queryset_list_middlesbrough.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_middlesbrough_icsi.items():
        queryset_list_middlesbrough_icsi_val = val

    queryset_list_middlesbrough_iui = queryset_list_middlesbrough.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_middlesbrough_iui.items():
        queryset_list_middlesbrough_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newcastle = queryset_list_uk.filter(clinicRegion__iexact='Newcastle')
    my_total_clinic_count_newcastle = queryset_list_newcastle.count()

    queryset_list_newcastle_ivf = queryset_list_newcastle.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newcastle_ivf.items():
        queryset_list_newcastle_ivf_val = val

    queryset_list_newcastle_egg = queryset_list_newcastle.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newcastle_egg.items():
        queryset_list_newcastle_egg_val = val

    queryset_list_newcastle_embryo = queryset_list_newcastle.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newcastle_embryo.items():
        queryset_list_newcastle_embryo_val = val

    queryset_list_newcastle_sperm = queryset_list_newcastle.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newcastle_sperm.items():
        queryset_list_newcastle_sperm_val = val

    queryset_list_newcastle_icsi = queryset_list_newcastle.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newcastle_icsi.items():
        queryset_list_newcastle_icsi_val = val

    queryset_list_newcastle_iui = queryset_list_newcastle.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newcastle_iui.items():
        queryset_list_newcastle_iui = val

    #--------------------------------------------------------------------------
    queryset_list_norwich = queryset_list_uk.filter(clinicRegion__iexact='Norwich')
    my_total_clinic_count_norwich = queryset_list_norwich.count()

    queryset_list_norwich_ivf = queryset_list_norwich.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_norwich_ivf.items():
        queryset_list_norwich_ivf_val = val

    queryset_list_norwich_egg = queryset_list_norwich.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_norwich_egg.items():
        queryset_list_norwich_egg_val = val

    queryset_list_norwich_embryo = queryset_list_norwich.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_norwich_embryo.items():
        queryset_list_norwich_embryo_val = val

    queryset_list_norwich_sperm = queryset_list_norwich.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_norwich_sperm.items():
        queryset_list_norwich_sperm_val = val

    queryset_list_norwich_icsi = queryset_list_norwich.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_norwich_icsi.items():
        queryset_list_norwich_icsi_val = val

    queryset_list_norwich_iui = queryset_list_norwich.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_norwich_iui.items():
        queryset_list_norwich_iui = val

    #--------------------------------------------------------------------------
    queryset_list_nottingham = queryset_list_uk.filter(clinicRegion__iexact='Nottingham')
    my_total_clinic_count_nottingham = queryset_list_nottingham.count()

    queryset_list_nottingham_ivf = queryset_list_nottingham.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nottingham_ivf.items():
        queryset_list_nottingham_ivf_val = val

    queryset_list_nottingham_egg = queryset_list_nottingham.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nottingham_egg.items():
        queryset_list_nottingham_egg_val = val

    queryset_list_nottingham_embryo = queryset_list_nottingham.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nottingham_embryo.items():
        queryset_list_nottingham_embryo_val = val

    queryset_list_nottingham_sperm = queryset_list_nottingham.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nottingham_sperm.items():
        queryset_list_nottingham_sperm_val = val

    queryset_list_nottingham_icsi = queryset_list_nottingham.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nottingham_icsi.items():
        queryset_list_nottingham_icsi_val = val

    queryset_list_nottingham_iui = queryset_list_nottingham.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nottingham_iui.items():
        queryset_list_nottingham_iui = val

    #--------------------------------------------------------------------------
    queryset_list_oxford = queryset_list_uk.filter(clinicRegion__iexact='Oxford')
    my_total_clinic_count_oxford = queryset_list_oxford.count()

    queryset_list_oxford_ivf = queryset_list_oxford.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_oxford_ivf.items():
        queryset_list_oxford_ivf_val = val

    queryset_list_oxford_egg = queryset_list_oxford.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_oxford_egg.items():
        queryset_list_oxford_egg_val = val

    queryset_list_oxford_embryo = queryset_list_oxford.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_oxford_embryo.items():
        queryset_list_oxford_embryo_val = val

    queryset_list_oxford_sperm = queryset_list_oxford.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_oxford_sperm.items():
        queryset_list_oxford_sperm_val = val

    queryset_list_oxford_icsi = queryset_list_oxford.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_oxford_icsi.items():
        queryset_list_oxford_icsi_val = val

    queryset_list_oxford_iui = queryset_list_oxford.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_oxford_iui.items():
        queryset_list_oxford_iui = val

    #--------------------------------------------------------------------------
    queryset_list_peterborough = queryset_list_uk.filter(clinicRegion__iexact='Peterborough')
    my_total_clinic_count_peterborough = queryset_list_peterborough.count()

    queryset_list_peterborough_ivf = queryset_list_peterborough.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_peterborough_ivf.items():
        queryset_list_peterborough_ivf_val = val

    queryset_list_peterborough_egg = queryset_list_peterborough.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_peterborough_egg.items():
        queryset_list_peterborough_egg_val = val

    queryset_list_peterborough_embryo = queryset_list_peterborough.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_peterborough_embryo.items():
        queryset_list_peterborough_embryo_val = val

    queryset_list_peterborough_sperm = queryset_list_peterborough.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_peterborough_sperm.items():
        queryset_list_peterborough_sperm_val = val

    queryset_list_peterborough_icsi = queryset_list_peterborough.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_peterborough_icsi.items():
        queryset_list_peterborough_icsi_val = val

    queryset_list_peterborough_iui = queryset_list_peterborough.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_peterborough_iui.items():
        queryset_list_peterborough_iui = val

    #--------------------------------------------------------------------------
    queryset_list_plymouth = queryset_list_uk.filter(clinicRegion__iexact='Plymouth')
    my_total_clinic_count_plymouth = queryset_list_plymouth.count()

    queryset_list_plymouth_ivf = queryset_list_plymouth.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_plymouth_ivf.items():
        queryset_list_plymouth_ivf_val = val

    queryset_list_plymouth_egg = queryset_list_plymouth.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_plymouth_egg.items():
        queryset_list_plymouth_egg_val = val

    queryset_list_plymouth_embryo = queryset_list_plymouth.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_plymouth_embryo.items():
        queryset_list_plymouth_embryo_val = val

    queryset_list_plymouth_sperm = queryset_list_plymouth.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_plymouth_sperm.items():
        queryset_list_plymouth_sperm_val = val

    queryset_list_plymouth_icsi = queryset_list_plymouth.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_plymouth_icsi.items():
        queryset_list_plymouth_icsi_val = val

    queryset_list_plymouth_iui = queryset_list_plymouth.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_plymouth_iui.items():
        queryset_list_plymouth_iui = val

    #--------------------------------------------------------------------------
    queryset_list_portsmouth = queryset_list_uk.filter(clinicRegion__iexact='Portsmouth')
    my_total_clinic_count_portsmouth = queryset_list_portsmouth.count()

    queryset_list_portsmouth_ivf = queryset_list_portsmouth.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_portsmouth_ivf.items():
        queryset_list_portsmouth_ivf_val = val

    queryset_list_portsmouth_egg = queryset_list_portsmouth.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_portsmouth_egg.items():
        queryset_list_portsmouth_egg_val = val

    queryset_list_portsmouth_embryo = queryset_list_portsmouth.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_portsmouth_embryo.items():
        queryset_list_portsmouth_embryo_val = val

    queryset_list_portsmouth_sperm = queryset_list_portsmouth.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_portsmouth_sperm.items():
        queryset_list_portsmouth_sperm_val = val

    queryset_list_portsmouth_icsi = queryset_list_portsmouth.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_portsmouth_icsi.items():
        queryset_list_portsmouth_icsi_val = val

    queryset_list_portsmouth_iui = queryset_list_portsmouth.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_portsmouth_iui.items():
        queryset_list_portsmouth_iui = val

    #--------------------------------------------------------------------------
    queryset_list_salisbury = queryset_list_uk.filter(clinicRegion__iexact='Salisbury')
    my_total_clinic_count_salisbury = queryset_list_salisbury.count()

    queryset_list_salisbury_ivf = queryset_list_salisbury.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_salisbury_ivf.items():
        queryset_list_salisbury_ivf_val = val

    queryset_list_salisbury_egg = queryset_list_salisbury.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_salisbury_egg.items():
        queryset_list_salisbury_egg_val = val

    queryset_list_salisbury_embryo = queryset_list_salisbury.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_salisbury_embryo.items():
        queryset_list_salisbury_embryo_val = val

    queryset_list_salisbury_sperm = queryset_list_salisbury.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_salisbury_sperm.items():
        queryset_list_salisbury_sperm_val = val

    queryset_list_salisbury_icsi = queryset_list_salisbury.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_salisbury_icsi.items():
        queryset_list_salisbury_icsi_val = val

    queryset_list_salisbury_iui = queryset_list_salisbury.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_salisbury_iui.items():
        queryset_list_salisbury_iui = val

    #--------------------------------------------------------------------------
    queryset_list_sheffield = queryset_list_uk.filter(clinicRegion__iexact='Sheffield')
    my_total_clinic_count_sheffield = queryset_list_sheffield.count()

    queryset_list_sheffield_ivf = queryset_list_sheffield.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_sheffield_ivf.items():
        queryset_list_sheffield_ivf_val = val

    queryset_list_sheffield_egg = queryset_list_sheffield.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_sheffield_egg.items():
        queryset_list_sheffield_egg_val = val

    queryset_list_sheffield_embryo = queryset_list_sheffield.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_sheffield_embryo.items():
        queryset_list_sheffield_embryo_val = val

    queryset_list_sheffield_sperm = queryset_list_sheffield.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_sheffield_sperm.items():
        queryset_list_sheffield_sperm_val = val

    queryset_list_sheffield_icsi = queryset_list_sheffield.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_sheffield_icsi.items():
        queryset_list_sheffield_icsi_val = val

    queryset_list_sheffield_iui = queryset_list_sheffield.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_sheffield_iui.items():
        queryset_list_sheffield_iui = val

    #--------------------------------------------------------------------------
    queryset_list_southampton = queryset_list_uk.filter(clinicRegion__iexact='Southampton')
    my_total_clinic_count_southampton = queryset_list_southampton.count()

    queryset_list_southampton_ivf = queryset_list_southampton.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_southampton_ivf.items():
        queryset_list_southampton_ivf_val = val

    queryset_list_southampton_egg = queryset_list_southampton.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_southampton_egg.items():
        queryset_list_southampton_egg_val = val

    queryset_list_southampton_embryo = queryset_list_southampton.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_southampton_embryo.items():
        queryset_list_southampton_embryo_val = val

    queryset_list_southampton_sperm = queryset_list_southampton.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_southampton_sperm.items():
        queryset_list_southampton_sperm_val = val

    queryset_list_southampton_icsi = queryset_list_southampton.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_southampton_icsi.items():
        queryset_list_southampton_icsi_val = val

    queryset_list_southampton_iui = queryset_list_southampton.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_southampton_iui.items():
        queryset_list_southampton_iui = val

    #--------------------------------------------------------------------------
    queryset_list_swansea = queryset_list_uk.filter(clinicRegion__iexact='Swansea')
    my_total_clinic_count_swansea = queryset_list_swansea.count()

    queryset_list_swansea_ivf = queryset_list_swansea.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_swansea_ivf.items():
        queryset_list_swansea_ivf_val = val

    queryset_list_swansea_egg = queryset_list_swansea.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_swansea_egg.items():
        queryset_list_swansea_egg_val = val

    queryset_list_swansea_embryo = queryset_list_swansea.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_swansea_embryo.items():
        queryset_list_swansea_embryo_val = val

    queryset_list_swansea_sperm = queryset_list_swansea.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_swansea_sperm.items():
        queryset_list_swansea_sperm_val = val

    queryset_list_swansea_icsi = queryset_list_swansea.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_swansea_icsi.items():
        queryset_list_swansea_icsi_val = val

    queryset_list_swansea_iui = queryset_list_swansea.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_swansea_iui.items():
        queryset_list_swansea_iui = val


    context = {
        'my_total_clinic_count_aberdeen': my_total_clinic_count_aberdeen,
        'queryset_list_aberdeen_ivf_val': queryset_list_aberdeen_ivf_val,
        'queryset_list_aberdeen_egg_val': queryset_list_aberdeen_egg_val,
        'queryset_list_aberdeen_embryo_val': queryset_list_aberdeen_embryo_val,
        'queryset_list_aberdeen_sperm_val': queryset_list_aberdeen_sperm_val,
        'queryset_list_aberdeen_icsi_val': queryset_list_aberdeen_icsi_val,
        'queryset_list_aberdeen_iui': queryset_list_aberdeen_iui,

        'my_total_clinic_count_bath': my_total_clinic_count_bath,
        'queryset_list_bath_ivf_val': queryset_list_bath_ivf_val,
        'queryset_list_bath_egg_val': queryset_list_bath_egg_val,
        'queryset_list_bath_embryo_val': queryset_list_bath_embryo_val,
        'queryset_list_bath_sperm_val': queryset_list_bath_sperm_val,
        'queryset_list_bath_icsi_val': queryset_list_bath_icsi_val,
        'queryset_list_bath_iui': queryset_list_bath_iui,

        'my_total_clinic_count_belfast': my_total_clinic_count_belfast,
        'queryset_list_belfast_ivf_val': queryset_list_belfast_ivf_val,
        'queryset_list_belfast_egg_val': queryset_list_belfast_egg_val,
        'queryset_list_belfast_embryo_val': queryset_list_belfast_embryo_val,
        'queryset_list_belfast_sperm_val': queryset_list_belfast_sperm_val,
        'queryset_list_belfast_icsi_val': queryset_list_belfast_icsi_val,
        'queryset_list_belfast_iui': queryset_list_belfast_iui,

        'my_total_clinic_count_birmingham': my_total_clinic_count_birmingham,
        'queryset_list_birmingham_ivf_val': queryset_list_birmingham_ivf_val,
        'queryset_list_birmingham_egg_val': queryset_list_birmingham_egg_val,
        'queryset_list_birmingham_embryo_val': queryset_list_birmingham_embryo_val,
        'queryset_list_birmingham_sperm_val': queryset_list_birmingham_sperm_val,
        'queryset_list_birmingham_icsi_val': queryset_list_birmingham_icsi_val,
        'queryset_list_birmingham_iui': queryset_list_birmingham_iui,

        'my_total_clinic_count_bournemouth': my_total_clinic_count_bournemouth,
        'queryset_list_bournemouth_ivf_val': queryset_list_bournemouth_ivf_val,
        'queryset_list_bournemouth_egg_val': queryset_list_bournemouth_egg_val,
        'queryset_list_bournemouth_embryo_val': queryset_list_bournemouth_embryo_val,
        'queryset_list_bournemouth_sperm_val': queryset_list_bournemouth_sperm_val,
        'queryset_list_bournemouth_icsi_val': queryset_list_bournemouth_icsi_val,
        'queryset_list_bournemouth_iui': queryset_list_bournemouth_iui,

        'my_total_clinic_count_brighton': my_total_clinic_count_brighton,
        'queryset_list_brighton_ivf_val': queryset_list_brighton_ivf_val,
        'queryset_list_brighton_egg_val': queryset_list_brighton_egg_val,
        'queryset_list_brighton_embryo_val': queryset_list_brighton_embryo_val,
        'queryset_list_brighton_sperm_val': queryset_list_brighton_sperm_val,
        'queryset_list_brighton_icsi_val': queryset_list_brighton_icsi_val,
        'queryset_list_brighton_iui': queryset_list_brighton_iui,

        'my_total_clinic_count_bristol': my_total_clinic_count_bristol,
        'queryset_list_bristol_ivf_val': queryset_list_bristol_ivf_val,
        'queryset_list_bristol_egg_val': queryset_list_bristol_egg_val,
        'queryset_list_bristol_embryo_val': queryset_list_bristol_embryo_val,
        'queryset_list_bristol_sperm_val': queryset_list_bristol_sperm_val,
        'queryset_list_bristol_icsi_val': queryset_list_bristol_icsi_val,
        'queryset_list_bristol_iui': queryset_list_bristol_iui,

        'my_total_clinic_count_cambridge': my_total_clinic_count_cambridge,
        'queryset_list_cambridge_ivf_val': queryset_list_cambridge_ivf_val,
        'queryset_list_cambridge_egg_val': queryset_list_cambridge_egg_val,
        'queryset_list_cambridge_embryo_val': queryset_list_cambridge_embryo_val,
        'queryset_list_cambridge_sperm_val': queryset_list_cambridge_sperm_val,
        'queryset_list_cambridge_icsi_val': queryset_list_cambridge_icsi_val,
        'queryset_list_cambridge_iui': queryset_list_cambridge_iui,

        'my_total_clinic_count_cardiff': my_total_clinic_count_cardiff,
        'queryset_list_cardiff_ivf_val': queryset_list_cardiff_ivf_val,
        'queryset_list_cardiff_egg_val': queryset_list_cardiff_egg_val,
        'queryset_list_cardiff_embryo_val': queryset_list_cardiff_embryo_val,
        'queryset_list_cardiff_sperm_val': queryset_list_cardiff_sperm_val,
        'queryset_list_cardiff_icsi_val': queryset_list_cardiff_icsi_val,
        'queryset_list_cardiff_iui': queryset_list_cardiff_iui,

        'my_total_clinic_count_colchester': my_total_clinic_count_colchester,
        'queryset_list_colchester_ivf_val': queryset_list_colchester_ivf_val,
        'queryset_list_colchester_egg_val': queryset_list_colchester_egg_val,
        'queryset_list_colchester_embryo_val': queryset_list_colchester_embryo_val,
        'queryset_list_colchester_sperm_val': queryset_list_colchester_sperm_val,
        'queryset_list_colchester_icsi_val': queryset_list_colchester_icsi_val,
        'queryset_list_colchester_iui': queryset_list_colchester_iui,

        'my_total_clinic_count_derby': my_total_clinic_count_derby,
        'queryset_list_derby_ivf_val': queryset_list_derby_ivf_val,
        'queryset_list_derby_egg_val': queryset_list_derby_egg_val,
        'queryset_list_derby_embryo_val': queryset_list_derby_embryo_val,
        'queryset_list_derby_sperm_val': queryset_list_derby_sperm_val,
        'queryset_list_derby_icsi_val': queryset_list_derby_icsi_val,
        'queryset_list_derby_iui': queryset_list_derby_iui,

        'my_total_clinic_count_exeter': my_total_clinic_count_exeter,
        'queryset_list_exeter_ivf_val': queryset_list_exeter_ivf_val,
        'queryset_list_exeter_egg_val': queryset_list_exeter_egg_val,
        'queryset_list_exeter_embryo_val': queryset_list_exeter_embryo_val,
        'queryset_list_exeter_sperm_val': queryset_list_exeter_sperm_val,
        'queryset_list_exeter_icsi_val': queryset_list_exeter_icsi_val,
        'queryset_list_exeter_iui': queryset_list_exeter_iui,

        'my_total_clinic_count_glasgow': my_total_clinic_count_glasgow,
        'queryset_list_glasgow_ivf_val': queryset_list_glasgow_ivf_val,
        'queryset_list_glasgow_egg_val': queryset_list_glasgow_egg_val,
        'queryset_list_glasgow_embryo_val': queryset_list_glasgow_embryo_val,
        'queryset_list_glasgow_sperm_val': queryset_list_glasgow_sperm_val,
        'queryset_list_glasgow_icsi_val': queryset_list_glasgow_icsi_val,
        'queryset_list_glasgow_iui': queryset_list_glasgow_iui,

        'my_total_clinic_count_hull': my_total_clinic_count_hull,
        'queryset_list_hull_ivf_val': queryset_list_hull_ivf_val,
        'queryset_list_hull_egg_val': queryset_list_hull_egg_val,
        'queryset_list_hull_embryo_val': queryset_list_hull_embryo_val,
        'queryset_list_hull_sperm_val': queryset_list_hull_sperm_val,
        'queryset_list_hull_icsi_val': queryset_list_hull_icsi_val,
        'queryset_list_hull_iui': queryset_list_hull_iui,

        'my_total_clinic_count_chelmsford': my_total_clinic_count_chelmsford,
        'queryset_list_chelmsford_ivf_val': queryset_list_chelmsford_ivf_val,
        'queryset_list_chelmsford_egg_val': queryset_list_chelmsford_egg_val,
        'queryset_list_chelmsford_embryo_val': queryset_list_chelmsford_embryo_val,
        'queryset_list_chelmsford_sperm_val': queryset_list_chelmsford_sperm_val,
        'queryset_list_chelmsford_icsi_val': queryset_list_chelmsford_icsi_val,
        'queryset_list_chelmsford_iui': queryset_list_chelmsford_iui,

        'my_total_clinic_count_leeds': my_total_clinic_count_leeds,
        'queryset_list_leeds_ivf_val': queryset_list_leeds_ivf_val,
        'queryset_list_leeds_egg_val': queryset_list_leeds_egg_val,
        'queryset_list_leeds_embryo_val': queryset_list_leeds_embryo_val,
        'queryset_list_leeds_sperm_val': queryset_list_leeds_sperm_val,
        'queryset_list_leeds_icsi_val': queryset_list_leeds_icsi_val,
        'queryset_list_leeds_iui': queryset_list_leeds_iui,

        'my_total_clinic_count_leicester': my_total_clinic_count_leicester,
        'queryset_list_leicester_ivf_val': queryset_list_leicester_ivf_val,
        'queryset_list_leicester_egg_val': queryset_list_leicester_egg_val,
        'queryset_list_leicester_embryo_val': queryset_list_leicester_embryo_val,
        'queryset_list_leicester_sperm_val': queryset_list_leicester_sperm_val,
        'queryset_list_leicester_icsi_val': queryset_list_leicester_icsi_val,
        'queryset_list_leicester_iui': queryset_list_leicester_iui,

        'my_total_clinic_count_liverpool': my_total_clinic_count_liverpool,
        'queryset_list_liverpool_ivf_val': queryset_list_liverpool_ivf_val,
        'queryset_list_liverpool_egg_val': queryset_list_liverpool_egg_val,
        'queryset_list_liverpool_embryo_val': queryset_list_liverpool_embryo_val,
        'queryset_list_liverpool_sperm_val': queryset_list_liverpool_sperm_val,
        'queryset_list_liverpool_icsi_val': queryset_list_liverpool_icsi_val,
        'queryset_list_liverpool_iui': queryset_list_liverpool_iui,

        'my_total_clinic_count_london': my_total_clinic_count_london,
        'queryset_list_london_ivf_val': queryset_list_london_ivf_val,
        'queryset_list_london_egg_val': queryset_list_london_egg_val,
        'queryset_list_london_embryo_val': queryset_list_london_embryo_val,
        'queryset_list_london_sperm_val': queryset_list_london_sperm_val,
        'queryset_list_london_icsi_val': queryset_list_london_icsi_val,
        'queryset_list_london_iui': queryset_list_london_iui,

        'my_total_clinic_count_manchester': my_total_clinic_count_manchester,
        'queryset_list_manchester_ivf_val': queryset_list_manchester_ivf_val,
        'queryset_list_manchester_egg_val': queryset_list_manchester_egg_val,
        'queryset_list_manchester_embryo_val': queryset_list_manchester_embryo_val,
        'queryset_list_manchester_sperm_val': queryset_list_manchester_sperm_val,
        'queryset_list_manchester_icsi_val': queryset_list_manchester_icsi_val,
        'queryset_list_manchester_iui': queryset_list_manchester_iui,

        'my_total_clinic_count_middlesbrough': my_total_clinic_count_middlesbrough,
        'queryset_list_middlesbrough_ivf_val': queryset_list_middlesbrough_ivf_val,
        'queryset_list_middlesbrough_egg_val': queryset_list_middlesbrough_egg_val,
        'queryset_list_middlesbrough_embryo_val': queryset_list_middlesbrough_embryo_val,
        'queryset_list_middlesbrough_sperm_val': queryset_list_middlesbrough_sperm_val,
        'queryset_list_middlesbrough_icsi_val': queryset_list_middlesbrough_icsi_val,
        'queryset_list_middlesbrough_iui': queryset_list_middlesbrough_iui,

        'my_total_clinic_count_newcastle': my_total_clinic_count_newcastle,
        'queryset_list_newcastle_ivf_val': queryset_list_newcastle_ivf_val,
        'queryset_list_newcastle_egg_val': queryset_list_newcastle_egg_val,
        'queryset_list_newcastle_embryo_val': queryset_list_newcastle_embryo_val,
        'queryset_list_newcastle_sperm_val': queryset_list_newcastle_sperm_val,
        'queryset_list_newcastle_icsi_val': queryset_list_newcastle_icsi_val,
        'queryset_list_newcastle_iui': queryset_list_newcastle_iui,

        'my_total_clinic_count_norwich': my_total_clinic_count_norwich,
        'queryset_list_norwich_ivf_val': queryset_list_norwich_ivf_val,
        'queryset_list_norwich_egg_val': queryset_list_norwich_egg_val,
        'queryset_list_norwich_embryo_val': queryset_list_norwich_embryo_val,
        'queryset_list_norwich_sperm_val': queryset_list_norwich_sperm_val,
        'queryset_list_norwich_icsi_val': queryset_list_norwich_icsi_val,
        'queryset_list_norwich_iui': queryset_list_norwich_iui,

        'my_total_clinic_count_nottingham': my_total_clinic_count_nottingham,
        'queryset_list_nottingham_ivf_val': queryset_list_nottingham_ivf_val,
        'queryset_list_nottingham_egg_val': queryset_list_nottingham_egg_val,
        'queryset_list_nottingham_embryo_val': queryset_list_nottingham_embryo_val,
        'queryset_list_nottingham_sperm_val': queryset_list_nottingham_sperm_val,
        'queryset_list_nottingham_icsi_val': queryset_list_nottingham_icsi_val,
        'queryset_list_nottingham_iui': queryset_list_nottingham_iui,

        'my_total_clinic_count_oxford': my_total_clinic_count_oxford,
        'queryset_list_oxford_ivf_val': queryset_list_oxford_ivf_val,
        'queryset_list_oxford_egg_val': queryset_list_oxford_egg_val,
        'queryset_list_oxford_embryo_val': queryset_list_oxford_embryo_val,
        'queryset_list_oxford_sperm_val': queryset_list_oxford_sperm_val,
        'queryset_list_oxford_icsi_val': queryset_list_oxford_icsi_val,
        'queryset_list_oxford_iui': queryset_list_oxford_iui,

        'my_total_clinic_count_peterborough': my_total_clinic_count_peterborough,
        'queryset_list_peterborough_ivf_val': queryset_list_peterborough_ivf_val,
        'queryset_list_peterborough_egg_val': queryset_list_peterborough_egg_val,
        'queryset_list_peterborough_embryo_val': queryset_list_peterborough_embryo_val,
        'queryset_list_peterborough_sperm_val': queryset_list_peterborough_sperm_val,
        'queryset_list_peterborough_icsi_val': queryset_list_peterborough_icsi_val,
        'queryset_list_peterborough_iui': queryset_list_peterborough_iui,

        'my_total_clinic_count_plymouth': my_total_clinic_count_plymouth,
        'queryset_list_plymouth_ivf_val': queryset_list_plymouth_ivf_val,
        'queryset_list_plymouth_egg_val': queryset_list_plymouth_egg_val,
        'queryset_list_plymouth_embryo_val': queryset_list_plymouth_embryo_val,
        'queryset_list_plymouth_sperm_val': queryset_list_plymouth_sperm_val,
        'queryset_list_plymouth_icsi_val': queryset_list_plymouth_icsi_val,
        'queryset_list_plymouth_iui': queryset_list_plymouth_iui,

        'my_total_clinic_count_portsmouth': my_total_clinic_count_portsmouth,
        'queryset_list_portsmouth_ivf_val': queryset_list_portsmouth_ivf_val,
        'queryset_list_portsmouth_egg_val': queryset_list_portsmouth_egg_val,
        'queryset_list_portsmouth_embryo_val': queryset_list_portsmouth_embryo_val,
        'queryset_list_portsmouth_sperm_val': queryset_list_portsmouth_sperm_val,
        'queryset_list_portsmouth_icsi_val': queryset_list_portsmouth_icsi_val,
        'queryset_list_portsmouth_iui': queryset_list_portsmouth_iui,

        'my_total_clinic_count_salisbury': my_total_clinic_count_salisbury,
        'queryset_list_salisbury_ivf_val': queryset_list_salisbury_ivf_val,
        'queryset_list_salisbury_egg_val': queryset_list_salisbury_egg_val,
        'queryset_list_salisbury_embryo_val': queryset_list_salisbury_embryo_val,
        'queryset_list_salisbury_sperm_val': queryset_list_salisbury_sperm_val,
        'queryset_list_salisbury_icsi_val': queryset_list_salisbury_icsi_val,
        'queryset_list_salisbury_iui': queryset_list_salisbury_iui,

        'my_total_clinic_count_sheffield': my_total_clinic_count_sheffield,
        'queryset_list_sheffield_ivf_val': queryset_list_sheffield_ivf_val,
        'queryset_list_sheffield_egg_val': queryset_list_sheffield_egg_val,
        'queryset_list_sheffield_embryo_val': queryset_list_sheffield_embryo_val,
        'queryset_list_sheffield_sperm_val': queryset_list_sheffield_sperm_val,
        'queryset_list_sheffield_icsi_val': queryset_list_sheffield_icsi_val,
        'queryset_list_sheffield_iui': queryset_list_sheffield_iui,

        'my_total_clinic_count_southampton': my_total_clinic_count_southampton,
        'queryset_list_southampton_ivf_val': queryset_list_southampton_ivf_val,
        'queryset_list_southampton_egg_val': queryset_list_southampton_egg_val,
        'queryset_list_southampton_embryo_val': queryset_list_southampton_embryo_val,
        'queryset_list_southampton_sperm_val': queryset_list_southampton_sperm_val,
        'queryset_list_southampton_icsi_val': queryset_list_southampton_icsi_val,
        'queryset_list_southampton_iui': queryset_list_southampton_iui,

        'my_total_clinic_count_swansea': my_total_clinic_count_swansea,
        'queryset_list_swansea_ivf_val': queryset_list_swansea_ivf_val,
        'queryset_list_swansea_egg_val': queryset_list_swansea_egg_val,
        'queryset_list_swansea_embryo_val': queryset_list_swansea_embryo_val,
        'queryset_list_swansea_sperm_val': queryset_list_swansea_sperm_val,
        'queryset_list_swansea_icsi_val': queryset_list_swansea_icsi_val,
        'queryset_list_swansea_iui': queryset_list_swansea_iui,
        }


    return render(request, 'main/Locations/UKLocations/uk-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsCZRegions(request):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_prague = queryset_list_cz.filter(clinicRegion__iexact='Prague')
    my_total_clinic_count_prague = queryset_list_prague.count()

    queryset_list_prague_ivf = queryset_list_prague.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_prague_ivf.items():
        queryset_list_prague_ivf_val = val

    queryset_list_prague_egg = queryset_list_prague.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_prague_egg.items():
        queryset_list_prague_egg_val = val

    queryset_list_prague_embryo = queryset_list_prague.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_prague_embryo.items():
        queryset_list_prague_embryo_val = val

    queryset_list_prague_sperm = queryset_list_prague.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_prague_sperm.items():
        queryset_list_prague_sperm_val = val

    queryset_list_prague_icsi = queryset_list_prague.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_prague_icsi.items():
        queryset_list_prague_icsi_val = val

    queryset_list_prague_iui = queryset_list_prague.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_prague_iui.items():
        queryset_list_prague_iui = val

    #--------------------------------------------------------------------------
    queryset_list_brno = queryset_list_cz.filter(clinicRegion__iexact='Brno')
    my_total_clinic_count_brno = queryset_list_brno.count()

    queryset_list_brno_ivf = queryset_list_brno.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_brno_ivf.items():
        queryset_list_brno_ivf_val = val

    queryset_list_brno_egg = queryset_list_brno.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_brno_egg.items():
        queryset_list_brno_egg_val = val

    queryset_list_brno_embryo = queryset_list_brno.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_brno_embryo.items():
        queryset_list_brno_embryo_val = val

    queryset_list_brno_sperm = queryset_list_brno.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_brno_sperm.items():
        queryset_list_brno_sperm_val = val

    queryset_list_brno_icsi = queryset_list_brno.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_brno_icsi.items():
        queryset_list_brno_icsi_val = val

    queryset_list_brno_iui = queryset_list_brno.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_brno_iui.items():
        queryset_list_brno_iui = val

    context = {
        'my_total_clinic_count_prague': my_total_clinic_count_prague,
        'queryset_list_prague_ivf_val': queryset_list_prague_ivf_val,
        'queryset_list_prague_egg_val': queryset_list_prague_egg_val,
        'queryset_list_prague_embryo_val': queryset_list_prague_embryo_val,
        'queryset_list_prague_sperm_val': queryset_list_prague_sperm_val,
        'queryset_list_prague_icsi_val': queryset_list_prague_icsi_val,
        'queryset_list_prague_iui': queryset_list_prague_iui,

        'my_total_clinic_count_brno': my_total_clinic_count_brno,
        'queryset_list_brno_ivf_val': queryset_list_brno_ivf_val,
        'queryset_list_brno_egg_val': queryset_list_brno_egg_val,
        'queryset_list_brno_embryo_val': queryset_list_brno_embryo_val,
        'queryset_list_brno_sperm_val': queryset_list_brno_sperm_val,
        'queryset_list_brno_icsi_val': queryset_list_brno_icsi_val,
        'queryset_list_brno_iui': queryset_list_brno_iui,
        }
    return render(request, 'main/Locations/CZLocations/cz-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsSPRegions(request):
    queryset_list_sp = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_alicante = queryset_list_sp.filter(clinicRegion__iexact='Alicante')
    my_total_clinic_count_alicante = queryset_list_alicante.count()

    queryset_list_alicante_ivf = queryset_list_alicante.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_alicante_ivf.items():
        queryset_list_alicante_ivf_val = val

    queryset_list_alicante_egg = queryset_list_alicante.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_alicante_egg.items():
        queryset_list_alicante_egg_val = val

    queryset_list_alicante_embryo = queryset_list_alicante.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_alicante_embryo.items():
        queryset_list_alicante_embryo_val = val

    queryset_list_alicante_sperm = queryset_list_alicante.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_alicante_sperm.items():
        queryset_list_alicante_sperm_val = val

    queryset_list_alicante_icsi = queryset_list_alicante.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_alicante_icsi.items():
        queryset_list_alicante_icsi_val = val

    queryset_list_alicante_iui = queryset_list_alicante.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_alicante_iui.items():
        queryset_list_alicante_iui = val

    #--------------------------------------------------------------------------
    queryset_list_barcelona = queryset_list_sp.filter(clinicRegion__iexact='Barcelona')
    my_total_clinic_count_barcelona = queryset_list_barcelona.count()

    queryset_list_barcelona_ivf = queryset_list_barcelona.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_barcelona_ivf.items():
        queryset_list_barcelona_ivf_val = val

    queryset_list_barcelona_egg = queryset_list_barcelona.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_egg.items():
        queryset_list_barcelona_egg_val = val

    queryset_list_barcelona_embryo = queryset_list_barcelona.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_embryo.items():
        queryset_list_barcelona_embryo_val = val

    queryset_list_barcelona_sperm = queryset_list_barcelona.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_barcelona_sperm.items():
        queryset_list_barcelona_sperm_val = val

    queryset_list_barcelona_icsi = queryset_list_barcelona.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_barcelona_icsi.items():
        queryset_list_barcelona_icsi_val = val

    queryset_list_barcelona_iui = queryset_list_barcelona.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_barcelona_iui.items():
        queryset_list_barcelona_iui = val

    #--------------------------------------------------------------------------
    queryset_list_madrid = queryset_list_sp.filter(clinicRegion__iexact='Madrid')
    my_total_clinic_count_madrid = queryset_list_madrid.count()

    queryset_list_madrid_ivf = queryset_list_madrid.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_madrid_ivf.items():
        queryset_list_madrid_ivf_val = val

    queryset_list_madrid_egg = queryset_list_madrid.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_madrid_egg.items():
        queryset_list_madrid_egg_val = val

    queryset_list_madrid_embryo = queryset_list_madrid.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_madrid_embryo.items():
        queryset_list_madrid_embryo_val = val

    queryset_list_madrid_sperm = queryset_list_madrid.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_madrid_sperm.items():
        queryset_list_madrid_sperm_val = val

    queryset_list_madrid_icsi = queryset_list_madrid.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_madrid_icsi.items():
        queryset_list_madrid_icsi_val = val

    queryset_list_madrid_iui = queryset_list_madrid.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_madrid_iui.items():
        queryset_list_madrid_iui = val

    #--------------------------------------------------------------------------
    queryset_list_malaga = queryset_list_sp.filter(clinicRegion__iexact='Malaga')
    my_total_clinic_count_malaga = queryset_list_malaga.count()

    queryset_list_malaga_ivf = queryset_list_malaga.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_malaga_ivf.items():
        queryset_list_malaga_ivf_val = val

    queryset_list_malaga_egg = queryset_list_malaga.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_malaga_egg.items():
        queryset_list_malaga_egg_val = val

    queryset_list_malaga_embryo = queryset_list_malaga.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_malaga_embryo.items():
        queryset_list_malaga_embryo_val = val

    queryset_list_malaga_sperm = queryset_list_malaga.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_malaga_sperm.items():
        queryset_list_malaga_sperm_val = val

    queryset_list_malaga_icsi = queryset_list_malaga.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_malaga_icsi.items():
        queryset_list_malaga_icsi_val = val

    queryset_list_malaga_iui = queryset_list_malaga.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_malaga_iui.items():
        queryset_list_malaga_iui = val

    #--------------------------------------------------------------------------
    queryset_list_sevilla = queryset_list_sp.filter(clinicRegion__iexact='Sevilla')
    my_total_clinic_count_sevilla = queryset_list_sevilla.count()

    queryset_list_sevilla_ivf = queryset_list_sevilla.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_sevilla_ivf.items():
        queryset_list_sevilla_ivf_val = val

    queryset_list_sevilla_egg = queryset_list_sevilla.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_egg.items():
        queryset_list_sevilla_egg_val = val

    queryset_list_sevilla_embryo = queryset_list_sevilla.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_embryo.items():
        queryset_list_sevilla_embryo_val = val

    queryset_list_sevilla_sperm = queryset_list_sevilla.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_sevilla_sperm.items():
        queryset_list_sevilla_sperm_val = val

    queryset_list_sevilla_icsi = queryset_list_sevilla.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_sevilla_icsi.items():
        queryset_list_sevilla_icsi_val = val

    queryset_list_sevilla_iui = queryset_list_sevilla.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_sevilla_iui.items():
        queryset_list_sevilla_iui = val

    #--------------------------------------------------------------------------
    queryset_list_valencia = queryset_list_sp.filter(clinicRegion__iexact='Valencia')
    my_total_clinic_count_valencia = queryset_list_valencia.count()

    queryset_list_valencia_ivf = queryset_list_valencia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_valencia_ivf.items():
        queryset_list_valencia_ivf_val = val

    queryset_list_valencia_egg = queryset_list_valencia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_valencia_egg.items():
        queryset_list_valencia_egg_val = val

    queryset_list_valencia_embryo = queryset_list_valencia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_valencia_embryo.items():
        queryset_list_valencia_embryo_val = val

    queryset_list_valencia_sperm = queryset_list_valencia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_valencia_sperm.items():
        queryset_list_valencia_sperm_val = val

    queryset_list_valencia_icsi = queryset_list_valencia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_valencia_icsi.items():
        queryset_list_valencia_icsi_val = val

    queryset_list_valencia_iui = queryset_list_valencia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_valencia_iui.items():
        queryset_list_valencia_iui = val

    context = {
        'my_total_clinic_count_barcelona': my_total_clinic_count_barcelona,
        'queryset_list_alicante_ivf_val': queryset_list_alicante_ivf_val,
        'queryset_list_alicante_egg_val': queryset_list_alicante_egg_val,
        'queryset_list_alicante_embryo_val': queryset_list_alicante_embryo_val,
        'queryset_list_alicante_sperm_val': queryset_list_alicante_sperm_val,
        'queryset_list_alicante_icsi_val': queryset_list_alicante_icsi_val,
        'queryset_list_alicante_iui': queryset_list_alicante_iui,

        'my_total_clinic_count_barcelona': my_total_clinic_count_barcelona,
        'queryset_list_barcelona_ivf_val': queryset_list_barcelona_ivf_val,
        'queryset_list_barcelona_egg_val': queryset_list_barcelona_egg_val,
        'queryset_list_barcelona_embryo_val': queryset_list_barcelona_embryo_val,
        'queryset_list_barcelona_sperm_val': queryset_list_barcelona_sperm_val,
        'queryset_list_barcelona_icsi_val': queryset_list_barcelona_icsi_val,
        'queryset_list_barcelona_iui': queryset_list_barcelona_iui,

        'my_total_clinic_count_madrid': my_total_clinic_count_madrid,
        'queryset_list_madrid_ivf_val': queryset_list_madrid_ivf_val,
        'queryset_list_madrid_egg_val': queryset_list_madrid_egg_val,
        'queryset_list_madrid_embryo_val': queryset_list_madrid_embryo_val,
        'queryset_list_madrid_sperm_val': queryset_list_madrid_sperm_val,
        'queryset_list_madrid_icsi_val': queryset_list_madrid_icsi_val,
        'queryset_list_madrid_iui': queryset_list_madrid_iui,

        'my_total_clinic_count_malaga': my_total_clinic_count_malaga,
        'queryset_list_malaga_ivf_val': queryset_list_malaga_ivf_val,
        'queryset_list_malaga_egg_val': queryset_list_malaga_egg_val,
        'queryset_list_malaga_embryo_val': queryset_list_malaga_embryo_val,
        'queryset_list_malaga_sperm_val': queryset_list_malaga_sperm_val,
        'queryset_list_malaga_icsi_val': queryset_list_malaga_icsi_val,
        'queryset_list_malaga_iui': queryset_list_malaga_iui,

        'my_total_clinic_count_sevilla': my_total_clinic_count_sevilla,
        'queryset_list_sevilla_ivf_val': queryset_list_sevilla_ivf_val,
        'queryset_list_sevilla_egg_val': queryset_list_sevilla_egg_val,
        'queryset_list_sevilla_embryo_val': queryset_list_sevilla_embryo_val,
        'queryset_list_sevilla_sperm_val': queryset_list_sevilla_sperm_val,
        'queryset_list_sevilla_icsi_val': queryset_list_sevilla_icsi_val,
        'queryset_list_sevilla_iui': queryset_list_sevilla_iui,

        'my_total_clinic_count_valencia': my_total_clinic_count_valencia,
        'queryset_list_valencia_ivf_val': queryset_list_valencia_ivf_val,
        'queryset_list_valencia_egg_val': queryset_list_valencia_egg_val,
        'queryset_list_valencia_embryo_val': queryset_list_valencia_embryo_val,
        'queryset_list_valencia_sperm_val': queryset_list_valencia_sperm_val,
        'queryset_list_valencia_icsi_val': queryset_list_valencia_icsi_val,
        'queryset_list_valencia_iui': queryset_list_valencia_iui,
        }

    return render(request, 'main/Locations/SPLocations/sp-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsINRegions(request):
    queryset_list_in = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_amdavad = queryset_list_in.filter(clinicCity__iexact='Amdavad')
    my_total_clinic_count_amdavad = queryset_list_amdavad.count()

    queryset_list_amdavad_ivf = queryset_list_amdavad.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_amdavad_ivf.items():
        queryset_list_amdavad_ivf_val = val

    queryset_list_amdavad_egg = queryset_list_amdavad.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_amdavad_egg.items():
        queryset_list_amdavad_egg_val = val

    queryset_list_amdavad_embryo = queryset_list_amdavad.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_amdavad_embryo.items():
        queryset_list_amdavad_embryo_val = val

    queryset_list_amdavad_sperm = queryset_list_amdavad.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_amdavad_sperm.items():
        queryset_list_amdavad_sperm_val = val

    queryset_list_amdavad_icsi = queryset_list_amdavad.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_amdavad_icsi.items():
        queryset_list_amdavad_icsi_val = val

    queryset_list_amdavad_iui = queryset_list_amdavad.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_amdavad_iui.items():
        queryset_list_amdavad_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bangalore = queryset_list_in.filter(clinicCity__iexact='Bangalore')
    my_total_clinic_count_bangalore = queryset_list_bangalore.count()

    queryset_list_bangalore_ivf = queryset_list_bangalore.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bangalore_ivf.items():
        queryset_list_bangalore_ivf_val = val

    queryset_list_bangalore_egg = queryset_list_bangalore.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bangalore_egg.items():
        queryset_list_bangalore_egg_val = val

    queryset_list_bangalore_embryo = queryset_list_bangalore.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bangalore_embryo.items():
        queryset_list_bangalore_embryo_val = val

    queryset_list_bangalore_sperm = queryset_list_bangalore.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bangalore_sperm.items():
        queryset_list_bangalore_sperm_val = val

    queryset_list_bangalore_icsi = queryset_list_bangalore.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bangalore_icsi.items():
        queryset_list_bangalore_icsi_val = val

    queryset_list_bangalore_iui = queryset_list_bangalore.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bangalore_iui.items():
        queryset_list_bangalore_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bhopal = queryset_list_in.filter(clinicCity__iexact='Bhopal')
    my_total_clinic_count_bhopal = queryset_list_bhopal.count()

    queryset_list_bhopal_ivf = queryset_list_bhopal.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bhopal_ivf.items():
        queryset_list_bhopal_ivf_val = val

    queryset_list_bhopal_egg = queryset_list_bhopal.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bhopal_egg.items():
        queryset_list_bhopal_egg_val = val

    queryset_list_bhopal_embryo = queryset_list_bhopal.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bhopal_embryo.items():
        queryset_list_bhopal_embryo_val = val

    queryset_list_bhopal_sperm = queryset_list_bhopal.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bhopal_sperm.items():
        queryset_list_bhopal_sperm_val = val

    queryset_list_bhopal_icsi = queryset_list_bhopal.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bhopal_icsi.items():
        queryset_list_bhopal_icsi_val = val

    queryset_list_bhopal_iui = queryset_list_bhopal.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bhopal_iui.items():
        queryset_list_bhopal_iui = val

    #--------------------------------------------------------------------------
    queryset_list_bhubaneswar = queryset_list_in.filter(clinicCity__iexact='Bhubaneswar')
    my_total_clinic_count_bhubaneswar = queryset_list_bhubaneswar.count()

    queryset_list_bhubaneswar_ivf = queryset_list_bhubaneswar.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_bhubaneswar_ivf.items():
        queryset_list_bhubaneswar_ivf_val = val

    queryset_list_bhubaneswar_egg = queryset_list_bhubaneswar.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_bhubaneswar_egg.items():
        queryset_list_bhubaneswar_egg_val = val

    queryset_list_bhubaneswar_embryo = queryset_list_bhubaneswar.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_bhubaneswar_embryo.items():
        queryset_list_bhubaneswar_embryo_val = val

    queryset_list_bhubaneswar_sperm = queryset_list_bhubaneswar.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_bhubaneswar_sperm.items():
        queryset_list_bhubaneswar_sperm_val = val

    queryset_list_bhubaneswar_icsi = queryset_list_bhubaneswar.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_bhubaneswar_icsi.items():
        queryset_list_bhubaneswar_icsi_val = val

    queryset_list_bhubaneswar_iui = queryset_list_bhubaneswar.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_bhubaneswar_iui.items():
        queryset_list_bhubaneswar_iui = val

    #--------------------------------------------------------------------------
    queryset_list_dehradun = queryset_list_in.filter(clinicCity__iexact='Dehradun')
    my_total_clinic_count_dehradun = queryset_list_dehradun.count()

    queryset_list_dehradun_ivf = queryset_list_dehradun.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_dehradun_ivf.items():
        queryset_list_dehradun_ivf_val = val

    queryset_list_dehradun_egg = queryset_list_dehradun.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_dehradun_egg.items():
        queryset_list_dehradun_egg_val = val

    queryset_list_dehradun_embryo = queryset_list_dehradun.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_dehradun_embryo.items():
        queryset_list_dehradun_embryo_val = val

    queryset_list_dehradun_sperm = queryset_list_dehradun.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_dehradun_sperm.items():
        queryset_list_dehradun_sperm_val = val

    queryset_list_dehradun_icsi = queryset_list_dehradun.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_dehradun_icsi.items():
        queryset_list_dehradun_icsi_val = val

    queryset_list_dehradun_iui = queryset_list_dehradun.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_dehradun_iui.items():
        queryset_list_dehradun_iui = val

    #--------------------------------------------------------------------------
    queryset_list_faridabad = queryset_list_in.filter(clinicCity__iexact='Faridabad')
    my_total_clinic_count_faridabad = queryset_list_faridabad.count()

    queryset_list_faridabad_ivf = queryset_list_faridabad.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_faridabad_ivf.items():
        queryset_list_faridabad_ivf_val = val

    queryset_list_faridabad_egg = queryset_list_faridabad.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_faridabad_egg.items():
        queryset_list_faridabad_egg_val = val

    queryset_list_faridabad_embryo = queryset_list_faridabad.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_faridabad_embryo.items():
        queryset_list_faridabad_embryo_val = val

    queryset_list_faridabad_sperm = queryset_list_faridabad.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_faridabad_sperm.items():
        queryset_list_faridabad_sperm_val = val

    queryset_list_faridabad_icsi = queryset_list_faridabad.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_faridabad_icsi.items():
        queryset_list_faridabad_icsi_val = val

    queryset_list_faridabad_iui = queryset_list_faridabad.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_faridabad_iui.items():
        queryset_list_faridabad_iui = val

    #--------------------------------------------------------------------------
    queryset_list_hyderabad = queryset_list_in.filter(clinicCity__iexact='Hyderabad')
    my_total_clinic_count_hyderabad = queryset_list_hyderabad.count()

    queryset_list_hyderabad_ivf = queryset_list_hyderabad.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_hyderabad_ivf.items():
        queryset_list_hyderabad_ivf_val = val

    queryset_list_hyderabad_egg = queryset_list_hyderabad.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_hyderabad_egg.items():
        queryset_list_hyderabad_egg_val = val

    queryset_list_hyderabad_embryo = queryset_list_hyderabad.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_hyderabad_embryo.items():
        queryset_list_hyderabad_embryo_val = val

    queryset_list_hyderabad_sperm = queryset_list_hyderabad.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_hyderabad_sperm.items():
        queryset_list_hyderabad_sperm_val = val

    queryset_list_hyderabad_icsi = queryset_list_hyderabad.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_hyderabad_icsi.items():
        queryset_list_hyderabad_icsi_val = val

    queryset_list_hyderabad_iui = queryset_list_hyderabad.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_hyderabad_iui.items():
        queryset_list_hyderabad_iui = val

    #--------------------------------------------------------------------------
    queryset_list_chandigarh = queryset_list_in.filter(clinicCity__iexact='Chandigarh')
    my_total_clinic_count_chandigarh = queryset_list_chandigarh.count()

    queryset_list_chandigarh_ivf = queryset_list_chandigarh.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_chandigarh_ivf.items():
        queryset_list_chandigarh_ivf_val = val

    queryset_list_chandigarh_egg = queryset_list_chandigarh.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_chandigarh_egg.items():
        queryset_list_chandigarh_egg_val = val

    queryset_list_chandigarh_embryo = queryset_list_chandigarh.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_chandigarh_embryo.items():
        queryset_list_chandigarh_embryo_val = val

    queryset_list_chandigarh_sperm = queryset_list_chandigarh.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_chandigarh_sperm.items():
        queryset_list_chandigarh_sperm_val = val

    queryset_list_chandigarh_icsi = queryset_list_chandigarh.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_chandigarh_icsi.items():
        queryset_list_chandigarh_icsi_val = val

    queryset_list_chandigarh_iui = queryset_list_chandigarh.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_chandigarh_iui.items():
        queryset_list_chandigarh_iui = val

    #--------------------------------------------------------------------------
    queryset_list_chennai = queryset_list_in.filter(clinicCity__iexact='Chennai')
    my_total_clinic_count_chennai = queryset_list_chennai.count()

    queryset_list_chennai_ivf = queryset_list_chennai.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_chennai_ivf.items():
        queryset_list_chennai_ivf_val = val

    queryset_list_chennai_egg = queryset_list_chennai.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_chennai_egg.items():
        queryset_list_chennai_egg_val = val

    queryset_list_chennai_embryo = queryset_list_chennai.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_chennai_embryo.items():
        queryset_list_chennai_embryo_val = val

    queryset_list_chennai_sperm = queryset_list_chennai.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_chennai_sperm.items():
        queryset_list_chennai_sperm_val = val

    queryset_list_chennai_icsi = queryset_list_chennai.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_chennai_icsi.items():
        queryset_list_chennai_icsi_val = val

    queryset_list_chennai_iui = queryset_list_chennai.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_chennai_iui.items():
        queryset_list_chennai_iui = val

    #--------------------------------------------------------------------------
    queryset_list_indore = queryset_list_in.filter(clinicCity__iexact='Indore')
    my_total_clinic_count_indore = queryset_list_indore.count()

    queryset_list_indore_ivf = queryset_list_indore.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_indore_ivf.items():
        queryset_list_indore_ivf_val = val

    queryset_list_indore_egg = queryset_list_indore.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_indore_egg.items():
        queryset_list_indore_egg_val = val

    queryset_list_indore_embryo = queryset_list_indore.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_indore_embryo.items():
        queryset_list_indore_embryo_val = val

    queryset_list_indore_sperm = queryset_list_indore.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_indore_sperm.items():
        queryset_list_indore_sperm_val = val

    queryset_list_indore_icsi = queryset_list_indore.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_indore_icsi.items():
        queryset_list_indore_icsi_val = val

    queryset_list_indore_iui = queryset_list_indore.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_indore_iui.items():
        queryset_list_indore_iui = val

    #--------------------------------------------------------------------------
    queryset_list_jaipur = queryset_list_in.filter(clinicCity__iexact='Jaipur')
    my_total_clinic_count_jaipur = queryset_list_jaipur.count()

    queryset_list_jaipur_ivf = queryset_list_jaipur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_jaipur_ivf.items():
        queryset_list_jaipur_ivf_val = val

    queryset_list_jaipur_egg = queryset_list_jaipur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_jaipur_egg.items():
        queryset_list_jaipur_egg_val = val

    queryset_list_jaipur_embryo = queryset_list_jaipur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_jaipur_embryo.items():
        queryset_list_jaipur_embryo_val = val

    queryset_list_jaipur_sperm = queryset_list_jaipur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_jaipur_sperm.items():
        queryset_list_jaipur_sperm_val = val

    queryset_list_jaipur_icsi = queryset_list_jaipur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_jaipur_icsi.items():
        queryset_list_jaipur_icsi_val = val

    queryset_list_jaipur_iui = queryset_list_jaipur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_jaipur_iui.items():
        queryset_list_jaipur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_jamshedpur = queryset_list_in.filter(clinicCity__iexact='Jamshedpur')
    my_total_clinic_count_jamshedpur = queryset_list_jamshedpur.count()

    queryset_list_jamshedpur_ivf = queryset_list_jamshedpur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_jamshedpur_ivf.items():
        queryset_list_jamshedpur_ivf_val = val

    queryset_list_jamshedpur_egg = queryset_list_jamshedpur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_jamshedpur_egg.items():
        queryset_list_jamshedpur_egg_val = val

    queryset_list_jamshedpur_embryo = queryset_list_jamshedpur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_jamshedpur_embryo.items():
        queryset_list_jamshedpur_embryo_val = val

    queryset_list_jamshedpur_sperm = queryset_list_jamshedpur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_jamshedpur_sperm.items():
        queryset_list_jamshedpur_sperm_val = val

    queryset_list_jamshedpur_icsi = queryset_list_jamshedpur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_jamshedpur_icsi.items():
        queryset_list_jamshedpur_icsi_val = val

    queryset_list_jamshedpur_iui = queryset_list_jamshedpur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_jamshedpur_iui.items():
        queryset_list_jamshedpur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_kanpur = queryset_list_in.filter(clinicCity__iexact='Kanpur')
    my_total_clinic_count_kanpur = queryset_list_kanpur.count()

    queryset_list_kanpur_ivf = queryset_list_kanpur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_kanpur_ivf.items():
        queryset_list_kanpur_ivf_val = val

    queryset_list_kanpur_egg = queryset_list_kanpur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kanpur_egg.items():
        queryset_list_kanpur_egg_val = val

    queryset_list_kanpur_embryo = queryset_list_kanpur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kanpur_embryo.items():
        queryset_list_kanpur_embryo_val = val

    queryset_list_kanpur_sperm = queryset_list_kanpur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kanpur_sperm.items():
        queryset_list_kanpur_sperm_val = val

    queryset_list_kanpur_icsi = queryset_list_kanpur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kanpur_icsi.items():
        queryset_list_kanpur_icsi_val = val

    queryset_list_kanpur_iui = queryset_list_kanpur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kanpur_iui.items():
        queryset_list_kanpur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_kochi = queryset_list_in.filter(clinicCity__iexact='Kochi')
    my_total_clinic_count_kochi = queryset_list_kochi.count()

    queryset_list_kochi_ivf = queryset_list_kochi.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_kochi_ivf.items():
        queryset_list_kochi_ivf_val = val

    queryset_list_kochi_egg = queryset_list_kochi.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kochi_egg.items():
        queryset_list_kochi_egg_val = val

    queryset_list_kochi_embryo = queryset_list_kochi.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kochi_embryo.items():
        queryset_list_kochi_embryo_val = val

    queryset_list_kochi_sperm = queryset_list_kochi.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kochi_sperm.items():
        queryset_list_kochi_sperm_val = val

    queryset_list_kochi_icsi = queryset_list_kochi.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kochi_icsi.items():
        queryset_list_kochi_icsi_val = val

    queryset_list_kochi_iui = queryset_list_kochi.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kochi_iui.items():
        queryset_list_kochi_iui = val

    #--------------------------------------------------------------------------
    queryset_list_kolkata = queryset_list_in.filter(clinicCity__iexact='Kolkata')
    my_total_clinic_count_kolkata = queryset_list_kolkata.count()

    queryset_list_kolkata_ivf = queryset_list_kolkata.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_kolkata_ivf.items():
        queryset_list_kolkata_ivf_val = val

    queryset_list_kolkata_egg = queryset_list_kolkata.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_kolkata_egg.items():
        queryset_list_kolkata_egg_val = val

    queryset_list_kolkata_embryo = queryset_list_kolkata.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_kolkata_embryo.items():
        queryset_list_kolkata_embryo_val = val

    queryset_list_kolkata_sperm = queryset_list_kolkata.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_kolkata_sperm.items():
        queryset_list_kolkata_sperm_val = val

    queryset_list_kolkata_icsi = queryset_list_kolkata.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_kolkata_icsi.items():
        queryset_list_kolkata_icsi_val = val

    queryset_list_kolkata_iui = queryset_list_kolkata.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_kolkata_iui.items():
        queryset_list_kolkata_iui = val

    #--------------------------------------------------------------------------
    queryset_list_lucknow = queryset_list_in.filter(clinicCity__iexact='Lucknow')
    my_total_clinic_count_lucknow = queryset_list_lucknow.count()

    queryset_list_lucknow_ivf = queryset_list_lucknow.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_lucknow_ivf.items():
        queryset_list_lucknow_ivf_val = val

    queryset_list_lucknow_egg = queryset_list_lucknow.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_lucknow_egg.items():
        queryset_list_lucknow_egg_val = val

    queryset_list_lucknow_embryo = queryset_list_lucknow.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_lucknow_embryo.items():
        queryset_list_lucknow_embryo_val = val

    queryset_list_lucknow_sperm = queryset_list_lucknow.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_lucknow_sperm.items():
        queryset_list_lucknow_sperm_val = val

    queryset_list_lucknow_icsi = queryset_list_lucknow.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_lucknow_icsi.items():
        queryset_list_lucknow_icsi_val = val

    queryset_list_lucknow_iui = queryset_list_lucknow.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_lucknow_iui.items():
        queryset_list_lucknow_iui = val

    #--------------------------------------------------------------------------
    queryset_list_mumbai = queryset_list_in.filter(clinicCity__iexact='Mumbai')
    my_total_clinic_count_mumbai = queryset_list_mumbai.count()

    queryset_list_mumbai_ivf = queryset_list_mumbai.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_mumbai_ivf.items():
        queryset_list_mumbai_ivf_val = val

    queryset_list_mumbai_egg = queryset_list_mumbai.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_mumbai_egg.items():
        queryset_list_mumbai_egg_val = val

    queryset_list_mumbai_embryo = queryset_list_mumbai.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_mumbai_embryo.items():
        queryset_list_mumbai_embryo_val = val

    queryset_list_mumbai_sperm = queryset_list_mumbai.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_mumbai_sperm.items():
        queryset_list_mumbai_sperm_val = val

    queryset_list_mumbai_icsi = queryset_list_mumbai.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_mumbai_icsi.items():
        queryset_list_mumbai_icsi_val = val

    queryset_list_mumbai_iui = queryset_list_mumbai.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_mumbai_iui.items():
        queryset_list_mumbai_iui = val

    #--------------------------------------------------------------------------
    queryset_list_nagpur = queryset_list_in.filter(clinicCity__iexact='Nagpur')
    my_total_clinic_count_nagpur = queryset_list_nagpur.count()

    queryset_list_nagpur_ivf = queryset_list_nagpur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nagpur_ivf.items():
        queryset_list_nagpur_ivf_val = val

    queryset_list_nagpur_egg = queryset_list_nagpur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nagpur_egg.items():
        queryset_list_nagpur_egg_val = val

    queryset_list_nagpur_embryo = queryset_list_nagpur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nagpur_embryo.items():
        queryset_list_nagpur_embryo_val = val

    queryset_list_nagpur_sperm = queryset_list_nagpur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nagpur_sperm.items():
        queryset_list_nagpur_sperm_val = val

    queryset_list_nagpur_icsi = queryset_list_nagpur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nagpur_icsi.items():
        queryset_list_nagpur_icsi_val = val

    queryset_list_nagpur_iui = queryset_list_nagpur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nagpur_iui.items():
        queryset_list_nagpur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_patna = queryset_list_in.filter(clinicCity__iexact='Patna')
    my_total_clinic_count_patna = queryset_list_patna.count()

    queryset_list_patna_ivf = queryset_list_patna.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_patna_ivf.items():
        queryset_list_patna_ivf_val = val

    queryset_list_patna_egg = queryset_list_patna.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_patna_egg.items():
        queryset_list_patna_egg_val = val

    queryset_list_patna_embryo = queryset_list_patna.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_patna_embryo.items():
        queryset_list_patna_embryo_val = val

    queryset_list_patna_sperm = queryset_list_patna.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_patna_sperm.items():
        queryset_list_patna_sperm_val = val

    queryset_list_patna_icsi = queryset_list_patna.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_patna_icsi.items():
        queryset_list_patna_icsi_val = val

    queryset_list_patna_iui = queryset_list_patna.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_patna_iui.items():
        queryset_list_patna_iui = val

    #--------------------------------------------------------------------------
    queryset_list_raipur = queryset_list_in.filter(clinicCity__iexact='Raipur')
    my_total_clinic_count_raipur = queryset_list_raipur.count()

    queryset_list_raipur_ivf = queryset_list_raipur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_raipur_ivf.items():
        queryset_list_raipur_ivf_val = val

    queryset_list_raipur_egg = queryset_list_raipur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_raipur_egg.items():
        queryset_list_raipur_egg_val = val

    queryset_list_raipur_embryo = queryset_list_raipur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_raipur_embryo.items():
        queryset_list_raipur_embryo_val = val

    queryset_list_raipur_sperm = queryset_list_raipur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_raipur_sperm.items():
        queryset_list_raipur_sperm_val = val

    queryset_list_raipur_icsi = queryset_list_raipur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_raipur_icsi.items():
        queryset_list_raipur_icsi_val = val

    queryset_list_raipur_iui = queryset_list_raipur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_raipur_iui.items():
        queryset_list_raipur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_trivandrum = queryset_list_in.filter(clinicCity__iexact='Trivandrum')
    my_total_clinic_count_trivandrum = queryset_list_trivandrum.count()

    queryset_list_trivandrum_ivf = queryset_list_trivandrum.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_trivandrum_ivf.items():
        queryset_list_trivandrum_ivf_val = val

    queryset_list_trivandrum_egg = queryset_list_trivandrum.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_trivandrum_egg.items():
        queryset_list_trivandrum_egg_val = val

    queryset_list_trivandrum_embryo = queryset_list_trivandrum.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_trivandrum_embryo.items():
        queryset_list_trivandrum_embryo_val = val

    queryset_list_trivandrum_sperm = queryset_list_trivandrum.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_trivandrum_sperm.items():
        queryset_list_trivandrum_sperm_val = val

    queryset_list_trivandrum_icsi = queryset_list_trivandrum.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_trivandrum_icsi.items():
        queryset_list_trivandrum_icsi_val = val

    queryset_list_trivandrum_iui = queryset_list_trivandrum.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_trivandrum_iui.items():
        queryset_list_trivandrum_iui = val

    #--------------------------------------------------------------------------
    queryset_list_ludhiana = queryset_list_in.filter(clinicCity__iexact='Ludhiana')
    my_total_clinic_count_ludhiana = queryset_list_ludhiana.count()

    queryset_list_ludhiana_ivf = queryset_list_ludhiana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_ludhiana_ivf.items():
        queryset_list_ludhiana_ivf_val = val

    queryset_list_ludhiana_egg = queryset_list_ludhiana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_ludhiana_egg.items():
        queryset_list_ludhiana_egg_val = val

    queryset_list_ludhiana_embryo = queryset_list_ludhiana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_ludhiana_embryo.items():
        queryset_list_ludhiana_embryo_val = val

    queryset_list_ludhiana_sperm = queryset_list_ludhiana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_ludhiana_sperm.items():
        queryset_list_ludhiana_sperm_val = val

    queryset_list_ludhiana_icsi = queryset_list_ludhiana.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_ludhiana_icsi.items():
        queryset_list_ludhiana_icsi_val = val

    queryset_list_ludhiana_iui = queryset_list_ludhiana.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_ludhiana_iui.items():
        queryset_list_ludhiana_iui = val

    #--------------------------------------------------------------------------
    queryset_list_visakhapatnam = queryset_list_in.filter(clinicCity__iexact='Visakhapatnam')
    my_total_clinic_count_visakhapatnam = queryset_list_visakhapatnam.count()

    queryset_list_visakhapatnam_ivf = queryset_list_visakhapatnam.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_visakhapatnam_ivf.items():
        queryset_list_visakhapatnam_ivf_val = val

    queryset_list_visakhapatnam_egg = queryset_list_visakhapatnam.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_visakhapatnam_egg.items():
        queryset_list_visakhapatnam_egg_val = val

    queryset_list_visakhapatnam_embryo = queryset_list_visakhapatnam.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_visakhapatnam_embryo.items():
        queryset_list_visakhapatnam_embryo_val = val

    queryset_list_visakhapatnam_sperm = queryset_list_visakhapatnam.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_visakhapatnam_sperm.items():
        queryset_list_visakhapatnam_sperm_val = val

    queryset_list_visakhapatnam_icsi = queryset_list_visakhapatnam.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_visakhapatnam_icsi.items():
        queryset_list_visakhapatnam_icsi_val = val

    queryset_list_visakhapatnam_iui = queryset_list_visakhapatnam.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_visakhapatnam_iui.items():
        queryset_list_visakhapatnam_iui = val

    #--------------------------------------------------------------------------
    queryset_list_vijayawada = queryset_list_in.filter(clinicCity__iexact='Vijayawada')
    my_total_clinic_count_vijayawada = queryset_list_vijayawada.count()

    queryset_list_vijayawada_ivf = queryset_list_vijayawada.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_vijayawada_ivf.items():
        queryset_list_vijayawada_ivf_val = val

    queryset_list_vijayawada_egg = queryset_list_vijayawada.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_vijayawada_egg.items():
        queryset_list_vijayawada_egg_val = val

    queryset_list_vijayawada_embryo = queryset_list_vijayawada.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_vijayawada_embryo.items():
        queryset_list_vijayawada_embryo_val = val

    queryset_list_vijayawada_sperm = queryset_list_vijayawada.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_vijayawada_sperm.items():
        queryset_list_vijayawada_sperm_val = val

    queryset_list_vijayawada_icsi = queryset_list_vijayawada.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_vijayawada_icsi.items():
        queryset_list_vijayawada_icsi_val = val

    queryset_list_vijayawada_iui = queryset_list_vijayawada.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_vijayawada_iui.items():
        queryset_list_vijayawada_iui = val

    #--------------------------------------------------------------------------
    queryset_list_newdelhi = queryset_list_in.filter(clinicCity__iexact='New Delhi')
    my_total_clinic_count_newdelhi = queryset_list_newdelhi.count()

    queryset_list_newdelhi_ivf = queryset_list_newdelhi.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_newdelhi_ivf.items():
        queryset_list_newdelhi_ivf_val = val

    queryset_list_newdelhi_egg = queryset_list_newdelhi.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_newdelhi_egg.items():
        queryset_list_newdelhi_egg_val = val

    queryset_list_newdelhi_embryo = queryset_list_newdelhi.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_newdelhi_embryo.items():
        queryset_list_newdelhi_embryo_val = val

    queryset_list_newdelhi_sperm = queryset_list_newdelhi.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_newdelhi_sperm.items():
        queryset_list_newdelhi_sperm_val = val

    queryset_list_newdelhi_icsi = queryset_list_newdelhi.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_newdelhi_icsi.items():
        queryset_list_newdelhi_icsi_val = val

    queryset_list_newdelhi_iui = queryset_list_newdelhi.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_newdelhi_iui.items():
        queryset_list_newdelhi_iui = val

    #--------------------------------------------------------------------------
    queryset_list_vadodara = queryset_list_in.filter(clinicCity__iexact='Vadodara')
    my_total_clinic_count_vadodara = queryset_list_vadodara.count()

    queryset_list_vadodara_ivf = queryset_list_vadodara.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_vadodara_ivf.items():
        queryset_list_vadodara_ivf_val = val

    queryset_list_vadodara_egg = queryset_list_vadodara.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_vadodara_egg.items():
        queryset_list_vadodara_egg_val = val

    queryset_list_vadodara_embryo = queryset_list_vadodara.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_vadodara_embryo.items():
        queryset_list_vadodara_embryo_val = val

    queryset_list_vadodara_sperm = queryset_list_vadodara.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_vadodara_sperm.items():
        queryset_list_vadodara_sperm_val = val

    queryset_list_vadodara_icsi = queryset_list_vadodara.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_vadodara_icsi.items():
        queryset_list_vadodara_icsi_val = val

    queryset_list_vadodara_iui = queryset_list_vadodara.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_vadodara_iui.items():
        queryset_list_vadodara_iui = val

    #--------------------------------------------------------------------------
    queryset_list_gurugram = queryset_list_in.filter(clinicCity__iexact='Gurugram')
    my_total_clinic_count_gurugram = queryset_list_gurugram.count()

    queryset_list_gurugram_ivf = queryset_list_gurugram.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_gurugram_ivf.items():
        queryset_list_gurugram_ivf_val = val

    queryset_list_gurugram_egg = queryset_list_gurugram.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_gurugram_egg.items():
        queryset_list_gurugram_egg_val = val

    queryset_list_gurugram_embryo = queryset_list_gurugram.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_gurugram_embryo.items():
        queryset_list_gurugram_embryo_val = val

    queryset_list_gurugram_sperm = queryset_list_gurugram.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_gurugram_sperm.items():
        queryset_list_gurugram_sperm_val = val

    queryset_list_gurugram_icsi = queryset_list_gurugram.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_gurugram_icsi.items():
        queryset_list_gurugram_icsi_val = val

    queryset_list_gurugram_iui = queryset_list_gurugram.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_gurugram_iui.items():
        queryset_list_gurugram_iui = val

    #--------------------------------------------------------------------------
    queryset_list_rohtak = queryset_list_in.filter(clinicCity__iexact='Rohtak')
    my_total_clinic_count_rohtak = queryset_list_rohtak.count()

    queryset_list_rohtak_ivf = queryset_list_rohtak.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_rohtak_ivf.items():
        queryset_list_rohtak_ivf_val = val

    queryset_list_rohtak_egg = queryset_list_rohtak.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_rohtak_egg.items():
        queryset_list_rohtak_egg_val = val

    queryset_list_rohtak_embryo = queryset_list_rohtak.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_rohtak_embryo.items():
        queryset_list_rohtak_embryo_val = val

    queryset_list_rohtak_sperm = queryset_list_rohtak.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_rohtak_sperm.items():
        queryset_list_rohtak_sperm_val = val

    queryset_list_rohtak_icsi = queryset_list_rohtak.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_rohtak_icsi.items():
        queryset_list_rohtak_icsi_val = val

    queryset_list_rohtak_iui = queryset_list_rohtak.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_rohtak_iui.items():
        queryset_list_rohtak_iui = val

    #--------------------------------------------------------------------------
    queryset_list_jammu = queryset_list_in.filter(clinicCity__iexact='Jammu')
    my_total_clinic_count_jammu = queryset_list_jammu.count()

    queryset_list_jammu_ivf = queryset_list_jammu.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_jammu_ivf.items():
        queryset_list_jammu_ivf_val = val

    queryset_list_jammu_egg = queryset_list_jammu.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_jammu_egg.items():
        queryset_list_jammu_egg_val = val

    queryset_list_jammu_embryo = queryset_list_jammu.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_jammu_embryo.items():
        queryset_list_jammu_embryo_val = val

    queryset_list_jammu_sperm = queryset_list_jammu.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_jammu_sperm.items():
        queryset_list_jammu_sperm_val = val

    queryset_list_jammu_icsi = queryset_list_jammu.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_jammu_icsi.items():
        queryset_list_jammu_icsi_val = val

    queryset_list_jammu_iui = queryset_list_jammu.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_jammu_iui.items():
        queryset_list_jammu_iui = val

    #--------------------------------------------------------------------------
    queryset_list_ranchi = queryset_list_in.filter(clinicCity__iexact='Ranchi')
    my_total_clinic_count_ranchi = queryset_list_ranchi.count()

    queryset_list_ranchi_ivf = queryset_list_ranchi.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_ranchi_ivf.items():
        queryset_list_ranchi_ivf_val = val

    queryset_list_ranchi_egg = queryset_list_ranchi.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_ranchi_egg.items():
        queryset_list_ranchi_egg_val = val

    queryset_list_ranchi_embryo = queryset_list_ranchi.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_ranchi_embryo.items():
        queryset_list_ranchi_embryo_val = val

    queryset_list_ranchi_sperm = queryset_list_ranchi.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_ranchi_sperm.items():
        queryset_list_ranchi_sperm_val = val

    queryset_list_ranchi_icsi = queryset_list_ranchi.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_ranchi_icsi.items():
        queryset_list_ranchi_icsi_val = val

    queryset_list_ranchi_iui = queryset_list_ranchi.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_ranchi_iui.items():
        queryset_list_ranchi_iui = val

    #--------------------------------------------------------------------------
    queryset_list_pune = queryset_list_in.filter(clinicCity__iexact='Pune')
    my_total_clinic_count_pune = queryset_list_pune.count()

    queryset_list_pune_ivf = queryset_list_pune.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_pune_ivf.items():
        queryset_list_pune_ivf_val = val

    queryset_list_pune_egg = queryset_list_pune.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_pune_egg.items():
        queryset_list_pune_egg_val = val

    queryset_list_pune_embryo = queryset_list_pune.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_pune_embryo.items():
        queryset_list_pune_embryo_val = val

    queryset_list_pune_sperm = queryset_list_pune.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_pune_sperm.items():
        queryset_list_pune_sperm_val = val

    queryset_list_pune_icsi = queryset_list_pune.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_pune_icsi.items():
        queryset_list_pune_icsi_val = val

    queryset_list_pune_iui = queryset_list_pune.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_pune_iui.items():
        queryset_list_pune_iui = val

    #--------------------------------------------------------------------------
    queryset_list_gwalior = queryset_list_in.filter(clinicCity__iexact='Gwalior')
    my_total_clinic_count_gwalior = queryset_list_gwalior.count()

    queryset_list_gwalior_ivf = queryset_list_gwalior.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_gwalior_ivf.items():
        queryset_list_gwalior_ivf_val = val

    queryset_list_gwalior_egg = queryset_list_gwalior.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_gwalior_egg.items():
        queryset_list_gwalior_egg_val = val

    queryset_list_gwalior_embryo = queryset_list_gwalior.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_gwalior_embryo.items():
        queryset_list_gwalior_embryo_val = val

    queryset_list_gwalior_sperm = queryset_list_gwalior.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_gwalior_sperm.items():
        queryset_list_gwalior_sperm_val = val

    queryset_list_gwalior_icsi = queryset_list_gwalior.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_gwalior_icsi.items():
        queryset_list_gwalior_icsi_val = val

    queryset_list_gwalior_iui = queryset_list_gwalior.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_gwalior_iui.items():
        queryset_list_gwalior_iui = val

    #--------------------------------------------------------------------------
    queryset_list_warangal = queryset_list_in.filter(clinicCity__iexact='Warangal')
    my_total_clinic_count_warangal = queryset_list_warangal.count()

    queryset_list_warangal_ivf = queryset_list_warangal.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_warangal_ivf.items():
        queryset_list_warangal_ivf_val = val

    queryset_list_warangal_egg = queryset_list_warangal.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_warangal_egg.items():
        queryset_list_warangal_egg_val = val

    queryset_list_warangal_embryo = queryset_list_warangal.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_warangal_embryo.items():
        queryset_list_warangal_embryo_val = val

    queryset_list_warangal_sperm = queryset_list_warangal.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_warangal_sperm.items():
        queryset_list_warangal_sperm_val = val

    queryset_list_warangal_icsi = queryset_list_warangal.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_warangal_icsi.items():
        queryset_list_warangal_icsi_val = val

    queryset_list_warangal_iui = queryset_list_warangal.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_warangal_iui.items():
        queryset_list_warangal_iui = val

    #--------------------------------------------------------------------------
    queryset_list_gachibowli = queryset_list_in.filter(clinicCity__iexact='Gachibowli')
    my_total_clinic_count_gachibowli = queryset_list_gachibowli.count()

    queryset_list_gachibowli_ivf = queryset_list_gachibowli.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_gachibowli_ivf.items():
        queryset_list_gachibowli_ivf_val = val

    queryset_list_gachibowli_egg = queryset_list_gachibowli.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_gachibowli_egg.items():
        queryset_list_gachibowli_egg_val = val

    queryset_list_gachibowli_embryo = queryset_list_gachibowli.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_gachibowli_embryo.items():
        queryset_list_gachibowli_embryo_val = val

    queryset_list_gachibowli_sperm = queryset_list_gachibowli.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_gachibowli_sperm.items():
        queryset_list_gachibowli_sperm_val = val

    queryset_list_gachibowli_icsi = queryset_list_gachibowli.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_gachibowli_icsi.items():
        queryset_list_gachibowli_icsi_val = val

    queryset_list_gachibowli_iui = queryset_list_gachibowli.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_gachibowli_iui.items():
        queryset_list_gachibowli_iui = val

    #--------------------------------------------------------------------------
    queryset_list_madhapur = queryset_list_in.filter(clinicCity__iexact='Madhapur')
    my_total_clinic_count_madhapur = queryset_list_madhapur.count()

    queryset_list_madhapur_ivf = queryset_list_madhapur.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_madhapur_ivf.items():
        queryset_list_madhapur_ivf_val = val

    queryset_list_madhapur_egg = queryset_list_madhapur.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_madhapur_egg.items():
        queryset_list_madhapur_egg_val = val

    queryset_list_madhapur_embryo = queryset_list_madhapur.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_madhapur_embryo.items():
        queryset_list_madhapur_embryo_val = val

    queryset_list_madhapur_sperm = queryset_list_madhapur.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_madhapur_sperm.items():
        queryset_list_madhapur_sperm_val = val

    queryset_list_madhapur_icsi = queryset_list_madhapur.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_madhapur_icsi.items():
        queryset_list_madhapur_icsi_val = val

    queryset_list_madhapur_iui = queryset_list_madhapur.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_madhapur_iui.items():
        queryset_list_madhapur_iui = val

    #--------------------------------------------------------------------------
    queryset_list_noida = queryset_list_in.filter(clinicCity__iexact='Noida')
    my_total_clinic_count_noida = queryset_list_noida.count()

    queryset_list_noida_ivf = queryset_list_noida.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_noida_ivf.items():
        queryset_list_noida_ivf_val = val

    queryset_list_noida_egg = queryset_list_noida.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_noida_egg.items():
        queryset_list_noida_egg_val = val

    queryset_list_noida_embryo = queryset_list_noida.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_noida_embryo.items():
        queryset_list_noida_embryo_val = val

    queryset_list_noida_sperm = queryset_list_noida.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_noida_sperm.items():
        queryset_list_noida_sperm_val = val

    queryset_list_noida_icsi = queryset_list_noida.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_noida_icsi.items():
        queryset_list_noida_icsi_val = val

    queryset_list_noida_iui = queryset_list_noida.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_noida_iui.items():
        queryset_list_noida_iui = val

    #--------------------------------------------------------------------------
    queryset_list_meerut = queryset_list_in.filter(clinicCity__iexact='Meerut')
    my_total_clinic_count_meerut = queryset_list_meerut.count()

    queryset_list_meerut_ivf = queryset_list_meerut.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_meerut_ivf.items():
        queryset_list_meerut_ivf_val = val

    queryset_list_meerut_egg = queryset_list_meerut.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_meerut_egg.items():
        queryset_list_meerut_egg_val = val

    queryset_list_meerut_embryo = queryset_list_meerut.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_meerut_embryo.items():
        queryset_list_meerut_embryo_val = val

    queryset_list_meerut_sperm = queryset_list_meerut.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_meerut_sperm.items():
        queryset_list_meerut_sperm_val = val

    queryset_list_meerut_icsi = queryset_list_meerut.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_meerut_icsi.items():
        queryset_list_meerut_icsi_val = val

    queryset_list_meerut_iui = queryset_list_meerut.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_meerut_iui.items():
        queryset_list_meerut_iui = val

    #--------------------------------------------------------------------------
    queryset_list_haldwani = queryset_list_in.filter(clinicCity__iexact='Haldwani')
    my_total_clinic_count_haldwani = queryset_list_haldwani.count()

    queryset_list_haldwani_ivf = queryset_list_haldwani.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_haldwani_ivf.items():
        queryset_list_haldwani_ivf_val = val

    queryset_list_haldwani_egg = queryset_list_haldwani.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_haldwani_egg.items():
        queryset_list_haldwani_egg_val = val

    queryset_list_haldwani_embryo = queryset_list_haldwani.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_haldwani_embryo.items():
        queryset_list_haldwani_embryo_val = val

    queryset_list_haldwani_sperm = queryset_list_haldwani.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_haldwani_sperm.items():
        queryset_list_haldwani_sperm_val = val

    queryset_list_haldwani_icsi = queryset_list_haldwani.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_haldwani_icsi.items():
        queryset_list_haldwani_icsi_val = val

    queryset_list_haldwani_iui = queryset_list_haldwani.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_haldwani_iui.items():
        queryset_list_haldwani_iui = val

    context = {
        'my_total_clinic_count_amdavad': my_total_clinic_count_amdavad,
        'queryset_list_amdavad_ivf_val': queryset_list_amdavad_ivf_val,
        'queryset_list_amdavad_egg_val': queryset_list_amdavad_egg_val,
        'queryset_list_amdavad_embryo_val': queryset_list_amdavad_embryo_val,
        'queryset_list_amdavad_sperm_val': queryset_list_amdavad_sperm_val,
        'queryset_list_amdavad_icsi_val': queryset_list_amdavad_icsi_val,
        'queryset_list_amdavad_iui': queryset_list_amdavad_iui,

        'my_total_clinic_count_bangalore': my_total_clinic_count_bangalore,
        'queryset_list_bangalore_ivf_val': queryset_list_bangalore_ivf_val,
        'queryset_list_bangalore_egg_val': queryset_list_bangalore_egg_val,
        'queryset_list_bangalore_embryo_val': queryset_list_bangalore_embryo_val,
        'queryset_list_bangalore_sperm_val': queryset_list_bangalore_sperm_val,
        'queryset_list_bangalore_icsi_val': queryset_list_bangalore_icsi_val,
        'queryset_list_bangalore_iui': queryset_list_bangalore_iui,

        'my_total_clinic_count_bhopal': my_total_clinic_count_bhopal,
        'queryset_list_bhopal_ivf_val': queryset_list_bhopal_ivf_val,
        'queryset_list_bhopal_egg_val': queryset_list_bhopal_egg_val,
        'queryset_list_bhopal_embryo_val': queryset_list_bhopal_embryo_val,
        'queryset_list_bhopal_sperm_val': queryset_list_bhopal_sperm_val,
        'queryset_list_bhopal_icsi_val': queryset_list_bhopal_icsi_val,
        'queryset_list_bhopal_iui': queryset_list_bhopal_iui,

        'my_total_clinic_count_bhubaneswar': my_total_clinic_count_bhubaneswar,
        'queryset_list_bhubaneswar_ivf_val': queryset_list_bhubaneswar_ivf_val,
        'queryset_list_bhubaneswar_egg_val': queryset_list_bhubaneswar_egg_val,
        'queryset_list_bhubaneswar_embryo_val': queryset_list_bhubaneswar_embryo_val,
        'queryset_list_bhubaneswar_sperm_val': queryset_list_bhubaneswar_sperm_val,
        'queryset_list_bhubaneswar_icsi_val': queryset_list_bhubaneswar_icsi_val,
        'queryset_list_bhubaneswar_iui': queryset_list_bhubaneswar_iui,

        'my_total_clinic_count_dehradun': my_total_clinic_count_dehradun,
        'queryset_list_dehradun_ivf_val': queryset_list_dehradun_ivf_val,
        'queryset_list_dehradun_egg_val': queryset_list_dehradun_egg_val,
        'queryset_list_dehradun_embryo_val': queryset_list_dehradun_embryo_val,
        'queryset_list_dehradun_sperm_val': queryset_list_dehradun_sperm_val,
        'queryset_list_dehradun_icsi_val': queryset_list_dehradun_icsi_val,
        'queryset_list_dehradun_iui': queryset_list_dehradun_iui,

        'my_total_clinic_count_faridabad': my_total_clinic_count_faridabad,
        'queryset_list_faridabad_ivf_val': queryset_list_faridabad_ivf_val,
        'queryset_list_faridabad_egg_val': queryset_list_faridabad_egg_val,
        'queryset_list_faridabad_embryo_val': queryset_list_faridabad_embryo_val,
        'queryset_list_faridabad_sperm_val': queryset_list_faridabad_sperm_val,
        'queryset_list_faridabad_icsi_val': queryset_list_faridabad_icsi_val,
        'queryset_list_faridabad_iui': queryset_list_faridabad_iui,

        'my_total_clinic_count_hyderabad': my_total_clinic_count_hyderabad,
        'queryset_list_hyderabad_ivf_val': queryset_list_hyderabad_ivf_val,
        'queryset_list_hyderabad_egg_val': queryset_list_hyderabad_egg_val,
        'queryset_list_hyderabad_embryo_val': queryset_list_hyderabad_embryo_val,
        'queryset_list_hyderabad_sperm_val': queryset_list_hyderabad_sperm_val,
        'queryset_list_hyderabad_icsi_val': queryset_list_hyderabad_icsi_val,
        'queryset_list_hyderabad_iui': queryset_list_hyderabad_iui,

        'my_total_clinic_count_chandigarh': my_total_clinic_count_chandigarh,
        'queryset_list_chandigarh_ivf_val': queryset_list_chandigarh_ivf_val,
        'queryset_list_chandigarh_egg_val': queryset_list_chandigarh_egg_val,
        'queryset_list_chandigarh_embryo_val': queryset_list_chandigarh_embryo_val,
        'queryset_list_chandigarh_sperm_val': queryset_list_chandigarh_sperm_val,
        'queryset_list_chandigarh_icsi_val': queryset_list_chandigarh_icsi_val,
        'queryset_list_chandigarh_iui': queryset_list_chandigarh_iui,

        'my_total_clinic_count_chennai': my_total_clinic_count_chennai,
        'queryset_list_chennai_ivf_val': queryset_list_chennai_ivf_val,
        'queryset_list_chennai_egg_val': queryset_list_chennai_egg_val,
        'queryset_list_chennai_embryo_val': queryset_list_chennai_embryo_val,
        'queryset_list_chennai_sperm_val': queryset_list_chennai_sperm_val,
        'queryset_list_chennai_icsi_val': queryset_list_chennai_icsi_val,
        'queryset_list_chennai_iui': queryset_list_chennai_iui,

        'my_total_clinic_count_indore': my_total_clinic_count_indore,
        'queryset_list_indore_ivf_val': queryset_list_indore_ivf_val,
        'queryset_list_indore_egg_val': queryset_list_indore_egg_val,
        'queryset_list_indore_embryo_val': queryset_list_indore_embryo_val,
        'queryset_list_indore_sperm_val': queryset_list_indore_sperm_val,
        'queryset_list_indore_icsi_val': queryset_list_indore_icsi_val,
        'queryset_list_indore_iui': queryset_list_indore_iui,

        'my_total_clinic_count_jaipur': my_total_clinic_count_jaipur,
        'queryset_list_jaipur_ivf_val': queryset_list_jaipur_ivf_val,
        'queryset_list_jaipur_egg_val': queryset_list_jaipur_egg_val,
        'queryset_list_jaipur_embryo_val': queryset_list_jaipur_embryo_val,
        'queryset_list_jaipur_sperm_val': queryset_list_jaipur_sperm_val,
        'queryset_list_jaipur_icsi_val': queryset_list_jaipur_icsi_val,
        'queryset_list_jaipur_iui': queryset_list_jaipur_iui,

        'my_total_clinic_count_jamshedpur': my_total_clinic_count_jamshedpur,
        'queryset_list_jamshedpur_ivf_val': queryset_list_jamshedpur_ivf_val,
        'queryset_list_jamshedpur_egg_val': queryset_list_jamshedpur_egg_val,
        'queryset_list_jamshedpur_embryo_val': queryset_list_jamshedpur_embryo_val,
        'queryset_list_jamshedpur_sperm_val': queryset_list_jamshedpur_sperm_val,
        'queryset_list_jamshedpur_icsi_val': queryset_list_jamshedpur_icsi_val,
        'queryset_list_jamshedpur_iui': queryset_list_jamshedpur_iui,

        'my_total_clinic_count_kanpur': my_total_clinic_count_kanpur,
        'queryset_list_kanpur_ivf_val': queryset_list_kanpur_ivf_val,
        'queryset_list_kanpur_egg_val': queryset_list_kanpur_egg_val,
        'queryset_list_kanpur_embryo_val': queryset_list_kanpur_embryo_val,
        'queryset_list_kanpur_sperm_val': queryset_list_kanpur_sperm_val,
        'queryset_list_kanpur_icsi_val': queryset_list_kanpur_icsi_val,
        'queryset_list_kanpur_iui': queryset_list_kanpur_iui,

        'my_total_clinic_count_kochi': my_total_clinic_count_kochi,
        'queryset_list_kochi_ivf_val': queryset_list_kochi_ivf_val,
        'queryset_list_kochi_egg_val': queryset_list_kochi_egg_val,
        'queryset_list_kochi_embryo_val': queryset_list_kochi_embryo_val,
        'queryset_list_kochi_sperm_val': queryset_list_kochi_sperm_val,
        'queryset_list_kochi_icsi_val': queryset_list_kochi_icsi_val,
        'queryset_list_kochi_iui': queryset_list_kochi_iui,

        'my_total_clinic_count_kolkata': my_total_clinic_count_kolkata,
        'queryset_list_kolkata_ivf_val': queryset_list_kolkata_ivf_val,
        'queryset_list_kolkata_egg_val': queryset_list_kolkata_egg_val,
        'queryset_list_kolkata_embryo_val': queryset_list_kolkata_embryo_val,
        'queryset_list_kolkata_sperm_val': queryset_list_kolkata_sperm_val,
        'queryset_list_kolkata_icsi_val': queryset_list_kolkata_icsi_val,
        'queryset_list_kolkata_iui': queryset_list_kolkata_iui,

        'my_total_clinic_count_lucknow': my_total_clinic_count_lucknow,
        'queryset_list_lucknow_ivf_val': queryset_list_lucknow_ivf_val,
        'queryset_list_lucknow_egg_val': queryset_list_lucknow_egg_val,
        'queryset_list_lucknow_embryo_val': queryset_list_lucknow_embryo_val,
        'queryset_list_lucknow_sperm_val': queryset_list_lucknow_sperm_val,
        'queryset_list_lucknow_icsi_val': queryset_list_lucknow_icsi_val,
        'queryset_list_lucknow_iui': queryset_list_lucknow_iui,

        'my_total_clinic_count_mumbai': my_total_clinic_count_mumbai,
        'queryset_list_mumbai_ivf_val': queryset_list_mumbai_ivf_val,
        'queryset_list_mumbai_egg_val': queryset_list_mumbai_egg_val,
        'queryset_list_mumbai_embryo_val': queryset_list_mumbai_embryo_val,
        'queryset_list_mumbai_sperm_val': queryset_list_mumbai_sperm_val,
        'queryset_list_mumbai_icsi_val': queryset_list_mumbai_icsi_val,
        'queryset_list_mumbai_iui': queryset_list_mumbai_iui,

        'my_total_clinic_count_nagpur': my_total_clinic_count_nagpur,
        'queryset_list_nagpur_ivf_val': queryset_list_nagpur_ivf_val,
        'queryset_list_nagpur_egg_val': queryset_list_nagpur_egg_val,
        'queryset_list_nagpur_embryo_val': queryset_list_nagpur_embryo_val,
        'queryset_list_nagpur_sperm_val': queryset_list_nagpur_sperm_val,
        'queryset_list_nagpur_icsi_val': queryset_list_nagpur_icsi_val,
        'queryset_list_nagpur_iui': queryset_list_nagpur_iui,

        'my_total_clinic_count_patna': my_total_clinic_count_patna,
        'queryset_list_patna_ivf_val': queryset_list_patna_ivf_val,
        'queryset_list_patna_egg_val': queryset_list_patna_egg_val,
        'queryset_list_patna_embryo_val': queryset_list_patna_embryo_val,
        'queryset_list_patna_sperm_val': queryset_list_patna_sperm_val,
        'queryset_list_patna_icsi_val': queryset_list_patna_icsi_val,
        'queryset_list_patna_iui': queryset_list_patna_iui,

        'my_total_clinic_count_raipur': my_total_clinic_count_raipur,
        'queryset_list_raipur_ivf_val': queryset_list_raipur_ivf_val,
        'queryset_list_raipur_egg_val': queryset_list_raipur_egg_val,
        'queryset_list_raipur_embryo_val': queryset_list_raipur_embryo_val,
        'queryset_list_raipur_sperm_val': queryset_list_raipur_sperm_val,
        'queryset_list_raipur_icsi_val': queryset_list_raipur_icsi_val,
        'queryset_list_raipur_iui': queryset_list_raipur_iui,

        'my_total_clinic_count_trivandrum': my_total_clinic_count_trivandrum,
        'queryset_list_trivandrum_ivf_val': queryset_list_trivandrum_ivf_val,
        'queryset_list_trivandrum_egg_val': queryset_list_trivandrum_egg_val,
        'queryset_list_trivandrum_embryo_val': queryset_list_trivandrum_embryo_val,
        'queryset_list_trivandrum_sperm_val': queryset_list_trivandrum_sperm_val,
        'queryset_list_trivandrum_icsi_val': queryset_list_trivandrum_icsi_val,
        'queryset_list_trivandrum_iui': queryset_list_trivandrum_iui,

        'my_total_clinic_count_ludhiana': my_total_clinic_count_ludhiana,
        'queryset_list_ludhiana_ivf_val': queryset_list_ludhiana_ivf_val,
        'queryset_list_ludhiana_egg_val': queryset_list_ludhiana_egg_val,
        'queryset_list_ludhiana_embryo_val': queryset_list_ludhiana_embryo_val,
        'queryset_list_ludhiana_sperm_val': queryset_list_ludhiana_sperm_val,
        'queryset_list_ludhiana_icsi_val': queryset_list_ludhiana_icsi_val,
        'queryset_list_ludhiana_iui': queryset_list_ludhiana_iui,

        'my_total_clinic_count_visakhapatnam': my_total_clinic_count_visakhapatnam,
        'queryset_list_visakhapatnam_ivf_val': queryset_list_visakhapatnam_ivf_val,
        'queryset_list_visakhapatnam_egg_val': queryset_list_visakhapatnam_egg_val,
        'queryset_list_visakhapatnam_embryo_val': queryset_list_visakhapatnam_embryo_val,
        'queryset_list_visakhapatnam_sperm_val': queryset_list_visakhapatnam_sperm_val,
        'queryset_list_visakhapatnam_icsi_val': queryset_list_visakhapatnam_icsi_val,
        'queryset_list_visakhapatnam_iui': queryset_list_visakhapatnam_iui,

        'my_total_clinic_count_vijayawada': my_total_clinic_count_vijayawada,
        'queryset_list_vijayawada_ivf_val': queryset_list_vijayawada_ivf_val,
        'queryset_list_vijayawada_egg_val': queryset_list_vijayawada_egg_val,
        'queryset_list_vijayawada_embryo_val': queryset_list_vijayawada_embryo_val,
        'queryset_list_vijayawada_sperm_val': queryset_list_vijayawada_sperm_val,
        'queryset_list_vijayawada_icsi_val': queryset_list_vijayawada_icsi_val,
        'queryset_list_vijayawada_iui': queryset_list_vijayawada_iui,

        'my_total_clinic_count_newdelhi': my_total_clinic_count_newdelhi,
        'queryset_list_newdelhi_ivf_val': queryset_list_newdelhi_ivf_val,
        'queryset_list_newdelhi_egg_val': queryset_list_newdelhi_egg_val,
        'queryset_list_newdelhi_embryo_val': queryset_list_newdelhi_embryo_val,
        'queryset_list_newdelhi_sperm_val': queryset_list_newdelhi_sperm_val,
        'queryset_list_newdelhi_icsi_val': queryset_list_newdelhi_icsi_val,
        'queryset_list_newdelhi_iui': queryset_list_newdelhi_iui,

        'my_total_clinic_count_vadodara': my_total_clinic_count_vadodara,
        'queryset_list_vadodara_ivf_val': queryset_list_vadodara_ivf_val,
        'queryset_list_vadodara_egg_val': queryset_list_vadodara_egg_val,
        'queryset_list_vadodara_embryo_val': queryset_list_vadodara_embryo_val,
        'queryset_list_vadodara_sperm_val': queryset_list_vadodara_sperm_val,
        'queryset_list_vadodara_icsi_val': queryset_list_vadodara_icsi_val,
        'queryset_list_vadodara_iui': queryset_list_vadodara_iui,

        'my_total_clinic_count_gurugram': my_total_clinic_count_gurugram,
        'queryset_list_gurugram_ivf_val': queryset_list_gurugram_ivf_val,
        'queryset_list_gurugram_egg_val': queryset_list_gurugram_egg_val,
        'queryset_list_gurugram_embryo_val': queryset_list_gurugram_embryo_val,
        'queryset_list_gurugram_sperm_val': queryset_list_gurugram_sperm_val,
        'queryset_list_gurugram_icsi_val': queryset_list_gurugram_icsi_val,
        'queryset_list_gurugram_iui': queryset_list_gurugram_iui,

        'my_total_clinic_count_rohtak': my_total_clinic_count_rohtak,
        'queryset_list_rohtak_ivf_val': queryset_list_rohtak_ivf_val,
        'queryset_list_rohtak_egg_val': queryset_list_rohtak_egg_val,
        'queryset_list_rohtak_embryo_val': queryset_list_rohtak_embryo_val,
        'queryset_list_rohtak_sperm_val': queryset_list_rohtak_sperm_val,
        'queryset_list_rohtak_icsi_val': queryset_list_rohtak_icsi_val,
        'queryset_list_rohtak_iui': queryset_list_rohtak_iui,

        'my_total_clinic_count_jammu': my_total_clinic_count_jammu,
        'queryset_list_jammu_ivf_val': queryset_list_jammu_ivf_val,
        'queryset_list_jammu_egg_val': queryset_list_jammu_egg_val,
        'queryset_list_jammu_embryo_val': queryset_list_jammu_embryo_val,
        'queryset_list_jammu_sperm_val': queryset_list_jammu_sperm_val,
        'queryset_list_jammu_icsi_val': queryset_list_jammu_icsi_val,
        'queryset_list_jammu_iui': queryset_list_jammu_iui,

        'my_total_clinic_count_ranchi': my_total_clinic_count_ranchi,
        'queryset_list_ranchi_ivf_val': queryset_list_ranchi_ivf_val,
        'queryset_list_ranchi_egg_val': queryset_list_ranchi_egg_val,
        'queryset_list_ranchi_embryo_val': queryset_list_ranchi_embryo_val,
        'queryset_list_ranchi_sperm_val': queryset_list_ranchi_sperm_val,
        'queryset_list_ranchi_icsi_val': queryset_list_ranchi_icsi_val,
        'queryset_list_ranchi_iui': queryset_list_ranchi_iui,

        'my_total_clinic_count_gwalior': my_total_clinic_count_gwalior,
        'queryset_list_gwalior_ivf_val': queryset_list_gwalior_ivf_val,
        'queryset_list_gwalior_egg_val': queryset_list_gwalior_egg_val,
        'queryset_list_gwalior_embryo_val': queryset_list_gwalior_embryo_val,
        'queryset_list_gwalior_sperm_val': queryset_list_gwalior_sperm_val,
        'queryset_list_gwalior_icsi_val': queryset_list_gwalior_icsi_val,
        'queryset_list_gwalior_iui': queryset_list_gwalior_iui,

        'my_total_clinic_count_pune': my_total_clinic_count_pune,
        'queryset_list_pune_ivf_val': queryset_list_pune_ivf_val,
        'queryset_list_pune_egg_val': queryset_list_pune_egg_val,
        'queryset_list_pune_embryo_val': queryset_list_pune_embryo_val,
        'queryset_list_pune_sperm_val': queryset_list_pune_sperm_val,
        'queryset_list_pune_icsi_val': queryset_list_pune_icsi_val,
        'queryset_list_pune_iui': queryset_list_pune_iui,

        'my_total_clinic_count_warangal': my_total_clinic_count_warangal,
        'queryset_list_warangal_ivf_val': queryset_list_warangal_ivf_val,
        'queryset_list_warangal_egg_val': queryset_list_warangal_egg_val,
        'queryset_list_warangal_embryo_val': queryset_list_warangal_embryo_val,
        'queryset_list_warangal_sperm_val': queryset_list_warangal_sperm_val,
        'queryset_list_warangal_icsi_val': queryset_list_warangal_icsi_val,
        'queryset_list_warangal_iui': queryset_list_warangal_iui,

        'my_total_clinic_count_gachibowli': my_total_clinic_count_gachibowli,
        'queryset_list_gachibowli_ivf_val': queryset_list_gachibowli_ivf_val,
        'queryset_list_gachibowli_egg_val': queryset_list_gachibowli_egg_val,
        'queryset_list_gachibowli_embryo_val': queryset_list_gachibowli_embryo_val,
        'queryset_list_gachibowli_sperm_val': queryset_list_gachibowli_sperm_val,
        'queryset_list_gachibowli_icsi_val': queryset_list_gachibowli_icsi_val,
        'queryset_list_gachibowli_iui': queryset_list_gachibowli_iui,

        'my_total_clinic_count_madhapur': my_total_clinic_count_madhapur,
        'queryset_list_madhapur_ivf_val': queryset_list_madhapur_ivf_val,
        'queryset_list_madhapur_egg_val': queryset_list_madhapur_egg_val,
        'queryset_list_madhapur_embryo_val': queryset_list_madhapur_embryo_val,
        'queryset_list_madhapur_sperm_val': queryset_list_madhapur_sperm_val,
        'queryset_list_madhapur_icsi_val': queryset_list_madhapur_icsi_val,
        'queryset_list_madhapur_iui': queryset_list_madhapur_iui,

        'my_total_clinic_count_noida': my_total_clinic_count_noida,
        'queryset_list_noida_ivf_val': queryset_list_noida_ivf_val,
        'queryset_list_noida_egg_val': queryset_list_noida_egg_val,
        'queryset_list_noida_embryo_val': queryset_list_noida_embryo_val,
        'queryset_list_noida_sperm_val': queryset_list_noida_sperm_val,
        'queryset_list_noida_icsi_val': queryset_list_noida_icsi_val,
        'queryset_list_noida_iui': queryset_list_noida_iui,

        'my_total_clinic_count_meerut': my_total_clinic_count_meerut,
        'queryset_list_meerut_ivf_val': queryset_list_meerut_ivf_val,
        'queryset_list_meerut_egg_val': queryset_list_meerut_egg_val,
        'queryset_list_meerut_embryo_val': queryset_list_meerut_embryo_val,
        'queryset_list_meerut_sperm_val': queryset_list_meerut_sperm_val,
        'queryset_list_meerut_icsi_val': queryset_list_meerut_icsi_val,
        'queryset_list_meerut_iui': queryset_list_meerut_iui,

        'my_total_clinic_count_haldwani': my_total_clinic_count_haldwani,
        'queryset_list_haldwani_ivf_val': queryset_list_haldwani_ivf_val,
        'queryset_list_haldwani_egg_val': queryset_list_haldwani_egg_val,
        'queryset_list_haldwani_embryo_val': queryset_list_haldwani_embryo_val,
        'queryset_list_haldwani_sperm_val': queryset_list_haldwani_sperm_val,
        'queryset_list_haldwani_icsi_val': queryset_list_haldwani_icsi_val,
        'queryset_list_haldwani_iui': queryset_list_haldwani_iui,
        }

    return render(request, 'main/Locations/INLocations/in-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsGRRegions(request):
    queryset_list_gr = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_athens = queryset_list_gr.filter(clinicCity__iexact='Athens')
    my_total_clinic_count_athens = queryset_list_athens.count()

    queryset_list_athens_ivf = queryset_list_athens.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_athens_ivf.items():
        queryset_list_athens_ivf_val = val

    queryset_list_athens_egg = queryset_list_athens.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_athens_egg.items():
        queryset_list_athens_egg_val = val

    queryset_list_athens_embryo = queryset_list_athens.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_athens_embryo.items():
        queryset_list_athens_embryo_val = val

    queryset_list_athens_sperm = queryset_list_athens.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_athens_sperm.items():
        queryset_list_athens_sperm_val = val

    queryset_list_athens_icsi = queryset_list_athens.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_athens_icsi.items():
        queryset_list_athens_icsi_val = val

    queryset_list_athens_iui = queryset_list_athens.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_athens_iui.items():
        queryset_list_athens_iui = val

    #--------------------------------------------------------------------------
    queryset_list_thessaloniki = queryset_list_gr.filter(clinicCity__iexact='Thessaloniki')
    my_total_clinic_count_thessaloniki = queryset_list_thessaloniki.count()

    queryset_list_thessaloniki_ivf = queryset_list_thessaloniki.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_thessaloniki_ivf.items():
        queryset_list_thessaloniki_ivf_val = val

    queryset_list_thessaloniki_egg = queryset_list_thessaloniki.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_thessaloniki_egg.items():
        queryset_list_thessaloniki_egg_val = val

    queryset_list_thessaloniki_embryo = queryset_list_thessaloniki.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_thessaloniki_embryo.items():
        queryset_list_thessaloniki_embryo_val = val

    queryset_list_thessaloniki_sperm = queryset_list_thessaloniki.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_thessaloniki_sperm.items():
        queryset_list_thessaloniki_sperm_val = val

    queryset_list_thessaloniki_icsi = queryset_list_thessaloniki.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_thessaloniki_icsi.items():
        queryset_list_thessaloniki_icsi_val = val

    queryset_list_thessaloniki_iui = queryset_list_thessaloniki.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_thessaloniki_iui.items():
        queryset_list_thessaloniki_iui = val

    context = {
        'my_total_clinic_count_athens': my_total_clinic_count_athens,
        'queryset_list_athens_ivf_val': queryset_list_athens_ivf_val,
        'queryset_list_athens_egg_val': queryset_list_athens_egg_val,
        'queryset_list_athens_embryo_val': queryset_list_athens_embryo_val,
        'queryset_list_athens_sperm_val': queryset_list_athens_sperm_val,
        'queryset_list_athens_icsi_val': queryset_list_athens_icsi_val,
        'queryset_list_athens_iui': queryset_list_athens_iui,

        'my_total_clinic_count_thessaloniki': my_total_clinic_count_thessaloniki,
        'queryset_list_thessaloniki_ivf_val': queryset_list_thessaloniki_ivf_val,
        'queryset_list_thessaloniki_egg_val': queryset_list_thessaloniki_egg_val,
        'queryset_list_thessaloniki_embryo_val': queryset_list_thessaloniki_embryo_val,
        'queryset_list_thessaloniki_sperm_val': queryset_list_thessaloniki_sperm_val,
        'queryset_list_thessaloniki_icsi_val': queryset_list_thessaloniki_icsi_val,
        'queryset_list_thessaloniki_iui': queryset_list_thessaloniki_iui,
        }

    return render(request, 'main/Locations/GRLocations/gr-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsCYRegions(request):
    queryset_list_cy = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_nicosia = queryset_list_cy.filter(clinicCity__iexact='Nicosia')
    my_total_clinic_count_nicosia = queryset_list_nicosia.count()

    queryset_list_nicosia_ivf = queryset_list_nicosia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_nicosia_ivf.items():
        queryset_list_nicosia_ivf_val = val

    queryset_list_nicosia_egg = queryset_list_nicosia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_nicosia_egg.items():
        queryset_list_nicosia_egg_val = val

    queryset_list_nicosia_embryo = queryset_list_nicosia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_nicosia_embryo.items():
        queryset_list_nicosia_embryo_val = val

    queryset_list_nicosia_sperm = queryset_list_nicosia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_nicosia_sperm.items():
        queryset_list_nicosia_sperm_val = val

    queryset_list_nicosia_icsi = queryset_list_nicosia.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_nicosia_icsi.items():
        queryset_list_nicosia_icsi_val = val

    queryset_list_nicosia_iui = queryset_list_nicosia.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_nicosia_iui.items():
        queryset_list_nicosia_iui = val

    #--------------------------------------------------------------------------
    queryset_list_girne = queryset_list_cy.filter(clinicCity__iexact='girne')
    my_total_clinic_count_girne = queryset_list_girne.count()

    queryset_list_girne_ivf = queryset_list_girne.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_girne_ivf.items():
        queryset_list_girne_ivf_val = val

    queryset_list_girne_egg = queryset_list_girne.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_girne_egg.items():
        queryset_list_girne_egg_val = val

    queryset_list_girne_embryo = queryset_list_girne.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_girne_embryo.items():
        queryset_list_girne_embryo_val = val

    queryset_list_girne_sperm = queryset_list_girne.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_girne_sperm.items():
        queryset_list_girne_sperm_val = val

    queryset_list_girne_icsi = queryset_list_girne.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_girne_icsi.items():
        queryset_list_girne_icsi_val = val

    queryset_list_girne_iui = queryset_list_girne.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_girne_iui.items():
        queryset_list_girne_iui = val


    context = {
        'my_total_clinic_count_nicosia': my_total_clinic_count_nicosia,
        'queryset_list_nicosia_ivf_val': queryset_list_nicosia_ivf_val,
        'queryset_list_nicosia_egg_val': queryset_list_nicosia_egg_val,
        'queryset_list_nicosia_embryo_val': queryset_list_nicosia_embryo_val,
        'queryset_list_nicosia_sperm_val': queryset_list_nicosia_sperm_val,
        'queryset_list_nicosia_icsi_val': queryset_list_nicosia_icsi_val,
        'queryset_list_nicosia_iui': queryset_list_nicosia_iui,

        'my_total_clinic_count_girne': my_total_clinic_count_girne,
        'queryset_list_girne_ivf_val': queryset_list_girne_ivf_val,
        'queryset_list_girne_egg_val': queryset_list_girne_egg_val,
        'queryset_list_girne_embryo_val': queryset_list_girne_embryo_val,
        'queryset_list_girne_sperm_val': queryset_list_girne_sperm_val,
        'queryset_list_girne_icsi_val': queryset_list_girne_icsi_val,
        'queryset_list_girne_iui': queryset_list_girne_iui,
        }
    return render(request, 'main/Locations/CYLocations/cy-regions-ivf.html', context)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def locationsMXRegions(request):
    queryset_list_mx = BasicClinic.objects.all().exclude(is_published=False)

    #--------------------------------------------------------------------------
    queryset_list_mexicocity = queryset_list_mx.filter(clinicCity__iexact='Mexico City')
    my_total_clinic_count_mexicocity = queryset_list_mexicocity.count()

    queryset_list_mexicocity_ivf = queryset_list_mexicocity.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_mexicocity_ivf.items():
        queryset_list_mexicocity_ivf_val = val

    queryset_list_mexicocity_egg = queryset_list_mexicocity.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_mexicocity_egg.items():
        queryset_list_mexicocity_egg_val = val

    queryset_list_mexicocity_embryo = queryset_list_mexicocity.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_mexicocity_embryo.items():
        queryset_list_mexicocity_embryo_val = val

    queryset_list_mexicocity_sperm = queryset_list_mexicocity.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_mexicocity_sperm.items():
        queryset_list_mexicocity_sperm_val = val

    queryset_list_mexicocity_icsi = queryset_list_mexicocity.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_mexicocity_icsi.items():
        queryset_list_mexicocity_icsi_val = val

    queryset_list_mexicocity_iui = queryset_list_mexicocity.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_mexicocity_iui.items():
        queryset_list_mexicocity_iui = val

    #--------------------------------------------------------------------------
    queryset_list_cancun = queryset_list_mx.filter(clinicCity__iexact='Cancún')
    my_total_clinic_count_cancun = queryset_list_cancun.count()

    queryset_list_cancun_ivf = queryset_list_cancun.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cancun_ivf.items():
        queryset_list_cancun_ivf_val = val

    queryset_list_cancun_egg = queryset_list_cancun.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cancun_egg.items():
        queryset_list_cancun_egg_val = val

    queryset_list_cancun_embryo = queryset_list_cancun.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cancun_embryo.items():
        queryset_list_cancun_embryo_val = val

    queryset_list_cancun_sperm = queryset_list_cancun.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_cancun_sperm.items():
        queryset_list_cancun_sperm_val = val

    queryset_list_cancun_icsi = queryset_list_cancun.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_cancun_icsi.items():
        queryset_list_cancun_icsi_val = val

    queryset_list_cancun_iui = queryset_list_cancun.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cancun_iui.items():
        queryset_list_cancun_iui = val

    context = {
        'my_total_clinic_count_mexicocity': my_total_clinic_count_mexicocity,
        'queryset_list_mexicocity_ivf_val': queryset_list_mexicocity_ivf_val,
        'queryset_list_mexicocity_egg_val': queryset_list_mexicocity_egg_val,
        'queryset_list_mexicocity_embryo_val': queryset_list_mexicocity_embryo_val,
        'queryset_list_mexicocity_sperm_val': queryset_list_mexicocity_sperm_val,
        'queryset_list_mexicocity_icsi_val': queryset_list_mexicocity_icsi_val,
        'queryset_list_mexicocity_iui': queryset_list_mexicocity_iui,

        'my_total_clinic_count_cancun': my_total_clinic_count_cancun,
        'queryset_list_cancun_ivf_val': queryset_list_cancun_ivf_val,
        'queryset_list_cancun_egg_val': queryset_list_cancun_egg_val,
        'queryset_list_cancun_embryo_val': queryset_list_cancun_embryo_val,
        'queryset_list_cancun_sperm_val': queryset_list_cancun_sperm_val,
        'queryset_list_cancun_icsi_val': queryset_list_cancun_icsi_val,
        'queryset_list_cancun_iui': queryset_list_cancun_iui,
        }
    return render(request, 'main/Locations/MXLocations/mx-regions-ivf.html', context)
