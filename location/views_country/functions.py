from clinic.models import BasicClinic
from django.db.models import Sum


def country_count(country_name):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list_cz = queryset_list_cz.filter(clinicState=country_name)
    return queryset_list_cz.count()


def region_count(region_name):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list_cz = queryset_list_cz.filter(clinicRegion__iexact=region_name)
    return queryset_list_cz.count()


def procedure_country_average_value(cost_name, country_name, clinic_count):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list_cz = queryset_list_cz.filter(clinicState=country_name)

    queryset_list_cz_usd = queryset_list_cz.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_cz_eur = queryset_list_cz.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_cz_usd:
        queryset_list_cz_usd = queryset_list_cz_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_usd.items():
            if val != None:
                queryset_list_cz_usd_val = val
            else:
                queryset_list_cz_usd_val = 0
    else:
        queryset_list_cz_usd_val = 0

    if queryset_list_cz_eur:
        queryset_list_cz_eur = queryset_list_cz_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_eur.items():
            if val != None:
                queryset_list_cz_eur_val = val
            else:
                queryset_list_cz_eur_val = 0
    else:
        queryset_list_cz_eur_val = 0

    queryset_list_cz_sum = queryset_list_cz_eur_val + queryset_list_cz_usd_val
    if queryset_list_cz_sum != 0:
        queryset_list_cz_known_egg_ivf_val = queryset_list_cz_sum / clinic_count
    else:
        queryset_list_cz_known_egg_ivf_val = 0

    return queryset_list_cz_known_egg_ivf_val


def procedure_region_average_value(cost_name, region_name, clinic_count):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list_cz = queryset_list_cz.filter(clinicRegion__iexact=region_name)

    queryset_list_cz_usd = queryset_list_cz.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_cz_eur = queryset_list_cz.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_cz_usd:
        queryset_list_cz_usd = queryset_list_cz_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_usd.items():
            if val != None:
                queryset_list_cz_usd_val = val
            else:
                queryset_list_cz_usd_val = 0
    else:
        queryset_list_cz_usd_val = 0

    if queryset_list_cz_eur:
        queryset_list_cz_eur = queryset_list_cz_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_eur.items():
            if val != None:
                queryset_list_cz_eur_val = val
            else:
                queryset_list_cz_eur_val = 0
    else:
        queryset_list_cz_eur_val = 0

    queryset_list_cz_sum = queryset_list_cz_eur_val + queryset_list_cz_usd_val
    if queryset_list_cz_sum != 0:
        queryset_list_cz_known_egg_ivf_val = queryset_list_cz_sum / clinic_count
    else:
        queryset_list_cz_known_egg_ivf_val = 0

    return queryset_list_cz_known_egg_ivf_val

def procedure_city_average_value(cost_name, city_name, clinic_count):
    queryset_list_cz = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list_cz = queryset_list_cz.filter(clinicCity__iexact=city_name)

    queryset_list_cz_usd = queryset_list_cz.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_cz_eur = queryset_list_cz.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_cz_usd:
        queryset_list_cz_usd = queryset_list_cz_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_usd.items():
            if val != None:
                queryset_list_cz_usd_val = val
            else:
                queryset_list_cz_usd_val = 0
    else:
        queryset_list_cz_usd_val = 0

    if queryset_list_cz_eur:
        queryset_list_cz_eur = queryset_list_cz_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_cz_eur.items():
            if val != None:
                queryset_list_cz_eur_val = val
            else:
                queryset_list_cz_eur_val = 0
    else:
        queryset_list_cz_eur_val = 0

    queryset_list_cz_sum = queryset_list_cz_eur_val + queryset_list_cz_usd_val
    if queryset_list_cz_sum != 0:
        queryset_list_cz_known_egg_ivf_val = queryset_list_cz_sum / clinic_count
    else:
        queryset_list_cz_known_egg_ivf_val = 0

    return queryset_list_cz_known_egg_ivf_val