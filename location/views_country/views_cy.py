from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_city_average_value
from base.constant_variables import year


def locationsCYRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Cyprus'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    queryset_list_cy_natural_ivf_val = procedure_country_average_value('ivf_treatment_cost', country_name)
    queryset_list_cy_mild_ivf_val = procedure_country_average_value('mild_ivf_treatment_cost', country_name)
    queryset_list_cy_standard_ivf_val = procedure_country_average_value('ovarian_ivf_treatment_cost', country_name)
    queryset_list_cy_egg_ivf_val = procedure_country_average_value('egg_donor_recipients_cost', country_name)
    queryset_list_cy_known_egg_ivf_val = procedure_country_average_value('known_egg_donor_recipients_cost', country_name)
    queryset_list_cy_shared_egg_ivf_val = procedure_country_average_value('shared_egg_donor_recipients_cost', country_name)

    queryset_list_cy_embryo_ivf_val = procedure_country_average_value('embryo_donor_recipients_cost', country_name)
    queryset_list_cy_known_embryo_ivf_val = procedure_country_average_value('known_embryo_donor_recipients_cost', country_name)
    queryset_list_cy_sperm_ivf_val = procedure_country_average_value('sperm_donor_recipients_cost', country_name)
    queryset_list_cy_known_sperm_ivf_val = procedure_country_average_value('known_sperm_donor_recipients_cost', country_name)
    queryset_list_cy_icsi_val = procedure_country_average_value('icsi_treatment_cost', country_name)
    queryset_list_cy_iui_val = procedure_country_average_value('iui_treatment_cost', country_name)

    #--------------------------------------------------------------------------
    city_name = 'Nicosia'
    my_total_clinic_count_nicosia = region_count(city_name)
    clinic_count = my_total_clinic_count_nicosia

    queryset_list_nicosia_ivf_val = procedure_city_average_value('ivf_treatment_cost', city_name)
    queryset_list_nicosia_egg_val = procedure_city_average_value('mild_ivf_treatment_cost', city_name)
    queryset_list_nicosia_embryo_val = procedure_city_average_value('ovarian_ivf_treatment_cost', city_name)
    queryset_list_nicosia_sperm_val = procedure_city_average_value('egg_donor_recipients_cost', city_name)
    queryset_list_nicosia_icsi_val = procedure_city_average_value('known_egg_donor_recipients_cost', city_name)
    queryset_list_nicosia_iui_val = procedure_city_average_value('shared_egg_donor_recipients_cost', city_name)

    #--------------------------------------------------------------------------
    city_name = 'Girne'
    my_total_clinic_count_girne = region_count(city_name)
    clinic_count = my_total_clinic_count_girne

    queryset_list_girne_ivf_val = procedure_city_average_value('ivf_treatment_cost', city_name)
    queryset_list_girne_egg_val = procedure_city_average_value('mild_ivf_treatment_cost', city_name)
    queryset_list_girne_embryo_val = procedure_city_average_value('ovarian_ivf_treatment_cost', city_name)
    queryset_list_girne_sperm_val = procedure_city_average_value('egg_donor_recipients_cost', city_name)
    queryset_list_girne_icsi_val = procedure_city_average_value('known_egg_donor_recipients_cost', city_name)
    queryset_list_girne_iui_val = procedure_city_average_value('shared_egg_donor_recipients_cost', city_name)

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_cy_natural_ivf_val': queryset_list_cy_natural_ivf_val,
        'queryset_list_cy_mild_ivf_val': queryset_list_cy_mild_ivf_val,
        'queryset_list_cy_standard_ivf_val': queryset_list_cy_standard_ivf_val,
        'queryset_list_cy_egg_ivf_val': queryset_list_cy_egg_ivf_val,
        'queryset_list_cy_known_egg_ivf_val': queryset_list_cy_known_egg_ivf_val,
        'queryset_list_cy_shared_egg_ivf_val': queryset_list_cy_shared_egg_ivf_val,
        'queryset_list_cy_embryo_ivf_val': queryset_list_cy_embryo_ivf_val,
        'queryset_list_cy_known_embryo_ivf_val': queryset_list_cy_known_embryo_ivf_val,
        'queryset_list_cy_sperm_ivf_val': queryset_list_cy_sperm_ivf_val,
        'queryset_list_cy_known_sperm_ivf_val': queryset_list_cy_known_sperm_ivf_val,
        'queryset_list_cy_icsi_val': queryset_list_cy_icsi_val,
        'queryset_list_cy_iui_val': queryset_list_cy_iui_val,

        'my_total_clinic_count_nicosia': my_total_clinic_count_nicosia,
        'queryset_list_nicosia_ivf_val': queryset_list_nicosia_ivf_val,
        'queryset_list_nicosia_egg_val': queryset_list_nicosia_egg_val,
        'queryset_list_nicosia_embryo_val': queryset_list_nicosia_embryo_val,
        'queryset_list_nicosia_sperm_val': queryset_list_nicosia_sperm_val,
        'queryset_list_nicosia_icsi_val': queryset_list_nicosia_icsi_val,
        'queryset_list_nicosia_iui_val': queryset_list_nicosia_iui_val,

        'my_total_clinic_count_girne': my_total_clinic_count_girne,
        'queryset_list_girne_ivf_val': queryset_list_girne_ivf_val,
        'queryset_list_girne_egg_val': queryset_list_girne_egg_val,
        'queryset_list_girne_embryo_val': queryset_list_girne_embryo_val,
        'queryset_list_girne_sperm_val': queryset_list_girne_sperm_val,
        'queryset_list_girne_icsi_val': queryset_list_girne_icsi_val,
        'queryset_list_girne_iui_val': queryset_list_girne_iui_val,
        }
    return render(request, 'main/Locations/CYLocations/cy-regions-ivf.html', context)

