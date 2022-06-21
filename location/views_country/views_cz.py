from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsCZRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 1
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Czech Republic'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    country_average_costs_model = AverageTreatmentCostCzech.objects.get(pk=1)

    queryset_list_cz_natural_ivf_val = country_average_costs_model.natural_ivf_val
    queryset_list_cz_mild_ivf_val = country_average_costs_model.mild_ivf_val
    queryset_list_cz_standard_ivf_val = country_average_costs_model.standard_ivf_val
    queryset_list_cz_egg_ivf_val = country_average_costs_model.egg_ivf_val
    queryset_list_cz_known_egg_ivf_val = country_average_costs_model.known_egg_ivf_val
    queryset_list_cz_shared_egg_ivf_val = country_average_costs_model.shared_egg_ivf_val
    queryset_list_cz_embryo_ivf_val = country_average_costs_model.embryo_ivf_val
    queryset_list_cz_known_embryo_ivf_val = country_average_costs_model.known_embryo_ivf_val
    queryset_list_cz_sperm_ivf_val = country_average_costs_model.sperm_ivf_val
    queryset_list_cz_known_sperm_ivf_val = country_average_costs_model.known_sperm_ivf_val
    queryset_list_cz_icsi_val = country_average_costs_model.icsi_val
    queryset_list_cz_iui_val = country_average_costs_model.iui_val

    queryset_list_set = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact=country_name)

    queryset_list_prague = queryset_list_set.filter(clinicRegion__iexact='Prague')
    my_total_clinic_count_prague = queryset_list_prague.count()
    prague_average_costs_model = Prague.objects.get(pk=1)
    queryset_list_prague_ivf_val = prague_average_costs_model.standard_ivf_val
    queryset_list_prague_egg_val = prague_average_costs_model.egg_ivf_val
    queryset_list_prague_embryo_val = prague_average_costs_model.embryo_ivf_val
    queryset_list_prague_sperm_val = prague_average_costs_model.sperm_ivf_val
    queryset_list_prague_icsi_val = prague_average_costs_model.icsi_val
    queryset_list_prague_iui_val = prague_average_costs_model.iui_val

    queryset_list_brno = queryset_list_set.filter(clinicRegion__iexact='Brno')
    my_total_clinic_count_brno = queryset_list_brno.count()
    brno_average_costs_model = Brno.objects.get(pk=1)
    queryset_list_brno_ivf_val = brno_average_costs_model.standard_ivf_val
    queryset_list_brno_egg_val = brno_average_costs_model.egg_ivf_val
    queryset_list_brno_embryo_val = brno_average_costs_model.embryo_ivf_val
    queryset_list_brno_sperm_val = brno_average_costs_model.sperm_ivf_val
    queryset_list_brno_icsi_val = brno_average_costs_model.icsi_val
    queryset_list_brno_iui_val = brno_average_costs_model.iui_val

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_cz_natural_ivf_val': queryset_list_cz_natural_ivf_val,
        'queryset_list_cz_mild_ivf_val': queryset_list_cz_mild_ivf_val,
        'queryset_list_cz_standard_ivf_val': queryset_list_cz_standard_ivf_val,
        'queryset_list_cz_egg_ivf_val': queryset_list_cz_egg_ivf_val,
        'queryset_list_cz_known_egg_ivf_val': queryset_list_cz_known_egg_ivf_val,
        'queryset_list_cz_shared_egg_ivf_val': queryset_list_cz_shared_egg_ivf_val,
        'queryset_list_cz_embryo_ivf_val': queryset_list_cz_embryo_ivf_val,
        'queryset_list_cz_known_embryo_ivf_val': queryset_list_cz_known_embryo_ivf_val,
        'queryset_list_cz_sperm_ivf_val': queryset_list_cz_sperm_ivf_val,
        'queryset_list_cz_known_sperm_ivf_val': queryset_list_cz_known_sperm_ivf_val,
        'queryset_list_cz_icsi_val': queryset_list_cz_icsi_val,
        'queryset_list_cz_iui_val': queryset_list_cz_iui_val,

        'my_total_clinic_count_prague': my_total_clinic_count_prague,
        'queryset_list_prague_ivf_val': queryset_list_prague_ivf_val,
        'queryset_list_prague_egg_val': queryset_list_prague_egg_val,
        'queryset_list_prague_embryo_val': queryset_list_prague_embryo_val,
        'queryset_list_prague_sperm_val': queryset_list_prague_sperm_val,
        'queryset_list_prague_icsi_val': queryset_list_prague_icsi_val,
        'queryset_list_prague_iui_val': queryset_list_prague_iui_val,

        'my_total_clinic_count_brno': my_total_clinic_count_brno,
        'queryset_list_brno_ivf_val': queryset_list_brno_ivf_val,
        'queryset_list_brno_egg_val': queryset_list_brno_egg_val,
        'queryset_list_brno_embryo_val': queryset_list_brno_embryo_val,
        'queryset_list_brno_sperm_val': queryset_list_brno_sperm_val,
        'queryset_list_brno_icsi_val': queryset_list_brno_icsi_val,
        'queryset_list_brno_iui_val': queryset_list_brno_iui_val,
        }
    return render(request, 'main/Locations/CZLocations/cz-regions-ivf.html', context)

