from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsSKRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 4
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Slovakia'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    country_average_costs_model = AverageTreatmentCostSlovakia.objects.get(pk=1)

    queryset_list_sk_natural_ivf_val = country_average_costs_model.natural_ivf_val
    queryset_list_sk_mild_ivf_val = country_average_costs_model.mild_ivf_val
    queryset_list_sk_standard_ivf_val = country_average_costs_model.standard_ivf_val
    queryset_list_sk_egg_ivf_val = country_average_costs_model.egg_ivf_val
    queryset_list_sk_known_egg_ivf_val = country_average_costs_model.known_egg_ivf_val
    queryset_list_sk_shared_egg_ivf_val = country_average_costs_model.shared_egg_ivf_val
    queryset_list_sk_embryo_ivf_val = country_average_costs_model.embryo_ivf_val
    queryset_list_sk_known_embryo_ivf_val = country_average_costs_model.known_embryo_ivf_val
    queryset_list_sk_sperm_ivf_val = country_average_costs_model.sperm_ivf_val
    queryset_list_sk_known_sperm_ivf_val = country_average_costs_model.known_sperm_ivf_val
    queryset_list_sk_icsi_val = country_average_costs_model.icsi_val
    queryset_list_sk_iui_val = country_average_costs_model.iui_val

    queryset_list_set = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact='Slovakia')

    queryset_list_bratislava = queryset_list_set.filter(clinicRegion__iexact='Bratislava')
    my_total_clinic_count_bratislava = queryset_list_bratislava.count()
    bratislava_average_costs_model = Bratislava.objects.get(pk=1)
    queryset_list_bratislava_ivf_val = bratislava_average_costs_model.standard_ivf_val
    queryset_list_bratislava_egg_val = bratislava_average_costs_model.egg_ivf_val
    queryset_list_bratislava_embryo_val = bratislava_average_costs_model.embryo_ivf_val
    queryset_list_bratislava_sperm_val = bratislava_average_costs_model.sperm_ivf_val
    queryset_list_bratislava_icsi_val = bratislava_average_costs_model.icsi_val
    queryset_list_bratislava_iui_val = bratislava_average_costs_model.iui_val

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_sk_natural_ivf_val': queryset_list_sk_natural_ivf_val,
        'queryset_list_sk_mild_ivf_val': queryset_list_sk_mild_ivf_val,
        'queryset_list_sk_standard_ivf_val': queryset_list_sk_standard_ivf_val,
        'queryset_list_sk_egg_ivf_val': queryset_list_sk_egg_ivf_val,
        'queryset_list_sk_known_egg_ivf_val': queryset_list_sk_known_egg_ivf_val,
        'queryset_list_sk_shared_egg_ivf_val': queryset_list_sk_shared_egg_ivf_val,
        'queryset_list_sk_embryo_ivf_val': queryset_list_sk_embryo_ivf_val,
        'queryset_list_sk_known_embryo_ivf_val': queryset_list_sk_known_embryo_ivf_val,
        'queryset_list_sk_sperm_ivf_val': queryset_list_sk_sperm_ivf_val,
        'queryset_list_sk_known_sperm_ivf_val': queryset_list_sk_known_sperm_ivf_val,
        'queryset_list_sk_icsi_val': queryset_list_sk_icsi_val,
        'queryset_list_sk_iui_val': queryset_list_sk_iui_val,

        'my_total_clinic_count_bratislava': my_total_clinic_count_bratislava,
        'queryset_list_bratislava_ivf_val': queryset_list_bratislava_ivf_val,
        'queryset_list_bratislava_egg_val': queryset_list_bratislava_egg_val,
        'queryset_list_bratislava_embryo_val': queryset_list_bratislava_embryo_val,
        'queryset_list_bratislava_sperm_val': queryset_list_bratislava_sperm_val,
        'queryset_list_bratislava_icsi_val': queryset_list_bratislava_icsi_val,
        'queryset_list_bratislava_iui_val': queryset_list_bratislava_iui_val,
        }
    return render(request, 'main/Locations/SKLocations/sk-regions-ivf.html', context)

