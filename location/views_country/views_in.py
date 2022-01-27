from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_city_average_value
from base.constant_variables import year


def locationsINRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'India'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_in_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_in_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_in_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_in_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_in_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_in_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_in_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_in_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_in_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_in_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_in_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_in_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    city_name = 'Amdavad'
    my_total_clinic_count_amdavad = region_count(city_name)
    clinic_count = my_total_clinic_count_amdavad

    queryset_list_amdavad_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_amdavad_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_amdavad_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_amdavad_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_amdavad_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_amdavad_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Bangalore'
    my_total_clinic_count_bangalore = region_count(city_name)
    clinic_count = my_total_clinic_count_bangalore

    queryset_list_bangalore_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_bangalore_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_bangalore_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_bangalore_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_bangalore_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_bangalore_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Bhopal'
    my_total_clinic_count_bhopal = region_count(city_name)
    clinic_count = my_total_clinic_count_bhopal

    queryset_list_bhopal_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_bhopal_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_bhopal_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_bhopal_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_bhopal_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_bhopal_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Bhubaneswar'
    my_total_clinic_count_bhubaneswar = region_count(city_name)
    clinic_count = my_total_clinic_count_bhubaneswar

    queryset_list_bhubaneswar_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_bhubaneswar_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_bhubaneswar_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_bhubaneswar_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_bhubaneswar_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_bhubaneswar_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Dehradun'
    my_total_clinic_count_dehradun = region_count(city_name)
    clinic_count = my_total_clinic_count_dehradun

    queryset_list_dehradun_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_dehradun_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_dehradun_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_dehradun_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_dehradun_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_dehradun_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Faridabad'
    my_total_clinic_count_faridabad = region_count(city_name)
    clinic_count = my_total_clinic_count_faridabad

    queryset_list_faridabad_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_faridabad_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_faridabad_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_faridabad_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_faridabad_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_faridabad_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Hyderabad'
    my_total_clinic_count_hyderabad = region_count(city_name)
    clinic_count = my_total_clinic_count_hyderabad

    queryset_list_hyderabad_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_hyderabad_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_hyderabad_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_hyderabad_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_hyderabad_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_hyderabad_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Chandigarh'
    my_total_clinic_count_chandigarh = region_count(city_name)
    clinic_count = my_total_clinic_count_chandigarh

    queryset_list_chandigarh_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_chandigarh_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_chandigarh_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_chandigarh_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_chandigarh_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_chandigarh_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Chennai'
    my_total_clinic_count_chennai = region_count(city_name)
    clinic_count = my_total_clinic_count_chennai

    queryset_list_chennai_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_chennai_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_chennai_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_chennai_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_chennai_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_chennai_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Indore'
    my_total_clinic_count_indore = region_count(city_name)
    clinic_count = my_total_clinic_count_indore

    queryset_list_indore_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_indore_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_indore_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_indore_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_indore_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_indore_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Jaipur'
    my_total_clinic_count_jaipur = region_count(city_name)
    clinic_count = my_total_clinic_count_jaipur

    queryset_list_jaipur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_jaipur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_jaipur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_jaipur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_jaipur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_jaipur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Jamshedpur'
    my_total_clinic_count_jamshedpur = region_count(city_name)
    clinic_count = my_total_clinic_count_jamshedpur

    queryset_list_jamshedpur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_jamshedpur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_jamshedpur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_jamshedpur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_jamshedpur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_jamshedpur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Kanpur'
    my_total_clinic_count_kanpur = region_count(city_name)
    clinic_count = my_total_clinic_count_kanpur

    queryset_list_kanpur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_kanpur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_kanpur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_kanpur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_kanpur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_kanpur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Kochi'
    my_total_clinic_count_kochi = region_count(city_name)
    clinic_count = my_total_clinic_count_kochi

    queryset_list_kochi_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_kochi_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_kochi_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_kochi_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_kochi_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_kochi_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Kolkata'
    my_total_clinic_count_kolkata = region_count(city_name)
    clinic_count = my_total_clinic_count_kolkata

    queryset_list_kolkata_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_kolkata_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_kolkata_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_kolkata_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_kolkata_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_kolkata_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Lucknow'
    my_total_clinic_count_lucknow = region_count(city_name)
    clinic_count = my_total_clinic_count_lucknow

    queryset_list_lucknow_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_lucknow_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_lucknow_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_lucknow_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_lucknow_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_lucknow_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Mumbai'
    my_total_clinic_count_mumbai = region_count(city_name)
    clinic_count = my_total_clinic_count_mumbai

    queryset_list_mumbai_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_mumbai_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_mumbai_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_mumbai_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_mumbai_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_mumbai_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Nagpur'
    my_total_clinic_count_nagpur = region_count(city_name)
    clinic_count = my_total_clinic_count_nagpur

    queryset_list_nagpur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_nagpur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_nagpur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_nagpur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_nagpur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_nagpur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Patna'
    my_total_clinic_count_patna = region_count(city_name)
    clinic_count = my_total_clinic_count_patna

    queryset_list_patna_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_patna_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_patna_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_patna_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_patna_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_patna_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Raipur'
    my_total_clinic_count_raipur = region_count(city_name)
    clinic_count = my_total_clinic_count_raipur

    queryset_list_raipur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_raipur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_raipur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_raipur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_raipur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_raipur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Trivandrum'
    my_total_clinic_count_trivandrum = region_count(city_name)
    clinic_count = my_total_clinic_count_trivandrum

    queryset_list_trivandrum_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_trivandrum_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_trivandrum_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_trivandrum_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_trivandrum_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_trivandrum_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Ludhiana'
    my_total_clinic_count_ludhiana = region_count(city_name)
    clinic_count = my_total_clinic_count_ludhiana

    queryset_list_ludhiana_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_ludhiana_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_ludhiana_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_ludhiana_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_ludhiana_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_ludhiana_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Visakhapatnam'
    my_total_clinic_count_visakhapatnam = region_count(city_name)
    clinic_count = my_total_clinic_count_visakhapatnam

    queryset_list_visakhapatnam_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_visakhapatnam_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_visakhapatnam_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_visakhapatnam_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_visakhapatnam_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_visakhapatnam_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Vijayawada'
    my_total_clinic_count_vijayawada = region_count(city_name)
    clinic_count = my_total_clinic_count_vijayawada

    queryset_list_vijayawada_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_vijayawada_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_vijayawada_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_vijayawada_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_vijayawada_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_vijayawada_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'New Delhi'
    my_total_clinic_count_newdelhi = region_count(city_name)
    clinic_count = my_total_clinic_count_newdelhi

    queryset_list_newdelhi_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_newdelhi_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_newdelhi_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_newdelhi_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_newdelhi_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_newdelhi_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Vadodara'
    my_total_clinic_count_vadodara = region_count(city_name)
    clinic_count = my_total_clinic_count_vadodara

    queryset_list_vadodara_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_vadodara_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_vadodara_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_vadodara_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_vadodara_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_vadodara_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Gurugram'
    my_total_clinic_count_gurugram = region_count(city_name)
    clinic_count = my_total_clinic_count_gurugram

    queryset_list_gurugram_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_gurugram_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_gurugram_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_gurugram_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_gurugram_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_gurugram_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Rohtak'
    my_total_clinic_count_rohtak = region_count(city_name)
    clinic_count = my_total_clinic_count_rohtak

    queryset_list_rohtak_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_rohtak_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_rohtak_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_rohtak_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_rohtak_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_rohtak_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Jammu'
    my_total_clinic_count_jammu = region_count(city_name)
    clinic_count = my_total_clinic_count_jammu

    queryset_list_jammu_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_jammu_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_jammu_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_jammu_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_jammu_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_jammu_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Ranchi'
    my_total_clinic_count_ranchi = region_count(city_name)
    clinic_count = my_total_clinic_count_ranchi

    queryset_list_ranchi_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_ranchi_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_ranchi_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_ranchi_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_ranchi_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_ranchi_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Pune'
    my_total_clinic_count_pune = region_count(city_name)
    clinic_count = my_total_clinic_count_pune

    queryset_list_pune_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_pune_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_pune_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_pune_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_pune_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_pune_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Gwalior'
    my_total_clinic_count_gwalior = region_count(city_name)
    clinic_count = my_total_clinic_count_gwalior

    queryset_list_gwalior_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_gwalior_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_gwalior_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_gwalior_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_gwalior_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_gwalior_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Warangal'
    my_total_clinic_count_warangal = region_count(city_name)
    clinic_count = my_total_clinic_count_warangal

    queryset_list_warangal_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_warangal_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_warangal_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_warangal_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_warangal_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_warangal_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Gachibowli'
    my_total_clinic_count_gachibowli = region_count(city_name)
    clinic_count = my_total_clinic_count_gachibowli

    queryset_list_gachibowli_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_gachibowli_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_gachibowli_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_gachibowli_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_gachibowli_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_gachibowli_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Madhapur'
    my_total_clinic_count_madhapur = region_count(city_name)
    clinic_count = my_total_clinic_count_madhapur

    queryset_list_madhapur_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_madhapur_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_madhapur_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_madhapur_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_madhapur_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_madhapur_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Noida'
    my_total_clinic_count_noida = region_count(city_name)
    clinic_count = my_total_clinic_count_noida

    queryset_list_noida_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_noida_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_noida_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_noida_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_noida_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_noida_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Meerut'
    my_total_clinic_count_meerut = region_count(city_name)
    clinic_count = my_total_clinic_count_meerut

    queryset_list_meerut_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_meerut_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_meerut_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_meerut_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_meerut_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_meerut_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Haldwani'
    my_total_clinic_count_haldwani = region_count(city_name)
    clinic_count = my_total_clinic_count_haldwani

    queryset_list_haldwani_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_haldwani_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_haldwani_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_haldwani_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_haldwani_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_haldwani_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_in_natural_ivf_val': queryset_list_in_natural_ivf_val,
        'queryset_list_in_mild_ivf_val': queryset_list_in_mild_ivf_val,
        'queryset_list_in_standard_ivf_val': queryset_list_in_standard_ivf_val,
        'queryset_list_in_egg_ivf_val': queryset_list_in_egg_ivf_val,
        'queryset_list_in_known_egg_ivf_val': queryset_list_in_known_egg_ivf_val,
        'queryset_list_in_shared_egg_ivf_val': queryset_list_in_shared_egg_ivf_val,
        'queryset_list_in_embryo_ivf_val': queryset_list_in_embryo_ivf_val,
        'queryset_list_in_known_embryo_ivf_val': queryset_list_in_known_embryo_ivf_val,
        'queryset_list_in_sperm_ivf_val': queryset_list_in_sperm_ivf_val,
        'queryset_list_in_known_sperm_ivf_val': queryset_list_in_known_sperm_ivf_val,
        'queryset_list_in_icsi_val': queryset_list_in_icsi_val,
        'queryset_list_in_iui_val': queryset_list_in_iui_val,

        'my_total_clinic_count_amdavad': my_total_clinic_count_amdavad,
        'queryset_list_amdavad_ivf_val': queryset_list_amdavad_ivf_val,
        'queryset_list_amdavad_egg_val': queryset_list_amdavad_egg_val,
        'queryset_list_amdavad_embryo_val': queryset_list_amdavad_embryo_val,
        'queryset_list_amdavad_sperm_val': queryset_list_amdavad_sperm_val,
        'queryset_list_amdavad_icsi_val': queryset_list_amdavad_icsi_val,
        'queryset_list_amdavad_iui_val': queryset_list_amdavad_iui_val,

        'my_total_clinic_count_bangalore': my_total_clinic_count_bangalore,
        'queryset_list_bangalore_ivf_val': queryset_list_bangalore_ivf_val,
        'queryset_list_bangalore_egg_val': queryset_list_bangalore_egg_val,
        'queryset_list_bangalore_embryo_val': queryset_list_bangalore_embryo_val,
        'queryset_list_bangalore_sperm_val': queryset_list_bangalore_sperm_val,
        'queryset_list_bangalore_icsi_val': queryset_list_bangalore_icsi_val,
        'queryset_list_bangalore_iui_val': queryset_list_bangalore_iui_val,

        'my_total_clinic_count_bhopal': my_total_clinic_count_bhopal,
        'queryset_list_bhopal_ivf_val': queryset_list_bhopal_ivf_val,
        'queryset_list_bhopal_egg_val': queryset_list_bhopal_egg_val,
        'queryset_list_bhopal_embryo_val': queryset_list_bhopal_embryo_val,
        'queryset_list_bhopal_sperm_val': queryset_list_bhopal_sperm_val,
        'queryset_list_bhopal_icsi_val': queryset_list_bhopal_icsi_val,
        'queryset_list_bhopal_iui_val': queryset_list_bhopal_iui_val,

        'my_total_clinic_count_bhubaneswar': my_total_clinic_count_bhubaneswar,
        'queryset_list_bhubaneswar_ivf_val': queryset_list_bhubaneswar_ivf_val,
        'queryset_list_bhubaneswar_egg_val': queryset_list_bhubaneswar_egg_val,
        'queryset_list_bhubaneswar_embryo_val': queryset_list_bhubaneswar_embryo_val,
        'queryset_list_bhubaneswar_sperm_val': queryset_list_bhubaneswar_sperm_val,
        'queryset_list_bhubaneswar_icsi_val': queryset_list_bhubaneswar_icsi_val,
        'queryset_list_bhubaneswar_iui_val': queryset_list_bhubaneswar_iui_val,

        'my_total_clinic_count_dehradun': my_total_clinic_count_dehradun,
        'queryset_list_dehradun_ivf_val': queryset_list_dehradun_ivf_val,
        'queryset_list_dehradun_egg_val': queryset_list_dehradun_egg_val,
        'queryset_list_dehradun_embryo_val': queryset_list_dehradun_embryo_val,
        'queryset_list_dehradun_sperm_val': queryset_list_dehradun_sperm_val,
        'queryset_list_dehradun_icsi_val': queryset_list_dehradun_icsi_val,
        'queryset_list_dehradun_iui_val': queryset_list_dehradun_iui_val,

        'my_total_clinic_count_faridabad': my_total_clinic_count_faridabad,
        'queryset_list_faridabad_ivf_val': queryset_list_faridabad_ivf_val,
        'queryset_list_faridabad_egg_val': queryset_list_faridabad_egg_val,
        'queryset_list_faridabad_embryo_val': queryset_list_faridabad_embryo_val,
        'queryset_list_faridabad_sperm_val': queryset_list_faridabad_sperm_val,
        'queryset_list_faridabad_icsi_val': queryset_list_faridabad_icsi_val,
        'queryset_list_faridabad_iui_val': queryset_list_faridabad_iui_val,

        'my_total_clinic_count_hyderabad': my_total_clinic_count_hyderabad,
        'queryset_list_hyderabad_ivf_val': queryset_list_hyderabad_ivf_val,
        'queryset_list_hyderabad_egg_val': queryset_list_hyderabad_egg_val,
        'queryset_list_hyderabad_embryo_val': queryset_list_hyderabad_embryo_val,
        'queryset_list_hyderabad_sperm_val': queryset_list_hyderabad_sperm_val,
        'queryset_list_hyderabad_icsi_val': queryset_list_hyderabad_icsi_val,
        'queryset_list_hyderabad_iui_val': queryset_list_hyderabad_iui_val,

        'my_total_clinic_count_chandigarh': my_total_clinic_count_chandigarh,
        'queryset_list_chandigarh_ivf_val': queryset_list_chandigarh_ivf_val,
        'queryset_list_chandigarh_egg_val': queryset_list_chandigarh_egg_val,
        'queryset_list_chandigarh_embryo_val': queryset_list_chandigarh_embryo_val,
        'queryset_list_chandigarh_sperm_val': queryset_list_chandigarh_sperm_val,
        'queryset_list_chandigarh_icsi_val': queryset_list_chandigarh_icsi_val,
        'queryset_list_chandigarh_iui_val': queryset_list_chandigarh_iui_val,

        'my_total_clinic_count_chennai': my_total_clinic_count_chennai,
        'queryset_list_chennai_ivf_val': queryset_list_chennai_ivf_val,
        'queryset_list_chennai_egg_val': queryset_list_chennai_egg_val,
        'queryset_list_chennai_embryo_val': queryset_list_chennai_embryo_val,
        'queryset_list_chennai_sperm_val': queryset_list_chennai_sperm_val,
        'queryset_list_chennai_icsi_val': queryset_list_chennai_icsi_val,
        'queryset_list_chennai_iui_val': queryset_list_chennai_iui_val,

        'my_total_clinic_count_indore': my_total_clinic_count_indore,
        'queryset_list_indore_ivf_val': queryset_list_indore_ivf_val,
        'queryset_list_indore_egg_val': queryset_list_indore_egg_val,
        'queryset_list_indore_embryo_val': queryset_list_indore_embryo_val,
        'queryset_list_indore_sperm_val': queryset_list_indore_sperm_val,
        'queryset_list_indore_icsi_val': queryset_list_indore_icsi_val,
        'queryset_list_indore_iui_val': queryset_list_indore_iui_val,

        'my_total_clinic_count_jaipur': my_total_clinic_count_jaipur,
        'queryset_list_jaipur_ivf_val': queryset_list_jaipur_ivf_val,
        'queryset_list_jaipur_egg_val': queryset_list_jaipur_egg_val,
        'queryset_list_jaipur_embryo_val': queryset_list_jaipur_embryo_val,
        'queryset_list_jaipur_sperm_val': queryset_list_jaipur_sperm_val,
        'queryset_list_jaipur_icsi_val': queryset_list_jaipur_icsi_val,
        'queryset_list_jaipur_iui_val': queryset_list_jaipur_iui_val,

        'my_total_clinic_count_jamshedpur': my_total_clinic_count_jamshedpur,
        'queryset_list_jamshedpur_ivf_val': queryset_list_jamshedpur_ivf_val,
        'queryset_list_jamshedpur_egg_val': queryset_list_jamshedpur_egg_val,
        'queryset_list_jamshedpur_embryo_val': queryset_list_jamshedpur_embryo_val,
        'queryset_list_jamshedpur_sperm_val': queryset_list_jamshedpur_sperm_val,
        'queryset_list_jamshedpur_icsi_val': queryset_list_jamshedpur_icsi_val,
        'queryset_list_jamshedpur_iui_val': queryset_list_jamshedpur_iui_val,

        'my_total_clinic_count_kanpur': my_total_clinic_count_kanpur,
        'queryset_list_kanpur_ivf_val': queryset_list_kanpur_ivf_val,
        'queryset_list_kanpur_egg_val': queryset_list_kanpur_egg_val,
        'queryset_list_kanpur_embryo_val': queryset_list_kanpur_embryo_val,
        'queryset_list_kanpur_sperm_val': queryset_list_kanpur_sperm_val,
        'queryset_list_kanpur_icsi_val': queryset_list_kanpur_icsi_val,
        'queryset_list_kanpur_iui_val': queryset_list_kanpur_iui_val,

        'my_total_clinic_count_kochi': my_total_clinic_count_kochi,
        'queryset_list_kochi_ivf_val': queryset_list_kochi_ivf_val,
        'queryset_list_kochi_egg_val': queryset_list_kochi_egg_val,
        'queryset_list_kochi_embryo_val': queryset_list_kochi_embryo_val,
        'queryset_list_kochi_sperm_val': queryset_list_kochi_sperm_val,
        'queryset_list_kochi_icsi_val': queryset_list_kochi_icsi_val,
        'queryset_list_kochi_iui_val': queryset_list_kochi_iui_val,

        'my_total_clinic_count_kolkata': my_total_clinic_count_kolkata,
        'queryset_list_kolkata_ivf_val': queryset_list_kolkata_ivf_val,
        'queryset_list_kolkata_egg_val': queryset_list_kolkata_egg_val,
        'queryset_list_kolkata_embryo_val': queryset_list_kolkata_embryo_val,
        'queryset_list_kolkata_sperm_val': queryset_list_kolkata_sperm_val,
        'queryset_list_kolkata_icsi_val': queryset_list_kolkata_icsi_val,
        'queryset_list_kolkata_iui_val': queryset_list_kolkata_iui_val,

        'my_total_clinic_count_lucknow': my_total_clinic_count_lucknow,
        'queryset_list_lucknow_ivf_val': queryset_list_lucknow_ivf_val,
        'queryset_list_lucknow_egg_val': queryset_list_lucknow_egg_val,
        'queryset_list_lucknow_embryo_val': queryset_list_lucknow_embryo_val,
        'queryset_list_lucknow_sperm_val': queryset_list_lucknow_sperm_val,
        'queryset_list_lucknow_icsi_val': queryset_list_lucknow_icsi_val,
        'queryset_list_lucknow_iui_val': queryset_list_lucknow_iui_val,

        'my_total_clinic_count_mumbai': my_total_clinic_count_mumbai,
        'queryset_list_mumbai_ivf_val': queryset_list_mumbai_ivf_val,
        'queryset_list_mumbai_egg_val': queryset_list_mumbai_egg_val,
        'queryset_list_mumbai_embryo_val': queryset_list_mumbai_embryo_val,
        'queryset_list_mumbai_sperm_val': queryset_list_mumbai_sperm_val,
        'queryset_list_mumbai_icsi_val': queryset_list_mumbai_icsi_val,
        'queryset_list_mumbai_iui_val': queryset_list_mumbai_iui_val,

        'my_total_clinic_count_nagpur': my_total_clinic_count_nagpur,
        'queryset_list_nagpur_ivf_val': queryset_list_nagpur_ivf_val,
        'queryset_list_nagpur_egg_val': queryset_list_nagpur_egg_val,
        'queryset_list_nagpur_embryo_val': queryset_list_nagpur_embryo_val,
        'queryset_list_nagpur_sperm_val': queryset_list_nagpur_sperm_val,
        'queryset_list_nagpur_icsi_val': queryset_list_nagpur_icsi_val,
        'queryset_list_nagpur_iui_val': queryset_list_nagpur_iui_val,

        'my_total_clinic_count_patna': my_total_clinic_count_patna,
        'queryset_list_patna_ivf_val': queryset_list_patna_ivf_val,
        'queryset_list_patna_egg_val': queryset_list_patna_egg_val,
        'queryset_list_patna_embryo_val': queryset_list_patna_embryo_val,
        'queryset_list_patna_sperm_val': queryset_list_patna_sperm_val,
        'queryset_list_patna_icsi_val': queryset_list_patna_icsi_val,
        'queryset_list_patna_iui_val': queryset_list_patna_iui_val,

        'my_total_clinic_count_raipur': my_total_clinic_count_raipur,
        'queryset_list_raipur_ivf_val': queryset_list_raipur_ivf_val,
        'queryset_list_raipur_egg_val': queryset_list_raipur_egg_val,
        'queryset_list_raipur_embryo_val': queryset_list_raipur_embryo_val,
        'queryset_list_raipur_sperm_val': queryset_list_raipur_sperm_val,
        'queryset_list_raipur_icsi_val': queryset_list_raipur_icsi_val,
        'queryset_list_raipur_iui_val': queryset_list_raipur_iui_val,

        'my_total_clinic_count_trivandrum': my_total_clinic_count_trivandrum,
        'queryset_list_trivandrum_ivf_val': queryset_list_trivandrum_ivf_val,
        'queryset_list_trivandrum_egg_val': queryset_list_trivandrum_egg_val,
        'queryset_list_trivandrum_embryo_val': queryset_list_trivandrum_embryo_val,
        'queryset_list_trivandrum_sperm_val': queryset_list_trivandrum_sperm_val,
        'queryset_list_trivandrum_icsi_val': queryset_list_trivandrum_icsi_val,
        'queryset_list_trivandrum_iui_val': queryset_list_trivandrum_iui_val,

        'my_total_clinic_count_ludhiana': my_total_clinic_count_ludhiana,
        'queryset_list_ludhiana_ivf_val': queryset_list_ludhiana_ivf_val,
        'queryset_list_ludhiana_egg_val': queryset_list_ludhiana_egg_val,
        'queryset_list_ludhiana_embryo_val': queryset_list_ludhiana_embryo_val,
        'queryset_list_ludhiana_sperm_val': queryset_list_ludhiana_sperm_val,
        'queryset_list_ludhiana_icsi_val': queryset_list_ludhiana_icsi_val,
        'queryset_list_ludhiana_iui_val': queryset_list_ludhiana_iui_val,

        'my_total_clinic_count_visakhapatnam': my_total_clinic_count_visakhapatnam,
        'queryset_list_visakhapatnam_ivf_val': queryset_list_visakhapatnam_ivf_val,
        'queryset_list_visakhapatnam_egg_val': queryset_list_visakhapatnam_egg_val,
        'queryset_list_visakhapatnam_embryo_val': queryset_list_visakhapatnam_embryo_val,
        'queryset_list_visakhapatnam_sperm_val': queryset_list_visakhapatnam_sperm_val,
        'queryset_list_visakhapatnam_icsi_val': queryset_list_visakhapatnam_icsi_val,
        'queryset_list_visakhapatnam_iui_val': queryset_list_visakhapatnam_iui_val,

        'my_total_clinic_count_vijayawada': my_total_clinic_count_vijayawada,
        'queryset_list_vijayawada_ivf_val': queryset_list_vijayawada_ivf_val,
        'queryset_list_vijayawada_egg_val': queryset_list_vijayawada_egg_val,
        'queryset_list_vijayawada_embryo_val': queryset_list_vijayawada_embryo_val,
        'queryset_list_vijayawada_sperm_val': queryset_list_vijayawada_sperm_val,
        'queryset_list_vijayawada_icsi_val': queryset_list_vijayawada_icsi_val,
        'queryset_list_vijayawada_iui_val': queryset_list_vijayawada_iui_val,

        'my_total_clinic_count_newdelhi': my_total_clinic_count_newdelhi,
        'queryset_list_newdelhi_ivf_val': queryset_list_newdelhi_ivf_val,
        'queryset_list_newdelhi_egg_val': queryset_list_newdelhi_egg_val,
        'queryset_list_newdelhi_embryo_val': queryset_list_newdelhi_embryo_val,
        'queryset_list_newdelhi_sperm_val': queryset_list_newdelhi_sperm_val,
        'queryset_list_newdelhi_icsi_val': queryset_list_newdelhi_icsi_val,
        'queryset_list_newdelhi_iui_val': queryset_list_newdelhi_iui_val,

        'my_total_clinic_count_vadodara': my_total_clinic_count_vadodara,
        'queryset_list_vadodara_ivf_val': queryset_list_vadodara_ivf_val,
        'queryset_list_vadodara_egg_val': queryset_list_vadodara_egg_val,
        'queryset_list_vadodara_embryo_val': queryset_list_vadodara_embryo_val,
        'queryset_list_vadodara_sperm_val': queryset_list_vadodara_sperm_val,
        'queryset_list_vadodara_icsi_val': queryset_list_vadodara_icsi_val,
        'queryset_list_vadodara_iui_val': queryset_list_vadodara_iui_val,

        'my_total_clinic_count_gurugram': my_total_clinic_count_gurugram,
        'queryset_list_gurugram_ivf_val': queryset_list_gurugram_ivf_val,
        'queryset_list_gurugram_egg_val': queryset_list_gurugram_egg_val,
        'queryset_list_gurugram_embryo_val': queryset_list_gurugram_embryo_val,
        'queryset_list_gurugram_sperm_val': queryset_list_gurugram_sperm_val,
        'queryset_list_gurugram_icsi_val': queryset_list_gurugram_icsi_val,
        'queryset_list_gurugram_iui_val': queryset_list_gurugram_iui_val,

        'my_total_clinic_count_rohtak': my_total_clinic_count_rohtak,
        'queryset_list_rohtak_ivf_val': queryset_list_rohtak_ivf_val,
        'queryset_list_rohtak_egg_val': queryset_list_rohtak_egg_val,
        'queryset_list_rohtak_embryo_val': queryset_list_rohtak_embryo_val,
        'queryset_list_rohtak_sperm_val': queryset_list_rohtak_sperm_val,
        'queryset_list_rohtak_icsi_val': queryset_list_rohtak_icsi_val,
        'queryset_list_rohtak_iui_val': queryset_list_rohtak_iui_val,

        'my_total_clinic_count_jammu': my_total_clinic_count_jammu,
        'queryset_list_jammu_ivf_val': queryset_list_jammu_ivf_val,
        'queryset_list_jammu_egg_val': queryset_list_jammu_egg_val,
        'queryset_list_jammu_embryo_val': queryset_list_jammu_embryo_val,
        'queryset_list_jammu_sperm_val': queryset_list_jammu_sperm_val,
        'queryset_list_jammu_icsi_val': queryset_list_jammu_icsi_val,
        'queryset_list_jammu_iui_val': queryset_list_jammu_iui_val,

        'my_total_clinic_count_ranchi': my_total_clinic_count_ranchi,
        'queryset_list_ranchi_ivf_val': queryset_list_ranchi_ivf_val,
        'queryset_list_ranchi_egg_val': queryset_list_ranchi_egg_val,
        'queryset_list_ranchi_embryo_val': queryset_list_ranchi_embryo_val,
        'queryset_list_ranchi_sperm_val': queryset_list_ranchi_sperm_val,
        'queryset_list_ranchi_icsi_val': queryset_list_ranchi_icsi_val,
        'queryset_list_ranchi_iui_val': queryset_list_ranchi_iui_val,

        'my_total_clinic_count_pune': my_total_clinic_count_pune,
        'queryset_list_pune_ivf_val': queryset_list_pune_ivf_val,
        'queryset_list_pune_egg_val': queryset_list_pune_egg_val,
        'queryset_list_pune_embryo_val': queryset_list_pune_embryo_val,
        'queryset_list_pune_sperm_val': queryset_list_pune_sperm_val,
        'queryset_list_pune_icsi_val': queryset_list_pune_icsi_val,
        'queryset_list_pune_iui_val': queryset_list_pune_iui_val,

        'my_total_clinic_count_gwalior': my_total_clinic_count_gwalior,
        'queryset_list_gwalior_ivf_val': queryset_list_gwalior_ivf_val,
        'queryset_list_gwalior_egg_val': queryset_list_gwalior_egg_val,
        'queryset_list_gwalior_embryo_val': queryset_list_gwalior_embryo_val,
        'queryset_list_gwalior_sperm_val': queryset_list_gwalior_sperm_val,
        'queryset_list_gwalior_icsi_val': queryset_list_gwalior_icsi_val,
        'queryset_list_gwalior_iui_val': queryset_list_gwalior_iui_val,

        'my_total_clinic_count_warangal': my_total_clinic_count_warangal,
        'queryset_list_warangal_ivf_val': queryset_list_warangal_ivf_val,
        'queryset_list_warangal_egg_val': queryset_list_warangal_egg_val,
        'queryset_list_warangal_embryo_val': queryset_list_warangal_embryo_val,
        'queryset_list_warangal_sperm_val': queryset_list_warangal_sperm_val,
        'queryset_list_warangal_icsi_val': queryset_list_warangal_icsi_val,
        'queryset_list_warangal_iui_val': queryset_list_warangal_iui_val,

        'my_total_clinic_count_gachibowli': my_total_clinic_count_gachibowli,
        'queryset_list_gachibowli_ivf_val': queryset_list_gachibowli_ivf_val,
        'queryset_list_gachibowli_egg_val': queryset_list_gachibowli_egg_val,
        'queryset_list_gachibowli_embryo_val': queryset_list_gachibowli_embryo_val,
        'queryset_list_gachibowli_sperm_val': queryset_list_gachibowli_sperm_val,
        'queryset_list_gachibowli_icsi_val': queryset_list_gachibowli_icsi_val,
        'queryset_list_gachibowli_iui_val': queryset_list_gachibowli_iui_val,

        'my_total_clinic_count_madhapur': my_total_clinic_count_madhapur,
        'queryset_list_madhapur_ivf_val': queryset_list_madhapur_ivf_val,
        'queryset_list_madhapur_egg_val': queryset_list_madhapur_egg_val,
        'queryset_list_madhapur_embryo_val': queryset_list_madhapur_embryo_val,
        'queryset_list_madhapur_sperm_val': queryset_list_madhapur_sperm_val,
        'queryset_list_madhapur_icsi_val': queryset_list_madhapur_icsi_val,
        'queryset_list_madhapur_iui_val': queryset_list_madhapur_iui_val,

        'my_total_clinic_count_noida': my_total_clinic_count_noida,
        'queryset_list_noida_ivf_val': queryset_list_noida_ivf_val,
        'queryset_list_noida_egg_val': queryset_list_noida_egg_val,
        'queryset_list_noida_embryo_val': queryset_list_noida_embryo_val,
        'queryset_list_noida_sperm_val': queryset_list_noida_sperm_val,
        'queryset_list_noida_icsi_val': queryset_list_noida_icsi_val,
        'queryset_list_noida_iui_val': queryset_list_noida_iui_val,

        'my_total_clinic_count_meerut': my_total_clinic_count_meerut,
        'queryset_list_meerut_ivf_val': queryset_list_meerut_ivf_val,
        'queryset_list_meerut_egg_val': queryset_list_meerut_egg_val,
        'queryset_list_meerut_embryo_val': queryset_list_meerut_embryo_val,
        'queryset_list_meerut_sperm_val': queryset_list_meerut_sperm_val,
        'queryset_list_meerut_icsi_val': queryset_list_meerut_icsi_val,
        'queryset_list_meerut_iui_val': queryset_list_meerut_iui_val,

        'my_total_clinic_count_haldwani': my_total_clinic_count_haldwani,
        'queryset_list_haldwani_ivf_val': queryset_list_haldwani_ivf_val,
        'queryset_list_haldwani_egg_val': queryset_list_haldwani_egg_val,
        'queryset_list_haldwani_embryo_val': queryset_list_haldwani_embryo_val,
        'queryset_list_haldwani_sperm_val': queryset_list_haldwani_sperm_val,
        'queryset_list_haldwani_icsi_val': queryset_list_haldwani_icsi_val,
        'queryset_list_haldwani_iui_val': queryset_list_haldwani_iui_val,
        }
    return render(request, 'main/Locations/INLocations/in-regions-ivf.html', context)

