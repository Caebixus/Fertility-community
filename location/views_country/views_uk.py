from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsUKRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'United Kingdom'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_uk_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_uk_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_uk_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_uk_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_uk_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_uk_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_uk_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_uk_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_uk_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_uk_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_uk_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_uk_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    region_name = 'Aberdeen'
    my_total_clinic_count_aberdeen = region_count(region_name)
    clinic_count = my_total_clinic_count_aberdeen

    queryset_list_aberdeen_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_aberdeen_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_aberdeen_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_aberdeen_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_aberdeen_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_aberdeen_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Bath'
    my_total_clinic_count_bath = region_count(region_name)
    clinic_count = my_total_clinic_count_bath

    queryset_list_bath_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_bath_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_bath_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_bath_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_bath_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_bath_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Belfast'
    my_total_clinic_count_belfast = region_count(region_name)
    clinic_count = my_total_clinic_count_belfast

    queryset_list_belfast_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_belfast_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_belfast_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_belfast_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_belfast_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_belfast_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Birmingham'
    my_total_clinic_count_birmingham = region_count(region_name)
    clinic_count = my_total_clinic_count_birmingham

    queryset_list_birmingham_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_birmingham_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_birmingham_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_birmingham_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_birmingham_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_birmingham_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Bournemouth'
    my_total_clinic_count_bournemouth = region_count(region_name)
    clinic_count = my_total_clinic_count_bournemouth

    queryset_list_bournemouth_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_bournemouth_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_bournemouth_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_bournemouth_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_bournemouth_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_bournemouth_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Brighton'
    my_total_clinic_count_brighton = region_count(region_name)
    clinic_count = my_total_clinic_count_brighton

    queryset_list_brighton_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_brighton_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_brighton_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_brighton_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_brighton_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_brighton_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Bristol'
    my_total_clinic_count_bristol = region_count(region_name)
    clinic_count = my_total_clinic_count_bristol

    queryset_list_bristol_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_bristol_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_bristol_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_bristol_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_bristol_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_bristol_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Cambridge'
    my_total_clinic_count_cambridge = region_count(region_name)
    clinic_count = my_total_clinic_count_cambridge

    queryset_list_cambridge_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_cambridge_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_cambridge_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_cambridge_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_cambridge_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_cambridge_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Cardiff'
    my_total_clinic_count_cardiff = region_count(region_name)
    clinic_count = my_total_clinic_count_cardiff

    queryset_list_cardiff_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_cardiff_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_cardiff_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_cardiff_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_cardiff_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_cardiff_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Colchester'
    my_total_clinic_count_colchester = region_count(region_name)
    clinic_count = my_total_clinic_count_colchester

    queryset_list_colchester_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_colchester_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_colchester_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_colchester_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_colchester_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_colchester_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Derby'
    my_total_clinic_count_derby = region_count(region_name)
    clinic_count = my_total_clinic_count_derby

    queryset_list_derby_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_derby_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_derby_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_derby_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_derby_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_derby_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Exeter'
    my_total_clinic_count_exeter = region_count(region_name)
    clinic_count = my_total_clinic_count_exeter

    queryset_list_exeter_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_exeter_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_exeter_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_exeter_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_exeter_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_exeter_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Glasgow'
    my_total_clinic_count_glasgow = region_count(region_name)
    clinic_count = my_total_clinic_count_glasgow

    queryset_list_glasgow_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_glasgow_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_glasgow_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_glasgow_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_glasgow_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_glasgow_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Hull'
    my_total_clinic_count_hull = region_count(region_name)
    clinic_count = my_total_clinic_count_hull

    queryset_list_hull_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_hull_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_hull_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_hull_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_hull_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_hull_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Chelmsford'
    my_total_clinic_count_chelmsford = region_count(region_name)
    clinic_count = my_total_clinic_count_chelmsford

    queryset_list_chelmsford_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_chelmsford_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_chelmsford_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_chelmsford_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_chelmsford_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_chelmsford_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Leeds'
    my_total_clinic_count_leeds = region_count(region_name)
    clinic_count = my_total_clinic_count_leeds

    queryset_list_leeds_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_leeds_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_leeds_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_leeds_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_leeds_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_leeds_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Leicester'
    my_total_clinic_count_leicester = region_count(region_name)
    clinic_count = my_total_clinic_count_leicester

    queryset_list_leicester_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_leicester_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_leicester_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_leicester_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_leicester_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_leicester_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Liverpool'
    my_total_clinic_count_liverpool = region_count(region_name)
    clinic_count = my_total_clinic_count_liverpool

    queryset_list_liverpool_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_liverpool_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_liverpool_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_liverpool_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_liverpool_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_liverpool_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'London'
    my_total_clinic_count_london = region_count(region_name)
    clinic_count = my_total_clinic_count_london

    queryset_list_london_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_london_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_london_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_london_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_london_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_london_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Manchester'
    my_total_clinic_count_manchester = region_count(region_name)
    clinic_count = my_total_clinic_count_manchester

    queryset_list_manchester_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_manchester_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_manchester_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_manchester_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_manchester_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_manchester_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Middlesbrough'
    my_total_clinic_count_middlesbrough = region_count(region_name)
    clinic_count = my_total_clinic_count_middlesbrough

    queryset_list_middlesbrough_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_middlesbrough_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_middlesbrough_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_middlesbrough_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_middlesbrough_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_middlesbrough_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Newcastle'
    my_total_clinic_count_newcastle = region_count(region_name)
    clinic_count = my_total_clinic_count_newcastle

    queryset_list_newcastle_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_newcastle_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_newcastle_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_newcastle_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_newcastle_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_newcastle_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Norwich'
    my_total_clinic_count_norwich = region_count(region_name)
    clinic_count = my_total_clinic_count_norwich

    queryset_list_norwich_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_norwich_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_norwich_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_norwich_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_norwich_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_norwich_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Nottingham'
    my_total_clinic_count_nottingham = region_count(region_name)
    clinic_count = my_total_clinic_count_nottingham

    queryset_list_nottingham_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_nottingham_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_nottingham_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_nottingham_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_nottingham_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_nottingham_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Oxford'
    my_total_clinic_count_oxford = region_count(region_name)
    clinic_count = my_total_clinic_count_oxford

    queryset_list_oxford_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_oxford_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_oxford_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_oxford_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_oxford_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_oxford_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Peterborough'
    my_total_clinic_count_peterborough = region_count(region_name)
    clinic_count = my_total_clinic_count_peterborough

    queryset_list_peterborough_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_peterborough_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_peterborough_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_peterborough_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_peterborough_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_peterborough_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Plymouth'
    my_total_clinic_count_plymouth = region_count(region_name)
    clinic_count = my_total_clinic_count_plymouth

    queryset_list_plymouth_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_plymouth_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_plymouth_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_plymouth_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_plymouth_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_plymouth_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Portsmouth'
    my_total_clinic_count_portsmouth = region_count(region_name)
    clinic_count = my_total_clinic_count_portsmouth

    queryset_list_portsmouth_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_portsmouth_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_portsmouth_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_portsmouth_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_portsmouth_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_portsmouth_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Salisbury'
    my_total_clinic_count_salisbury = region_count(region_name)
    clinic_count = my_total_clinic_count_salisbury

    queryset_list_salisbury_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_salisbury_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_salisbury_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_salisbury_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_salisbury_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_salisbury_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Sheffield'
    my_total_clinic_count_sheffield = region_count(region_name)
    clinic_count = my_total_clinic_count_sheffield

    queryset_list_sheffield_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_sheffield_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_sheffield_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_sheffield_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_sheffield_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_sheffield_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Southampton'
    my_total_clinic_count_southampton = region_count(region_name)
    clinic_count = my_total_clinic_count_southampton

    queryset_list_southampton_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_southampton_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_southampton_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_southampton_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_southampton_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_southampton_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    #--------------------------------------------------------------------------
    region_name = 'Swansea'
    my_total_clinic_count_swansea = region_count(region_name)
    clinic_count = my_total_clinic_count_swansea

    queryset_list_swansea_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_swansea_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_swansea_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_swansea_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_swansea_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_swansea_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_uk_natural_ivf_val': queryset_list_uk_natural_ivf_val,
        'queryset_list_uk_mild_ivf_val': queryset_list_uk_mild_ivf_val,
        'queryset_list_uk_standard_ivf_val': queryset_list_uk_standard_ivf_val,
        'queryset_list_uk_egg_ivf_val': queryset_list_uk_egg_ivf_val,
        'queryset_list_uk_known_egg_ivf_val': queryset_list_uk_known_egg_ivf_val,
        'queryset_list_uk_shared_egg_ivf_val': queryset_list_uk_shared_egg_ivf_val,
        'queryset_list_uk_embryo_ivf_val': queryset_list_uk_embryo_ivf_val,
        'queryset_list_uk_known_embryo_ivf_val': queryset_list_uk_known_embryo_ivf_val,
        'queryset_list_uk_sperm_ivf_val': queryset_list_uk_sperm_ivf_val,
        'queryset_list_uk_known_sperm_ivf_val': queryset_list_uk_known_sperm_ivf_val,
        'queryset_list_uk_icsi_val': queryset_list_uk_icsi_val,
        'queryset_list_uk_iui_val': queryset_list_uk_iui_val,

        'my_total_clinic_count_aberdeen': my_total_clinic_count_aberdeen,
        'queryset_list_aberdeen_ivf_val': queryset_list_aberdeen_ivf_val,
        'queryset_list_aberdeen_egg_val': queryset_list_aberdeen_egg_val,
        'queryset_list_aberdeen_embryo_val': queryset_list_aberdeen_embryo_val,
        'queryset_list_aberdeen_sperm_val': queryset_list_aberdeen_sperm_val,
        'queryset_list_aberdeen_icsi_val': queryset_list_aberdeen_icsi_val,
        'queryset_list_aberdeen_iui_val': queryset_list_aberdeen_iui_val,

        'my_total_clinic_count_bath': my_total_clinic_count_bath,
        'queryset_list_bath_ivf_val': queryset_list_bath_ivf_val,
        'queryset_list_bath_egg_val': queryset_list_bath_egg_val,
        'queryset_list_bath_embryo_val': queryset_list_bath_embryo_val,
        'queryset_list_bath_sperm_val': queryset_list_bath_sperm_val,
        'queryset_list_bath_icsi_val': queryset_list_bath_icsi_val,
        'queryset_list_bath_iui_val': queryset_list_bath_iui_val,

        'my_total_clinic_count_belfast': my_total_clinic_count_belfast,
        'queryset_list_belfast_ivf_val': queryset_list_belfast_ivf_val,
        'queryset_list_belfast_egg_val': queryset_list_belfast_egg_val,
        'queryset_list_belfast_embryo_val': queryset_list_belfast_embryo_val,
        'queryset_list_belfast_sperm_val': queryset_list_belfast_sperm_val,
        'queryset_list_belfast_icsi_val': queryset_list_belfast_icsi_val,
        'queryset_list_belfast_iui_val': queryset_list_belfast_iui_val,

        'my_total_clinic_count_birmingham': my_total_clinic_count_birmingham,
        'queryset_list_birmingham_ivf_val': queryset_list_birmingham_ivf_val,
        'queryset_list_birmingham_egg_val': queryset_list_birmingham_egg_val,
        'queryset_list_birmingham_embryo_val': queryset_list_birmingham_embryo_val,
        'queryset_list_birmingham_sperm_val': queryset_list_birmingham_sperm_val,
        'queryset_list_birmingham_icsi_val': queryset_list_birmingham_icsi_val,
        'queryset_list_birmingham_iui_val': queryset_list_birmingham_iui_val,

        'my_total_clinic_count_bournemouth': my_total_clinic_count_bournemouth,
        'queryset_list_bournemouth_ivf_val': queryset_list_bournemouth_ivf_val,
        'queryset_list_bournemouth_egg_val': queryset_list_bournemouth_egg_val,
        'queryset_list_bournemouth_embryo_val': queryset_list_bournemouth_embryo_val,
        'queryset_list_bournemouth_sperm_val': queryset_list_bournemouth_sperm_val,
        'queryset_list_bournemouth_icsi_val': queryset_list_bournemouth_icsi_val,
        'queryset_list_bournemouth_iui_val': queryset_list_bournemouth_iui_val,

        'my_total_clinic_count_brighton': my_total_clinic_count_brighton,
        'queryset_list_brighton_ivf_val': queryset_list_brighton_ivf_val,
        'queryset_list_brighton_egg_val': queryset_list_brighton_egg_val,
        'queryset_list_brighton_embryo_val': queryset_list_brighton_embryo_val,
        'queryset_list_brighton_sperm_val': queryset_list_brighton_sperm_val,
        'queryset_list_brighton_icsi_val': queryset_list_brighton_icsi_val,
        'queryset_list_brighton_iui_val': queryset_list_brighton_iui_val,

        'my_total_clinic_count_bristol': my_total_clinic_count_bristol,
        'queryset_list_bristol_ivf_val': queryset_list_bristol_ivf_val,
        'queryset_list_bristol_egg_val': queryset_list_bristol_egg_val,
        'queryset_list_bristol_embryo_val': queryset_list_bristol_embryo_val,
        'queryset_list_bristol_sperm_val': queryset_list_bristol_sperm_val,
        'queryset_list_bristol_icsi_val': queryset_list_bristol_icsi_val,
        'queryset_list_bristol_iui_val': queryset_list_bristol_iui_val,

        'my_total_clinic_count_cambridge': my_total_clinic_count_cambridge,
        'queryset_list_cambridge_ivf_val': queryset_list_cambridge_ivf_val,
        'queryset_list_cambridge_egg_val': queryset_list_cambridge_egg_val,
        'queryset_list_cambridge_embryo_val': queryset_list_cambridge_embryo_val,
        'queryset_list_cambridge_sperm_val': queryset_list_cambridge_sperm_val,
        'queryset_list_cambridge_icsi_val': queryset_list_cambridge_icsi_val,
        'queryset_list_cambridge_iui_val': queryset_list_cambridge_iui_val,

        'my_total_clinic_count_cardiff': my_total_clinic_count_cardiff,
        'queryset_list_cardiff_ivf_val': queryset_list_cardiff_ivf_val,
        'queryset_list_cardiff_egg_val': queryset_list_cardiff_egg_val,
        'queryset_list_cardiff_embryo_val': queryset_list_cardiff_embryo_val,
        'queryset_list_cardiff_sperm_val': queryset_list_cardiff_sperm_val,
        'queryset_list_cardiff_icsi_val': queryset_list_cardiff_icsi_val,
        'queryset_list_cardiff_iui_val': queryset_list_cardiff_iui_val,

        'my_total_clinic_count_colchester': my_total_clinic_count_colchester,
        'queryset_list_colchester_ivf_val': queryset_list_colchester_ivf_val,
        'queryset_list_colchester_egg_val': queryset_list_colchester_egg_val,
        'queryset_list_colchester_embryo_val': queryset_list_colchester_embryo_val,
        'queryset_list_colchester_sperm_val': queryset_list_colchester_sperm_val,
        'queryset_list_colchester_icsi_val': queryset_list_colchester_icsi_val,
        'queryset_list_colchester_iui_val': queryset_list_colchester_iui_val,

        'my_total_clinic_count_derby': my_total_clinic_count_derby,
        'queryset_list_derby_ivf_val': queryset_list_derby_ivf_val,
        'queryset_list_derby_egg_val': queryset_list_derby_egg_val,
        'queryset_list_derby_embryo_val': queryset_list_derby_embryo_val,
        'queryset_list_derby_sperm_val': queryset_list_derby_sperm_val,
        'queryset_list_derby_icsi_val': queryset_list_derby_icsi_val,
        'queryset_list_derby_iui_val': queryset_list_derby_iui_val,

        'my_total_clinic_count_exeter': my_total_clinic_count_exeter,
        'queryset_list_exeter_ivf_val': queryset_list_exeter_ivf_val,
        'queryset_list_exeter_egg_val': queryset_list_exeter_egg_val,
        'queryset_list_exeter_embryo_val': queryset_list_exeter_embryo_val,
        'queryset_list_exeter_sperm_val': queryset_list_exeter_sperm_val,
        'queryset_list_exeter_icsi_val': queryset_list_exeter_icsi_val,
        'queryset_list_exeter_iui_val': queryset_list_exeter_iui_val,

        'my_total_clinic_count_glasgow': my_total_clinic_count_glasgow,
        'queryset_list_glasgow_ivf_val': queryset_list_glasgow_ivf_val,
        'queryset_list_glasgow_egg_val': queryset_list_glasgow_egg_val,
        'queryset_list_glasgow_embryo_val': queryset_list_glasgow_embryo_val,
        'queryset_list_glasgow_sperm_val': queryset_list_glasgow_sperm_val,
        'queryset_list_glasgow_icsi_val': queryset_list_glasgow_icsi_val,
        'queryset_list_glasgow_iui_val': queryset_list_glasgow_iui_val,

        'my_total_clinic_count_hull': my_total_clinic_count_hull,
        'queryset_list_hull_ivf_val': queryset_list_hull_ivf_val,
        'queryset_list_hull_egg_val': queryset_list_hull_egg_val,
        'queryset_list_hull_embryo_val': queryset_list_hull_embryo_val,
        'queryset_list_hull_sperm_val': queryset_list_hull_sperm_val,
        'queryset_list_hull_icsi_val': queryset_list_hull_icsi_val,
        'queryset_list_hull_iui_val': queryset_list_hull_iui_val,

        'my_total_clinic_count_chelmsford': my_total_clinic_count_chelmsford,
        'queryset_list_chelmsford_ivf_val': queryset_list_chelmsford_ivf_val,
        'queryset_list_chelmsford_egg_val': queryset_list_chelmsford_egg_val,
        'queryset_list_chelmsford_embryo_val': queryset_list_chelmsford_embryo_val,
        'queryset_list_chelmsford_sperm_val': queryset_list_chelmsford_sperm_val,
        'queryset_list_chelmsford_icsi_val': queryset_list_chelmsford_icsi_val,
        'queryset_list_chelmsford_iui_val': queryset_list_chelmsford_iui_val,

        'my_total_clinic_count_leeds': my_total_clinic_count_leeds,
        'queryset_list_leeds_ivf_val': queryset_list_leeds_ivf_val,
        'queryset_list_leeds_egg_val': queryset_list_leeds_egg_val,
        'queryset_list_leeds_embryo_val': queryset_list_leeds_embryo_val,
        'queryset_list_leeds_sperm_val': queryset_list_leeds_sperm_val,
        'queryset_list_leeds_icsi_val': queryset_list_leeds_icsi_val,
        'queryset_list_leeds_iui_val': queryset_list_leeds_iui_val,

        'my_total_clinic_count_leicester': my_total_clinic_count_leicester,
        'queryset_list_leicester_ivf_val': queryset_list_leicester_ivf_val,
        'queryset_list_leicester_egg_val': queryset_list_leicester_egg_val,
        'queryset_list_leicester_embryo_val': queryset_list_leicester_embryo_val,
        'queryset_list_leicester_sperm_val': queryset_list_leicester_sperm_val,
        'queryset_list_leicester_icsi_val': queryset_list_leicester_icsi_val,
        'queryset_list_leicester_iui_val': queryset_list_leicester_iui_val,

        'my_total_clinic_count_liverpool': my_total_clinic_count_liverpool,
        'queryset_list_liverpool_ivf_val': queryset_list_liverpool_ivf_val,
        'queryset_list_liverpool_egg_val': queryset_list_liverpool_egg_val,
        'queryset_list_liverpool_embryo_val': queryset_list_liverpool_embryo_val,
        'queryset_list_liverpool_sperm_val': queryset_list_liverpool_sperm_val,
        'queryset_list_liverpool_icsi_val': queryset_list_liverpool_icsi_val,
        'queryset_list_liverpool_iui_val': queryset_list_liverpool_iui_val,

        'my_total_clinic_count_london': my_total_clinic_count_london,
        'queryset_list_london_ivf_val': queryset_list_london_ivf_val,
        'queryset_list_london_egg_val': queryset_list_london_egg_val,
        'queryset_list_london_embryo_val': queryset_list_london_embryo_val,
        'queryset_list_london_sperm_val': queryset_list_london_sperm_val,
        'queryset_list_london_icsi_val': queryset_list_london_icsi_val,
        'queryset_list_london_iui_val': queryset_list_london_iui_val,

        'my_total_clinic_count_manchester': my_total_clinic_count_manchester,
        'queryset_list_manchester_ivf_val': queryset_list_manchester_ivf_val,
        'queryset_list_manchester_egg_val': queryset_list_manchester_egg_val,
        'queryset_list_manchester_embryo_val': queryset_list_manchester_embryo_val,
        'queryset_list_manchester_sperm_val': queryset_list_manchester_sperm_val,
        'queryset_list_manchester_icsi_val': queryset_list_manchester_icsi_val,
        'queryset_list_manchester_iui_val': queryset_list_manchester_iui_val,

        'my_total_clinic_count_middlesbrough': my_total_clinic_count_middlesbrough,
        'queryset_list_middlesbrough_ivf_val': queryset_list_middlesbrough_ivf_val,
        'queryset_list_middlesbrough_egg_val': queryset_list_middlesbrough_egg_val,
        'queryset_list_middlesbrough_embryo_val': queryset_list_middlesbrough_embryo_val,
        'queryset_list_middlesbrough_sperm_val': queryset_list_middlesbrough_sperm_val,
        'queryset_list_middlesbrough_icsi_val': queryset_list_middlesbrough_icsi_val,
        'queryset_list_middlesbrough_iui_val': queryset_list_middlesbrough_iui_val,

        'my_total_clinic_count_newcastle': my_total_clinic_count_newcastle,
        'queryset_list_newcastle_ivf_val': queryset_list_newcastle_ivf_val,
        'queryset_list_newcastle_egg_val': queryset_list_newcastle_egg_val,
        'queryset_list_newcastle_embryo_val': queryset_list_newcastle_embryo_val,
        'queryset_list_newcastle_sperm_val': queryset_list_newcastle_sperm_val,
        'queryset_list_newcastle_icsi_val': queryset_list_newcastle_icsi_val,
        'queryset_list_newcastle_iui_val': queryset_list_newcastle_iui_val,

        'my_total_clinic_count_norwich': my_total_clinic_count_norwich,
        'queryset_list_norwich_ivf_val': queryset_list_norwich_ivf_val,
        'queryset_list_norwich_egg_val': queryset_list_norwich_egg_val,
        'queryset_list_norwich_embryo_val': queryset_list_norwich_embryo_val,
        'queryset_list_norwich_sperm_val': queryset_list_norwich_sperm_val,
        'queryset_list_norwich_icsi_val': queryset_list_norwich_icsi_val,
        'queryset_list_norwich_iui_val': queryset_list_norwich_iui_val,

        'my_total_clinic_count_nottingham': my_total_clinic_count_nottingham,
        'queryset_list_nottingham_ivf_val': queryset_list_nottingham_ivf_val,
        'queryset_list_nottingham_egg_val': queryset_list_nottingham_egg_val,
        'queryset_list_nottingham_embryo_val': queryset_list_nottingham_embryo_val,
        'queryset_list_nottingham_sperm_val': queryset_list_nottingham_sperm_val,
        'queryset_list_nottingham_icsi_val': queryset_list_nottingham_icsi_val,
        'queryset_list_nottingham_iui_val': queryset_list_nottingham_iui_val,

        'my_total_clinic_count_oxford': my_total_clinic_count_oxford,
        'queryset_list_oxford_ivf_val': queryset_list_oxford_ivf_val,
        'queryset_list_oxford_egg_val': queryset_list_oxford_egg_val,
        'queryset_list_oxford_embryo_val': queryset_list_oxford_embryo_val,
        'queryset_list_oxford_sperm_val': queryset_list_oxford_sperm_val,
        'queryset_list_oxford_icsi_val': queryset_list_oxford_icsi_val,
        'queryset_list_oxford_iui_val': queryset_list_oxford_iui_val,

        'my_total_clinic_count_peterborough': my_total_clinic_count_peterborough,
        'queryset_list_peterborough_ivf_val': queryset_list_peterborough_ivf_val,
        'queryset_list_peterborough_egg_val': queryset_list_peterborough_egg_val,
        'queryset_list_peterborough_embryo_val': queryset_list_peterborough_embryo_val,
        'queryset_list_peterborough_sperm_val': queryset_list_peterborough_sperm_val,
        'queryset_list_peterborough_icsi_val': queryset_list_peterborough_icsi_val,
        'queryset_list_peterborough_iui_val': queryset_list_peterborough_iui_val,

        'my_total_clinic_count_plymouth': my_total_clinic_count_plymouth,
        'queryset_list_plymouth_ivf_val': queryset_list_plymouth_ivf_val,
        'queryset_list_plymouth_egg_val': queryset_list_plymouth_egg_val,
        'queryset_list_plymouth_embryo_val': queryset_list_plymouth_embryo_val,
        'queryset_list_plymouth_sperm_val': queryset_list_plymouth_sperm_val,
        'queryset_list_plymouth_icsi_val': queryset_list_plymouth_icsi_val,
        'queryset_list_plymouth_iui_val': queryset_list_plymouth_iui_val,

        'my_total_clinic_count_portsmouth': my_total_clinic_count_portsmouth,
        'queryset_list_portsmouth_ivf_val': queryset_list_portsmouth_ivf_val,
        'queryset_list_portsmouth_egg_val': queryset_list_portsmouth_egg_val,
        'queryset_list_portsmouth_embryo_val': queryset_list_portsmouth_embryo_val,
        'queryset_list_portsmouth_sperm_val': queryset_list_portsmouth_sperm_val,
        'queryset_list_portsmouth_icsi_val': queryset_list_portsmouth_icsi_val,
        'queryset_list_portsmouth_iui_val': queryset_list_portsmouth_iui_val,

        'my_total_clinic_count_salisbury': my_total_clinic_count_salisbury,
        'queryset_list_salisbury_ivf_val': queryset_list_salisbury_ivf_val,
        'queryset_list_salisbury_egg_val': queryset_list_salisbury_egg_val,
        'queryset_list_salisbury_embryo_val': queryset_list_salisbury_embryo_val,
        'queryset_list_salisbury_sperm_val': queryset_list_salisbury_sperm_val,
        'queryset_list_salisbury_icsi_val': queryset_list_salisbury_icsi_val,
        'queryset_list_salisbury_iui_val': queryset_list_salisbury_iui_val,

        'my_total_clinic_count_sheffield': my_total_clinic_count_sheffield,
        'queryset_list_sheffield_ivf_val': queryset_list_sheffield_ivf_val,
        'queryset_list_sheffield_egg_val': queryset_list_sheffield_egg_val,
        'queryset_list_sheffield_embryo_val': queryset_list_sheffield_embryo_val,
        'queryset_list_sheffield_sperm_val': queryset_list_sheffield_sperm_val,
        'queryset_list_sheffield_icsi_val': queryset_list_sheffield_icsi_val,
        'queryset_list_sheffield_iui_val': queryset_list_sheffield_iui_val,

        'my_total_clinic_count_southampton': my_total_clinic_count_southampton,
        'queryset_list_southampton_ivf_val': queryset_list_southampton_ivf_val,
        'queryset_list_southampton_egg_val': queryset_list_southampton_egg_val,
        'queryset_list_southampton_embryo_val': queryset_list_southampton_embryo_val,
        'queryset_list_southampton_sperm_val': queryset_list_southampton_sperm_val,
        'queryset_list_southampton_icsi_val': queryset_list_southampton_icsi_val,
        'queryset_list_southampton_iui_val': queryset_list_southampton_iui_val,

        'my_total_clinic_count_swansea': my_total_clinic_count_swansea,
        'queryset_list_swansea_ivf_val': queryset_list_swansea_ivf_val,
        'queryset_list_swansea_egg_val': queryset_list_swansea_egg_val,
        'queryset_list_swansea_embryo_val': queryset_list_swansea_embryo_val,
        'queryset_list_swansea_sperm_val': queryset_list_swansea_sperm_val,
        'queryset_list_swansea_icsi_val': queryset_list_swansea_icsi_val,
        'queryset_list_swansea_iui_val': queryset_list_swansea_iui_val,
        }

    return render(request, 'main/Locations/UKLocations/uk-regions-ivf.html', context)

