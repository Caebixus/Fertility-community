from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsLVRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 7
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Latvia'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_lv_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name)
    queryset_list_lv_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name)
    queryset_list_lv_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name)
    queryset_list_lv_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name)
    queryset_list_lv_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name)
    queryset_list_lv_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name)

    queryset_list_lv_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name)
    queryset_list_lv_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name)
    queryset_list_lv_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name)
    queryset_list_lv_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name)
    queryset_list_lv_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name)
    queryset_list_lv_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    region_name = 'Riga'
    my_total_clinic_count_riga = region_count(region_name)
    clinic_count = my_total_clinic_count_riga

    queryset_list_riga_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name)
    queryset_list_riga_egg_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name)
    queryset_list_riga_embryo_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name)
    queryset_list_riga_sperm_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name)
    queryset_list_riga_icsi_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name)
    queryset_list_riga_iui_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_lv_natural_ivf_val': queryset_list_lv_natural_ivf_val,
        'queryset_list_lv_mild_ivf_val': queryset_list_lv_mild_ivf_val,
        'queryset_list_lv_standard_ivf_val': queryset_list_lv_standard_ivf_val,
        'queryset_list_lv_egg_ivf_val': queryset_list_lv_egg_ivf_val,
        'queryset_list_lv_known_egg_ivf_val': queryset_list_lv_known_egg_ivf_val,
        'queryset_list_lv_shared_egg_ivf_val': queryset_list_lv_shared_egg_ivf_val,
        'queryset_list_lv_embryo_ivf_val': queryset_list_lv_embryo_ivf_val,
        'queryset_list_lv_known_embryo_ivf_val': queryset_list_lv_known_embryo_ivf_val,
        'queryset_list_lv_sperm_ivf_val': queryset_list_lv_sperm_ivf_val,
        'queryset_list_lv_known_sperm_ivf_val': queryset_list_lv_known_sperm_ivf_val,
        'queryset_list_lv_icsi_val': queryset_list_lv_icsi_val,
        'queryset_list_lv_iui_val': queryset_list_lv_iui_val,

        'my_total_clinic_count_riga': my_total_clinic_count_riga,
        'queryset_list_riga_ivf_val': queryset_list_riga_ivf_val,
        'queryset_list_riga_egg_val': queryset_list_riga_egg_val,
        'queryset_list_riga_embryo_val': queryset_list_riga_embryo_val,
        'queryset_list_riga_sperm_val': queryset_list_riga_sperm_val,
        'queryset_list_riga_icsi_val': queryset_list_riga_icsi_val,
        'queryset_list_riga_iui_val': queryset_list_riga_iui_val,
        }
    return render(request, 'main/Locations/LVLocations/lv-regions-ivf.html', context)

