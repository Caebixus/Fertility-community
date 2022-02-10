from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.north_america_region_models import *
from django.apps import apps


def locationsUSRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'United States'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    us_average_costs_model = AverageTreatmentCostUsa.objects.get(pk=1)

    queryset_list_us_natural_ivf_val = us_average_costs_model.natural_ivf_val
    queryset_list_us_mild_ivf_val = us_average_costs_model.mild_ivf_val
    queryset_list_us_standard_ivf_val = us_average_costs_model.standard_ivf_val
    queryset_list_us_egg_ivf_val = us_average_costs_model.egg_ivf_val
    queryset_list_us_known_egg_ivf_val = us_average_costs_model.known_egg_ivf_val
    queryset_list_us_shared_egg_ivf_val = us_average_costs_model.shared_egg_ivf_val
    queryset_list_us_embryo_ivf_val = us_average_costs_model.embryo_ivf_val
    queryset_list_us_known_embryo_ivf_val = us_average_costs_model.known_embryo_ivf_val
    queryset_list_us_sperm_ivf_val = us_average_costs_model.sperm_ivf_val
    queryset_list_us_known_sperm_ivf_val = us_average_costs_model.known_sperm_ivf_val
    queryset_list_us_icsi_val = us_average_costs_model.icsi_val
    queryset_list_us_iui_val = us_average_costs_model.iui_val



    queryset_list_us = BasicClinic.objects.all().exclude(is_published=False)

    queryset_list_alabama = queryset_list_us.filter(clinicRegion__iexact='Alabama')
    my_total_clinic_count_alabama = queryset_list_alabama.count()
    alabama_average_costs_model = Alabama.objects.get(pk=1)
    queryset_list_alabama_ivf_val = alabama_average_costs_model.standard_ivf_val
    queryset_list_alabama_egg_val = alabama_average_costs_model.egg_ivf_val
    queryset_list_alabama_embryo_val = alabama_average_costs_model.embryo_ivf_val
    queryset_list_alabama_sperm_val = alabama_average_costs_model.sperm_ivf_val
    queryset_list_alabama_icsi_val = alabama_average_costs_model.icsi_val
    queryset_list_alabama_iui_val = alabama_average_costs_model.iui_val

    queryset_list_alaska = queryset_list_us.filter(clinicRegion__iexact='Alaska')
    my_total_clinic_count_alaska = queryset_list_alaska.count()
    alaska_average_costs_model = Alaska.objects.get(pk=1)
    queryset_list_alaska_ivf_val = alaska_average_costs_model.standard_ivf_val
    queryset_list_alaska_egg_val = alaska_average_costs_model.egg_ivf_val
    queryset_list_alaska_embryo_val = alaska_average_costs_model.embryo_ivf_val
    queryset_list_alaska_sperm_val = alaska_average_costs_model.sperm_ivf_val
    queryset_list_alaska_icsi_val = alaska_average_costs_model.icsi_val
    queryset_list_alaska_iui_val = alaska_average_costs_model.iui_val

    queryset_list_arizona = queryset_list_us.filter(clinicRegion__iexact='Arizona')
    my_total_clinic_count_arizona = queryset_list_arizona.count()
    arizona_average_costs_model = Arizona.objects.get(pk=1)
    queryset_list_arizona_ivf_val = arizona_average_costs_model.standard_ivf_val
    queryset_list_arizona_egg_val = arizona_average_costs_model.egg_ivf_val
    queryset_list_arizona_embryo_val = arizona_average_costs_model.embryo_ivf_val
    queryset_list_arizona_sperm_val = arizona_average_costs_model.sperm_ivf_val
    queryset_list_arizona_icsi_val = arizona_average_costs_model.icsi_val
    queryset_list_arizona_iui_val = arizona_average_costs_model.iui_val

    queryset_list_arkansas = queryset_list_us.filter(clinicRegion__iexact='Arkansas')
    my_total_clinic_count_arkansas = queryset_list_arkansas.count()
    arkansas_average_costs_model = Arkansas.objects.get(pk=1)
    queryset_list_arkansas_ivf_val = arkansas_average_costs_model.standard_ivf_val
    queryset_list_arkansas_egg_val = arkansas_average_costs_model.egg_ivf_val
    queryset_list_arkansas_embryo_val = arkansas_average_costs_model.embryo_ivf_val
    queryset_list_arkansas_sperm_val = arkansas_average_costs_model.sperm_ivf_val
    queryset_list_arkansas_icsi_val = arkansas_average_costs_model.icsi_val
    queryset_list_arkansas_iui_val = arkansas_average_costs_model.iui_val

    queryset_list_california = queryset_list_us.filter(clinicRegion__iexact='California')
    my_total_clinic_count_california = queryset_list_california.count()
    california_average_costs_model = California.objects.get(pk=1)
    queryset_list_california_ivf_val = california_average_costs_model.standard_ivf_val
    queryset_list_california_egg_val = california_average_costs_model.egg_ivf_val
    queryset_list_california_embryo_val = california_average_costs_model.embryo_ivf_val
    queryset_list_california_sperm_val = california_average_costs_model.sperm_ivf_val
    queryset_list_california_icsi_val = california_average_costs_model.icsi_val
    queryset_list_california_iui_val = california_average_costs_model.iui_val

    queryset_list_colorado = queryset_list_us.filter(clinicRegion__iexact='Colorado')
    my_total_clinic_count_colorado = queryset_list_colorado.count()
    colorado_average_costs_model = Colorado.objects.get(pk=1)
    queryset_list_colorado_ivf_val = colorado_average_costs_model.standard_ivf_val
    queryset_list_colorado_egg_val = colorado_average_costs_model.egg_ivf_val
    queryset_list_colorado_embryo_val = colorado_average_costs_model.embryo_ivf_val
    queryset_list_colorado_sperm_val = colorado_average_costs_model.sperm_ivf_val
    queryset_list_colorado_icsi_val = colorado_average_costs_model.icsi_val
    queryset_list_colorado_iui_val = colorado_average_costs_model.iui_val

    queryset_list_connecticut = queryset_list_us.filter(clinicRegion__iexact='Connecticut')
    my_total_clinic_count_connecticut = queryset_list_connecticut.count()
    connecticut_average_costs_model = Connecticut.objects.get(pk=1)
    queryset_list_connecticut_ivf_val = connecticut_average_costs_model.standard_ivf_val
    queryset_list_connecticut_egg_val = connecticut_average_costs_model.egg_ivf_val
    queryset_list_connecticut_embryo_val = connecticut_average_costs_model.embryo_ivf_val
    queryset_list_connecticut_sperm_val = connecticut_average_costs_model.sperm_ivf_val
    queryset_list_connecticut_icsi_val = connecticut_average_costs_model.icsi_val
    queryset_list_connecticut_iui_val = connecticut_average_costs_model.iui_val

    queryset_list_delaware = queryset_list_us.filter(clinicRegion__iexact='Delaware')
    my_total_clinic_count_delaware = queryset_list_delaware.count()
    delaware_average_costs_model = Delaware.objects.get(pk=1)
    queryset_list_delaware_ivf_val = delaware_average_costs_model.standard_ivf_val
    queryset_list_delaware_egg_val = delaware_average_costs_model.egg_ivf_val
    queryset_list_delaware_embryo_val = delaware_average_costs_model.embryo_ivf_val
    queryset_list_delaware_sperm_val = delaware_average_costs_model.sperm_ivf_val
    queryset_list_delaware_icsi_val = delaware_average_costs_model.icsi_val
    queryset_list_delaware_iui_val = delaware_average_costs_model.iui_val

    queryset_list_florida = queryset_list_us.filter(clinicRegion__iexact='Florida')
    my_total_clinic_count_florida = queryset_list_florida.count()
    florida_average_costs_model = Florida.objects.get(pk=1)
    queryset_list_florida_ivf_val = florida_average_costs_model.standard_ivf_val
    queryset_list_florida_egg_val = florida_average_costs_model.egg_ivf_val
    queryset_list_florida_embryo_val = florida_average_costs_model.embryo_ivf_val
    queryset_list_florida_sperm_val = florida_average_costs_model.sperm_ivf_val
    queryset_list_florida_icsi_val = florida_average_costs_model.icsi_val
    queryset_list_florida_iui_val = florida_average_costs_model.iui_val

    queryset_list_georgia = queryset_list_us.filter(clinicRegion__iexact='Georgia')
    my_total_clinic_count_georgia = queryset_list_georgia.count()
    georgia_average_costs_model = Georgia.objects.get(pk=1)
    queryset_list_georgia_ivf_val = georgia_average_costs_model.standard_ivf_val
    queryset_list_georgia_egg_val = georgia_average_costs_model.egg_ivf_val
    queryset_list_georgia_embryo_val = georgia_average_costs_model.embryo_ivf_val
    queryset_list_georgia_sperm_val = georgia_average_costs_model.sperm_ivf_val
    queryset_list_georgia_icsi_val = georgia_average_costs_model.icsi_val
    queryset_list_georgia_iui_val = georgia_average_costs_model.iui_val

    queryset_list_hawaii = queryset_list_us.filter(clinicRegion__iexact='Hawaii')
    my_total_clinic_count_hawaii = queryset_list_hawaii.count()
    hawaii_average_costs_model = Hawaii.objects.get(pk=1)
    queryset_list_hawaii_ivf_val = hawaii_average_costs_model.standard_ivf_val
    queryset_list_hawaii_egg_val = hawaii_average_costs_model.egg_ivf_val
    queryset_list_hawaii_embryo_val = hawaii_average_costs_model.embryo_ivf_val
    queryset_list_hawaii_sperm_val = hawaii_average_costs_model.sperm_ivf_val
    queryset_list_hawaii_icsi_val = hawaii_average_costs_model.icsi_val
    queryset_list_hawaii_iui_val = hawaii_average_costs_model.iui_val

    queryset_list_idaho = queryset_list_us.filter(clinicRegion__iexact='Idaho')
    my_total_clinic_count_idaho = queryset_list_idaho.count()
    idaho_average_costs_model = Idaho.objects.get(pk=1)
    queryset_list_idaho_ivf_val = idaho_average_costs_model.standard_ivf_val
    queryset_list_idaho_egg_val = idaho_average_costs_model.egg_ivf_val
    queryset_list_idaho_embryo_val = idaho_average_costs_model.embryo_ivf_val
    queryset_list_idaho_sperm_val = idaho_average_costs_model.sperm_ivf_val
    queryset_list_idaho_icsi_val = idaho_average_costs_model.icsi_val
    queryset_list_idaho_iui_val = idaho_average_costs_model.iui_val

    queryset_list_illinois = queryset_list_us.filter(clinicRegion__iexact='Illinois')
    my_total_clinic_count_illinois = queryset_list_illinois.count()
    illinois_average_costs_model = Illinois.objects.get(pk=1)
    queryset_list_illinois_ivf_val = illinois_average_costs_model.standard_ivf_val
    queryset_list_illinois_egg_val = illinois_average_costs_model.egg_ivf_val
    queryset_list_illinois_embryo_val = illinois_average_costs_model.embryo_ivf_val
    queryset_list_illinois_sperm_val = illinois_average_costs_model.sperm_ivf_val
    queryset_list_illinois_icsi_val = illinois_average_costs_model.icsi_val
    queryset_list_illinois_iui_val = illinois_average_costs_model.iui_val

    queryset_list_indiana = queryset_list_us.filter(clinicRegion__iexact='Indiana')
    my_total_clinic_count_indiana = queryset_list_indiana.count()
    indiana_average_costs_model = Indiana.objects.get(pk=1)
    queryset_list_indiana_ivf_val = indiana_average_costs_model.standard_ivf_val
    queryset_list_indiana_egg_val = indiana_average_costs_model.egg_ivf_val
    queryset_list_indiana_embryo_val = indiana_average_costs_model.embryo_ivf_val
    queryset_list_indiana_sperm_val = indiana_average_costs_model.sperm_ivf_val
    queryset_list_indiana_icsi_val = indiana_average_costs_model.icsi_val
    queryset_list_indiana_iui_val = indiana_average_costs_model.iui_val

    queryset_list_iowa = queryset_list_us.filter(clinicRegion__iexact='Iowa')
    my_total_clinic_count_iowa = queryset_list_iowa.count()
    iowa_average_costs_model = Iowa.objects.get(pk=1)
    queryset_list_iowa_ivf_val = iowa_average_costs_model.standard_ivf_val
    queryset_list_iowa_egg_val = iowa_average_costs_model.egg_ivf_val
    queryset_list_iowa_embryo_val = iowa_average_costs_model.embryo_ivf_val
    queryset_list_iowa_sperm_val = iowa_average_costs_model.sperm_ivf_val
    queryset_list_iowa_icsi_val = iowa_average_costs_model.icsi_val
    queryset_list_iowa_iui_val = iowa_average_costs_model.iui_val

    queryset_list_kansas = queryset_list_us.filter(clinicRegion__iexact='Kansas')
    my_total_clinic_count_kansas = queryset_list_kansas.count()
    kansas_average_costs_model = Kansas.objects.get(pk=1)
    queryset_list_kansas_ivf_val = kansas_average_costs_model.standard_ivf_val
    queryset_list_kansas_egg_val = kansas_average_costs_model.egg_ivf_val
    queryset_list_kansas_embryo_val = kansas_average_costs_model.embryo_ivf_val
    queryset_list_kansas_sperm_val = kansas_average_costs_model.sperm_ivf_val
    queryset_list_kansas_icsi_val = kansas_average_costs_model.icsi_val
    queryset_list_kansas_iui_val = kansas_average_costs_model.iui_val

    queryset_list_kentucky = queryset_list_us.filter(clinicRegion__iexact='Kentucky')
    my_total_clinic_count_kentucky = queryset_list_kentucky.count()
    kentucky_average_costs_model = Kentucky.objects.get(pk=1)
    queryset_list_kentucky_ivf_val = kentucky_average_costs_model.standard_ivf_val
    queryset_list_kentucky_egg_val = kentucky_average_costs_model.egg_ivf_val
    queryset_list_kentucky_embryo_val = kentucky_average_costs_model.embryo_ivf_val
    queryset_list_kentucky_sperm_val = kentucky_average_costs_model.sperm_ivf_val
    queryset_list_kentucky_icsi_val = kentucky_average_costs_model.icsi_val
    queryset_list_kentucky_iui_val = kentucky_average_costs_model.iui_val

    queryset_list_louisiana = queryset_list_us.filter(clinicRegion__iexact='Louisiana')
    my_total_clinic_count_louisiana = queryset_list_louisiana.count()
    louisiana_average_costs_model = Louisiana.objects.get(pk=1)
    queryset_list_louisiana_ivf_val = louisiana_average_costs_model.standard_ivf_val
    queryset_list_louisiana_egg_val = louisiana_average_costs_model.egg_ivf_val
    queryset_list_louisiana_embryo_val = louisiana_average_costs_model.embryo_ivf_val
    queryset_list_louisiana_sperm_val = louisiana_average_costs_model.sperm_ivf_val
    queryset_list_louisiana_icsi_val = louisiana_average_costs_model.icsi_val
    queryset_list_louisiana_iui_val = louisiana_average_costs_model.iui_val

    queryset_list_maine = queryset_list_us.filter(clinicRegion__iexact='Maine')
    my_total_clinic_count_maine = queryset_list_maine.count()
    maine_average_costs_model = Maine.objects.get(pk=1)
    queryset_list_maine_ivf_val = maine_average_costs_model.standard_ivf_val
    queryset_list_maine_egg_val = maine_average_costs_model.egg_ivf_val
    queryset_list_maine_embryo_val = maine_average_costs_model.embryo_ivf_val
    queryset_list_maine_sperm_val = maine_average_costs_model.sperm_ivf_val
    queryset_list_maine_icsi_val = maine_average_costs_model.icsi_val
    queryset_list_maine_iui_val = maine_average_costs_model.iui_val

    queryset_list_maryland = queryset_list_us.filter(clinicRegion__iexact='Maryland')
    my_total_clinic_count_maryland = queryset_list_maryland.count()
    maryland_average_costs_model = Maryland.objects.get(pk=1)
    queryset_list_maryland_ivf_val = maryland_average_costs_model.standard_ivf_val
    queryset_list_maryland_egg_val = maryland_average_costs_model.egg_ivf_val
    queryset_list_maryland_embryo_val = maryland_average_costs_model.embryo_ivf_val
    queryset_list_maryland_sperm_val = maryland_average_costs_model.sperm_ivf_val
    queryset_list_maryland_icsi_val = maryland_average_costs_model.icsi_val
    queryset_list_maryland_iui_val = maryland_average_costs_model.iui_val

    queryset_list_massachusetts = queryset_list_us.filter(clinicRegion__iexact='Massachusetts')
    my_total_clinic_count_massachusetts = queryset_list_massachusetts.count()
    massachusetts_average_costs_model = Massachusetts.objects.get(pk=1)
    queryset_list_massachusetts_ivf_val = massachusetts_average_costs_model.standard_ivf_val
    queryset_list_massachusetts_egg_val = massachusetts_average_costs_model.egg_ivf_val
    queryset_list_massachusetts_embryo_val = massachusetts_average_costs_model.embryo_ivf_val
    queryset_list_massachusetts_sperm_val = massachusetts_average_costs_model.sperm_ivf_val
    queryset_list_massachusetts_icsi_val = massachusetts_average_costs_model.icsi_val
    queryset_list_massachusetts_iui_val = massachusetts_average_costs_model.iui_val

    queryset_list_michigan = queryset_list_us.filter(clinicRegion__iexact='Michigan')
    my_total_clinic_count_michigan = queryset_list_michigan.count()
    michigan_average_costs_model = Michigan.objects.get(pk=1)
    queryset_list_michigan_ivf_val = michigan_average_costs_model.standard_ivf_val
    queryset_list_michigan_egg_val = michigan_average_costs_model.egg_ivf_val
    queryset_list_michigan_embryo_val = michigan_average_costs_model.embryo_ivf_val
    queryset_list_michigan_sperm_val = michigan_average_costs_model.sperm_ivf_val
    queryset_list_michigan_icsi_val = michigan_average_costs_model.icsi_val
    queryset_list_michigan_iui_val = michigan_average_costs_model.iui_val

    queryset_list_minnesota = queryset_list_us.filter(clinicRegion__iexact='Minnesota')
    my_total_clinic_count_minnesota = queryset_list_minnesota.count()
    minnesota_average_costs_model = Minnesota.objects.get(pk=1)
    queryset_list_minnesota_ivf_val = minnesota_average_costs_model.standard_ivf_val
    queryset_list_minnesota_egg_val = minnesota_average_costs_model.egg_ivf_val
    queryset_list_minnesota_embryo_val = minnesota_average_costs_model.embryo_ivf_val
    queryset_list_minnesota_sperm_val = minnesota_average_costs_model.sperm_ivf_val
    queryset_list_minnesota_icsi_val = minnesota_average_costs_model.icsi_val
    queryset_list_minnesota_iui_val = minnesota_average_costs_model.iui_val

    queryset_list_mississippi = queryset_list_us.filter(clinicRegion__iexact='Mississippi')
    my_total_clinic_count_mississippi = queryset_list_mississippi.count()
    mississippi_average_costs_model = Mississippi.objects.get(pk=1)
    queryset_list_mississippi_ivf_val = mississippi_average_costs_model.standard_ivf_val
    queryset_list_mississippi_egg_val = mississippi_average_costs_model.egg_ivf_val
    queryset_list_mississippi_embryo_val = mississippi_average_costs_model.embryo_ivf_val
    queryset_list_mississippi_sperm_val = mississippi_average_costs_model.sperm_ivf_val
    queryset_list_mississippi_icsi_val = mississippi_average_costs_model.icsi_val
    queryset_list_mississippi_iui_val = mississippi_average_costs_model.iui_val

    queryset_list_missouri = queryset_list_us.filter(clinicRegion__iexact='Missouri')
    my_total_clinic_count_missouri = queryset_list_missouri.count()
    missouri_average_costs_model = Missouri.objects.get(pk=1)
    queryset_list_missouri_ivf_val = missouri_average_costs_model.standard_ivf_val
    queryset_list_missouri_egg_val = missouri_average_costs_model.egg_ivf_val
    queryset_list_missouri_embryo_val = missouri_average_costs_model.embryo_ivf_val
    queryset_list_missouri_sperm_val = missouri_average_costs_model.sperm_ivf_val
    queryset_list_missouri_icsi_val = missouri_average_costs_model.icsi_val
    queryset_list_missouri_iui_val = missouri_average_costs_model.iui_val

    queryset_list_montana = queryset_list_us.filter(clinicRegion__iexact='Montana')
    my_total_clinic_count_montana = queryset_list_montana.count()
    montana_average_costs_model = Montana.objects.get(pk=1)
    queryset_list_montana_ivf_val = montana_average_costs_model.standard_ivf_val
    queryset_list_montana_egg_val = montana_average_costs_model.egg_ivf_val
    queryset_list_montana_embryo_val = montana_average_costs_model.embryo_ivf_val
    queryset_list_montana_sperm_val = montana_average_costs_model.sperm_ivf_val
    queryset_list_montana_icsi_val = montana_average_costs_model.icsi_val
    queryset_list_montana_iui_val = montana_average_costs_model.iui_val

    queryset_list_nebraska = queryset_list_us.filter(clinicRegion__iexact='Nebraska')
    my_total_clinic_count_nebraska = queryset_list_nebraska.count()
    nebraska_average_costs_model = Nebraska.objects.get(pk=1)
    queryset_list_nebraska_ivf_val = nebraska_average_costs_model.standard_ivf_val
    queryset_list_nebraska_egg_val = nebraska_average_costs_model.egg_ivf_val
    queryset_list_nebraska_embryo_val = nebraska_average_costs_model.embryo_ivf_val
    queryset_list_nebraska_sperm_val = nebraska_average_costs_model.sperm_ivf_val
    queryset_list_nebraska_icsi_val = nebraska_average_costs_model.icsi_val
    queryset_list_nebraska_iui_val = nebraska_average_costs_model.iui_val

    queryset_list_newhampshire = queryset_list_us.filter(clinicRegion__iexact='NewHampshire')
    my_total_clinic_count_newhampshire = queryset_list_newhampshire.count()
    newhampshire_average_costs_model = NewHampshire.objects.get(pk=1)
    queryset_list_newhampshire_ivf_val = newhampshire_average_costs_model.standard_ivf_val
    queryset_list_newhampshire_egg_val = newhampshire_average_costs_model.egg_ivf_val
    queryset_list_newhampshire_embryo_val = newhampshire_average_costs_model.embryo_ivf_val
    queryset_list_newhampshire_sperm_val = newhampshire_average_costs_model.sperm_ivf_val
    queryset_list_newhampshire_icsi_val = newhampshire_average_costs_model.icsi_val
    queryset_list_newhampshire_iui_val = newhampshire_average_costs_model.iui_val

    queryset_list_newjersey = queryset_list_us.filter(clinicRegion__iexact='NewJersey')
    my_total_clinic_count_newjersey = queryset_list_newjersey.count()
    newjersey_average_costs_model = NewJersey.objects.get(pk=1)
    queryset_list_newjersey_ivf_val = newjersey_average_costs_model.standard_ivf_val
    queryset_list_newjersey_egg_val = newjersey_average_costs_model.egg_ivf_val
    queryset_list_newjersey_embryo_val = newjersey_average_costs_model.embryo_ivf_val
    queryset_list_newjersey_sperm_val = newjersey_average_costs_model.sperm_ivf_val
    queryset_list_newjersey_icsi_val = newjersey_average_costs_model.icsi_val
    queryset_list_newjersey_iui_val = newjersey_average_costs_model.iui_val

    queryset_list_newmexico = queryset_list_us.filter(clinicRegion__iexact='NewMexico')
    my_total_clinic_count_newmexico = queryset_list_newmexico.count()
    newmexico_average_costs_model = NewMexico.objects.get(pk=1)
    queryset_list_newmexico_ivf_val = newmexico_average_costs_model.standard_ivf_val
    queryset_list_newmexico_egg_val = newmexico_average_costs_model.egg_ivf_val
    queryset_list_newmexico_embryo_val = newmexico_average_costs_model.embryo_ivf_val
    queryset_list_newmexico_sperm_val = newmexico_average_costs_model.sperm_ivf_val
    queryset_list_newmexico_icsi_val = newmexico_average_costs_model.icsi_val
    queryset_list_newmexico_iui_val = newmexico_average_costs_model.iui_val

    queryset_list_newyork = queryset_list_us.filter(clinicRegion__iexact='NewYork')
    my_total_clinic_count_newyork = queryset_list_newyork.count()
    newyork_average_costs_model = NewYork.objects.get(pk=1)
    queryset_list_newyork_ivf_val = newyork_average_costs_model.standard_ivf_val
    queryset_list_newyork_egg_val = newyork_average_costs_model.egg_ivf_val
    queryset_list_newyork_embryo_val = newyork_average_costs_model.embryo_ivf_val
    queryset_list_newyork_sperm_val = newyork_average_costs_model.sperm_ivf_val
    queryset_list_newyork_icsi_val = newyork_average_costs_model.icsi_val
    queryset_list_newyork_iui_val = newyork_average_costs_model.iui_val

    queryset_list_northcarolina = queryset_list_us.filter(clinicRegion__iexact='NorthCarolina')
    my_total_clinic_count_northcarolina = queryset_list_northcarolina.count()
    northcarolina_average_costs_model = NorthCarolina.objects.get(pk=1)
    queryset_list_northcarolina_ivf_val = northcarolina_average_costs_model.standard_ivf_val
    queryset_list_northcarolina_egg_val = northcarolina_average_costs_model.egg_ivf_val
    queryset_list_northcarolina_embryo_val = northcarolina_average_costs_model.embryo_ivf_val
    queryset_list_northcarolina_sperm_val = northcarolina_average_costs_model.sperm_ivf_val
    queryset_list_northcarolina_icsi_val = northcarolina_average_costs_model.icsi_val
    queryset_list_northcarolina_iui_val = northcarolina_average_costs_model.iui_val

    queryset_list_northdakota = queryset_list_us.filter(clinicRegion__iexact='NorthDakota')
    my_total_clinic_count_northdakota = queryset_list_northdakota.count()
    northdakota_average_costs_model = NorthDakota.objects.get(pk=1)
    queryset_list_northdakota_ivf_val = northdakota_average_costs_model.standard_ivf_val
    queryset_list_northdakota_egg_val = northdakota_average_costs_model.egg_ivf_val
    queryset_list_northdakota_embryo_val = northdakota_average_costs_model.embryo_ivf_val
    queryset_list_northdakota_sperm_val = northdakota_average_costs_model.sperm_ivf_val
    queryset_list_northdakota_icsi_val = northdakota_average_costs_model.icsi_val
    queryset_list_northdakota_iui_val = northdakota_average_costs_model.iui_val

    queryset_list_nevada = queryset_list_us.filter(clinicRegion__iexact='Nevada')
    my_total_clinic_count_nevada = queryset_list_nevada.count()
    nevada_average_costs_model = Nevada.objects.get(pk=1)
    queryset_list_nevada_ivf_val = nevada_average_costs_model.standard_ivf_val
    queryset_list_nevada_egg_val = nevada_average_costs_model.egg_ivf_val
    queryset_list_nevada_embryo_val = nevada_average_costs_model.embryo_ivf_val
    queryset_list_nevada_sperm_val = nevada_average_costs_model.sperm_ivf_val
    queryset_list_nevada_icsi_val = nevada_average_costs_model.icsi_val
    queryset_list_nevada_iui_val = nevada_average_costs_model.iui_val

    queryset_list_ohio = queryset_list_us.filter(clinicRegion__iexact='Ohio')
    my_total_clinic_count_ohio = queryset_list_ohio.count()
    ohio_average_costs_model = Ohio.objects.get(pk=1)
    queryset_list_ohio_ivf_val = ohio_average_costs_model.standard_ivf_val
    queryset_list_ohio_egg_val = ohio_average_costs_model.egg_ivf_val
    queryset_list_ohio_embryo_val = ohio_average_costs_model.embryo_ivf_val
    queryset_list_ohio_sperm_val = ohio_average_costs_model.sperm_ivf_val
    queryset_list_ohio_icsi_val = ohio_average_costs_model.icsi_val
    queryset_list_ohio_iui_val = ohio_average_costs_model.iui_val

    queryset_list_oklahoma = queryset_list_us.filter(clinicRegion__iexact='Oklahoma')
    my_total_clinic_count_oklahoma = queryset_list_oklahoma.count()
    oklahoma_average_costs_model = Oklahoma.objects.get(pk=1)
    queryset_list_oklahoma_ivf_val = oklahoma_average_costs_model.standard_ivf_val
    queryset_list_oklahoma_egg_val = oklahoma_average_costs_model.egg_ivf_val
    queryset_list_oklahoma_embryo_val = oklahoma_average_costs_model.embryo_ivf_val
    queryset_list_oklahoma_sperm_val = oklahoma_average_costs_model.sperm_ivf_val
    queryset_list_oklahoma_icsi_val = oklahoma_average_costs_model.icsi_val
    queryset_list_oklahoma_iui_val = oklahoma_average_costs_model.iui_val

    queryset_list_oregon = queryset_list_us.filter(clinicRegion__iexact='Oregon')
    my_total_clinic_count_oregon = queryset_list_oregon.count()
    oregon_average_costs_model = Oregon.objects.get(pk=1)
    queryset_list_oregon_ivf_val = oregon_average_costs_model.standard_ivf_val
    queryset_list_oregon_egg_val = oregon_average_costs_model.egg_ivf_val
    queryset_list_oregon_embryo_val = oregon_average_costs_model.embryo_ivf_val
    queryset_list_oregon_sperm_val = oregon_average_costs_model.sperm_ivf_val
    queryset_list_oregon_icsi_val = oregon_average_costs_model.icsi_val
    queryset_list_oregon_iui_val = oregon_average_costs_model.iui_val

    queryset_list_pennsylvania = queryset_list_us.filter(clinicRegion__iexact='Pennsylvania')
    my_total_clinic_count_pennsylvania = queryset_list_pennsylvania.count()
    pennsylvania_average_costs_model = Pennsylvania.objects.get(pk=1)
    queryset_list_pennsylvania_ivf_val = pennsylvania_average_costs_model.standard_ivf_val
    queryset_list_pennsylvania_egg_val = pennsylvania_average_costs_model.egg_ivf_val
    queryset_list_pennsylvania_embryo_val = pennsylvania_average_costs_model.embryo_ivf_val
    queryset_list_pennsylvania_sperm_val = pennsylvania_average_costs_model.sperm_ivf_val
    queryset_list_pennsylvania_icsi_val = pennsylvania_average_costs_model.icsi_val
    queryset_list_pennsylvania_iui_val = pennsylvania_average_costs_model.iui_val

    queryset_list_puertorico = queryset_list_us.filter(clinicRegion__iexact='PuertoRico')
    my_total_clinic_count_puertorico = queryset_list_puertorico.count()
    puertorico_average_costs_model = PuertoRico.objects.get(pk=1)
    queryset_list_puertorico_ivf_val = puertorico_average_costs_model.standard_ivf_val
    queryset_list_puertorico_egg_val = puertorico_average_costs_model.egg_ivf_val
    queryset_list_puertorico_embryo_val = puertorico_average_costs_model.embryo_ivf_val
    queryset_list_puertorico_sperm_val = puertorico_average_costs_model.sperm_ivf_val
    queryset_list_puertorico_icsi_val = puertorico_average_costs_model.icsi_val
    queryset_list_puertorico_iui_val = puertorico_average_costs_model.iui_val

    queryset_list_rhodeisland = queryset_list_us.filter(clinicRegion__iexact='RhodeIsland')
    my_total_clinic_count_rhodeisland = queryset_list_rhodeisland.count()
    rhodeisland_average_costs_model = RhodeIsland.objects.get(pk=1)
    queryset_list_rhodeisland_ivf_val = rhodeisland_average_costs_model.standard_ivf_val
    queryset_list_rhodeisland_egg_val = rhodeisland_average_costs_model.egg_ivf_val
    queryset_list_rhodeisland_embryo_val = rhodeisland_average_costs_model.embryo_ivf_val
    queryset_list_rhodeisland_sperm_val = rhodeisland_average_costs_model.sperm_ivf_val
    queryset_list_rhodeisland_icsi_val = rhodeisland_average_costs_model.icsi_val
    queryset_list_rhodeisland_iui_val = rhodeisland_average_costs_model.iui_val

    queryset_list_southcarolina = queryset_list_us.filter(clinicRegion__iexact='SouthCarolina')
    my_total_clinic_count_southcarolina = queryset_list_southcarolina.count()
    southcarolina_average_costs_model = SouthCarolina.objects.get(pk=1)
    queryset_list_southcarolina_ivf_val = southcarolina_average_costs_model.standard_ivf_val
    queryset_list_southcarolina_egg_val = southcarolina_average_costs_model.egg_ivf_val
    queryset_list_southcarolina_embryo_val = southcarolina_average_costs_model.embryo_ivf_val
    queryset_list_southcarolina_sperm_val = southcarolina_average_costs_model.sperm_ivf_val
    queryset_list_southcarolina_icsi_val = southcarolina_average_costs_model.icsi_val
    queryset_list_southcarolina_iui_val = southcarolina_average_costs_model.iui_val

    queryset_list_southdakota = queryset_list_us.filter(clinicRegion__iexact='SouthDakota')
    my_total_clinic_count_southdakota = queryset_list_southdakota.count()
    southdakota_average_costs_model = SouthDakota.objects.get(pk=1)
    queryset_list_southdakota_ivf_val = southdakota_average_costs_model.standard_ivf_val
    queryset_list_southdakota_egg_val = southdakota_average_costs_model.egg_ivf_val
    queryset_list_southdakota_embryo_val = southdakota_average_costs_model.embryo_ivf_val
    queryset_list_southdakota_sperm_val = southdakota_average_costs_model.sperm_ivf_val
    queryset_list_southdakota_icsi_val = southdakota_average_costs_model.icsi_val
    queryset_list_southdakota_iui_val = southdakota_average_costs_model.iui_val

    queryset_list_tennessee = queryset_list_us.filter(clinicRegion__iexact='Tennessee')
    my_total_clinic_count_tennessee = queryset_list_tennessee.count()
    tennessee_average_costs_model = Tennessee.objects.get(pk=1)
    queryset_list_tennessee_ivf_val = tennessee_average_costs_model.standard_ivf_val
    queryset_list_tennessee_egg_val = tennessee_average_costs_model.egg_ivf_val
    queryset_list_tennessee_embryo_val = tennessee_average_costs_model.embryo_ivf_val
    queryset_list_tennessee_sperm_val = tennessee_average_costs_model.sperm_ivf_val
    queryset_list_tennessee_icsi_val = tennessee_average_costs_model.icsi_val
    queryset_list_tennessee_iui_val = tennessee_average_costs_model.iui_val

    queryset_list_texas = queryset_list_us.filter(clinicRegion__iexact='Texas')
    my_total_clinic_count_texas = queryset_list_texas.count()
    texas_average_costs_model = Texas.objects.get(pk=1)
    queryset_list_texas_ivf_val = texas_average_costs_model.standard_ivf_val
    queryset_list_texas_egg_val = texas_average_costs_model.egg_ivf_val
    queryset_list_texas_embryo_val = texas_average_costs_model.embryo_ivf_val
    queryset_list_texas_sperm_val = texas_average_costs_model.sperm_ivf_val
    queryset_list_texas_icsi_val = texas_average_costs_model.icsi_val
    queryset_list_texas_iui_val = texas_average_costs_model.iui_val

    queryset_list_utah = queryset_list_us.filter(clinicRegion__iexact='Utah')
    my_total_clinic_count_utah = queryset_list_utah.count()
    utah_average_costs_model = Utah.objects.get(pk=1)
    queryset_list_utah_ivf_val = utah_average_costs_model.standard_ivf_val
    queryset_list_utah_egg_val = utah_average_costs_model.egg_ivf_val
    queryset_list_utah_embryo_val = utah_average_costs_model.embryo_ivf_val
    queryset_list_utah_sperm_val = utah_average_costs_model.sperm_ivf_val
    queryset_list_utah_icsi_val = utah_average_costs_model.icsi_val
    queryset_list_utah_iui_val = utah_average_costs_model.iui_val

    queryset_list_vermont = queryset_list_us.filter(clinicRegion__iexact='Vermont')
    my_total_clinic_count_vermont = queryset_list_vermont.count()
    vermont_average_costs_model = Vermont.objects.get(pk=1)
    queryset_list_vermont_ivf_val = vermont_average_costs_model.standard_ivf_val
    queryset_list_vermont_egg_val = vermont_average_costs_model.egg_ivf_val
    queryset_list_vermont_embryo_val = vermont_average_costs_model.embryo_ivf_val
    queryset_list_vermont_sperm_val = vermont_average_costs_model.sperm_ivf_val
    queryset_list_vermont_icsi_val = vermont_average_costs_model.icsi_val
    queryset_list_vermont_iui_val = vermont_average_costs_model.iui_val

    queryset_list_virginia = queryset_list_us.filter(clinicRegion__iexact='Virginia')
    my_total_clinic_count_virginia = queryset_list_virginia.count()
    virginia_average_costs_model = Virginia.objects.get(pk=1)
    queryset_list_virginia_ivf_val = virginia_average_costs_model.standard_ivf_val
    queryset_list_virginia_egg_val = virginia_average_costs_model.egg_ivf_val
    queryset_list_virginia_embryo_val = virginia_average_costs_model.embryo_ivf_val
    queryset_list_virginia_sperm_val = virginia_average_costs_model.sperm_ivf_val
    queryset_list_virginia_icsi_val = virginia_average_costs_model.icsi_val
    queryset_list_virginia_iui_val = virginia_average_costs_model.iui_val

    queryset_list_washington = queryset_list_us.filter(clinicRegion__iexact='Washington')
    my_total_clinic_count_washington = queryset_list_washington.count()
    washington_average_costs_model = Washington.objects.get(pk=1)
    queryset_list_washington_ivf_val = washington_average_costs_model.standard_ivf_val
    queryset_list_washington_egg_val = washington_average_costs_model.egg_ivf_val
    queryset_list_washington_embryo_val = washington_average_costs_model.embryo_ivf_val
    queryset_list_washington_sperm_val = washington_average_costs_model.sperm_ivf_val
    queryset_list_washington_icsi_val = washington_average_costs_model.icsi_val
    queryset_list_washington_iui_val = washington_average_costs_model.iui_val

    queryset_list_westvirginia = queryset_list_us.filter(clinicRegion__iexact='WestVirginia')
    my_total_clinic_count_westvirginia = queryset_list_westvirginia.count()
    westvirginia_average_costs_model = WestVirginia.objects.get(pk=1)
    queryset_list_westvirginia_ivf_val = westvirginia_average_costs_model.standard_ivf_val
    queryset_list_westvirginia_egg_val = westvirginia_average_costs_model.egg_ivf_val
    queryset_list_westvirginia_embryo_val = westvirginia_average_costs_model.embryo_ivf_val
    queryset_list_westvirginia_sperm_val = westvirginia_average_costs_model.sperm_ivf_val
    queryset_list_westvirginia_icsi_val = westvirginia_average_costs_model.icsi_val
    queryset_list_westvirginia_iui_val = westvirginia_average_costs_model.iui_val

    queryset_list_wisconsin = queryset_list_us.filter(clinicRegion__iexact='Wisconsin')
    my_total_clinic_count_wisconsin = queryset_list_wisconsin.count()
    wisconsin_average_costs_model = Wisconsin.objects.get(pk=1)
    queryset_list_wisconsin_ivf_val = wisconsin_average_costs_model.standard_ivf_val
    queryset_list_wisconsin_egg_val = wisconsin_average_costs_model.egg_ivf_val
    queryset_list_wisconsin_embryo_val = wisconsin_average_costs_model.embryo_ivf_val
    queryset_list_wisconsin_sperm_val = wisconsin_average_costs_model.sperm_ivf_val
    queryset_list_wisconsin_icsi_val = wisconsin_average_costs_model.icsi_val
    queryset_list_wisconsin_iui_val = wisconsin_average_costs_model.iui_val

    queryset_list_wyoming = queryset_list_us.filter(clinicRegion__iexact='Wyoming')
    my_total_clinic_count_wyoming = queryset_list_wyoming.count()
    wyoming_average_costs_model = Wyoming.objects.get(pk=1)
    queryset_list_wyoming_ivf_val = wyoming_average_costs_model.standard_ivf_val
    queryset_list_wyoming_egg_val = wyoming_average_costs_model.egg_ivf_val
    queryset_list_wyoming_embryo_val = wyoming_average_costs_model.embryo_ivf_val
    queryset_list_wyoming_sperm_val = wyoming_average_costs_model.sperm_ivf_val
    queryset_list_wyoming_icsi_val = wyoming_average_costs_model.icsi_val
    queryset_list_wyoming_iui_val = wyoming_average_costs_model.iui_val

    queryset_list_districtofcolumbia = queryset_list_us.filter(clinicRegion__iexact='DistrictOfColumbia')
    my_total_clinic_count_districtofcolumbia = queryset_list_districtofcolumbia.count()
    districtofcolumbia_average_costs_model = DistrictOfColumbia.objects.get(pk=1)
    queryset_list_districtofcolumbia_ivf_val = districtofcolumbia_average_costs_model.standard_ivf_val
    queryset_list_districtofcolumbia_egg_val = districtofcolumbia_average_costs_model.egg_ivf_val
    queryset_list_districtofcolumbia_embryo_val = districtofcolumbia_average_costs_model.embryo_ivf_val
    queryset_list_districtofcolumbia_sperm_val = districtofcolumbia_average_costs_model.sperm_ivf_val
    queryset_list_districtofcolumbia_icsi_val = districtofcolumbia_average_costs_model.icsi_val
    queryset_list_districtofcolumbia_iui_val = districtofcolumbia_average_costs_model.iui_val



    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

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

