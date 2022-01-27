from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_city_average_value
from base.constant_variables import year


def locationsMXRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Mexico'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_mx_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_mx_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_mx_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_mx_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_mx_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_mx_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_mx_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_mx_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_mx_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_mx_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_mx_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_mx_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    city_name = 'Mexico City'
    my_total_clinic_count_mexicocity = region_count(city_name)
    clinic_count = my_total_clinic_count_mexicocity

    queryset_list_mexicocity_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name)
    queryset_list_mexicocity_egg_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name)
    queryset_list_mexicocity_embryo_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name)
    queryset_list_mexicocity_sperm_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name)
    queryset_list_mexicocity_icsi_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name)
    queryset_list_mexicocity_iui_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_mx_natural_ivf_val': queryset_list_mx_natural_ivf_val,
        'queryset_list_mx_mild_ivf_val': queryset_list_mx_mild_ivf_val,
        'queryset_list_mx_standard_ivf_val': queryset_list_mx_standard_ivf_val,
        'queryset_list_mx_egg_ivf_val': queryset_list_mx_egg_ivf_val,
        'queryset_list_mx_known_egg_ivf_val': queryset_list_mx_known_egg_ivf_val,
        'queryset_list_mx_shared_egg_ivf_val': queryset_list_mx_shared_egg_ivf_val,
        'queryset_list_mx_embryo_ivf_val': queryset_list_mx_embryo_ivf_val,
        'queryset_list_mx_known_embryo_ivf_val': queryset_list_mx_known_embryo_ivf_val,
        'queryset_list_mx_sperm_ivf_val': queryset_list_mx_sperm_ivf_val,
        'queryset_list_mx_known_sperm_ivf_val': queryset_list_mx_known_sperm_ivf_val,
        'queryset_list_mx_icsi_val': queryset_list_mx_icsi_val,
        'queryset_list_mx_iui_val': queryset_list_mx_iui_val,

        'my_total_clinic_count_mexicocity': my_total_clinic_count_mexicocity,
        'queryset_list_mexicocity_ivf_val': queryset_list_mexicocity_ivf_val,
        'queryset_list_mexicocity_egg_val': queryset_list_mexicocity_egg_val,
        'queryset_list_mexicocity_embryo_val': queryset_list_mexicocity_embryo_val,
        'queryset_list_mexicocity_sperm_val': queryset_list_mexicocity_sperm_val,
        'queryset_list_mexicocity_icsi_val': queryset_list_mexicocity_icsi_val,
        'queryset_list_mexicocity_iui_val': queryset_list_mexicocity_iui_val,

        }
    return render(request, 'main/Locations/MXLocations/mx-regions-ivf.html', context)

