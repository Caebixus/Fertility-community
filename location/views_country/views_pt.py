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

    queryset_list_pt_natural_ivf_val = procedure_country_average_value('ivf_treatment_cost', country_name, clinic_count)
    queryset_list_pt_mild_ivf_val = procedure_country_average_value('mild_ivf_treatment_cost', country_name, clinic_count)
    queryset_list_pt_standard_ivf_val = procedure_country_average_value('ovarian_ivf_treatment_cost', country_name, clinic_count)
    queryset_list_pt_egg_ivf_val = procedure_country_average_value('egg_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_known_egg_ivf_val = procedure_country_average_value('known_egg_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_shared_egg_ivf_val = procedure_country_average_value('shared_egg_donor_recipients_cost', country_name, clinic_count)

    queryset_list_pt_embryo_ivf_val = procedure_country_average_value('embryo_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_known_embryo_ivf_val = procedure_country_average_value('known_embryo_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_sperm_ivf_val = procedure_country_average_value('sperm_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_known_sperm_ivf_val = procedure_country_average_value('known_sperm_donor_recipients_cost', country_name, clinic_count)
    queryset_list_pt_icsi_val = procedure_country_average_value('icsi_treatment_cost', country_name, clinic_count)
    queryset_list_pt_iui_val = procedure_country_average_value('iui_treatment_cost', country_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Lisbon'
    my_total_clinic_count_lisbon = region_count(region_name)
    clinic_count = my_total_clinic_count_lisbon

    queryset_list_lisbon__ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_lisbon__egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_lisbon__embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_lisbon__sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_lisbon__icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_lisbon__iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

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
        'queryset_list_lisbon__ivf_val': queryset_list_lisbon__ivf_val,
        'queryset_list_lisbon__egg_val': queryset_list_lisbon__egg_val,
        'queryset_list_lisbon__embryo_val': queryset_list_lisbon__embryo_val,
        'queryset_list_lisbon__sperm_val': queryset_list_lisbon__sperm_val,
        'queryset_list_lisbon__icsi_val': queryset_list_lisbon__icsi_val,
        'queryset_list_lisbon__iui_val': queryset_list_lisbon__iui_val,
        }
    return render(request, 'main/Locations/PTLocations/pt-regions-ivf.html', context)

