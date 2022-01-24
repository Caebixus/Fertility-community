from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_city_average_value
from base.constant_variables import year


def locationsGRRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Greece'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_gr_natural_ivf_val = procedure_country_average_value('ivf_treatment_cost', country_name)
    queryset_list_gr_mild_ivf_val = procedure_country_average_value('mild_ivf_treatment_cost', country_name)
    queryset_list_gr_standard_ivf_val = procedure_country_average_value('ovarian_ivf_treatment_cost', country_name)
    queryset_list_gr_egg_ivf_val = procedure_country_average_value('egg_donor_recipients_cost', country_name)
    queryset_list_gr_known_egg_ivf_val = procedure_country_average_value('known_egg_donor_recipients_cost', country_name)
    queryset_list_gr_shared_egg_ivf_val = procedure_country_average_value('shared_egg_donor_recipients_cost', country_name)

    queryset_list_gr_embryo_ivf_val = procedure_country_average_value('embryo_donor_recipients_cost', country_name)
    queryset_list_gr_known_embryo_ivf_val = procedure_country_average_value('known_embryo_donor_recipients_cost', country_name)
    queryset_list_gr_sperm_ivf_val = procedure_country_average_value('sperm_donor_recipients_cost', country_name)
    queryset_list_gr_known_sperm_ivf_val = procedure_country_average_value('known_sperm_donor_recipients_cost', country_name)
    queryset_list_gr_icsi_val = procedure_country_average_value('icsi_treatment_cost', country_name)
    queryset_list_gr_iui_val = procedure_country_average_value('iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    city_name = 'Athens'
    my_total_clinic_count_athens = region_count(city_name)
    clinic_count = my_total_clinic_count_athens

    queryset_list_athens_ivf_val = procedure_city_average_value('ivf_treatment_cost', city_name)
    queryset_list_athens_egg_val = procedure_city_average_value('mild_ivf_treatment_cost', city_name)
    queryset_list_athens_embryo_val = procedure_city_average_value('ovarian_ivf_treatment_cost', city_name)
    queryset_list_athens_sperm_val = procedure_city_average_value('egg_donor_recipients_cost', city_name)
    queryset_list_athens_icsi_val = procedure_city_average_value('known_egg_donor_recipients_cost', city_name)
    queryset_list_athens_iui_val = procedure_city_average_value('shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Thessaloniki'
    my_total_clinic_count_thessaloniki = region_count(city_name)
    clinic_count = my_total_clinic_count_thessaloniki

    queryset_list_thessaloniki_ivf_val = procedure_city_average_value('ivf_treatment_cost', city_name)
    queryset_list_thessaloniki_egg_val = procedure_city_average_value('mild_ivf_treatment_cost', city_name)
    queryset_list_thessaloniki_embryo_val = procedure_city_average_value('ovarian_ivf_treatment_cost', city_name)
    queryset_list_thessaloniki_sperm_val = procedure_city_average_value('egg_donor_recipients_cost', city_name)
    queryset_list_thessaloniki_icsi_val = procedure_city_average_value('known_egg_donor_recipients_cost', city_name)
    queryset_list_thessaloniki_iui_val = procedure_city_average_value('shared_egg_donor_recipients_cost', city_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_gr_natural_ivf_val': queryset_list_gr_natural_ivf_val,
        'queryset_list_gr_mild_ivf_val': queryset_list_gr_mild_ivf_val,
        'queryset_list_gr_standard_ivf_val': queryset_list_gr_standard_ivf_val,
        'queryset_list_gr_egg_ivf_val': queryset_list_gr_egg_ivf_val,
        'queryset_list_gr_known_egg_ivf_val': queryset_list_gr_known_egg_ivf_val,
        'queryset_list_gr_shared_egg_ivf_val': queryset_list_gr_shared_egg_ivf_val,
        'queryset_list_gr_embryo_ivf_val': queryset_list_gr_embryo_ivf_val,
        'queryset_list_gr_known_embryo_ivf_val': queryset_list_gr_known_embryo_ivf_val,
        'queryset_list_gr_sperm_ivf_val': queryset_list_gr_sperm_ivf_val,
        'queryset_list_gr_known_sperm_ivf_val': queryset_list_gr_known_sperm_ivf_val,
        'queryset_list_gr_icsi_val': queryset_list_gr_icsi_val,
        'queryset_list_gr_iui_val': queryset_list_gr_iui_val,

        'my_total_clinic_count_athens': my_total_clinic_count_athens,
        'queryset_list_athens_ivf_val': queryset_list_athens_ivf_val,
        'queryset_list_athens_egg_val': queryset_list_athens_egg_val,
        'queryset_list_athens_embryo_val': queryset_list_athens_embryo_val,
        'queryset_list_athens_sperm_val': queryset_list_athens_sperm_val,
        'queryset_list_athens_icsi_val': queryset_list_athens_icsi_val,
        'queryset_list_athens_iui_val': queryset_list_athens_iui_val,

        'my_total_clinic_count_thessaloniki': my_total_clinic_count_thessaloniki,
        'queryset_list_thessaloniki_ivf_val': queryset_list_thessaloniki_ivf_val,
        'queryset_list_thessaloniki_egg_val': queryset_list_thessaloniki_egg_val,
        'queryset_list_thessaloniki_embryo_val': queryset_list_thessaloniki_embryo_val,
        'queryset_list_thessaloniki_sperm_val': queryset_list_thessaloniki_sperm_val,
        'queryset_list_thessaloniki_icsi_val': queryset_list_thessaloniki_icsi_val,
        'queryset_list_thessaloniki_iui_val': queryset_list_thessaloniki_iui_val,
        }
    return render(request, 'main/Locations/GRLocations/gr-regions-ivf.html', context)

