from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsCYRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Cyprus'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    country_average_costs_model = AverageTreatmentCostCyprus.objects.get(pk=1)

    queryset_list_cy_natural_ivf_val = country_average_costs_model.natural_ivf_val
    queryset_list_cy_mild_ivf_val = country_average_costs_model.mild_ivf_val
    queryset_list_cy_standard_ivf_val = country_average_costs_model.standard_ivf_val
    queryset_list_cy_egg_ivf_val = country_average_costs_model.egg_ivf_val
    queryset_list_cy_known_egg_ivf_val = country_average_costs_model.known_egg_ivf_val
    queryset_list_cy_shared_egg_ivf_val = country_average_costs_model.shared_egg_ivf_val
    queryset_list_cy_embryo_ivf_val = country_average_costs_model.embryo_ivf_val
    queryset_list_cy_known_embryo_ivf_val = country_average_costs_model.known_embryo_ivf_val
    queryset_list_cy_sperm_ivf_val = country_average_costs_model.sperm_ivf_val
    queryset_list_cy_known_sperm_ivf_val = country_average_costs_model.known_sperm_ivf_val
    queryset_list_cy_icsi_val = country_average_costs_model.icsi_val
    queryset_list_cy_iui_val = country_average_costs_model.iui_val

    queryset_list_set = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact=country_name)

    queryset_list_nicosia = queryset_list_set.filter(clinicCity__iexact='Nicosia')
    my_total_clinic_count_nicosia = queryset_list_nicosia.count()
    nicosia_average_costs_model = Nicosia.objects.get(pk=1)
    queryset_list_nicosia_ivf_val = nicosia_average_costs_model.standard_ivf_val
    queryset_list_nicosia_egg_val = nicosia_average_costs_model.egg_ivf_val
    queryset_list_nicosia_embryo_val = nicosia_average_costs_model.embryo_ivf_val
    queryset_list_nicosia_sperm_val = nicosia_average_costs_model.sperm_ivf_val
    queryset_list_nicosia_icsi_val = nicosia_average_costs_model.icsi_val
    queryset_list_nicosia_iui_val = nicosia_average_costs_model.iui_val

    queryset_list_girne = queryset_list_set.filter(clinicCity__iexact='Girne')
    my_total_clinic_count_girne = queryset_list_girne.count()
    girne_average_costs_model = Girne.objects.get(pk=1)
    queryset_list_girne_ivf_val = girne_average_costs_model.standard_ivf_val
    queryset_list_girne_egg_val = girne_average_costs_model.egg_ivf_val
    queryset_list_girne_embryo_val = girne_average_costs_model.embryo_ivf_val
    queryset_list_girne_sperm_val = girne_average_costs_model.sperm_ivf_val
    queryset_list_girne_icsi_val = girne_average_costs_model.icsi_val
    queryset_list_girne_iui_val = girne_average_costs_model.iui_val

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

