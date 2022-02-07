from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsPTRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Portugal'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_pt_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_pt_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_pt_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_pt_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_pt_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_pt_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_pt_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_pt_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_pt_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_pt_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_pt_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_pt_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    region_name = 'Lisbon'
    my_total_clinic_count_lisbon = region_count(region_name)
    clinic_count = my_total_clinic_count_lisbon

    queryset_list_lisbon_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_lisbon_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_lisbon_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_lisbon_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_lisbon_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_lisbon_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_pt_natural_ivf_val': queryset_list_pt_natural_ivf_val,
        'queryset_list_pt_mild_ivf_val': queryset_list_pt_mild_ivf_val,
        'queryset_list_pt_standard_ivf_val': queryset_list_pt_standard_ivf_val,
        'queryset_list_pt_egg_ivf_val': queryset_list_pt_egg_ivf_val,
        'queryset_list_pt_known_egg_ivf_val': queryset_list_pt_known_egg_ivf_val,
        'queryset_list_pt_shared_egg_ivf_val': queryset_list_pt_shared_egg_ivf_val,
        'queryset_list_pt_embryo_ivf_val': queryset_list_pt_embryo_ivf_val,
        'queryset_list_pt_known_embryo_ivf_val': queryset_list_pt_known_embryo_ivf_val,
        'queryset_list_pt_sperm_ivf_val': queryset_list_pt_sperm_ivf_val,
        'queryset_list_pt_known_sperm_ivf_val': queryset_list_pt_known_sperm_ivf_val,
        'queryset_list_pt_icsi_val': queryset_list_pt_icsi_val,
        'queryset_list_pt_iui_val': queryset_list_pt_iui_val,

        'my_total_clinic_count_lisbon': my_total_clinic_count_lisbon,
        'queryset_list_lisbon_ivf_val': queryset_list_lisbon_ivf_val,
        'queryset_list_lisbon_egg_val': queryset_list_lisbon_egg_val,
        'queryset_list_lisbon_embryo_val': queryset_list_lisbon_embryo_val,
        'queryset_list_lisbon_sperm_val': queryset_list_lisbon_sperm_val,
        'queryset_list_lisbon_icsi_val': queryset_list_lisbon_icsi_val,
        'queryset_list_lisbon_iui_val': queryset_list_lisbon_iui_val,
        }
    return render(request, 'main/Locations/PTLocations/pt-regions-ivf.html', context)

