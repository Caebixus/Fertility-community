from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsSPRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 2
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'Spain'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count
    
    sp_average_costs_model = AverageTreatmentCostSpain.objects.get(pk=1)

    queryset_list_sp_natural_ivf_val = sp_average_costs_model.natural_ivf_val
    queryset_list_sp_mild_ivf_val = sp_average_costs_model.mild_ivf_val
    queryset_list_sp_standard_ivf_val = sp_average_costs_model.standard_ivf_val
    queryset_list_sp_egg_ivf_val = sp_average_costs_model.egg_ivf_val
    queryset_list_sp_known_egg_ivf_val = sp_average_costs_model.known_egg_ivf_val
    queryset_list_sp_shared_egg_ivf_val = sp_average_costs_model.shared_egg_ivf_val
    queryset_list_sp_embryo_ivf_val = sp_average_costs_model.embryo_ivf_val
    queryset_list_sp_known_embryo_ivf_val = sp_average_costs_model.known_embryo_ivf_val
    queryset_list_sp_sperm_ivf_val = sp_average_costs_model.sperm_ivf_val
    queryset_list_sp_known_sperm_ivf_val = sp_average_costs_model.known_sperm_ivf_val
    queryset_list_sp_icsi_val = sp_average_costs_model.icsi_val
    queryset_list_sp_iui_val = sp_average_costs_model.iui_val

    queryset_list_sp = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact='Spain')

    queryset_list_alicante = queryset_list_sp.filter(clinicRegion__iexact='Alicante')
    my_total_clinic_count_alicante = queryset_list_alicante.count()
    alicante_average_costs_model = Alicante.objects.get(pk=1)
    queryset_list_alicante_ivf_val = alicante_average_costs_model.standard_ivf_val
    queryset_list_alicante_egg_val = alicante_average_costs_model.egg_ivf_val
    queryset_list_alicante_embryo_val = alicante_average_costs_model.embryo_ivf_val
    queryset_list_alicante_sperm_val = alicante_average_costs_model.sperm_ivf_val
    queryset_list_alicante_icsi_val = alicante_average_costs_model.icsi_val
    queryset_list_alicante_iui_val = alicante_average_costs_model.iui_val

    queryset_list_barcelona = queryset_list_sp.filter(clinicRegion__iexact='Barcelona')
    my_total_clinic_count_barcelona = queryset_list_barcelona.count()
    barcelona_average_costs_model = Barcelona.objects.get(pk=1)
    queryset_list_barcelona_ivf_val = barcelona_average_costs_model.standard_ivf_val
    queryset_list_barcelona_egg_val = barcelona_average_costs_model.egg_ivf_val
    queryset_list_barcelona_embryo_val = barcelona_average_costs_model.embryo_ivf_val
    queryset_list_barcelona_sperm_val = barcelona_average_costs_model.sperm_ivf_val
    queryset_list_barcelona_icsi_val = barcelona_average_costs_model.icsi_val
    queryset_list_barcelona_iui_val = barcelona_average_costs_model.iui_val

    queryset_list_madrid = queryset_list_sp.filter(clinicRegion__iexact='Madrid')
    my_total_clinic_count_madrid = queryset_list_madrid.count()
    madrid_average_costs_model = Madrid.objects.get(pk=1)
    queryset_list_madrid_ivf_val = madrid_average_costs_model.standard_ivf_val
    queryset_list_madrid_egg_val = madrid_average_costs_model.egg_ivf_val
    queryset_list_madrid_embryo_val = madrid_average_costs_model.embryo_ivf_val
    queryset_list_madrid_sperm_val = madrid_average_costs_model.sperm_ivf_val
    queryset_list_madrid_icsi_val = madrid_average_costs_model.icsi_val
    queryset_list_madrid_iui_val = madrid_average_costs_model.iui_val

    queryset_list_malaga = queryset_list_sp.filter(clinicRegion__iexact='Malaga')
    my_total_clinic_count_malaga = queryset_list_malaga.count()
    malaga_average_costs_model = Malaga.objects.get(pk=1)
    queryset_list_malaga_ivf_val = malaga_average_costs_model.standard_ivf_val
    queryset_list_malaga_egg_val = malaga_average_costs_model.egg_ivf_val
    queryset_list_malaga_embryo_val = malaga_average_costs_model.embryo_ivf_val
    queryset_list_malaga_sperm_val = malaga_average_costs_model.sperm_ivf_val
    queryset_list_malaga_icsi_val = malaga_average_costs_model.icsi_val
    queryset_list_malaga_iui_val = malaga_average_costs_model.iui_val

    queryset_list_seville = queryset_list_sp.filter(clinicRegion__iexact='Seville')
    my_total_clinic_count_seville = queryset_list_seville.count()
    seville_average_costs_model = Seville.objects.get(pk=1)
    queryset_list_seville_ivf_val = seville_average_costs_model.standard_ivf_val
    queryset_list_seville_egg_val = seville_average_costs_model.egg_ivf_val
    queryset_list_seville_embryo_val = seville_average_costs_model.embryo_ivf_val
    queryset_list_seville_sperm_val = seville_average_costs_model.sperm_ivf_val
    queryset_list_seville_icsi_val = seville_average_costs_model.icsi_val
    queryset_list_seville_iui_val = seville_average_costs_model.iui_val

    queryset_list_valencia = queryset_list_sp.filter(clinicRegion__iexact='Valencia')
    my_total_clinic_count_valencia = queryset_list_valencia.count()
    valencia_average_costs_model = Valencia.objects.get(pk=1)
    queryset_list_valencia_ivf_val = valencia_average_costs_model.standard_ivf_val
    queryset_list_valencia_egg_val = valencia_average_costs_model.egg_ivf_val
    queryset_list_valencia_embryo_val = valencia_average_costs_model.embryo_ivf_val
    queryset_list_valencia_sperm_val = valencia_average_costs_model.sperm_ivf_val
    queryset_list_valencia_icsi_val = valencia_average_costs_model.icsi_val
    queryset_list_valencia_iui_val = valencia_average_costs_model.iui_val

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

