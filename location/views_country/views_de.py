from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsDERegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Germany'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_de_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_de_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_de_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_de_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_de_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_de_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_de_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_de_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_de_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_de_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_de_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_de_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    region_name = 'Berlin'
    my_total_clinic_count_berlin = region_count(region_name)
    clinic_count = my_total_clinic_count_berlin

    queryset_list_berlin_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_berlin_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_berlin_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_berlin_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_berlin_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_berlin_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_de_natural_ivf_val': queryset_list_de_natural_ivf_val,
        'queryset_list_de_mild_ivf_val': queryset_list_de_mild_ivf_val,
        'queryset_list_de_standard_ivf_val': queryset_list_de_standard_ivf_val,
        'queryset_list_de_egg_ivf_val': queryset_list_de_egg_ivf_val,
        'queryset_list_de_known_egg_ivf_val': queryset_list_de_known_egg_ivf_val,
        'queryset_list_de_shared_egg_ivf_val': queryset_list_de_shared_egg_ivf_val,
        'queryset_list_de_embryo_ivf_val': queryset_list_de_embryo_ivf_val,
        'queryset_list_de_known_embryo_ivf_val': queryset_list_de_known_embryo_ivf_val,
        'queryset_list_de_sperm_ivf_val': queryset_list_de_sperm_ivf_val,
        'queryset_list_de_known_sperm_ivf_val': queryset_list_de_known_sperm_ivf_val,
        'queryset_list_de_icsi_val': queryset_list_de_icsi_val,
        'queryset_list_de_iui_val': queryset_list_de_iui_val,

        'my_total_clinic_count_berlin': my_total_clinic_count_berlin,
        'queryset_list_berlin_ivf_val': queryset_list_berlin_ivf_val,
        'queryset_list_berlin_egg_val': queryset_list_berlin_egg_val,
        'queryset_list_berlin_embryo_val': queryset_list_berlin_embryo_val,
        'queryset_list_berlin_sperm_val': queryset_list_berlin_sperm_val,
        'queryset_list_berlin_icsi_val': queryset_list_berlin_icsi_val,
        'queryset_list_berlin_iui_val': queryset_list_berlin_iui_val,
        }
    return render(request, 'main/Locations/DELocations/de-regions-ivf.html', context)

