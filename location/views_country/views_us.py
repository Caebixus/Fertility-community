from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsUSRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'United States'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_us_natural_ivf_val = procedure_country_average_value('ivf_treatment_cost', country_name)
    queryset_list_us_mild_ivf_val = procedure_country_average_value('mild_ivf_treatment_cost', country_name)
    queryset_list_us_standard_ivf_val = procedure_country_average_value('ovarian_ivf_treatment_cost', country_name)
    queryset_list_us_egg_ivf_val = procedure_country_average_value('egg_donor_recipients_cost', country_name)
    queryset_list_us_known_egg_ivf_val = procedure_country_average_value('known_egg_donor_recipients_cost', country_name)
    queryset_list_us_shared_egg_ivf_val = procedure_country_average_value('shared_egg_donor_recipients_cost', country_name)

    queryset_list_us_embryo_ivf_val = procedure_country_average_value('embryo_donor_recipients_cost', country_name)
    queryset_list_us_known_embryo_ivf_val = procedure_country_average_value('known_embryo_donor_recipients_cost', country_name)
    queryset_list_us_sperm_ivf_val = procedure_country_average_value('sperm_donor_recipients_cost', country_name)
    queryset_list_us_known_sperm_ivf_val = procedure_country_average_value('known_sperm_donor_recipients_cost', country_name)
    queryset_list_us_icsi_val = procedure_country_average_value('icsi_treatment_cost', country_name)
    queryset_list_us_iui_val = procedure_country_average_value('iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    region_name = 'Alabama'
    my_total_clinic_count_alabama = region_count(region_name)
    clinic_count = my_total_clinic_count_alabama

    queryset_list_alabama_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_alabama_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_alabama_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_alabama_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_alabama_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_alabama_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Alaska'
    my_total_clinic_count_alaska = region_count(region_name)
    clinic_count = my_total_clinic_count_alaska

    queryset_list_alaska_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_alaska_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_alaska_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_alaska_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_alaska_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_alaska_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Arizona'
    my_total_clinic_count_arizona = region_count(region_name)
    clinic_count = my_total_clinic_count_arizona

    queryset_list_arizona_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_arizona_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_arizona_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_arizona_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_arizona_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_arizona_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Arkansas'
    my_total_clinic_count_arkansas = region_count(region_name)
    clinic_count = my_total_clinic_count_arkansas

    queryset_list_arkansas_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_arkansas_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_arkansas_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_arkansas_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_arkansas_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_arkansas_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'California'
    my_total_clinic_count_california = region_count(region_name)
    clinic_count = my_total_clinic_count_california

    queryset_list_california_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_california_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_california_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_california_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_california_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_california_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Colorado'
    my_total_clinic_count_colorado = region_count(region_name)
    clinic_count = my_total_clinic_count_colorado

    queryset_list_colorado_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_colorado_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_colorado_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_colorado_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_colorado_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_colorado_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Connecticut'
    my_total_clinic_count_connecticut = region_count(region_name)
    clinic_count = my_total_clinic_count_connecticut

    queryset_list_connecticut_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_connecticut_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_connecticut_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_connecticut_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_connecticut_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_connecticut_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Delaware'
    my_total_clinic_count_delaware = region_count(region_name)
    clinic_count = my_total_clinic_count_delaware

    queryset_list_delaware_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_delaware_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_delaware_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_delaware_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_delaware_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_delaware_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Florida'
    my_total_clinic_count_florida = region_count(region_name)
    clinic_count = my_total_clinic_count_florida

    queryset_list_florida_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_florida_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_florida_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_florida_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_florida_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_florida_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Georgia'
    my_total_clinic_count_georgia = region_count(region_name)
    clinic_count = my_total_clinic_count_georgia

    queryset_list_georgia_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_georgia_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_georgia_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_georgia_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_georgia_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_georgia_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Hawaii'
    my_total_clinic_count_hawaii = region_count(region_name)
    clinic_count = my_total_clinic_count_hawaii

    queryset_list_hawaii_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_hawaii_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_hawaii_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_hawaii_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_hawaii_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_hawaii_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Idaho'
    my_total_clinic_count_idaho = region_count(region_name)
    clinic_count = my_total_clinic_count_idaho

    queryset_list_idaho_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_idaho_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_idaho_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_idaho_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_idaho_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_idaho_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Illinois'
    my_total_clinic_count_illinois = region_count(region_name)
    clinic_count = my_total_clinic_count_illinois

    queryset_list_illinois_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_illinois_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_illinois_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_illinois_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_illinois_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_illinois_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Indiana'
    my_total_clinic_count_indiana = region_count(region_name)
    clinic_count = my_total_clinic_count_indiana

    queryset_list_indiana_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_indiana_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_indiana_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_indiana_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_indiana_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_indiana_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Iowa'
    my_total_clinic_count_iowa = region_count(region_name)
    clinic_count = my_total_clinic_count_iowa

    queryset_list_iowa_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_iowa_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_iowa_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_iowa_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_iowa_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_iowa_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Kansas'
    my_total_clinic_count_kansas = region_count(region_name)
    clinic_count = my_total_clinic_count_kansas

    queryset_list_kansas_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_kansas_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_kansas_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_kansas_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_kansas_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_kansas_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Kentucky'
    my_total_clinic_count_kentucky = region_count(region_name)
    clinic_count = my_total_clinic_count_kentucky

    queryset_list_kentucky_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_kentucky_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_kentucky_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_kentucky_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_kentucky_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_kentucky_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Louisiana'
    my_total_clinic_count_louisiana = region_count(region_name)
    clinic_count = my_total_clinic_count_louisiana

    queryset_list_louisiana_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_louisiana_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_louisiana_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_louisiana_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_louisiana_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_louisiana_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'London'
    my_total_clinic_count_london = region_count(region_name)
    clinic_count = my_total_clinic_count_london

    queryset_list_london_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_london_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_london_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_london_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_london_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_london_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Maine'
    my_total_clinic_count_maine = region_count(region_name)
    clinic_count = my_total_clinic_count_maine

    queryset_list_maine_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_maine_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_maine_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_maine_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_maine_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_maine_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Maryland'
    my_total_clinic_count_maryland = region_count(region_name)
    clinic_count = my_total_clinic_count_maryland

    queryset_list_maryland_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_maryland_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_maryland_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_maryland_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_maryland_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_maryland_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Massachusetts'
    my_total_clinic_count_massachusetts = region_count(region_name)
    clinic_count = my_total_clinic_count_massachusetts

    queryset_list_massachusetts_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_massachusetts_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_massachusetts_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_massachusetts_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_massachusetts_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_massachusetts_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Michigan'
    my_total_clinic_count_michigan = region_count(region_name)
    clinic_count = my_total_clinic_count_michigan

    queryset_list_michigan_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_michigan_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_michigan_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_michigan_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_michigan_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_michigan_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Minnesota'
    my_total_clinic_count_minnesota = region_count(region_name)
    clinic_count = my_total_clinic_count_minnesota

    queryset_list_minnesota_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_minnesota_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_minnesota_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_minnesota_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_minnesota_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_minnesota_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Mississippi'
    my_total_clinic_count_mississippi = region_count(region_name)
    clinic_count = my_total_clinic_count_mississippi

    queryset_list_mississippi_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_mississippi_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_mississippi_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_mississippi_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_mississippi_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_mississippi_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Missouri'
    my_total_clinic_count_missouri = region_count(region_name)
    clinic_count = my_total_clinic_count_missouri

    queryset_list_missouri_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_missouri_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_missouri_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_missouri_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_missouri_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_missouri_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Montana'
    my_total_clinic_count_montana = region_count(region_name)
    clinic_count = my_total_clinic_count_montana

    queryset_list_montana_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_montana_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_montana_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_montana_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_montana_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_montana_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Nebraska'
    my_total_clinic_count_nebraska = region_count(region_name)
    clinic_count = my_total_clinic_count_nebraska

    queryset_list_nebraska_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_nebraska_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_nebraska_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_nebraska_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_nebraska_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_nebraska_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'New Hampshire'
    my_total_clinic_count_newhampshire = region_count(region_name)
    clinic_count = my_total_clinic_count_newhampshire

    queryset_list_newhampshire_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_newhampshire_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_newhampshire_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_newhampshire_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_newhampshire_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_newhampshire_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'New Jersey'
    my_total_clinic_count_newjersey = region_count(region_name)
    clinic_count = my_total_clinic_count_newjersey

    queryset_list_newjersey_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_newjersey_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_newjersey_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_newjersey_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_newjersey_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_newjersey_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'New Mexico'
    my_total_clinic_count_newmexico = region_count(region_name)
    clinic_count = my_total_clinic_count_newmexico

    queryset_list_newmexico_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_newmexico_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_newmexico_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_newmexico_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_newmexico_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_newmexico_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'New York'
    my_total_clinic_count_newyork = region_count(region_name)
    clinic_count = my_total_clinic_count_newyork

    queryset_list_newyork_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_newyork_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_newyork_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_newyork_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_newyork_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_newyork_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'North Carolina'
    my_total_clinic_count_northcarolina = region_count(region_name)
    clinic_count = my_total_clinic_count_northcarolina

    queryset_list_northcarolina_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_northcarolina_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_northcarolina_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_northcarolina_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_northcarolina_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_northcarolina_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'North Dakota'
    my_total_clinic_count_northdakota = region_count(region_name)
    clinic_count = my_total_clinic_count_northdakota

    queryset_list_northdakota_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_northdakota_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_northdakota_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_northdakota_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_northdakota_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_northdakota_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Nevada'
    my_total_clinic_count_nevada = region_count(region_name)
    clinic_count = my_total_clinic_count_nevada

    queryset_list_nevada_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_nevada_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_nevada_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_nevada_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_nevada_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_nevada_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Ohio'
    my_total_clinic_count_ohio = region_count(region_name)
    clinic_count = my_total_clinic_count_ohio

    queryset_list_ohio_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_ohio_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_ohio_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_ohio_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_ohio_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_ohio_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Oklahoma'
    my_total_clinic_count_oklahoma = region_count(region_name)
    clinic_count = my_total_clinic_count_oklahoma

    queryset_list_oklahoma_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_oklahoma_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_oklahoma_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_oklahoma_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_oklahoma_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_oklahoma_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Oregon'
    my_total_clinic_count_oregon = region_count(region_name)
    clinic_count = my_total_clinic_count_oregon

    queryset_list_oregon_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_oregon_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_oregon_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_oregon_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_oregon_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_oregon_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Pennsylvania'
    my_total_clinic_count_pennsylvania = region_count(region_name)
    clinic_count = my_total_clinic_count_pennsylvania

    queryset_list_pennsylvania_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_pennsylvania_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_pennsylvania_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_pennsylvania_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_pennsylvania_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_pennsylvania_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Puerto Rico'
    my_total_clinic_count_puertorico = region_count(region_name)
    clinic_count = my_total_clinic_count_puertorico

    queryset_list_puertorico_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_puertorico_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_puertorico_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_puertorico_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_puertorico_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_puertorico_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'South Carolina'
    my_total_clinic_count_southcarolina = region_count(region_name)
    clinic_count = my_total_clinic_count_southcarolina

    queryset_list_southcarolina_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_southcarolina_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_southcarolina_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_southcarolina_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_southcarolina_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_southcarolina_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Rhode Island'
    my_total_clinic_count_rhodeisland = region_count(region_name)
    clinic_count = my_total_clinic_count_rhodeisland

    queryset_list_rhodeisland_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_rhodeisland_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_rhodeisland_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_rhodeisland_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_rhodeisland_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_rhodeisland_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'South Dakota'
    my_total_clinic_count_southdakota = region_count(region_name)
    clinic_count = my_total_clinic_count_southdakota

    queryset_list_southdakota_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_southdakota_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_southdakota_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_southdakota_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_southdakota_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_southdakota_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Tennessee'
    my_total_clinic_count_tennessee = region_count(region_name)
    clinic_count = my_total_clinic_count_tennessee

    queryset_list_tennessee_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_tennessee_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_tennessee_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_tennessee_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_tennessee_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_tennessee_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Texas'
    my_total_clinic_count_texas = region_count(region_name)
    clinic_count = my_total_clinic_count_texas

    queryset_list_texas_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_texas_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_texas_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_texas_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_texas_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_texas_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Utah'
    my_total_clinic_count_utah = region_count(region_name)
    clinic_count = my_total_clinic_count_utah

    queryset_list_utah_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_utah_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_utah_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_utah_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_utah_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_utah_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Vermont'
    my_total_clinic_count_vermont = region_count(region_name)
    clinic_count = my_total_clinic_count_vermont

    queryset_list_vermont_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_vermont_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_vermont_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_vermont_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_vermont_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_vermont_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Virginia'
    my_total_clinic_count_virginia = region_count(region_name)
    clinic_count = my_total_clinic_count_virginia

    queryset_list_virginia_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_virginia_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_virginia_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_virginia_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_virginia_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_virginia_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Washington'
    my_total_clinic_count_washington = region_count(region_name)
    clinic_count = my_total_clinic_count_washington

    queryset_list_washington_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_washington_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_washington_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_washington_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_washington_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_washington_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'West Virginia'
    my_total_clinic_count_westvirginia = region_count(region_name)
    clinic_count = my_total_clinic_count_westvirginia

    queryset_list_westvirginia_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_westvirginia_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_westvirginia_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_westvirginia_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_westvirginia_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_westvirginia_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Wisconsin'
    my_total_clinic_count_wisconsin = region_count(region_name)
    clinic_count = my_total_clinic_count_wisconsin

    queryset_list_wisconsin_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_wisconsin_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_wisconsin_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_wisconsin_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_wisconsin_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_wisconsin_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Wyoming'
    my_total_clinic_count_wyoming = region_count(region_name)
    clinic_count = my_total_clinic_count_wyoming

    queryset_list_wyoming_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_wyoming_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_wyoming_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_wyoming_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_wyoming_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_wyoming_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'District of Columbia'
    my_total_clinic_count_districtofcolumbia = region_count(region_name)
    clinic_count = my_total_clinic_count_districtofcolumbia

    queryset_list_districtofcolumbia_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name)
    queryset_list_districtofcolumbia_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name)
    queryset_list_districtofcolumbia_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name)
    queryset_list_districtofcolumbia_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name)
    queryset_list_districtofcolumbia_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name)
    queryset_list_districtofcolumbia_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name)

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

        'my_total_clinic_count_alabama': my_total_clinic_count_alabama,
        'queryset_list_alabama_ivf_val': queryset_list_alabama_ivf_val,
        'queryset_list_alabama_egg_val': queryset_list_alabama_egg_val,
        'queryset_list_alabama_embryo_val': queryset_list_alabama_embryo_val,
        'queryset_list_alabama_sperm_val': queryset_list_alabama_sperm_val,
        'queryset_list_alabama_icsi_val': queryset_list_alabama_icsi_val,
        'queryset_list_alabama_iui_val': queryset_list_alabama_iui_val,

        'my_total_clinic_count_alaska': my_total_clinic_count_alaska,
        'queryset_list_alaska_ivf_val': queryset_list_alaska_ivf_val,
        'queryset_list_alaska_egg_val': queryset_list_alaska_egg_val,
        'queryset_list_alaska_embryo_val': queryset_list_alaska_embryo_val,
        'queryset_list_alaska_sperm_val': queryset_list_alaska_sperm_val,
        'queryset_list_alaska_icsi_val': queryset_list_alaska_icsi_val,
        'queryset_list_alaska_iui_val': queryset_list_alaska_iui_val,

        'my_total_clinic_count_arizona': my_total_clinic_count_arizona,
        'queryset_list_arizona_ivf_val': queryset_list_arizona_ivf_val,
        'queryset_list_arizona_egg_val': queryset_list_arizona_egg_val,
        'queryset_list_arizona_embryo_val': queryset_list_arizona_embryo_val,
        'queryset_list_arizona_sperm_val': queryset_list_arizona_sperm_val,
        'queryset_list_arizona_icsi_val': queryset_list_arizona_icsi_val,
        'queryset_list_arizona_iui_val': queryset_list_arizona_iui_val,

        'my_total_clinic_count_arkansas': my_total_clinic_count_arkansas,
        'queryset_list_arkansas_ivf_val': queryset_list_arkansas_ivf_val,
        'queryset_list_arkansas_egg_val': queryset_list_arkansas_egg_val,
        'queryset_list_arkansas_embryo_val': queryset_list_arkansas_embryo_val,
        'queryset_list_arkansas_sperm_val': queryset_list_arkansas_sperm_val,
        'queryset_list_arkansas_icsi_val': queryset_list_arkansas_icsi_val,
        'queryset_list_arkansas_iui_val': queryset_list_arkansas_iui_val,

        'my_total_clinic_count_california': my_total_clinic_count_california,
        'queryset_list_california_ivf_val': queryset_list_california_ivf_val,
        'queryset_list_california_egg_val': queryset_list_california_egg_val,
        'queryset_list_california_embryo_val': queryset_list_california_embryo_val,
        'queryset_list_california_sperm_val': queryset_list_california_sperm_val,
        'queryset_list_california_icsi_val': queryset_list_california_icsi_val,
        'queryset_list_california_iui_val': queryset_list_california_iui_val,

        'my_total_clinic_count_colorado': my_total_clinic_count_colorado,
        'queryset_list_colorado_ivf_val': queryset_list_colorado_ivf_val,
        'queryset_list_colorado_egg_val': queryset_list_colorado_egg_val,
        'queryset_list_colorado_embryo_val': queryset_list_colorado_embryo_val,
        'queryset_list_colorado_sperm_val': queryset_list_colorado_sperm_val,
        'queryset_list_colorado_icsi_val': queryset_list_colorado_icsi_val,
        'queryset_list_colorado_iui_val': queryset_list_colorado_iui_val,

        'my_total_clinic_count_connecticut': my_total_clinic_count_connecticut,
        'queryset_list_connecticut_ivf_val': queryset_list_connecticut_ivf_val,
        'queryset_list_connecticut_egg_val': queryset_list_connecticut_egg_val,
        'queryset_list_connecticut_embryo_val': queryset_list_connecticut_embryo_val,
        'queryset_list_connecticut_sperm_val': queryset_list_connecticut_sperm_val,
        'queryset_list_connecticut_icsi_val': queryset_list_connecticut_icsi_val,
        'queryset_list_connecticut_iui_val': queryset_list_connecticut_iui_val,

        'my_total_clinic_count_delaware': my_total_clinic_count_delaware,
        'queryset_list_delaware_ivf_val': queryset_list_delaware_ivf_val,
        'queryset_list_delaware_egg_val': queryset_list_delaware_egg_val,
        'queryset_list_delaware_embryo_val': queryset_list_delaware_embryo_val,
        'queryset_list_delaware_sperm_val': queryset_list_delaware_sperm_val,
        'queryset_list_delaware_icsi_val': queryset_list_delaware_icsi_val,
        'queryset_list_delaware_iui_val': queryset_list_delaware_iui_val,

        'my_total_clinic_count_florida': my_total_clinic_count_florida,
        'queryset_list_florida_ivf_val': queryset_list_florida_ivf_val,
        'queryset_list_florida_egg_val': queryset_list_florida_egg_val,
        'queryset_list_florida_embryo_val': queryset_list_florida_embryo_val,
        'queryset_list_florida_sperm_val': queryset_list_florida_sperm_val,
        'queryset_list_florida_icsi_val': queryset_list_florida_icsi_val,
        'queryset_list_florida_iui_val': queryset_list_florida_iui_val,

        'my_total_clinic_count_georgia': my_total_clinic_count_georgia,
        'queryset_list_georgia_ivf_val': queryset_list_georgia_ivf_val,
        'queryset_list_georgia_egg_val': queryset_list_georgia_egg_val,
        'queryset_list_georgia_embryo_val': queryset_list_georgia_embryo_val,
        'queryset_list_georgia_sperm_val': queryset_list_georgia_sperm_val,
        'queryset_list_georgia_icsi_val': queryset_list_georgia_icsi_val,
        'queryset_list_georgia_iui_val': queryset_list_georgia_iui_val,

        'my_total_clinic_count_hawaii': my_total_clinic_count_hawaii,
        'queryset_list_hawaii_ivf_val': queryset_list_hawaii_ivf_val,
        'queryset_list_hawaii_egg_val': queryset_list_hawaii_egg_val,
        'queryset_list_hawaii_embryo_val': queryset_list_hawaii_embryo_val,
        'queryset_list_hawaii_sperm_val': queryset_list_hawaii_sperm_val,
        'queryset_list_hawaii_icsi_val': queryset_list_hawaii_icsi_val,
        'queryset_list_hawaii_iui_val': queryset_list_hawaii_iui_val,

        'my_total_clinic_count_idaho': my_total_clinic_count_idaho,
        'queryset_list_idaho_ivf_val': queryset_list_idaho_ivf_val,
        'queryset_list_idaho_egg_val': queryset_list_idaho_egg_val,
        'queryset_list_idaho_embryo_val': queryset_list_idaho_embryo_val,
        'queryset_list_idaho_sperm_val': queryset_list_idaho_sperm_val,
        'queryset_list_idaho_icsi_val': queryset_list_idaho_icsi_val,
        'queryset_list_idaho_iui_val': queryset_list_idaho_iui_val,

        'my_total_clinic_count_illinois': my_total_clinic_count_illinois,
        'queryset_list_illinois_ivf_val': queryset_list_illinois_ivf_val,
        'queryset_list_illinois_egg_val': queryset_list_illinois_egg_val,
        'queryset_list_illinois_embryo_val': queryset_list_illinois_embryo_val,
        'queryset_list_illinois_sperm_val': queryset_list_illinois_sperm_val,
        'queryset_list_illinois_icsi_val': queryset_list_illinois_icsi_val,
        'queryset_list_illinois_iui_val': queryset_list_illinois_iui_val,

        'my_total_clinic_count_indiana': my_total_clinic_count_indiana,
        'queryset_list_indiana_ivf_val': queryset_list_indiana_ivf_val,
        'queryset_list_indiana_egg_val': queryset_list_indiana_egg_val,
        'queryset_list_indiana_embryo_val': queryset_list_indiana_embryo_val,
        'queryset_list_indiana_sperm_val': queryset_list_indiana_sperm_val,
        'queryset_list_indiana_icsi_val': queryset_list_indiana_icsi_val,
        'queryset_list_indiana_iui_val': queryset_list_indiana_iui_val,

        'my_total_clinic_count_iowa': my_total_clinic_count_iowa,
        'queryset_list_iowa_ivf_val': queryset_list_iowa_ivf_val,
        'queryset_list_iowa_egg_val': queryset_list_iowa_egg_val,
        'queryset_list_iowa_embryo_val': queryset_list_iowa_embryo_val,
        'queryset_list_iowa_sperm_val': queryset_list_iowa_sperm_val,
        'queryset_list_iowa_icsi_val': queryset_list_iowa_icsi_val,
        'queryset_list_iowa_iui_val': queryset_list_iowa_iui_val,

        'my_total_clinic_count_kansas': my_total_clinic_count_kansas,
        'queryset_list_kansas_ivf_val': queryset_list_kansas_ivf_val,
        'queryset_list_kansas_egg_val': queryset_list_kansas_egg_val,
        'queryset_list_kansas_embryo_val': queryset_list_kansas_embryo_val,
        'queryset_list_kansas_sperm_val': queryset_list_kansas_sperm_val,
        'queryset_list_kansas_icsi_val': queryset_list_kansas_icsi_val,
        'queryset_list_kansas_iui_val': queryset_list_kansas_iui_val,

        'my_total_clinic_count_kentucky': my_total_clinic_count_kentucky,
        'queryset_list_kentucky_ivf_val': queryset_list_kentucky_ivf_val,
        'queryset_list_kentucky_egg_val': queryset_list_kentucky_egg_val,
        'queryset_list_kentucky_embryo_val': queryset_list_kentucky_embryo_val,
        'queryset_list_kentucky_sperm_val': queryset_list_kentucky_sperm_val,
        'queryset_list_kentucky_icsi_val': queryset_list_kentucky_icsi_val,
        'queryset_list_kentucky_iui_val': queryset_list_kentucky_iui_val,

        'my_total_clinic_count_louisiana': my_total_clinic_count_louisiana,
        'queryset_list_louisiana_ivf_val': queryset_list_louisiana_ivf_val,
        'queryset_list_louisiana_egg_val': queryset_list_louisiana_egg_val,
        'queryset_list_louisiana_embryo_val': queryset_list_louisiana_embryo_val,
        'queryset_list_louisiana_sperm_val': queryset_list_louisiana_sperm_val,
        'queryset_list_louisiana_icsi_val': queryset_list_louisiana_icsi_val,
        'queryset_list_louisiana_iui_val': queryset_list_louisiana_iui_val,

        'my_total_clinic_count_london': my_total_clinic_count_london,
        'queryset_list_london_ivf_val': queryset_list_london_ivf_val,
        'queryset_list_london_egg_val': queryset_list_london_egg_val,
        'queryset_list_london_embryo_val': queryset_list_london_embryo_val,
        'queryset_list_london_sperm_val': queryset_list_london_sperm_val,
        'queryset_list_london_icsi_val': queryset_list_london_icsi_val,
        'queryset_list_london_iui_val': queryset_list_london_iui_val,

        'my_total_clinic_count_maine': my_total_clinic_count_maine,
        'queryset_list_maine_ivf_val': queryset_list_maine_ivf_val,
        'queryset_list_maine_egg_val': queryset_list_maine_egg_val,
        'queryset_list_maine_embryo_val': queryset_list_maine_embryo_val,
        'queryset_list_maine_sperm_val': queryset_list_maine_sperm_val,
        'queryset_list_maine_icsi_val': queryset_list_maine_icsi_val,
        'queryset_list_maine_iui_val': queryset_list_maine_iui_val,

        'my_total_clinic_count_maryland': my_total_clinic_count_maryland,
        'queryset_list_maryland_ivf_val': queryset_list_maryland_ivf_val,
        'queryset_list_maryland_egg_val': queryset_list_maryland_egg_val,
        'queryset_list_maryland_embryo_val': queryset_list_maryland_embryo_val,
        'queryset_list_maryland_sperm_val': queryset_list_maryland_sperm_val,
        'queryset_list_maryland_icsi_val': queryset_list_maryland_icsi_val,
        'queryset_list_maryland_iui_val': queryset_list_maryland_iui_val,

        'my_total_clinic_count_massachusetts': my_total_clinic_count_massachusetts,
        'queryset_list_massachusetts_ivf_val': queryset_list_massachusetts_ivf_val,
        'queryset_list_massachusetts_egg_val': queryset_list_massachusetts_egg_val,
        'queryset_list_massachusetts_embryo_val': queryset_list_massachusetts_embryo_val,
        'queryset_list_massachusetts_sperm_val': queryset_list_massachusetts_sperm_val,
        'queryset_list_massachusetts_icsi_val': queryset_list_massachusetts_icsi_val,
        'queryset_list_massachusetts_iui_val': queryset_list_massachusetts_iui_val,

        'my_total_clinic_count_michigan': my_total_clinic_count_michigan,
        'queryset_list_michigan_ivf_val': queryset_list_michigan_ivf_val,
        'queryset_list_michigan_egg_val': queryset_list_michigan_egg_val,
        'queryset_list_michigan_embryo_val': queryset_list_michigan_embryo_val,
        'queryset_list_michigan_sperm_val': queryset_list_michigan_sperm_val,
        'queryset_list_michigan_icsi_val': queryset_list_michigan_icsi_val,
        'queryset_list_michigan_iui_val': queryset_list_michigan_iui_val,

        'my_total_clinic_count_minnesota': my_total_clinic_count_minnesota,
        'queryset_list_minnesota_ivf_val': queryset_list_minnesota_ivf_val,
        'queryset_list_minnesota_egg_val': queryset_list_minnesota_egg_val,
        'queryset_list_minnesota_embryo_val': queryset_list_minnesota_embryo_val,
        'queryset_list_minnesota_sperm_val': queryset_list_minnesota_sperm_val,
        'queryset_list_minnesota_icsi_val': queryset_list_minnesota_icsi_val,
        'queryset_list_minnesota_iui_val': queryset_list_minnesota_iui_val,

        'my_total_clinic_count_mississippi': my_total_clinic_count_mississippi,
        'queryset_list_mississippi_ivf_val': queryset_list_mississippi_ivf_val,
        'queryset_list_mississippi_egg_val': queryset_list_mississippi_egg_val,
        'queryset_list_mississippi_embryo_val': queryset_list_mississippi_embryo_val,
        'queryset_list_mississippi_sperm_val': queryset_list_mississippi_sperm_val,
        'queryset_list_mississippi_icsi_val': queryset_list_mississippi_icsi_val,
        'queryset_list_mississippi_iui_val': queryset_list_mississippi_iui_val,

        'my_total_clinic_count_missouri': my_total_clinic_count_missouri,
        'queryset_list_missouri_ivf_val': queryset_list_missouri_ivf_val,
        'queryset_list_missouri_egg_val': queryset_list_missouri_egg_val,
        'queryset_list_missouri_embryo_val': queryset_list_missouri_embryo_val,
        'queryset_list_missouri_sperm_val': queryset_list_missouri_sperm_val,
        'queryset_list_missouri_icsi_val': queryset_list_missouri_icsi_val,
        'queryset_list_missouri_iui_val': queryset_list_missouri_iui_val,

        'my_total_clinic_count_montana': my_total_clinic_count_montana,
        'queryset_list_montana_ivf_val': queryset_list_montana_ivf_val,
        'queryset_list_montana_egg_val': queryset_list_montana_egg_val,
        'queryset_list_montana_embryo_val': queryset_list_montana_embryo_val,
        'queryset_list_montana_sperm_val': queryset_list_montana_sperm_val,
        'queryset_list_montana_icsi_val': queryset_list_montana_icsi_val,
        'queryset_list_montana_iui_val': queryset_list_montana_iui_val,

        'my_total_clinic_count_nebraska': my_total_clinic_count_nebraska,
        'queryset_list_nebraska_ivf_val': queryset_list_nebraska_ivf_val,
        'queryset_list_nebraska_egg_val': queryset_list_nebraska_egg_val,
        'queryset_list_nebraska_embryo_val': queryset_list_nebraska_embryo_val,
        'queryset_list_nebraska_sperm_val': queryset_list_nebraska_sperm_val,
        'queryset_list_nebraska_icsi_val': queryset_list_nebraska_icsi_val,
        'queryset_list_nebraska_iui_val': queryset_list_nebraska_iui_val,

        'my_total_clinic_count_newhampshire': my_total_clinic_count_newhampshire,
        'queryset_list_newhampshire_ivf_val': queryset_list_newhampshire_ivf_val,
        'queryset_list_newhampshire_egg_val': queryset_list_newhampshire_egg_val,
        'queryset_list_newhampshire_embryo_val': queryset_list_newhampshire_embryo_val,
        'queryset_list_newhampshire_sperm_val': queryset_list_newhampshire_sperm_val,
        'queryset_list_newhampshire_icsi_val': queryset_list_newhampshire_icsi_val,
        'queryset_list_newhampshire_iui_val': queryset_list_newhampshire_iui_val,

        'my_total_clinic_count_newjersey': my_total_clinic_count_newjersey,
        'queryset_list_newjersey_ivf_val': queryset_list_newjersey_ivf_val,
        'queryset_list_newjersey_egg_val': queryset_list_newjersey_egg_val,
        'queryset_list_newjersey_embryo_val': queryset_list_newjersey_embryo_val,
        'queryset_list_newjersey_sperm_val': queryset_list_newjersey_sperm_val,
        'queryset_list_newjersey_icsi_val': queryset_list_newjersey_icsi_val,
        'queryset_list_newjersey_iui_val': queryset_list_newjersey_iui_val,

        'my_total_clinic_count_newmexico': my_total_clinic_count_newmexico,
        'queryset_list_newmexico_ivf_val': queryset_list_newmexico_ivf_val,
        'queryset_list_newmexico_egg_val': queryset_list_newmexico_egg_val,
        'queryset_list_newmexico_embryo_val': queryset_list_newmexico_embryo_val,
        'queryset_list_newmexico_sperm_val': queryset_list_newmexico_sperm_val,
        'queryset_list_newmexico_icsi_val': queryset_list_newmexico_icsi_val,
        'queryset_list_newmexico_iui_val': queryset_list_newmexico_iui_val,

        'my_total_clinic_count_newyork': my_total_clinic_count_newyork,
        'queryset_list_newyork_ivf_val': queryset_list_newyork_ivf_val,
        'queryset_list_newyork_egg_val': queryset_list_newyork_egg_val,
        'queryset_list_newyork_embryo_val': queryset_list_newyork_embryo_val,
        'queryset_list_newyork_sperm_val': queryset_list_newyork_sperm_val,
        'queryset_list_newyork_icsi_val': queryset_list_newyork_icsi_val,
        'queryset_list_newyork_iui_val': queryset_list_newyork_iui_val,

        'my_total_clinic_count_northcarolina': my_total_clinic_count_northcarolina,
        'queryset_list_northcarolina_ivf_val': queryset_list_northcarolina_ivf_val,
        'queryset_list_northcarolina_egg_val': queryset_list_northcarolina_egg_val,
        'queryset_list_northcarolina_embryo_val': queryset_list_northcarolina_embryo_val,
        'queryset_list_northcarolina_sperm_val': queryset_list_northcarolina_sperm_val,
        'queryset_list_northcarolina_icsi_val': queryset_list_northcarolina_icsi_val,
        'queryset_list_northcarolina_iui_val': queryset_list_northcarolina_iui_val,

        'my_total_clinic_count_northdakota': my_total_clinic_count_northdakota,
        'queryset_list_northdakota_ivf_val': queryset_list_northdakota_ivf_val,
        'queryset_list_northdakota_egg_val': queryset_list_northdakota_egg_val,
        'queryset_list_northdakota_embryo_val': queryset_list_northdakota_embryo_val,
        'queryset_list_northdakota_sperm_val': queryset_list_northdakota_sperm_val,
        'queryset_list_northdakota_icsi_val': queryset_list_northdakota_icsi_val,
        'queryset_list_northdakota_iui_val': queryset_list_northdakota_iui_val,

        'my_total_clinic_count_nevada': my_total_clinic_count_nevada,
        'queryset_list_nevada_ivf_val': queryset_list_nevada_ivf_val,
        'queryset_list_nevada_egg_val': queryset_list_nevada_egg_val,
        'queryset_list_nevada_embryo_val': queryset_list_nevada_embryo_val,
        'queryset_list_nevada_sperm_val': queryset_list_nevada_sperm_val,
        'queryset_list_nevada_icsi_val': queryset_list_nevada_icsi_val,
        'queryset_list_nevada_iui_val': queryset_list_nevada_iui_val,

        'my_total_clinic_count_ohio': my_total_clinic_count_ohio,
        'queryset_list_ohio_ivf_val': queryset_list_ohio_ivf_val,
        'queryset_list_ohio_egg_val': queryset_list_ohio_egg_val,
        'queryset_list_ohio_embryo_val': queryset_list_ohio_embryo_val,
        'queryset_list_ohio_sperm_val': queryset_list_ohio_sperm_val,
        'queryset_list_ohio_icsi_val': queryset_list_ohio_icsi_val,
        'queryset_list_ohio_iui_val': queryset_list_ohio_iui_val,

        'my_total_clinic_count_oklahoma': my_total_clinic_count_oklahoma,
        'queryset_list_oklahoma_ivf_val': queryset_list_oklahoma_ivf_val,
        'queryset_list_oklahoma_egg_val': queryset_list_oklahoma_egg_val,
        'queryset_list_oklahoma_embryo_val': queryset_list_oklahoma_embryo_val,
        'queryset_list_oklahoma_sperm_val': queryset_list_oklahoma_sperm_val,
        'queryset_list_oklahoma_icsi_val': queryset_list_oklahoma_icsi_val,
        'queryset_list_oklahoma_iui_val': queryset_list_oklahoma_iui_val,

        'my_total_clinic_count_oregon': my_total_clinic_count_oregon,
        'queryset_list_oregon_ivf_val': queryset_list_oregon_ivf_val,
        'queryset_list_oregon_egg_val': queryset_list_oregon_egg_val,
        'queryset_list_oregon_embryo_val': queryset_list_oregon_embryo_val,
        'queryset_list_oregon_sperm_val': queryset_list_oregon_sperm_val,
        'queryset_list_oregon_icsi_val': queryset_list_oregon_icsi_val,
        'queryset_list_oregon_iui_val': queryset_list_oregon_iui_val,

        'my_total_clinic_count_pennsylvania': my_total_clinic_count_pennsylvania,
        'queryset_list_pennsylvania_ivf_val': queryset_list_pennsylvania_ivf_val,
        'queryset_list_pennsylvania_egg_val': queryset_list_pennsylvania_egg_val,
        'queryset_list_pennsylvania_embryo_val': queryset_list_pennsylvania_embryo_val,
        'queryset_list_pennsylvania_sperm_val': queryset_list_pennsylvania_sperm_val,
        'queryset_list_pennsylvania_icsi_val': queryset_list_pennsylvania_icsi_val,
        'queryset_list_pennsylvania_iui_val': queryset_list_pennsylvania_iui_val,

        'my_total_clinic_count_puertorico': my_total_clinic_count_puertorico,
        'queryset_list_puertorico_ivf_val': queryset_list_puertorico_ivf_val,
        'queryset_list_puertorico_egg_val': queryset_list_puertorico_egg_val,
        'queryset_list_puertorico_embryo_val': queryset_list_puertorico_embryo_val,
        'queryset_list_puertorico_sperm_val': queryset_list_puertorico_sperm_val,
        'queryset_list_puertorico_icsi_val': queryset_list_puertorico_icsi_val,
        'queryset_list_puertorico_iui_val': queryset_list_puertorico_iui_val,

        'my_total_clinic_count_southcarolina': my_total_clinic_count_southcarolina,
        'queryset_list_southcarolina_ivf_val': queryset_list_southcarolina_ivf_val,
        'queryset_list_southcarolina_egg_val': queryset_list_southcarolina_egg_val,
        'queryset_list_southcarolina_embryo_val': queryset_list_southcarolina_embryo_val,
        'queryset_list_southcarolina_sperm_val': queryset_list_southcarolina_sperm_val,
        'queryset_list_southcarolina_icsi_val': queryset_list_southcarolina_icsi_val,
        'queryset_list_southcarolina_iui_val': queryset_list_southcarolina_iui_val,

        'my_total_clinic_count_rhodeisland': my_total_clinic_count_rhodeisland,
        'queryset_list_rhodeisland_ivf_val': queryset_list_rhodeisland_ivf_val,
        'queryset_list_rhodeisland_egg_val': queryset_list_rhodeisland_egg_val,
        'queryset_list_rhodeisland_embryo_val': queryset_list_rhodeisland_embryo_val,
        'queryset_list_rhodeisland_sperm_val': queryset_list_rhodeisland_sperm_val,
        'queryset_list_rhodeisland_icsi_val': queryset_list_rhodeisland_icsi_val,
        'queryset_list_rhodeisland_iui_val': queryset_list_rhodeisland_iui_val,

        'my_total_clinic_count_southdakota': my_total_clinic_count_southdakota,
        'queryset_list_southdakota_ivf_val': queryset_list_southdakota_ivf_val,
        'queryset_list_southdakota_egg_val': queryset_list_southdakota_egg_val,
        'queryset_list_southdakota_embryo_val': queryset_list_southdakota_embryo_val,
        'queryset_list_southdakota_sperm_val': queryset_list_southdakota_sperm_val,
        'queryset_list_southdakota_icsi_val': queryset_list_southdakota_icsi_val,
        'queryset_list_southdakota_iui_val': queryset_list_southdakota_iui_val,

        'my_total_clinic_count_tennessee': my_total_clinic_count_tennessee,
        'queryset_list_tennessee_ivf_val': queryset_list_tennessee_ivf_val,
        'queryset_list_tennessee_egg_val': queryset_list_tennessee_egg_val,
        'queryset_list_tennessee_embryo_val': queryset_list_tennessee_embryo_val,
        'queryset_list_tennessee_sperm_val': queryset_list_tennessee_sperm_val,
        'queryset_list_tennessee_icsi_val': queryset_list_tennessee_icsi_val,
        'queryset_list_tennessee_iui_val': queryset_list_tennessee_iui_val,

        'my_total_clinic_count_texas': my_total_clinic_count_texas,
        'queryset_list_texas_ivf_val': queryset_list_texas_ivf_val,
        'queryset_list_texas_egg_val': queryset_list_texas_egg_val,
        'queryset_list_texas_embryo_val': queryset_list_texas_embryo_val,
        'queryset_list_texas_sperm_val': queryset_list_texas_sperm_val,
        'queryset_list_texas_icsi_val': queryset_list_texas_icsi_val,
        'queryset_list_texas_iui_val': queryset_list_texas_iui_val,

        'my_total_clinic_count_utah': my_total_clinic_count_utah,
        'queryset_list_utah_ivf_val': queryset_list_utah_ivf_val,
        'queryset_list_utah_egg_val': queryset_list_utah_egg_val,
        'queryset_list_utah_embryo_val': queryset_list_utah_embryo_val,
        'queryset_list_utah_sperm_val': queryset_list_utah_sperm_val,
        'queryset_list_utah_icsi_val': queryset_list_utah_icsi_val,
        'queryset_list_utah_iui_val': queryset_list_utah_iui_val,

        'my_total_clinic_count_vermont': my_total_clinic_count_vermont,
        'queryset_list_vermont_ivf_val': queryset_list_vermont_ivf_val,
        'queryset_list_vermont_egg_val': queryset_list_vermont_egg_val,
        'queryset_list_vermont_embryo_val': queryset_list_vermont_embryo_val,
        'queryset_list_vermont_sperm_val': queryset_list_vermont_sperm_val,
        'queryset_list_vermont_icsi_val': queryset_list_vermont_icsi_val,
        'queryset_list_vermont_iui_val': queryset_list_vermont_iui_val,

        'my_total_clinic_count_virginia': my_total_clinic_count_virginia,
        'queryset_list_virginia_ivf_val': queryset_list_virginia_ivf_val,
        'queryset_list_virginia_egg_val': queryset_list_virginia_egg_val,
        'queryset_list_virginia_embryo_val': queryset_list_virginia_embryo_val,
        'queryset_list_virginia_sperm_val': queryset_list_virginia_sperm_val,
        'queryset_list_virginia_icsi_val': queryset_list_virginia_icsi_val,
        'queryset_list_virginia_iui_val': queryset_list_virginia_iui_val,

        'my_total_clinic_count_washington': my_total_clinic_count_washington,
        'queryset_list_washington_ivf_val': queryset_list_washington_ivf_val,
        'queryset_list_washington_egg_val': queryset_list_washington_egg_val,
        'queryset_list_washington_embryo_val': queryset_list_washington_embryo_val,
        'queryset_list_washington_sperm_val': queryset_list_washington_sperm_val,
        'queryset_list_washington_icsi_val': queryset_list_washington_icsi_val,
        'queryset_list_washington_iui_val': queryset_list_washington_iui_val,

        'my_total_clinic_count_westvirginia': my_total_clinic_count_westvirginia,
        'queryset_list_westvirginia_ivf_val': queryset_list_westvirginia_ivf_val,
        'queryset_list_westvirginia_egg_val': queryset_list_westvirginia_egg_val,
        'queryset_list_westvirginia_embryo_val': queryset_list_westvirginia_embryo_val,
        'queryset_list_westvirginia_sperm_val': queryset_list_westvirginia_sperm_val,
        'queryset_list_westvirginia_icsi_val': queryset_list_westvirginia_icsi_val,
        'queryset_list_westvirginia_iui_val': queryset_list_westvirginia_iui_val,

        'my_total_clinic_count_wisconsin': my_total_clinic_count_wisconsin,
        'queryset_list_wisconsin_ivf_val': queryset_list_wisconsin_ivf_val,
        'queryset_list_wisconsin_egg_val': queryset_list_wisconsin_egg_val,
        'queryset_list_wisconsin_embryo_val': queryset_list_wisconsin_embryo_val,
        'queryset_list_wisconsin_sperm_val': queryset_list_wisconsin_sperm_val,
        'queryset_list_wisconsin_icsi_val': queryset_list_wisconsin_icsi_val,
        'queryset_list_wisconsin_iui_val': queryset_list_wisconsin_iui_val,

        'my_total_clinic_count_wyoming': my_total_clinic_count_wyoming,
        'queryset_list_wyoming_ivf_val': queryset_list_wyoming_ivf_val,
        'queryset_list_wyoming_egg_val': queryset_list_wyoming_egg_val,
        'queryset_list_wyoming_embryo_val': queryset_list_wyoming_embryo_val,
        'queryset_list_wyoming_sperm_val': queryset_list_wyoming_sperm_val,
        'queryset_list_wyoming_icsi_val': queryset_list_wyoming_icsi_val,
        'queryset_list_wyoming_iui_val': queryset_list_wyoming_iui_val,

        'my_total_clinic_count_districtofcolumbia': my_total_clinic_count_districtofcolumbia,
        'queryset_list_districtofcolumbia_ivf_val': queryset_list_districtofcolumbia_ivf_val,
        'queryset_list_districtofcolumbia_egg_val': queryset_list_districtofcolumbia_egg_val,
        'queryset_list_districtofcolumbia_embryo_val': queryset_list_districtofcolumbia_embryo_val,
        'queryset_list_districtofcolumbia_sperm_val': queryset_list_districtofcolumbia_sperm_val,
        'queryset_list_districtofcolumbia_icsi_val': queryset_list_districtofcolumbia_icsi_val,
        'queryset_list_districtofcolumbia_iui_val': queryset_list_districtofcolumbia_iui_val,
        }

    return render(request, 'main/Locations/USLocations/us-regions-ivf.html', context)

