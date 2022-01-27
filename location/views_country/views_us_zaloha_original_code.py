from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from django.db.models import Avg


def locationsUSRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'United States'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_us_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_us_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_us_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_us_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_us_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_us_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_us_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_us_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_us_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_us_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_us_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_us_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    # --------------------------------------------------------------------------
    queryset_list_us = BasicClinic.objects.all().exclude(is_published=False)

    queryset_list_us = queryset_list_us.filter(clinicState='United States')
    my_total_clinic_count_usa = queryset_list_us.count()

    queryset_list_alabama = queryset_list_us.filter(clinicRegion__iexact='Alabama')
    my_total_clinic_count_alabama = queryset_list_alabama.count()

    queryset_list_alabama_ivf = queryset_list_alabama.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_alabama_ivf.items():
        queryset_list_alabama_ivf_val = val

    queryset_list_alabama_egg = queryset_list_alabama.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_alabama_egg.items():
        queryset_list_alabama_egg_val = val

    queryset_list_alabama_embryo = queryset_list_alabama.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_alabama_embryo.items():
        queryset_list_alabama_embryo_val = val

    queryset_list_alabama_sperm = queryset_list_alabama.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_alabama_sperm.items():
        queryset_list_alabama_sperm_val = val

    queryset_list_alabama_icsi = queryset_list_alabama.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_alabama_icsi.items():
        queryset_list_alabama_icsi_val = val

    queryset_list_alabama_iui = queryset_list_alabama.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_alabama_iui.items():
        queryset_list_alabama_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_alaska = queryset_list_us.filter(clinicRegion__iexact='Alaska')
    my_total_clinic_count_alaska = queryset_list_alaska.count()

    queryset_list_alaska_ivf = queryset_list_alaska.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_alaska_ivf.items():
        queryset_list_alaska_ivf_val = val

    queryset_list_alaska_egg = queryset_list_alaska.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_alaska_egg.items():
        queryset_list_alaska_egg_val = val

    queryset_list_alaska_embryo = queryset_list_alaska.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_alaska_embryo.items():
        queryset_list_alaska_embryo_val = val

    queryset_list_alaska_sperm = queryset_list_alaska.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_alaska_sperm.items():
        queryset_list_alaska_sperm_val = val

    queryset_list_alaska_icsi = queryset_list_alaska.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_alaska_icsi.items():
        queryset_list_alaska_icsi_val = val

    queryset_list_alaska_iui = queryset_list_alaska.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_alaska_iui.items():
        queryset_list_alaska_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_arizona = queryset_list_us.filter(clinicRegion__iexact='Arizona')
    my_total_clinic_count_arizona = queryset_list_arizona.count()

    queryset_list_arizona_ivf = queryset_list_arizona.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_arizona_ivf.items():
        queryset_list_arizona_ivf_val = val

    queryset_list_arizona_egg = queryset_list_arizona.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_arizona_egg.items():
        queryset_list_arizona_egg_val = val

    queryset_list_arizona_embryo = queryset_list_arizona.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_arizona_embryo.items():
        queryset_list_arizona_embryo_val = val

    queryset_list_arizona_sperm = queryset_list_arizona.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_arizona_sperm.items():
        queryset_list_arizona_sperm_val = val

    queryset_list_arizona_icsi = queryset_list_arizona.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_arizona_icsi.items():
        queryset_list_arizona_icsi_val = val

    queryset_list_arizona_iui = queryset_list_arizona.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_arizona_iui.items():
        queryset_list_arizona_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_arkansas = queryset_list_us.filter(clinicRegion__iexact='Arkansas')
    my_total_clinic_count_arkansas = queryset_list_arkansas.count()

    queryset_list_arkansas_ivf = queryset_list_arkansas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_arkansas_ivf.items():
        queryset_list_arkansas_ivf_val = val

    queryset_list_arkansas_egg = queryset_list_arkansas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_arkansas_egg.items():
        queryset_list_arkansas_egg_val = val

    queryset_list_arkansas_embryo = queryset_list_arkansas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_arkansas_embryo.items():
        queryset_list_arkansas_embryo_val = val

    queryset_list_arkansas_sperm = queryset_list_arkansas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_arkansas_sperm.items():
        queryset_list_arkansas_sperm_val = val

    queryset_list_arkansas_icsi = queryset_list_arkansas.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_arkansas_icsi.items():
        queryset_list_arkansas_icsi_val = val

    queryset_list_arkansas_iui = queryset_list_arkansas.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_arkansas_iui.items():
        queryset_list_arkansas_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_california = queryset_list_us.filter(clinicRegion__iexact='California')
    my_total_clinic_count_california = queryset_list_california.count()

    queryset_list_california_ivf = queryset_list_california.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_california_ivf.items():
        queryset_list_california_ivf_val = val

    queryset_list_california_egg = queryset_list_california.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_california_egg.items():
        queryset_list_california_egg_val = val

    queryset_list_california_embryo = queryset_list_california.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_california_embryo.items():
        queryset_list_california_embryo_val = val

    queryset_list_california_sperm = queryset_list_california.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_california_sperm.items():
        queryset_list_california_sperm_val = val

    queryset_list_california_icsi = queryset_list_california.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_california_icsi.items():
        queryset_list_california_icsi_val = val

    queryset_list_california_iui = queryset_list_california.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_california_iui.items():
        queryset_list_california_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_colorado = queryset_list_us.filter(clinicRegion__iexact='Colorado')
    my_total_clinic_count_colorado = queryset_list_colorado.count()

    queryset_list_colorado_ivf = queryset_list_colorado.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_colorado_ivf.items():
        queryset_list_colorado_ivf_val = val

    queryset_list_colorado_egg = queryset_list_colorado.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_colorado_egg.items():
        queryset_list_colorado_egg_val = val

    queryset_list_colorado_embryo = queryset_list_colorado.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_colorado_embryo.items():
        queryset_list_colorado_embryo_val = val

    queryset_list_colorado_sperm = queryset_list_colorado.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_colorado_sperm.items():
        queryset_list_colorado_sperm_val = val

    queryset_list_colorado_icsi = queryset_list_colorado.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_colorado_icsi.items():
        queryset_list_colorado_icsi_val = val

    queryset_list_colorado_iui = queryset_list_colorado.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_colorado_iui.items():
        queryset_list_colorado_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_connecticut = queryset_list_us.filter(clinicRegion__iexact='Connecticut')
    my_total_clinic_count_connecticut = queryset_list_connecticut.count()

    queryset_list_connecticut_ivf = queryset_list_connecticut.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_connecticut_ivf.items():
        queryset_list_connecticut_ivf_val = val

    queryset_list_connecticut_egg = queryset_list_connecticut.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_connecticut_egg.items():
        queryset_list_connecticut_egg_val = val

    queryset_list_connecticut_embryo = queryset_list_connecticut.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_connecticut_embryo.items():
        queryset_list_connecticut_embryo_val = val

    queryset_list_connecticut_sperm = queryset_list_connecticut.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_connecticut_sperm.items():
        queryset_list_connecticut_sperm_val = val

    queryset_list_connecticut_icsi = queryset_list_connecticut.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_connecticut_icsi.items():
        queryset_list_connecticut_icsi_val = val

    queryset_list_connecticut_iui = queryset_list_connecticut.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_connecticut_iui.items():
        queryset_list_connecticut_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_delaware = queryset_list_us.filter(clinicRegion__iexact='Delaware')
    my_total_clinic_count_delaware = queryset_list_delaware.count()

    queryset_list_delaware_ivf = queryset_list_delaware.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_delaware_ivf.items():
        queryset_list_delaware_ivf_val = val

    queryset_list_delaware_egg = queryset_list_delaware.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_delaware_egg.items():
        queryset_list_delaware_egg_val = val

    queryset_list_delaware_embryo = queryset_list_delaware.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_delaware_embryo.items():
        queryset_list_delaware_embryo_val = val

    queryset_list_delaware_sperm = queryset_list_delaware.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_delaware_sperm.items():
        queryset_list_delaware_sperm_val = val

    queryset_list_delaware_icsi = queryset_list_delaware.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_delaware_icsi.items():
        queryset_list_delaware_icsi_val = val

    queryset_list_delaware_iui = queryset_list_delaware.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_delaware_iui.items():
        queryset_list_delaware_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_florida = queryset_list_us.filter(clinicRegion__iexact='Florida')
    my_total_clinic_count_florida = queryset_list_florida.count()

    queryset_list_florida_ivf = queryset_list_florida.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_florida_ivf.items():
        queryset_list_florida_ivf_val = val

    queryset_list_florida_egg = queryset_list_florida.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_florida_egg.items():
        queryset_list_florida_egg_val = val

    queryset_list_florida_embryo = queryset_list_florida.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_florida_embryo.items():
        queryset_list_florida_embryo_val = val

    queryset_list_florida_sperm = queryset_list_florida.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_florida_sperm.items():
        queryset_list_florida_sperm_val = val

    queryset_list_florida_icsi = queryset_list_florida.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_florida_icsi.items():
        queryset_list_florida_icsi_val = val

    queryset_list_florida_iui = queryset_list_florida.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_florida_iui.items():
        queryset_list_florida_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_georgia = queryset_list_us.filter(clinicRegion__iexact='Georgia')
    my_total_clinic_count_georgia = queryset_list_georgia.count()

    queryset_list_georgia_ivf = queryset_list_georgia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_georgia_ivf.items():
        queryset_list_georgia_ivf_val = val

    queryset_list_georgia_egg = queryset_list_georgia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_georgia_egg.items():
        queryset_list_georgia_egg_val = val

    queryset_list_georgia_embryo = queryset_list_georgia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_georgia_embryo.items():
        queryset_list_georgia_embryo_val = val

    queryset_list_georgia_sperm = queryset_list_georgia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_georgia_sperm.items():
        queryset_list_georgia_sperm_val = val

    queryset_list_georgia_icsi = queryset_list_georgia.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_georgia_icsi.items():
        queryset_list_georgia_icsi_val = val

    queryset_list_georgia_iui = queryset_list_georgia.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_georgia_iui.items():
        queryset_list_georgia_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_hawaii = queryset_list_us.filter(clinicRegion__iexact='Hawaii')
    my_total_clinic_count_hawaii = queryset_list_hawaii.count()

    queryset_list_hawaii_ivf = queryset_list_hawaii.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_hawaii_ivf.items():
        queryset_list_hawaii_ivf_val = val

    queryset_list_hawaii_egg = queryset_list_hawaii.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_hawaii_egg.items():
        queryset_list_hawaii_egg_val = val

    queryset_list_hawaii_embryo = queryset_list_hawaii.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_hawaii_embryo.items():
        queryset_list_hawaii_embryo_val = val

    queryset_list_hawaii_sperm = queryset_list_hawaii.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_hawaii_sperm.items():
        queryset_list_hawaii_sperm_val = val

    queryset_list_hawaii_icsi = queryset_list_hawaii.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_hawaii_icsi.items():
        queryset_list_hawaii_icsi_val = val

    queryset_list_hawaii_iui = queryset_list_hawaii.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_hawaii_iui.items():
        queryset_list_hawaii_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_idaho = queryset_list_us.filter(clinicRegion__iexact='Idaho')
    my_total_clinic_count_idaho = queryset_list_idaho.count()

    queryset_list_idaho_ivf = queryset_list_idaho.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_idaho_ivf.items():
        queryset_list_idaho_ivf_val = val

    queryset_list_idaho_egg = queryset_list_idaho.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_idaho_egg.items():
        queryset_list_idaho_egg_val = val

    queryset_list_idaho_embryo = queryset_list_idaho.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_idaho_embryo.items():
        queryset_list_idaho_embryo_val = val

    queryset_list_idaho_sperm = queryset_list_idaho.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_idaho_sperm.items():
        queryset_list_idaho_sperm_val = val

    queryset_list_idaho_icsi = queryset_list_idaho.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_idaho_icsi.items():
        queryset_list_idaho_icsi_val = val

    queryset_list_idaho_iui = queryset_list_idaho.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_idaho_iui.items():
        queryset_list_idaho_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_illinois = queryset_list_us.filter(clinicRegion__iexact='Illinois')
    my_total_clinic_count_illinois = queryset_list_illinois.count()

    queryset_list_illinois_ivf = queryset_list_illinois.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_illinois_ivf.items():
        queryset_list_illinois_ivf_val = val

    queryset_list_illinois_egg = queryset_list_illinois.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_illinois_egg.items():
        queryset_list_illinois_egg_val = val

    queryset_list_illinois_embryo = queryset_list_illinois.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_illinois_embryo.items():
        queryset_list_illinois_embryo_val = val

    queryset_list_illinois_sperm = queryset_list_illinois.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_illinois_sperm.items():
        queryset_list_illinois_sperm_val = val

    queryset_list_illinois_icsi = queryset_list_illinois.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_illinois_icsi.items():
        queryset_list_illinois_icsi_val = val

    queryset_list_illinois_iui = queryset_list_illinois.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_illinois_iui.items():
        queryset_list_illinois_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_indiana = queryset_list_us.filter(clinicRegion__iexact='Indiana')
    my_total_clinic_count_indiana = queryset_list_indiana.count()

    queryset_list_indiana_ivf = queryset_list_indiana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_indiana_ivf.items():
        queryset_list_indiana_ivf_val = val

    queryset_list_indiana_egg = queryset_list_indiana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_indiana_egg.items():
        queryset_list_indiana_egg_val = val

    queryset_list_indiana_embryo = queryset_list_indiana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_indiana_embryo.items():
        queryset_list_indiana_embryo_val = val

    queryset_list_indiana_sperm = queryset_list_indiana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_indiana_sperm.items():
        queryset_list_indiana_sperm_val = val

    queryset_list_indiana_icsi = queryset_list_indiana.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_indiana_icsi.items():
        queryset_list_indiana_icsi_val = val

    queryset_list_indiana_iui = queryset_list_indiana.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_indiana_iui.items():
        queryset_list_indiana_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_iowa = queryset_list_us.filter(clinicRegion__iexact='Iowa')
    my_total_clinic_count_iowa = queryset_list_iowa.count()

    queryset_list_iowa_ivf = queryset_list_iowa.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_iowa_ivf.items():
        queryset_list_iowa_ivf_val = val

    queryset_list_iowa_egg = queryset_list_iowa.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_iowa_egg.items():
        queryset_list_iowa_egg_val = val

    queryset_list_iowa_embryo = queryset_list_iowa.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_iowa_embryo.items():
        queryset_list_iowa_embryo_val = val

    queryset_list_iowa_sperm = queryset_list_iowa.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_iowa_sperm.items():
        queryset_list_iowa_sperm_val = val

    queryset_list_iowa_icsi = queryset_list_iowa.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_iowa_icsi.items():
        queryset_list_iowa_icsi_val = val

    queryset_list_iowa_iui = queryset_list_iowa.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_iowa_iui.items():
        queryset_list_iowa_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_kansas = queryset_list_us.filter(clinicRegion__iexact='Kansas')
    my_total_clinic_count_kansas = queryset_list_kansas.count()

    queryset_list_kansas_ivf = queryset_list_kansas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_kansas_ivf.items():
        queryset_list_kansas_ivf_val = val

    queryset_list_kansas_egg = queryset_list_kansas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_kansas_egg.items():
        queryset_list_kansas_egg_val = val

    queryset_list_kansas_embryo = queryset_list_kansas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_kansas_embryo.items():
        queryset_list_kansas_embryo_val = val

    queryset_list_kansas_sperm = queryset_list_kansas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_kansas_sperm.items():
        queryset_list_kansas_sperm_val = val

    queryset_list_kansas_icsi = queryset_list_kansas.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_kansas_icsi.items():
        queryset_list_kansas_icsi_val = val

    queryset_list_kansas_iui = queryset_list_kansas.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_kansas_iui.items():
        queryset_list_kansas_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_kentucky = queryset_list_us.filter(clinicRegion__iexact='Kentucky')
    my_total_clinic_count_kentucky = queryset_list_kentucky.count()

    queryset_list_kentucky_ivf = queryset_list_kentucky.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_kentucky_ivf.items():
        queryset_list_kentucky_ivf_val = val

    queryset_list_kentucky_egg = queryset_list_kentucky.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_kentucky_egg.items():
        queryset_list_kentucky_egg_val = val

    queryset_list_kentucky_embryo = queryset_list_kentucky.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_kentucky_embryo.items():
        queryset_list_kentucky_embryo_val = val

    queryset_list_kentucky_sperm = queryset_list_kentucky.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_kentucky_sperm.items():
        queryset_list_kentucky_sperm_val = val

    queryset_list_kentucky_icsi = queryset_list_kentucky.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_kentucky_icsi.items():
        queryset_list_kentucky_icsi_val = val

    queryset_list_kentucky_iui = queryset_list_kentucky.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_kentucky_iui.items():
        queryset_list_kentucky_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_louisiana = queryset_list_us.filter(clinicRegion__iexact='Louisiana')
    my_total_clinic_count_louisiana = queryset_list_louisiana.count()

    queryset_list_louisiana_ivf = queryset_list_louisiana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_louisiana_ivf.items():
        queryset_list_louisiana_ivf_val = val

    queryset_list_louisiana_egg = queryset_list_louisiana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_louisiana_egg.items():
        queryset_list_louisiana_egg_val = val

    queryset_list_louisiana_embryo = queryset_list_louisiana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_louisiana_embryo.items():
        queryset_list_louisiana_embryo_val = val

    queryset_list_louisiana_sperm = queryset_list_louisiana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_louisiana_sperm.items():
        queryset_list_louisiana_sperm_val = val

    queryset_list_louisiana_icsi = queryset_list_louisiana.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_louisiana_icsi.items():
        queryset_list_louisiana_icsi_val = val

    queryset_list_louisiana_iui = queryset_list_louisiana.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_louisiana_iui.items():
        queryset_list_louisiana_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_maine = queryset_list_us.filter(clinicRegion__iexact='Maine')
    my_total_clinic_count_maine = queryset_list_maine.count()

    queryset_list_maine_ivf = queryset_list_maine.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_maine_ivf.items():
        queryset_list_maine_ivf_val = val

    queryset_list_maine_egg = queryset_list_maine.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_maine_egg.items():
        queryset_list_maine_egg_val = val

    queryset_list_maine_embryo = queryset_list_maine.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_maine_embryo.items():
        queryset_list_maine_embryo_val = val

    queryset_list_maine_sperm = queryset_list_maine.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_maine_sperm.items():
        queryset_list_maine_sperm_val = val

    queryset_list_maine_icsi = queryset_list_maine.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_maine_icsi.items():
        queryset_list_maine_icsi_val = val

    queryset_list_maine_iui = queryset_list_maine.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_maine_iui.items():
        queryset_list_maine_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_maryland = queryset_list_us.filter(clinicRegion__iexact='Maryland')
    my_total_clinic_count_maryland = queryset_list_maryland.count()

    queryset_list_maryland_ivf = queryset_list_maryland.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_maryland_ivf.items():
        queryset_list_maryland_ivf_val = val

    queryset_list_maryland_egg = queryset_list_maryland.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_maryland_egg.items():
        queryset_list_maryland_egg_val = val

    queryset_list_maryland_embryo = queryset_list_maryland.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_maryland_embryo.items():
        queryset_list_maryland_embryo_val = val

    queryset_list_maryland_sperm = queryset_list_maryland.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_maryland_sperm.items():
        queryset_list_maryland_sperm_val = val

    queryset_list_maryland_icsi = queryset_list_maryland.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_maryland_icsi.items():
        queryset_list_maryland_icsi_val = val

    queryset_list_maryland_iui = queryset_list_maryland.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_maryland_iui.items():
        queryset_list_maryland_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_massachusetts = queryset_list_us.filter(clinicRegion__iexact='Massachusetts')
    my_total_clinic_count_massachusetts = queryset_list_massachusetts.count()

    queryset_list_massachusetts_ivf = queryset_list_massachusetts.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_massachusetts_ivf.items():
        queryset_list_massachusetts_ivf_val = val

    queryset_list_massachusetts_egg = queryset_list_massachusetts.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_massachusetts_egg.items():
        queryset_list_massachusetts_egg_val = val

    queryset_list_massachusetts_embryo = queryset_list_massachusetts.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_massachusetts_embryo.items():
        queryset_list_massachusetts_embryo_val = val

    queryset_list_massachusetts_sperm = queryset_list_massachusetts.aggregate(
        average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_massachusetts_sperm.items():
        queryset_list_massachusetts_sperm_val = val

    queryset_list_massachusetts_icsi = queryset_list_massachusetts.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_massachusetts_icsi.items():
        queryset_list_massachusetts_icsi_val = val

    queryset_list_massachusetts_iui = queryset_list_massachusetts.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_massachusetts_iui.items():
        queryset_list_massachusetts_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_michigan = queryset_list_us.filter(clinicRegion__iexact='Michigan')
    my_total_clinic_count_michigan = queryset_list_michigan.count()

    queryset_list_michigan_ivf = queryset_list_michigan.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_michigan_ivf.items():
        queryset_list_michigan_ivf_val = val

    queryset_list_michigan_egg = queryset_list_michigan.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_michigan_egg.items():
        queryset_list_michigan_egg_val = val

    queryset_list_michigan_embryo = queryset_list_michigan.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_michigan_embryo.items():
        queryset_list_michigan_embryo_val = val

    queryset_list_michigan_sperm = queryset_list_michigan.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_michigan_sperm.items():
        queryset_list_michigan_sperm_val = val

    queryset_list_michigan_icsi = queryset_list_michigan.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_michigan_icsi.items():
        queryset_list_michigan_icsi_val = val

    queryset_list_michigan_iui = queryset_list_michigan.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_michigan_iui.items():
        queryset_list_michigan_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_minnesota = queryset_list_us.filter(clinicRegion__iexact='Minnesota')
    my_total_clinic_count_minnesota = queryset_list_minnesota.count()

    queryset_list_minnesota_ivf = queryset_list_minnesota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_minnesota_ivf.items():
        queryset_list_minnesota_ivf_val = val

    queryset_list_minnesota_egg = queryset_list_minnesota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_minnesota_egg.items():
        queryset_list_minnesota_egg_val = val

    queryset_list_minnesota_embryo = queryset_list_minnesota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_minnesota_embryo.items():
        queryset_list_minnesota_embryo_val = val

    queryset_list_minnesota_sperm = queryset_list_minnesota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_minnesota_sperm.items():
        queryset_list_minnesota_sperm_val = val

    queryset_list_minnesota_icsi = queryset_list_minnesota.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_minnesota_icsi.items():
        queryset_list_minnesota_icsi_val = val

    queryset_list_minnesota_iui = queryset_list_minnesota.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_minnesota_iui.items():
        queryset_list_minnesota_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_mississippi = queryset_list_us.filter(clinicRegion__iexact='Mississippi')
    my_total_clinic_count_mississippi = queryset_list_mississippi.count()

    queryset_list_mississippi_ivf = queryset_list_mississippi.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_mississippi_ivf.items():
        queryset_list_mississippi_ivf_val = val

    queryset_list_mississippi_egg = queryset_list_mississippi.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_mississippi_egg.items():
        queryset_list_mississippi_egg_val = val

    queryset_list_mississippi_embryo = queryset_list_mississippi.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_mississippi_embryo.items():
        queryset_list_mississippi_embryo_val = val

    queryset_list_mississippi_sperm = queryset_list_mississippi.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_mississippi_sperm.items():
        queryset_list_mississippi_sperm_val = val

    queryset_list_mississippi_icsi = queryset_list_mississippi.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_mississippi_icsi.items():
        queryset_list_mississippi_icsi_val = val

    queryset_list_mississippi_iui = queryset_list_mississippi.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_mississippi_iui.items():
        queryset_list_mississippi_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_missouri = queryset_list_us.filter(clinicRegion__iexact='Missouri')
    my_total_clinic_count_missouri = queryset_list_missouri.count()

    queryset_list_missouri_ivf = queryset_list_missouri.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_missouri_ivf.items():
        queryset_list_missouri_ivf_val = val

    queryset_list_missouri_egg = queryset_list_missouri.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_missouri_egg.items():
        queryset_list_missouri_egg_val = val

    queryset_list_missouri_embryo = queryset_list_missouri.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_missouri_embryo.items():
        queryset_list_missouri_embryo_val = val

    queryset_list_missouri_sperm = queryset_list_missouri.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_missouri_sperm.items():
        queryset_list_missouri_sperm_val = val

    queryset_list_missouri_icsi = queryset_list_missouri.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_missouri_icsi.items():
        queryset_list_missouri_icsi_val = val

    queryset_list_missouri_iui = queryset_list_missouri.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_missouri_iui.items():
        queryset_list_missouri_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_montana = queryset_list_us.filter(clinicRegion__iexact='Montana')
    my_total_clinic_count_montana = queryset_list_montana.count()

    queryset_list_montana_ivf = queryset_list_montana.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_montana_ivf.items():
        queryset_list_montana_ivf_val = val

    queryset_list_montana_egg = queryset_list_montana.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_montana_egg.items():
        queryset_list_montana_egg_val = val

    queryset_list_montana_embryo = queryset_list_montana.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_montana_embryo.items():
        queryset_list_montana_embryo_val = val

    queryset_list_montana_sperm = queryset_list_montana.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_montana_sperm.items():
        queryset_list_montana_sperm_val = val

    queryset_list_montana_icsi = queryset_list_montana.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_montana_icsi.items():
        queryset_list_montana_icsi_val = val

    queryset_list_montana_iui = queryset_list_montana.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_montana_iui.items():
        queryset_list_montana_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_nebraska = queryset_list_us.filter(clinicRegion__iexact='Nebraska')
    my_total_clinic_count_nebraska = queryset_list_nebraska.count()

    queryset_list_nebraska_ivf = queryset_list_nebraska.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_nebraska_ivf.items():
        queryset_list_nebraska_ivf_val = val

    queryset_list_nebraska_egg = queryset_list_nebraska.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_nebraska_egg.items():
        queryset_list_nebraska_egg_val = val

    queryset_list_nebraska_embryo = queryset_list_nebraska.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_nebraska_embryo.items():
        queryset_list_nebraska_embryo_val = val

    queryset_list_nebraska_sperm = queryset_list_nebraska.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_nebraska_sperm.items():
        queryset_list_nebraska_sperm_val = val

    queryset_list_nebraska_icsi = queryset_list_nebraska.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_nebraska_icsi.items():
        queryset_list_nebraska_icsi_val = val

    queryset_list_nebraska_iui = queryset_list_nebraska.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_nebraska_iui.items():
        queryset_list_nebraska_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_newhampshire = queryset_list_us.filter(clinicRegion__iexact='New Hampshire')
    my_total_clinic_count_newhampshire = queryset_list_newhampshire.count()

    queryset_list_newhampshire_ivf = queryset_list_newhampshire.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_newhampshire_ivf.items():
        queryset_list_newhampshire_ivf_val = val

    queryset_list_newhampshire_egg = queryset_list_newhampshire.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_newhampshire_egg.items():
        queryset_list_newhampshire_egg_val = val

    queryset_list_newhampshire_embryo = queryset_list_newhampshire.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_newhampshire_embryo.items():
        queryset_list_newhampshire_embryo_val = val

    queryset_list_newhampshire_sperm = queryset_list_newhampshire.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_newhampshire_sperm.items():
        queryset_list_newhampshire_sperm_val = val

    queryset_list_newhampshire_icsi = queryset_list_newhampshire.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_newhampshire_icsi.items():
        queryset_list_newhampshire_icsi_val = val

    queryset_list_newhampshire_iui = queryset_list_newhampshire.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_newhampshire_iui.items():
        queryset_list_newhampshire_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_newjersey = queryset_list_us.filter(clinicRegion__iexact='New Jersey')
    my_total_clinic_count_newjersey = queryset_list_newjersey.count()

    queryset_list_newjersey_ivf = queryset_list_newjersey.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_newjersey_ivf.items():
        queryset_list_newjersey_ivf_val = val

    queryset_list_newjersey_egg = queryset_list_newjersey.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_newjersey_egg.items():
        queryset_list_newjersey_egg_val = val

    queryset_list_newjersey_embryo = queryset_list_newjersey.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_newjersey_embryo.items():
        queryset_list_newjersey_embryo_val = val

    queryset_list_newjersey_sperm = queryset_list_newjersey.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_newjersey_sperm.items():
        queryset_list_newjersey_sperm_val = val

    queryset_list_newjersey_icsi = queryset_list_newjersey.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_newjersey_icsi.items():
        queryset_list_newjersey_icsi_val = val

    queryset_list_newjersey_iui = queryset_list_newjersey.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_newjersey_iui.items():
        queryset_list_newjersey_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_newmexico = queryset_list_us.filter(clinicRegion__iexact='New Mexico')
    my_total_clinic_count_newmexico = queryset_list_newmexico.count()

    queryset_list_newmexico_ivf = queryset_list_newmexico.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_newmexico_ivf.items():
        queryset_list_newmexico_ivf_val = val

    queryset_list_newmexico_egg = queryset_list_newmexico.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_newmexico_egg.items():
        queryset_list_newmexico_egg_val = val

    queryset_list_newmexico_embryo = queryset_list_newmexico.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_newmexico_embryo.items():
        queryset_list_newmexico_embryo_val = val

    queryset_list_newmexico_sperm = queryset_list_newmexico.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_newmexico_sperm.items():
        queryset_list_newmexico_sperm_val = val

    queryset_list_newmexico_icsi = queryset_list_newmexico.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_newmexico_icsi.items():
        queryset_list_newmexico_icsi_val = val

    queryset_list_newmexico_iui = queryset_list_newmexico.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_newmexico_iui.items():
        queryset_list_newmexico_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_newyork = queryset_list_us.filter(clinicRegion__iexact='New York')
    my_total_clinic_count_newyork = queryset_list_newyork.count()

    queryset_list_newyork_ivf = queryset_list_newyork.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_newyork_ivf.items():
        queryset_list_newyork_ivf_val = val

    queryset_list_newyork_egg = queryset_list_newyork.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_newyork_egg.items():
        queryset_list_newyork_egg_val = val

    queryset_list_newyork_embryo = queryset_list_newyork.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_newyork_embryo.items():
        queryset_list_newyork_embryo_val = val

    queryset_list_newyork_sperm = queryset_list_newyork.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_newyork_sperm.items():
        queryset_list_newyork_sperm_val = val

    queryset_list_newyork_icsi = queryset_list_newyork.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_newyork_icsi.items():
        queryset_list_newyork_icsi_val = val

    queryset_list_newyork_iui = queryset_list_newyork.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_newyork_iui.items():
        queryset_list_newyork_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_northcarolina = queryset_list_us.filter(clinicRegion__iexact='North Carolina')
    my_total_clinic_count_northcarolina = queryset_list_northcarolina.count()

    queryset_list_northcarolina_ivf = queryset_list_northcarolina.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_northcarolina_ivf.items():
        queryset_list_northcarolina_ivf_val = val

    queryset_list_northcarolina_egg = queryset_list_northcarolina.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_northcarolina_egg.items():
        queryset_list_northcarolina_egg_val = val

    queryset_list_northcarolina_embryo = queryset_list_northcarolina.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_northcarolina_embryo.items():
        queryset_list_northcarolina_embryo_val = val

    queryset_list_northcarolina_sperm = queryset_list_northcarolina.aggregate(
        average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_northcarolina_sperm.items():
        queryset_list_northcarolina_sperm_val = val

    queryset_list_northcarolina_icsi = queryset_list_northcarolina.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_northcarolina_icsi.items():
        queryset_list_northcarolina_icsi_val = val

    queryset_list_northcarolina_iui = queryset_list_northcarolina.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_northcarolina_iui.items():
        queryset_list_northcarolina_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_northdakota = queryset_list_us.filter(clinicRegion__iexact='North Dakota')
    my_total_clinic_count_northdakota = queryset_list_northdakota.count()

    queryset_list_northdakota_ivf = queryset_list_northdakota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_northdakota_ivf.items():
        queryset_list_northdakota_ivf_val = val

    queryset_list_northdakota_egg = queryset_list_northdakota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_northdakota_egg.items():
        queryset_list_northdakota_egg_val = val

    queryset_list_northdakota_embryo = queryset_list_northdakota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_northdakota_embryo.items():
        queryset_list_northdakota_embryo_val = val

    queryset_list_northdakota_sperm = queryset_list_northdakota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_northdakota_sperm.items():
        queryset_list_northdakota_sperm_val = val

    queryset_list_northdakota_icsi = queryset_list_northdakota.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_northdakota_icsi.items():
        queryset_list_northdakota_icsi_val = val

    queryset_list_northdakota_iui = queryset_list_northdakota.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_northdakota_iui.items():
        queryset_list_northdakota_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_nevada = queryset_list_us.filter(clinicRegion__iexact='Nevada')
    my_total_clinic_count_nevada = queryset_list_nevada.count()

    queryset_list_nevada_ivf = queryset_list_nevada.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_nevada_ivf.items():
        queryset_list_nevada_ivf_val = val

    queryset_list_nevada_egg = queryset_list_nevada.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_nevada_egg.items():
        queryset_list_nevada_egg_val = val

    queryset_list_nevada_embryo = queryset_list_nevada.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_nevada_embryo.items():
        queryset_list_nevada_embryo_val = val

    queryset_list_nevada_sperm = queryset_list_nevada.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_nevada_sperm.items():
        queryset_list_nevada_sperm_val = val

    queryset_list_nevada_icsi = queryset_list_nevada.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_nevada_icsi.items():
        queryset_list_nevada_icsi_val = val

    queryset_list_nevada_iui = queryset_list_nevada.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_nevada_iui.items():
        queryset_list_nevada_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_ohio = queryset_list_us.filter(clinicRegion__iexact='Ohio')
    my_total_clinic_count_ohio = queryset_list_ohio.count()

    queryset_list_ohio_ivf = queryset_list_ohio.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_ohio_ivf.items():
        queryset_list_ohio_ivf_val = val

    queryset_list_ohio_egg = queryset_list_ohio.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_ohio_egg.items():
        queryset_list_ohio_egg_val = val

    queryset_list_ohio_embryo = queryset_list_ohio.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_ohio_embryo.items():
        queryset_list_ohio_embryo_val = val

    queryset_list_ohio_sperm = queryset_list_ohio.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_ohio_sperm.items():
        queryset_list_ohio_sperm_val = val

    queryset_list_ohio_icsi = queryset_list_ohio.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_ohio_icsi.items():
        queryset_list_ohio_icsi_val = val

    queryset_list_ohio_iui = queryset_list_ohio.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_ohio_iui.items():
        queryset_list_ohio_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_oklahoma = queryset_list_us.filter(clinicRegion__iexact='Oklahoma')
    my_total_clinic_count_oklahoma = queryset_list_oklahoma.count()

    queryset_list_oklahoma_ivf = queryset_list_oklahoma.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_oklahoma_ivf.items():
        queryset_list_oklahoma_ivf_val = val

    queryset_list_oklahoma_egg = queryset_list_oklahoma.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_oklahoma_egg.items():
        queryset_list_oklahoma_egg_val = val

    queryset_list_oklahoma_embryo = queryset_list_oklahoma.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_oklahoma_embryo.items():
        queryset_list_oklahoma_embryo_val = val

    queryset_list_oklahoma_sperm = queryset_list_oklahoma.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_oklahoma_sperm.items():
        queryset_list_oklahoma_sperm_val = val

    queryset_list_oklahoma_icsi = queryset_list_oklahoma.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_oklahoma_icsi.items():
        queryset_list_oklahoma_icsi_val = val

    queryset_list_oklahoma_iui = queryset_list_oklahoma.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_oklahoma_iui.items():
        queryset_list_oklahoma_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_oregon = queryset_list_us.filter(clinicRegion__iexact='Oregon')
    my_total_clinic_count_oregon = queryset_list_oregon.count()

    queryset_list_oregon_ivf = queryset_list_oregon.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_oregon_ivf.items():
        queryset_list_oregon_ivf_val = val

    queryset_list_oregon_egg = queryset_list_oregon.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_oregon_egg.items():
        queryset_list_oregon_egg_val = val

    queryset_list_oregon_embryo = queryset_list_oregon.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_oregon_embryo.items():
        queryset_list_oregon_embryo_val = val

    queryset_list_oregon_sperm = queryset_list_oregon.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_oregon_sperm.items():
        queryset_list_oregon_sperm_val = val

    queryset_list_oregon_icsi = queryset_list_oregon.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_oregon_icsi.items():
        queryset_list_oregon_icsi_val = val

    queryset_list_oregon_iui = queryset_list_oregon.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_oregon_iui.items():
        queryset_list_oregon_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_pennsylvania = queryset_list_us.filter(clinicRegion__iexact='Pennsylvania')
    my_total_clinic_count_pennsylvania = queryset_list_pennsylvania.count()

    queryset_list_pennsylvania_ivf = queryset_list_pennsylvania.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_pennsylvania_ivf.items():
        queryset_list_pennsylvania_ivf_val = val

    queryset_list_pennsylvania_egg = queryset_list_pennsylvania.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_pennsylvania_egg.items():
        queryset_list_pennsylvania_egg_val = val

    queryset_list_pennsylvania_embryo = queryset_list_pennsylvania.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_pennsylvania_embryo.items():
        queryset_list_pennsylvania_embryo_val = val

    queryset_list_pennsylvania_sperm = queryset_list_pennsylvania.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_pennsylvania_sperm.items():
        queryset_list_pennsylvania_sperm_val = val

    queryset_list_pennsylvania_icsi = queryset_list_pennsylvania.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_pennsylvania_icsi.items():
        queryset_list_pennsylvania_icsi_val = val

    queryset_list_pennsylvania_iui = queryset_list_pennsylvania.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_pennsylvania_iui.items():
        queryset_list_pennsylvania_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_puertorico = queryset_list_us.filter(clinicRegion__iexact='Puerto Rico')
    my_total_clinic_count_puertorico = queryset_list_puertorico.count()

    queryset_list_puertorico_ivf = queryset_list_puertorico.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_puertorico_ivf.items():
        queryset_list_puertorico_ivf_val = val

    queryset_list_puertorico_egg = queryset_list_puertorico.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_puertorico_egg.items():
        queryset_list_puertorico_egg_val = val

    queryset_list_puertorico_embryo = queryset_list_puertorico.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_puertorico_embryo.items():
        queryset_list_puertorico_embryo_val = val

    queryset_list_puertorico_sperm = queryset_list_puertorico.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_puertorico_sperm.items():
        queryset_list_puertorico_sperm_val = val

    queryset_list_puertorico_icsi = queryset_list_puertorico.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_puertorico_icsi.items():
        queryset_list_puertorico_icsi_val = val

    queryset_list_puertorico_iui = queryset_list_puertorico.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_puertorico_iui.items():
        queryset_list_puertorico_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_southcarolina = queryset_list_us.filter(clinicRegion__iexact='South Carolina')
    my_total_clinic_count_southcarolina = queryset_list_southcarolina.count()

    queryset_list_southcarolina_ivf = queryset_list_southcarolina.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_southcarolina_ivf.items():
        queryset_list_southcarolina_ivf_val = val

    queryset_list_southcarolina_egg = queryset_list_southcarolina.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_southcarolina_egg.items():
        queryset_list_southcarolina_egg_val = val

    queryset_list_southcarolina_embryo = queryset_list_southcarolina.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_southcarolina_embryo.items():
        queryset_list_southcarolina_embryo_val = val

    queryset_list_southcarolina_sperm = queryset_list_southcarolina.aggregate(
        average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_southcarolina_sperm.items():
        queryset_list_southcarolina_sperm_val = val

    queryset_list_southcarolina_icsi = queryset_list_southcarolina.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_southcarolina_icsi.items():
        queryset_list_southcarolina_icsi_val = val

    queryset_list_southcarolina_iui = queryset_list_southcarolina.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_southcarolina_iui.items():
        queryset_list_southcarolina_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_rhodeisland = queryset_list_us.filter(clinicRegion__iexact='Rhode Island')
    my_total_clinic_count_rhodeisland = queryset_list_rhodeisland.count()

    queryset_list_rhodeisland_ivf = queryset_list_rhodeisland.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_rhodeisland_ivf.items():
        queryset_list_rhodeisland_ivf_val = val

    queryset_list_rhodeisland_egg = queryset_list_rhodeisland.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_rhodeisland_egg.items():
        queryset_list_rhodeisland_egg_val = val

    queryset_list_rhodeisland_embryo = queryset_list_rhodeisland.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_rhodeisland_embryo.items():
        queryset_list_rhodeisland_embryo_val = val

    queryset_list_rhodeisland_sperm = queryset_list_rhodeisland.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_rhodeisland_sperm.items():
        queryset_list_rhodeisland_sperm_val = val

    queryset_list_rhodeisland_icsi = queryset_list_rhodeisland.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_rhodeisland_icsi.items():
        queryset_list_rhodeisland_icsi_val = val

    queryset_list_rhodeisland_iui = queryset_list_rhodeisland.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_rhodeisland_iui.items():
        queryset_list_rhodeisland_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_southdakota = queryset_list_us.filter(clinicRegion__iexact='South Dakota')
    my_total_clinic_count_southdakota = queryset_list_southdakota.count()

    queryset_list_southdakota_ivf = queryset_list_southdakota.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_southdakota_ivf.items():
        queryset_list_southdakota_ivf_val = val

    queryset_list_southdakota_egg = queryset_list_southdakota.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_southdakota_egg.items():
        queryset_list_southdakota_egg_val = val

    queryset_list_southdakota_embryo = queryset_list_southdakota.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_southdakota_embryo.items():
        queryset_list_southdakota_embryo_val = val

    queryset_list_southdakota_sperm = queryset_list_southdakota.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_southdakota_sperm.items():
        queryset_list_southdakota_sperm_val = val

    queryset_list_southdakota_icsi = queryset_list_southdakota.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_southdakota_icsi.items():
        queryset_list_southdakota_icsi_val = val

    queryset_list_southdakota_iui = queryset_list_southdakota.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_southdakota_iui.items():
        queryset_list_southdakota_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_tennessee = queryset_list_us.filter(clinicRegion__iexact='Tennessee')
    my_total_clinic_count_tennessee = queryset_list_tennessee.count()

    queryset_list_tennessee_ivf = queryset_list_tennessee.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_tennessee_ivf.items():
        queryset_list_tennessee_ivf_val = val

    queryset_list_tennessee_egg = queryset_list_tennessee.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_tennessee_egg.items():
        queryset_list_tennessee_egg_val = val

    queryset_list_tennessee_embryo = queryset_list_tennessee.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_tennessee_embryo.items():
        queryset_list_tennessee_embryo_val = val

    queryset_list_tennessee_sperm = queryset_list_tennessee.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_tennessee_sperm.items():
        queryset_list_tennessee_sperm_val = val

    queryset_list_tennessee_icsi = queryset_list_tennessee.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_tennessee_icsi.items():
        queryset_list_tennessee_icsi_val = val

    queryset_list_tennessee_iui = queryset_list_tennessee.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_tennessee_iui.items():
        queryset_list_tennessee_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_texas = queryset_list_us.filter(clinicRegion__iexact='Texas')
    my_total_clinic_count_texas = queryset_list_texas.count()

    queryset_list_texas_ivf = queryset_list_texas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_texas_ivf.items():
        queryset_list_texas_ivf_val = val

    queryset_list_texas_egg = queryset_list_texas.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_texas_egg.items():
        queryset_list_texas_egg_val = val

    queryset_list_texas_embryo = queryset_list_texas.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_texas_embryo.items():
        queryset_list_texas_embryo_val = val

    queryset_list_texas_sperm = queryset_list_texas.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_texas_sperm.items():
        queryset_list_texas_sperm_val = val

    queryset_list_texas_icsi = queryset_list_texas.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_texas_icsi.items():
        queryset_list_texas_icsi_val = val

    queryset_list_texas_iui = queryset_list_texas.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_texas_iui.items():
        queryset_list_texas_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_utah = queryset_list_us.filter(clinicRegion__iexact='Utah')
    my_total_clinic_count_utah = queryset_list_utah.count()

    queryset_list_utah_ivf = queryset_list_utah.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_utah_ivf.items():
        queryset_list_utah_ivf_val = val

    queryset_list_utah_egg = queryset_list_utah.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_utah_egg.items():
        queryset_list_utah_egg_val = val

    queryset_list_utah_embryo = queryset_list_utah.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_utah_embryo.items():
        queryset_list_utah_embryo_val = val

    queryset_list_utah_sperm = queryset_list_utah.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_utah_sperm.items():
        queryset_list_utah_sperm_val = val

    queryset_list_utah_icsi = queryset_list_utah.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_utah_icsi.items():
        queryset_list_utah_icsi_val = val

    queryset_list_utah_iui = queryset_list_utah.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_utah_iui.items():
        queryset_list_utah_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_vermont = queryset_list_us.filter(clinicRegion__iexact='Vermont')
    my_total_clinic_count_vermont = queryset_list_vermont.count()

    queryset_list_vermont_ivf = queryset_list_vermont.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_vermont_ivf.items():
        queryset_list_vermont_ivf_val = val

    queryset_list_vermont_egg = queryset_list_vermont.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_vermont_egg.items():
        queryset_list_vermont_egg_val = val

    queryset_list_vermont_embryo = queryset_list_vermont.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_vermont_embryo.items():
        queryset_list_vermont_embryo_val = val

    queryset_list_vermont_sperm = queryset_list_vermont.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_vermont_sperm.items():
        queryset_list_vermont_sperm_val = val

    queryset_list_vermont_icsi = queryset_list_vermont.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_vermont_icsi.items():
        queryset_list_vermont_icsi_val = val

    queryset_list_vermont_iui = queryset_list_vermont.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_vermont_iui.items():
        queryset_list_vermont_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_virginia = queryset_list_us.filter(clinicRegion__iexact='Virginia')
    my_total_clinic_count_virginia = queryset_list_virginia.count()

    queryset_list_virginia_ivf = queryset_list_virginia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_virginia_ivf.items():
        queryset_list_virginia_ivf_val = val

    queryset_list_virginia_egg = queryset_list_virginia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_virginia_egg.items():
        queryset_list_virginia_egg_val = val

    queryset_list_virginia_embryo = queryset_list_virginia.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_virginia_embryo.items():
        queryset_list_virginia_embryo_val = val

    queryset_list_virginia_sperm = queryset_list_virginia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_virginia_sperm.items():
        queryset_list_virginia_sperm_val = val

    queryset_list_virginia_icsi = queryset_list_virginia.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_virginia_icsi.items():
        queryset_list_virginia_icsi_val = val

    queryset_list_virginia_iui = queryset_list_virginia.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_virginia_iui.items():
        queryset_list_virginia_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_washington = queryset_list_us.filter(clinicRegion__iexact='Washington')
    my_total_clinic_count_washington = queryset_list_washington.count()

    queryset_list_washington_ivf = queryset_list_washington.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_washington_ivf.items():
        queryset_list_washington_ivf_val = val

    queryset_list_washington_egg = queryset_list_washington.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_washington_egg.items():
        queryset_list_washington_egg_val = val

    queryset_list_washington_embryo = queryset_list_washington.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_washington_embryo.items():
        queryset_list_washington_embryo_val = val

    queryset_list_washington_sperm = queryset_list_washington.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_washington_sperm.items():
        queryset_list_washington_sperm_val = val

    queryset_list_washington_icsi = queryset_list_washington.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_washington_icsi.items():
        queryset_list_washington_icsi_val = val

    queryset_list_washington_iui = queryset_list_washington.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_washington_iui.items():
        queryset_list_washington_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_westvirginia = queryset_list_us.filter(clinicRegion__iexact='West Virginia')
    my_total_clinic_count_westvirginia = queryset_list_westvirginia.count()

    queryset_list_westvirginia_ivf = queryset_list_westvirginia.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_westvirginia_ivf.items():
        queryset_list_westvirginia_ivf_val = val

    queryset_list_westvirginia_egg = queryset_list_westvirginia.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_westvirginia_egg.items():
        queryset_list_westvirginia_egg_val = val

    queryset_list_westvirginia_embryo = queryset_list_westvirginia.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_westvirginia_embryo.items():
        queryset_list_westvirginia_embryo_val = val

    queryset_list_westvirginia_sperm = queryset_list_westvirginia.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_westvirginia_sperm.items():
        queryset_list_westvirginia_sperm_val = val

    queryset_list_westvirginia_icsi = queryset_list_westvirginia.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_westvirginia_icsi.items():
        queryset_list_westvirginia_icsi_val = val

    queryset_list_westvirginia_iui = queryset_list_westvirginia.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_westvirginia_iui.items():
        queryset_list_westvirginia_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_wisconsin = queryset_list_us.filter(clinicRegion__iexact='Wisconsin')
    my_total_clinic_count_wisconsin = queryset_list_wisconsin.count()

    queryset_list_wisconsin_ivf = queryset_list_wisconsin.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_wisconsin_ivf.items():
        queryset_list_wisconsin_ivf_val = val

    queryset_list_wisconsin_egg = queryset_list_wisconsin.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_wisconsin_egg.items():
        queryset_list_wisconsin_egg_val = val

    queryset_list_wisconsin_embryo = queryset_list_wisconsin.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_wisconsin_embryo.items():
        queryset_list_wisconsin_embryo_val = val

    queryset_list_wisconsin_sperm = queryset_list_wisconsin.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_wisconsin_sperm.items():
        queryset_list_wisconsin_sperm_val = val

    queryset_list_wisconsin_icsi = queryset_list_wisconsin.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_wisconsin_icsi.items():
        queryset_list_wisconsin_icsi_val = val

    queryset_list_wisconsin_iui = queryset_list_wisconsin.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_wisconsin_iui.items():
        queryset_list_wisconsin_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_wyoming = queryset_list_us.filter(clinicRegion__iexact='Wyoming')
    my_total_clinic_count_wyoming = queryset_list_wyoming.count()

    queryset_list_wyoming_ivf = queryset_list_wyoming.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_wyoming_ivf.items():
        queryset_list_wyoming_ivf_val = val

    queryset_list_wyoming_egg = queryset_list_wyoming.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_wyoming_egg.items():
        queryset_list_wyoming_egg_val = val

    queryset_list_wyoming_embryo = queryset_list_wyoming.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_wyoming_embryo.items():
        queryset_list_wyoming_embryo_val = val

    queryset_list_wyoming_sperm = queryset_list_wyoming.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_wyoming_sperm.items():
        queryset_list_wyoming_sperm_val = val

    queryset_list_wyoming_icsi = queryset_list_wyoming.aggregate(average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_wyoming_icsi.items():
        queryset_list_wyoming_icsi_val = val

    queryset_list_wyoming_iui = queryset_list_wyoming.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_wyoming_iui.items():
        queryset_list_wyoming_iui_val = val

    # --------------------------------------------------------------------------
    queryset_list_districtofcolumbia = queryset_list_us.filter(clinicRegion__iexact='District of Columbia')
    my_total_clinic_count_districtofcolumbia = queryset_list_districtofcolumbia.count()

    queryset_list_districtofcolumbia_ivf = queryset_list_districtofcolumbia.aggregate(
        average=Avg('ovarian_ivf_treatment_cost'))
    for key, val in queryset_list_districtofcolumbia_ivf.items():
        queryset_list_districtofcolumbia_ivf_val = val

    queryset_list_districtofcolumbia_egg = queryset_list_districtofcolumbia.aggregate(
        average=Avg('egg_donor_recipients_cost'))
    for key, val in queryset_list_districtofcolumbia_egg.items():
        queryset_list_districtofcolumbia_egg_val = val

    queryset_list_districtofcolumbia_embryo = queryset_list_districtofcolumbia.aggregate(
        average=Avg('embryo_donor_recipients_cost'))
    for key, val in queryset_list_districtofcolumbia_embryo.items():
        queryset_list_districtofcolumbia_embryo_val = val

    queryset_list_districtofcolumbia_sperm = queryset_list_districtofcolumbia.aggregate(
        average=Avg('sperm_donor_recipients_cost'))
    for key, val in queryset_list_districtofcolumbia_sperm.items():
        queryset_list_districtofcolumbia_sperm_val = val

    queryset_list_districtofcolumbia_icsi = queryset_list_districtofcolumbia.aggregate(
        average=Avg('icsi_treatment_cost'))
    for key, val in queryset_list_districtofcolumbia_icsi.items():
        queryset_list_districtofcolumbia_icsi_val = val

    queryset_list_districtofcolumbia_iui = queryset_list_districtofcolumbia.aggregate(average=Avg('iui_treatment_cost'))
    for key, val in queryset_list_districtofcolumbia_iui.items():
        queryset_list_districtofcolumbia_iui_val = val

    context = {
        'year': year,
        'my_total_clinic_count_usa': my_total_clinic_count_usa,

        'queryset_list_us_natural_ivf_val': queryset_list_us_natural_ivf_val,
        'queryset_list_us_mild_ivf_val': queryset_list_us_mild_ivf_val,
        'queryset_list_us_standard_ivf_val': queryset_list_us_standard_ivf_val,

        'queryset_list_us_egg_ivf_val': queryset_list_us_egg_ivf_val,
        'queryset_list_us_known_egg_ivf_val': queryset_list_us_known_egg_ivf_val,
        'queryset_list_us_shared_egg_ivf_val': queryset_list_us_shared_egg_ivf_val,

        'queryset_list_us_embryo_ivf_val': queryset_list_us_embryo_ivf_val,
        'queryset_list_us_known_embryo_ivf_val': queryset_list_us_known_embryo_ivf_val,

        'queryset_list_us_sperm_ivf_val': queryset_list_us_sperm_ivf_val,
        'queryset_list_us_known_sperm_ivf_val': queryset_list_us_known_sperm_ivf_val,

        'queryset_list_us_icsi_val': queryset_list_us_icsi_val,
        'queryset_list_us_iui_val': queryset_list_us_iui_val,

        'queryset_list_alabama_ivf_val': queryset_list_alabama_ivf_val,
        'queryset_list_alabama_egg_val': queryset_list_alabama_egg_val,
        'queryset_list_alabama_embryo_val': queryset_list_alabama_embryo_val,
        'queryset_list_alabama_sperm_val': queryset_list_alabama_sperm_val,
        'queryset_list_alabama_icsi_val': queryset_list_alabama_icsi_val,
        'queryset_list_alabama_iui_val': queryset_list_alabama_iui_val,

        'queryset_list_arizona_ivf_val': queryset_list_arizona_ivf_val,
        'queryset_list_arizona_egg_val': queryset_list_arizona_egg_val,
        'queryset_list_arizona_embryo_val': queryset_list_arizona_embryo_val,
        'queryset_list_arizona_sperm_val': queryset_list_arizona_sperm_val,
        'queryset_list_arizona_icsi_val': queryset_list_arizona_icsi_val,
        'queryset_list_arizona_iui_val': queryset_list_arizona_iui_val,

        'queryset_list_alaska_ivf_val': queryset_list_alaska_ivf_val,
        'queryset_list_alaska_egg_val': queryset_list_alaska_egg_val,
        'queryset_list_alaska_embryo_val': queryset_list_alaska_embryo_val,
        'queryset_list_alaska_sperm_val': queryset_list_alaska_sperm_val,
        'queryset_list_alaska_icsi_val': queryset_list_alaska_icsi_val,
        'queryset_list_alaska_iui_val': queryset_list_alaska_iui_val,

        'queryset_list_arkansas_ivf_val': queryset_list_arkansas_ivf_val,
        'queryset_list_arkansas_egg_val': queryset_list_arkansas_egg_val,
        'queryset_list_arkansas_embryo_val': queryset_list_arkansas_embryo_val,
        'queryset_list_arkansas_sperm_val': queryset_list_arkansas_sperm_val,
        'queryset_list_arkansas_icsi_val': queryset_list_arkansas_icsi_val,
        'queryset_list_arkansas_iui_val': queryset_list_arkansas_iui_val,

        'queryset_list_california_ivf_val': queryset_list_california_ivf_val,
        'queryset_list_california_egg_val': queryset_list_california_egg_val,
        'queryset_list_california_embryo_val': queryset_list_california_embryo_val,
        'queryset_list_california_sperm_val': queryset_list_california_sperm_val,
        'queryset_list_california_icsi_val': queryset_list_california_icsi_val,
        'queryset_list_california_iui_val': queryset_list_california_iui_val,

        'queryset_list_colorado_ivf_val': queryset_list_colorado_ivf_val,
        'queryset_list_colorado_egg_val': queryset_list_colorado_egg_val,
        'queryset_list_colorado_embryo_val': queryset_list_colorado_embryo_val,
        'queryset_list_colorado_sperm_val': queryset_list_colorado_sperm_val,
        'queryset_list_colorado_icsi_val': queryset_list_colorado_icsi_val,
        'queryset_list_colorado_iui_val': queryset_list_colorado_iui_val,

        'queryset_list_connecticut_ivf_val': queryset_list_connecticut_ivf_val,
        'queryset_list_connecticut_egg_val': queryset_list_connecticut_egg_val,
        'queryset_list_connecticut_embryo_val': queryset_list_connecticut_embryo_val,
        'queryset_list_connecticut_sperm_val': queryset_list_connecticut_sperm_val,
        'queryset_list_connecticut_icsi_val': queryset_list_connecticut_icsi_val,
        'queryset_list_connecticut_iui_val': queryset_list_connecticut_iui_val,

        'queryset_list_delaware_ivf_val': queryset_list_delaware_ivf_val,
        'queryset_list_delaware_egg_val': queryset_list_delaware_egg_val,
        'queryset_list_delaware_embryo_val': queryset_list_delaware_embryo_val,
        'queryset_list_delaware_sperm_val': queryset_list_delaware_sperm_val,
        'queryset_list_delaware_icsi_val': queryset_list_delaware_icsi_val,
        'queryset_list_delaware_iui_val': queryset_list_delaware_iui_val,

        'queryset_list_florida_ivf_val': queryset_list_florida_ivf_val,
        'queryset_list_florida_egg_val': queryset_list_florida_egg_val,
        'queryset_list_florida_embryo_val': queryset_list_florida_embryo_val,
        'queryset_list_florida_sperm_val': queryset_list_florida_sperm_val,
        'queryset_list_florida_icsi_val': queryset_list_florida_icsi_val,
        'queryset_list_florida_iui_val': queryset_list_florida_iui_val,

        'queryset_list_georgia_ivf_val': queryset_list_georgia_ivf_val,
        'queryset_list_georgia_egg_val': queryset_list_georgia_egg_val,
        'queryset_list_georgia_embryo_val': queryset_list_georgia_embryo_val,
        'queryset_list_georgia_sperm_val': queryset_list_georgia_sperm_val,
        'queryset_list_georgia_icsi_val': queryset_list_georgia_icsi_val,
        'queryset_list_georgia_iui_val': queryset_list_georgia_iui_val,

        'queryset_list_hawaii_ivf_val': queryset_list_hawaii_ivf_val,
        'queryset_list_hawaii_egg_val': queryset_list_hawaii_egg_val,
        'queryset_list_hawaii_embryo_val': queryset_list_hawaii_embryo_val,
        'queryset_list_hawaii_sperm_val': queryset_list_hawaii_sperm_val,
        'queryset_list_hawaii_icsi_val': queryset_list_hawaii_icsi_val,
        'queryset_list_hawaii_iui_val': queryset_list_hawaii_iui_val,

        'queryset_list_idaho_ivf_val': queryset_list_idaho_ivf_val,
        'queryset_list_idaho_egg_val': queryset_list_idaho_egg_val,
        'queryset_list_idaho_embryo_val': queryset_list_idaho_embryo_val,
        'queryset_list_idaho_sperm_val': queryset_list_idaho_sperm_val,
        'queryset_list_idaho_icsi_val': queryset_list_idaho_icsi_val,
        'queryset_list_idaho_iui_val': queryset_list_idaho_iui_val,

        'queryset_list_illinois_ivf_val': queryset_list_illinois_ivf_val,
        'queryset_list_illinois_egg_val': queryset_list_illinois_egg_val,
        'queryset_list_illinois_embryo_val': queryset_list_illinois_embryo_val,
        'queryset_list_illinois_sperm_val': queryset_list_illinois_sperm_val,
        'queryset_list_illinois_icsi_val': queryset_list_illinois_icsi_val,
        'queryset_list_illinois_iui_val': queryset_list_illinois_iui_val,

        'queryset_list_indiana_ivf_val': queryset_list_indiana_ivf_val,
        'queryset_list_indiana_egg_val': queryset_list_indiana_egg_val,
        'queryset_list_indiana_embryo_val': queryset_list_indiana_embryo_val,
        'queryset_list_indiana_sperm_val': queryset_list_indiana_sperm_val,
        'queryset_list_indiana_icsi_val': queryset_list_indiana_icsi_val,
        'queryset_list_indiana_iui_val': queryset_list_indiana_iui_val,

        'queryset_list_iowa_ivf_val': queryset_list_iowa_ivf_val,
        'queryset_list_iowa_egg_val': queryset_list_iowa_egg_val,
        'queryset_list_iowa_embryo_val': queryset_list_iowa_embryo_val,
        'queryset_list_iowa_sperm_val': queryset_list_iowa_sperm_val,
        'queryset_list_iowa_icsi_val': queryset_list_iowa_icsi_val,
        'queryset_list_iowa_iui_val': queryset_list_iowa_iui_val,

        'queryset_list_kansas_ivf_val': queryset_list_kansas_ivf_val,
        'queryset_list_kansas_egg_val': queryset_list_kansas_egg_val,
        'queryset_list_kansas_embryo_val': queryset_list_kansas_embryo_val,
        'queryset_list_kansas_sperm_val': queryset_list_kansas_sperm_val,
        'queryset_list_kansas_icsi_val': queryset_list_kansas_icsi_val,
        'queryset_list_kansas_iui_val': queryset_list_kansas_iui_val,

        'queryset_list_kentucky_ivf_val': queryset_list_kentucky_ivf_val,
        'queryset_list_kentucky_egg_val': queryset_list_kentucky_egg_val,
        'queryset_list_kentucky_embryo_val': queryset_list_kentucky_embryo_val,
        'queryset_list_kentucky_sperm_val': queryset_list_kentucky_sperm_val,
        'queryset_list_kentucky_icsi_val': queryset_list_kentucky_icsi_val,
        'queryset_list_kentucky_iui_val': queryset_list_kentucky_iui_val,

        'queryset_list_louisiana_ivf_val': queryset_list_louisiana_ivf_val,
        'queryset_list_louisiana_egg_val': queryset_list_louisiana_egg_val,
        'queryset_list_louisiana_embryo_val': queryset_list_louisiana_embryo_val,
        'queryset_list_louisiana_sperm_val': queryset_list_louisiana_sperm_val,
        'queryset_list_louisiana_icsi_val': queryset_list_louisiana_icsi_val,
        'queryset_list_louisiana_iui_val': queryset_list_louisiana_iui_val,

        'queryset_list_maine_ivf_val': queryset_list_maine_ivf_val,
        'queryset_list_maine_egg_val': queryset_list_maine_egg_val,
        'queryset_list_maine_embryo_val': queryset_list_maine_embryo_val,
        'queryset_list_maine_sperm_val': queryset_list_maine_sperm_val,
        'queryset_list_maine_icsi_val': queryset_list_maine_icsi_val,
        'queryset_list_maine_iui_val': queryset_list_maine_iui_val,

        'queryset_list_maryland_ivf_val': queryset_list_maryland_ivf_val,
        'queryset_list_maryland_egg_val': queryset_list_maryland_egg_val,
        'queryset_list_maryland_embryo_val': queryset_list_maryland_embryo_val,
        'queryset_list_maryland_sperm_val': queryset_list_maryland_sperm_val,
        'queryset_list_maryland_icsi_val': queryset_list_maryland_icsi_val,
        'queryset_list_maryland_iui_val': queryset_list_maryland_iui_val,

        'queryset_list_massachusetts_ivf_val': queryset_list_massachusetts_ivf_val,
        'queryset_list_massachusetts_egg_val': queryset_list_massachusetts_egg_val,
        'queryset_list_massachusetts_embryo_val': queryset_list_massachusetts_embryo_val,
        'queryset_list_massachusetts_sperm_val': queryset_list_massachusetts_sperm_val,
        'queryset_list_massachusetts_icsi_val': queryset_list_massachusetts_icsi_val,
        'queryset_list_massachusetts_iui_val': queryset_list_massachusetts_iui_val,

        'queryset_list_michigan_ivf_val': queryset_list_michigan_ivf_val,
        'queryset_list_michigan_egg_val': queryset_list_michigan_egg_val,
        'queryset_list_michigan_embryo_val': queryset_list_michigan_embryo_val,
        'queryset_list_michigan_sperm_val': queryset_list_michigan_sperm_val,
        'queryset_list_michigan_icsi_val': queryset_list_michigan_icsi_val,
        'queryset_list_michigan_iui_val': queryset_list_michigan_iui_val,

        'queryset_list_minnesota_ivf_val': queryset_list_minnesota_ivf_val,
        'queryset_list_minnesota_egg_val': queryset_list_minnesota_egg_val,
        'queryset_list_minnesota_embryo_val': queryset_list_minnesota_embryo_val,
        'queryset_list_minnesota_sperm_val': queryset_list_minnesota_sperm_val,
        'queryset_list_minnesota_icsi_val': queryset_list_minnesota_icsi_val,
        'queryset_list_minnesota_iui_val': queryset_list_minnesota_iui_val,

        'queryset_list_mississippi_ivf_val': queryset_list_mississippi_ivf_val,
        'queryset_list_mississippi_egg_val': queryset_list_mississippi_egg_val,
        'queryset_list_mississippi_embryo_val': queryset_list_mississippi_embryo_val,
        'queryset_list_mississippi_sperm_val': queryset_list_mississippi_sperm_val,
        'queryset_list_mississippi_icsi_val': queryset_list_mississippi_icsi_val,
        'queryset_list_mississippi_iui_val': queryset_list_mississippi_iui_val,

        'queryset_list_missouri_ivf_val': queryset_list_missouri_ivf_val,
        'queryset_list_missouri_egg_val': queryset_list_missouri_egg_val,
        'queryset_list_missouri_embryo_val': queryset_list_missouri_embryo_val,
        'queryset_list_missouri_sperm_val': queryset_list_missouri_sperm_val,
        'queryset_list_missouri_icsi_val': queryset_list_missouri_icsi_val,
        'queryset_list_missouri_iui_val': queryset_list_missouri_iui_val,

        'queryset_list_montana_ivf_val': queryset_list_montana_ivf_val,
        'queryset_list_montana_egg_val': queryset_list_montana_egg_val,
        'queryset_list_montana_embryo_val': queryset_list_montana_embryo_val,
        'queryset_list_montana_sperm_val': queryset_list_montana_sperm_val,
        'queryset_list_montana_icsi_val': queryset_list_montana_icsi_val,
        'queryset_list_montana_iui_val': queryset_list_montana_iui_val,

        'queryset_list_nebraska_ivf_val': queryset_list_nebraska_ivf_val,
        'queryset_list_nebraska_egg_val': queryset_list_nebraska_egg_val,
        'queryset_list_nebraska_embryo_val': queryset_list_nebraska_embryo_val,
        'queryset_list_nebraska_sperm_val': queryset_list_nebraska_sperm_val,
        'queryset_list_nebraska_icsi_val': queryset_list_nebraska_icsi_val,
        'queryset_list_nebraska_iui_val': queryset_list_nebraska_iui_val,

        'queryset_list_newhampshire_ivf_val': queryset_list_newhampshire_ivf_val,
        'queryset_list_newhampshire_egg_val': queryset_list_newhampshire_egg_val,
        'queryset_list_newhampshire_embryo_val': queryset_list_newhampshire_embryo_val,
        'queryset_list_newhampshire_sperm_val': queryset_list_newhampshire_sperm_val,
        'queryset_list_newhampshire_icsi_val': queryset_list_newhampshire_icsi_val,
        'queryset_list_newhampshire_iui_val': queryset_list_newhampshire_iui_val,

        'queryset_list_newjersey_ivf_val': queryset_list_newjersey_ivf_val,
        'queryset_list_newjersey_egg_val': queryset_list_newjersey_egg_val,
        'queryset_list_newjersey_embryo_val': queryset_list_newjersey_embryo_val,
        'queryset_list_newjersey_sperm_val': queryset_list_newjersey_sperm_val,
        'queryset_list_newjersey_icsi_val': queryset_list_newjersey_icsi_val,
        'queryset_list_newjersey_iui_val': queryset_list_newjersey_iui_val,

        'queryset_list_newmexico_ivf_val': queryset_list_newmexico_ivf_val,
        'queryset_list_newmexico_egg_val': queryset_list_newmexico_egg_val,
        'queryset_list_newmexico_embryo_val': queryset_list_newmexico_embryo_val,
        'queryset_list_newmexico_sperm_val': queryset_list_newmexico_sperm_val,
        'queryset_list_newmexico_icsi_val': queryset_list_newmexico_icsi_val,
        'queryset_list_newmexico_iui_val': queryset_list_newmexico_iui_val,

        'queryset_list_newyork_ivf_val': queryset_list_newyork_ivf_val,
        'queryset_list_newyork_egg_val': queryset_list_newyork_egg_val,
        'queryset_list_newyork_embryo_val': queryset_list_newyork_embryo_val,
        'queryset_list_newyork_sperm_val': queryset_list_newyork_sperm_val,
        'queryset_list_newyork_icsi_val': queryset_list_newyork_icsi_val,
        'queryset_list_newyork_iui_val': queryset_list_newyork_iui_val,

        'queryset_list_northcarolina_ivf_val': queryset_list_northcarolina_ivf_val,
        'queryset_list_northcarolina_egg_val': queryset_list_northcarolina_egg_val,
        'queryset_list_northcarolina_embryo_val': queryset_list_northcarolina_embryo_val,
        'queryset_list_northcarolina_sperm_val': queryset_list_northcarolina_sperm_val,
        'queryset_list_northcarolina_icsi_val': queryset_list_northcarolina_icsi_val,
        'queryset_list_northcarolina_iui_val': queryset_list_northcarolina_iui_val,

        'queryset_list_northdakota_ivf_val': queryset_list_northdakota_ivf_val,
        'queryset_list_northdakota_egg_val': queryset_list_northdakota_egg_val,
        'queryset_list_northdakota_embryo_val': queryset_list_northdakota_embryo_val,
        'queryset_list_northdakota_sperm_val': queryset_list_northdakota_sperm_val,
        'queryset_list_northdakota_icsi_val': queryset_list_northdakota_icsi_val,
        'queryset_list_northdakota_iui_val': queryset_list_northdakota_iui_val,

        'queryset_list_nevada_ivf_val': queryset_list_nevada_ivf_val,
        'queryset_list_nevada_egg_val': queryset_list_nevada_egg_val,
        'queryset_list_nevada_embryo_val': queryset_list_nevada_embryo_val,
        'queryset_list_nevada_sperm_val': queryset_list_nevada_sperm_val,
        'queryset_list_nevada_icsi_val': queryset_list_nevada_icsi_val,
        'queryset_list_nevada_iui_val': queryset_list_nevada_iui_val,

        'queryset_list_ohio_ivf_val': queryset_list_ohio_ivf_val,
        'queryset_list_ohio_egg_val': queryset_list_ohio_egg_val,
        'queryset_list_ohio_embryo_val': queryset_list_ohio_embryo_val,
        'queryset_list_ohio_sperm_val': queryset_list_ohio_sperm_val,
        'queryset_list_ohio_icsi_val': queryset_list_ohio_icsi_val,
        'queryset_list_ohio_iui_val': queryset_list_ohio_iui_val,

        'queryset_list_oklahoma_ivf_val': queryset_list_oklahoma_ivf_val,
        'queryset_list_oklahoma_egg_val': queryset_list_oklahoma_egg_val,
        'queryset_list_oklahoma_embryo_val': queryset_list_oklahoma_embryo_val,
        'queryset_list_oklahoma_sperm_val': queryset_list_oklahoma_sperm_val,
        'queryset_list_oklahoma_icsi_val': queryset_list_oklahoma_icsi_val,
        'queryset_list_oklahoma_iui_val': queryset_list_oklahoma_iui_val,

        'queryset_list_oregon_ivf_val': queryset_list_oregon_ivf_val,
        'queryset_list_oregon_egg_val': queryset_list_oregon_egg_val,
        'queryset_list_oregon_embryo_val': queryset_list_oregon_embryo_val,
        'queryset_list_oregon_sperm_val': queryset_list_oregon_sperm_val,
        'queryset_list_oregon_icsi_val': queryset_list_oregon_icsi_val,
        'queryset_list_oregon_iui_val': queryset_list_oregon_iui_val,

        'queryset_list_pennsylvania_ivf_val': queryset_list_pennsylvania_ivf_val,
        'queryset_list_pennsylvania_egg_val': queryset_list_pennsylvania_egg_val,
        'queryset_list_pennsylvania_embryo_val': queryset_list_pennsylvania_embryo_val,
        'queryset_list_pennsylvania_sperm_val': queryset_list_pennsylvania_sperm_val,
        'queryset_list_pennsylvania_icsi_val': queryset_list_pennsylvania_icsi_val,
        'queryset_list_pennsylvania_iui_val': queryset_list_pennsylvania_iui_val,

        'queryset_list_puertorico_ivf_val': queryset_list_puertorico_ivf_val,
        'queryset_list_puertorico_egg_val': queryset_list_puertorico_egg_val,
        'queryset_list_puertorico_embryo_val': queryset_list_puertorico_embryo_val,
        'queryset_list_puertorico_sperm_val': queryset_list_puertorico_sperm_val,
        'queryset_list_puertorico_icsi_val': queryset_list_puertorico_icsi_val,
        'queryset_list_puertorico_iui_val': queryset_list_puertorico_iui_val,

        'queryset_list_rhodeisland_ivf_val': queryset_list_rhodeisland_ivf_val,
        'queryset_list_rhodeisland_egg_val': queryset_list_rhodeisland_egg_val,
        'queryset_list_rhodeisland_embryo_val': queryset_list_rhodeisland_embryo_val,
        'queryset_list_rhodeisland_sperm_val': queryset_list_rhodeisland_sperm_val,
        'queryset_list_rhodeisland_icsi_val': queryset_list_rhodeisland_icsi_val,
        'queryset_list_rhodeisland_iui_val': queryset_list_rhodeisland_iui_val,

        'queryset_list_southcarolina_ivf_val': queryset_list_southcarolina_ivf_val,
        'queryset_list_southcarolina_egg_val': queryset_list_southcarolina_egg_val,
        'queryset_list_southcarolina_embryo_val': queryset_list_southcarolina_embryo_val,
        'queryset_list_southcarolina_sperm_val': queryset_list_southcarolina_sperm_val,
        'queryset_list_southcarolina_icsi_val': queryset_list_southcarolina_icsi_val,
        'queryset_list_southcarolina_iui_val': queryset_list_southcarolina_iui_val,

        'queryset_list_southdakota_ivf_val': queryset_list_southdakota_ivf_val,
        'queryset_list_southdakota_egg_val': queryset_list_southdakota_egg_val,
        'queryset_list_southdakota_embryo_val': queryset_list_southdakota_embryo_val,
        'queryset_list_southdakota_sperm_val': queryset_list_southdakota_sperm_val,
        'queryset_list_southdakota_icsi_val': queryset_list_southdakota_icsi_val,
        'queryset_list_southdakota_iui_val': queryset_list_southdakota_iui_val,

        'queryset_list_tennessee_ivf_val': queryset_list_tennessee_ivf_val,
        'queryset_list_tennessee_egg_val': queryset_list_tennessee_egg_val,
        'queryset_list_tennessee_embryo_val': queryset_list_tennessee_embryo_val,
        'queryset_list_tennessee_sperm_val': queryset_list_tennessee_sperm_val,
        'queryset_list_tennessee_icsi_val': queryset_list_tennessee_icsi_val,
        'queryset_list_tennessee_iui_val': queryset_list_tennessee_iui_val,

        'queryset_list_texas_ivf_val': queryset_list_texas_ivf_val,
        'queryset_list_texas_egg_val': queryset_list_texas_egg_val,
        'queryset_list_texas_embryo_val': queryset_list_texas_embryo_val,
        'queryset_list_texas_sperm_val': queryset_list_texas_sperm_val,
        'queryset_list_texas_icsi_val': queryset_list_texas_icsi_val,
        'queryset_list_texas_iui_val': queryset_list_texas_iui_val,

        'queryset_list_utah_ivf_val': queryset_list_utah_ivf_val,
        'queryset_list_utah_egg_val': queryset_list_utah_egg_val,
        'queryset_list_utah_embryo_val': queryset_list_utah_embryo_val,
        'queryset_list_utah_sperm_val': queryset_list_utah_sperm_val,
        'queryset_list_utah_icsi_val': queryset_list_utah_icsi_val,
        'queryset_list_utah_iui_val': queryset_list_utah_iui_val,

        'queryset_list_vermont_ivf_val': queryset_list_vermont_ivf_val,
        'queryset_list_vermont_egg_val': queryset_list_vermont_egg_val,
        'queryset_list_vermont_embryo_val': queryset_list_vermont_embryo_val,
        'queryset_list_vermont_sperm_val': queryset_list_vermont_sperm_val,
        'queryset_list_vermont_icsi_val': queryset_list_vermont_icsi_val,
        'queryset_list_vermont_iui_val': queryset_list_vermont_iui_val,

        'queryset_list_virginia_ivf_val': queryset_list_virginia_ivf_val,
        'queryset_list_virginia_egg_val': queryset_list_virginia_egg_val,
        'queryset_list_virginia_embryo_val': queryset_list_virginia_embryo_val,
        'queryset_list_virginia_sperm_val': queryset_list_virginia_sperm_val,
        'queryset_list_virginia_icsi_val': queryset_list_virginia_icsi_val,
        'queryset_list_virginia_iui_val': queryset_list_virginia_iui_val,

        'queryset_list_washington_ivf_val': queryset_list_washington_ivf_val,
        'queryset_list_washington_egg_val': queryset_list_washington_egg_val,
        'queryset_list_washington_embryo_val': queryset_list_washington_embryo_val,
        'queryset_list_washington_sperm_val': queryset_list_washington_sperm_val,
        'queryset_list_washington_icsi_val': queryset_list_washington_icsi_val,
        'queryset_list_washington_iui_val': queryset_list_washington_iui_val,

        'queryset_list_westvirginia_ivf_val': queryset_list_westvirginia_ivf_val,
        'queryset_list_westvirginia_egg_val': queryset_list_westvirginia_egg_val,
        'queryset_list_westvirginia_embryo_val': queryset_list_westvirginia_embryo_val,
        'queryset_list_westvirginia_sperm_val': queryset_list_westvirginia_sperm_val,
        'queryset_list_westvirginia_icsi_val': queryset_list_westvirginia_icsi_val,
        'queryset_list_westvirginia_iui_val': queryset_list_westvirginia_iui_val,

        'queryset_list_wisconsin_ivf_val': queryset_list_wisconsin_ivf_val,
        'queryset_list_wisconsin_egg_val': queryset_list_wisconsin_egg_val,
        'queryset_list_wisconsin_embryo_val': queryset_list_wisconsin_embryo_val,
        'queryset_list_wisconsin_sperm_val': queryset_list_wisconsin_sperm_val,
        'queryset_list_wisconsin_icsi_val': queryset_list_wisconsin_icsi_val,
        'queryset_list_wisconsin_iui_val': queryset_list_wisconsin_iui_val,

        'queryset_list_wyoming_ivf_val': queryset_list_wyoming_ivf_val,
        'queryset_list_wyoming_egg_val': queryset_list_wyoming_egg_val,
        'queryset_list_wyoming_embryo_val': queryset_list_wyoming_embryo_val,
        'queryset_list_wyoming_sperm_val': queryset_list_wyoming_sperm_val,
        'queryset_list_wyoming_icsi_val': queryset_list_wyoming_icsi_val,
        'queryset_list_wyoming_iui_val': queryset_list_wyoming_iui_val,

        'queryset_list_districtofcolumbia_ivf_val': queryset_list_districtofcolumbia_ivf_val,
        'queryset_list_districtofcolumbia_egg_val': queryset_list_districtofcolumbia_egg_val,
        'queryset_list_districtofcolumbia_embryo_val': queryset_list_districtofcolumbia_embryo_val,
        'queryset_list_districtofcolumbia_sperm_val': queryset_list_districtofcolumbia_sperm_val,
        'queryset_list_districtofcolumbia_icsi_val': queryset_list_districtofcolumbia_icsi_val,
        'queryset_list_districtofcolumbia_iui_val': queryset_list_districtofcolumbia_iui_val,

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

