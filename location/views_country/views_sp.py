from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year


def locationsSPRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Spain'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_sp_natural_ivf_val = procedure_country_average_value('ivf_treatment_cost', country_name, clinic_count)
    queryset_list_sp_mild_ivf_val = procedure_country_average_value('mild_ivf_treatment_cost', country_name, clinic_count)
    queryset_list_sp_standard_ivf_val = procedure_country_average_value('ovarian_ivf_treatment_cost', country_name, clinic_count)
    queryset_list_sp_egg_ivf_val = procedure_country_average_value('egg_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_known_egg_ivf_val = procedure_country_average_value('known_egg_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_shared_egg_ivf_val = procedure_country_average_value('shared_egg_donor_recipients_cost', country_name, clinic_count)

    queryset_list_sp_embryo_ivf_val = procedure_country_average_value('embryo_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_known_embryo_ivf_val = procedure_country_average_value('known_embryo_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_sperm_ivf_val = procedure_country_average_value('sperm_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_known_sperm_ivf_val = procedure_country_average_value('known_sperm_donor_recipients_cost', country_name, clinic_count)
    queryset_list_sp_icsi_val = procedure_country_average_value('icsi_treatment_cost', country_name, clinic_count)
    queryset_list_sp_iui_val = procedure_country_average_value('iui_treatment_cost', country_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Alicante'
    my_total_clinic_count_alicante = region_count(region_name)
    clinic_count = my_total_clinic_count_alicante

    queryset_list_alicante_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_alicante_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_alicante_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_alicante_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_alicante_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_alicante_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Barcelona'
    my_total_clinic_count_barcelona = region_count(region_name)
    clinic_count = my_total_clinic_count_barcelona

    queryset_list_barcelona_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_barcelona_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_barcelona_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_barcelona_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_barcelona_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_barcelona_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Madrid'
    my_total_clinic_count_madrid = region_count(region_name)
    clinic_count = my_total_clinic_count_madrid

    queryset_list_madrid_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_madrid_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_madrid_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_madrid_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_madrid_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_madrid_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Malaga'
    my_total_clinic_count_malaga = region_count(region_name)
    clinic_count = my_total_clinic_count_malaga

    queryset_list_malaga_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_malaga_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_malaga_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_malaga_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_malaga_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_malaga_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Seville'
    my_total_clinic_count_seville = region_count(region_name)
    clinic_count = my_total_clinic_count_seville

    queryset_list_seville_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_seville_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_seville_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_seville_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_seville_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_seville_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    #--------------------------------------------------------------------------
    region_name = 'Valencia'
    my_total_clinic_count_valencia = region_count(region_name)
    clinic_count = my_total_clinic_count_valencia

    queryset_list_valencia_ivf_val = procedure_region_average_value('ivf_treatment_cost', region_name, clinic_count)
    queryset_list_valencia_egg_val = procedure_region_average_value('mild_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_valencia_embryo_val = procedure_region_average_value('ovarian_ivf_treatment_cost', region_name, clinic_count)
    queryset_list_valencia_sperm_val = procedure_region_average_value('egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_valencia_icsi_val = procedure_region_average_value('known_egg_donor_recipients_cost', region_name, clinic_count)
    queryset_list_valencia_iui_val = procedure_region_average_value('shared_egg_donor_recipients_cost', region_name, clinic_count)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_sp_natural_ivf_val': queryset_list_sp_natural_ivf_val,
        'queryset_list_sp_mild_ivf_val': queryset_list_sp_mild_ivf_val,
        'queryset_list_sp_standard_ivf_val': queryset_list_sp_standard_ivf_val,
        'queryset_list_sp_egg_ivf_val': queryset_list_sp_egg_ivf_val,
        'queryset_list_sp_known_egg_ivf_val': queryset_list_sp_known_egg_ivf_val,
        'queryset_list_sp_shared_egg_ivf_val': queryset_list_sp_shared_egg_ivf_val,
        'queryset_list_sp_embryo_ivf_val': queryset_list_sp_embryo_ivf_val,
        'queryset_list_sp_known_embryo_ivf_val': queryset_list_sp_known_embryo_ivf_val,
        'queryset_list_sp_sperm_ivf_val': queryset_list_sp_sperm_ivf_val,
        'queryset_list_sp_known_sperm_ivf_val': queryset_list_sp_known_sperm_ivf_val,
        'queryset_list_sp_icsi_val': queryset_list_sp_icsi_val,
        'queryset_list_sp_iui_val': queryset_list_sp_iui_val,

        'my_total_clinic_count_alicante': my_total_clinic_count_alicante,
        'queryset_list_alicante_ivf_val': queryset_list_alicante_ivf_val,
        'queryset_list_alicante_egg_val': queryset_list_alicante_egg_val,
        'queryset_list_alicante_embryo_val': queryset_list_alicante_embryo_val,
        'queryset_list_alicante_sperm_val': queryset_list_alicante_sperm_val,
        'queryset_list_alicante_icsi_val': queryset_list_alicante_icsi_val,
        'queryset_list_alicante_iui_val': queryset_list_alicante_iui_val,

        'my_total_clinic_count_barcelona': my_total_clinic_count_barcelona,
        'queryset_list_barcelona_ivf_val': queryset_list_barcelona_ivf_val,
        'queryset_list_barcelona_egg_val': queryset_list_barcelona_egg_val,
        'queryset_list_barcelona_embryo_val': queryset_list_barcelona_embryo_val,
        'queryset_list_barcelona_sperm_val': queryset_list_barcelona_sperm_val,
        'queryset_list_barcelona_icsi_val': queryset_list_barcelona_icsi_val,
        'queryset_list_barcelona_iui_val': queryset_list_barcelona_iui_val,

        'my_total_clinic_count_madrid': my_total_clinic_count_madrid,
        'queryset_list_madrid_ivf_val': queryset_list_madrid_ivf_val,
        'queryset_list_madrid_egg_val': queryset_list_madrid_egg_val,
        'queryset_list_madrid_embryo_val': queryset_list_madrid_embryo_val,
        'queryset_list_madrid_sperm_val': queryset_list_madrid_sperm_val,
        'queryset_list_madrid_icsi_val': queryset_list_madrid_icsi_val,
        'queryset_list_madrid_iui_val': queryset_list_madrid_iui_val,

        'my_total_clinic_count_malaga': my_total_clinic_count_malaga,
        'queryset_list_malaga_ivf_val': queryset_list_malaga_ivf_val,
        'queryset_list_malaga_egg_val': queryset_list_malaga_egg_val,
        'queryset_list_malaga_embryo_val': queryset_list_malaga_embryo_val,
        'queryset_list_malaga_sperm_val': queryset_list_malaga_sperm_val,
        'queryset_list_malaga_icsi_val': queryset_list_malaga_icsi_val,
        'queryset_list_malaga_iui_val': queryset_list_malaga_iui_val,

        'my_total_clinic_count_seville': my_total_clinic_count_seville,
        'queryset_list_seville_ivf_val': queryset_list_seville_ivf_val,
        'queryset_list_seville_egg_val': queryset_list_seville_egg_val,
        'queryset_list_seville_embryo_val': queryset_list_seville_embryo_val,
        'queryset_list_seville_sperm_val': queryset_list_seville_sperm_val,
        'queryset_list_seville_icsi_val': queryset_list_seville_icsi_val,
        'queryset_list_seville_iui_val': queryset_list_seville_iui_val,

        'my_total_clinic_count_valencia': my_total_clinic_count_valencia,
        'queryset_list_valencia_ivf_val': queryset_list_valencia_ivf_val,
        'queryset_list_valencia_egg_val': queryset_list_valencia_egg_val,
        'queryset_list_valencia_embryo_val': queryset_list_valencia_embryo_val,
        'queryset_list_valencia_sperm_val': queryset_list_valencia_sperm_val,
        'queryset_list_valencia_icsi_val': queryset_list_valencia_icsi_val,
        'queryset_list_valencia_iui_val': queryset_list_valencia_iui_val,
        }
    return render(request, 'main/Locations/SPLocations/sp-regions-ivf.html', context)

