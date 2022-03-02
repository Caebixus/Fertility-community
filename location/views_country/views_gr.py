from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsGRRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Greece'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    country_average_costs_model = AverageTreatmentCostGreece.objects.get(pk=1)

    queryset_list_gr_natural_ivf_val = country_average_costs_model.natural_ivf_val
    queryset_list_gr_mild_ivf_val = country_average_costs_model.mild_ivf_val
    queryset_list_gr_standard_ivf_val = country_average_costs_model.standard_ivf_val
    queryset_list_gr_egg_ivf_val = country_average_costs_model.egg_ivf_val
    queryset_list_gr_known_egg_ivf_val = country_average_costs_model.known_egg_ivf_val
    queryset_list_gr_shared_egg_ivf_val = country_average_costs_model.shared_egg_ivf_val
    queryset_list_gr_embryo_ivf_val = country_average_costs_model.embryo_ivf_val
    queryset_list_gr_known_embryo_ivf_val = country_average_costs_model.known_embryo_ivf_val
    queryset_list_gr_sperm_ivf_val = country_average_costs_model.sperm_ivf_val
    queryset_list_gr_known_sperm_ivf_val = country_average_costs_model.known_sperm_ivf_val
    queryset_list_gr_icsi_val = country_average_costs_model.icsi_val
    queryset_list_gr_iui_val = country_average_costs_model.iui_val

    queryset_list_set = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact=country_name)

    queryset_list_athens = queryset_list_set.filter(clinicCity__iexact='Athens')
    my_total_clinic_count_athens = queryset_list_athens.count()
    athens_average_costs_model = Athens.objects.get(pk=1)
    queryset_list_athens_ivf_val = athens_average_costs_model.standard_ivf_val
    queryset_list_athens_egg_val = athens_average_costs_model.egg_ivf_val
    queryset_list_athens_embryo_val = athens_average_costs_model.embryo_ivf_val
    queryset_list_athens_sperm_val = athens_average_costs_model.sperm_ivf_val
    queryset_list_athens_icsi_val = athens_average_costs_model.icsi_val
    queryset_list_athens_iui_val = athens_average_costs_model.iui_val

    queryset_list_thessaloniki = queryset_list_set.filter(clinicCity__iexact='Thessaloniki')
    my_total_clinic_count_thessaloniki = queryset_list_thessaloniki.count()
    thessaloniki_average_costs_model = Thessaloniki.objects.get(pk=1)
    queryset_list_thessaloniki_ivf_val = thessaloniki_average_costs_model.standard_ivf_val
    queryset_list_thessaloniki_egg_val = thessaloniki_average_costs_model.egg_ivf_val
    queryset_list_thessaloniki_embryo_val = thessaloniki_average_costs_model.embryo_ivf_val
    queryset_list_thessaloniki_sperm_val = thessaloniki_average_costs_model.sperm_ivf_val
    queryset_list_thessaloniki_icsi_val = thessaloniki_average_costs_model.icsi_val
    queryset_list_thessaloniki_iui_val = thessaloniki_average_costs_model.iui_val

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_gr_natural_ivf_val': queryset_list_gr_natural_ivf_val,
        'queryset_list_gr_mild_ivf_val': queryset_list_gr_mild_ivf_val,
        'queryset_list_gr_standard_ivf_val': queryset_list_gr_standard_ivf_val,
        'queryset_list_gr_egg_ivf_val': queryset_list_gr_egg_ivf_val,
        'queryset_list_gr_known_egg_ivf_val': queryset_list_gr_known_egg_ivf_val,
        'queryset_list_gr_shared_egg_ivf_val': queryset_list_gr_shared_egg_ivf_val,
        'queryset_list_gr_embryo_ivf_val': queryset_list_gr_embryo_ivf_val,
        'queryset_list_gr_known_embryo_ivf_val': queryset_list_gr_known_embryo_ivf_val,
        'queryset_list_gr_sperm_ivf_val': queryset_list_gr_sperm_ivf_val,
        'queryset_list_gr_known_sperm_ivf_val': queryset_list_gr_known_sperm_ivf_val,
        'queryset_list_gr_icsi_val': queryset_list_gr_icsi_val,
        'queryset_list_gr_iui_val': queryset_list_gr_iui_val,

        'my_total_clinic_count_athens': my_total_clinic_count_athens,
        'queryset_list_athens_ivf_val': queryset_list_athens_ivf_val,
        'queryset_list_athens_egg_val': queryset_list_athens_egg_val,
        'queryset_list_athens_embryo_val': queryset_list_athens_embryo_val,
        'queryset_list_athens_sperm_val': queryset_list_athens_sperm_val,
        'queryset_list_athens_icsi_val': queryset_list_athens_icsi_val,
        'queryset_list_athens_iui_val': queryset_list_athens_iui_val,

        'my_total_clinic_count_thessaloniki': my_total_clinic_count_thessaloniki,
        'queryset_list_thessaloniki_ivf_val': queryset_list_thessaloniki_ivf_val,
        'queryset_list_thessaloniki_egg_val': queryset_list_thessaloniki_egg_val,
        'queryset_list_thessaloniki_embryo_val': queryset_list_thessaloniki_embryo_val,
        'queryset_list_thessaloniki_sperm_val': queryset_list_thessaloniki_sperm_val,
        'queryset_list_thessaloniki_icsi_val': queryset_list_thessaloniki_icsi_val,
        'queryset_list_thessaloniki_iui_val': queryset_list_thessaloniki_iui_val,
        }
    return render(request, 'main/Locations/GRLocations/gr-regions-ivf.html', context)

