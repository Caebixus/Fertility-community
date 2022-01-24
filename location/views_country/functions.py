from clinic.models import BasicClinic
from django.db.models import Sum


def country_count(country_name):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list = queryset_list.filter(clinicState=country_name)
    return queryset_list.count()


def region_count(region_name):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list = queryset_list.filter(clinicRegion__iexact=region_name)
    return queryset_list.count()


def procedure_country_average_value(cost_name, country_name):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list = queryset_list.filter(clinicState=country_name)

    filter = cost_name + '__' + 'isnull'
    clinic_count = queryset_list.filter(**{ filter: False })
    clinic_count = clinic_count.count()

    queryset_list_usd = queryset_list.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_eur = queryset_list.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_usd:
        queryset_list_usd = queryset_list_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_usd.items():
            if val != None:
                queryset_list_usd_val = val
            else:
                queryset_list_usd_val = 0
    else:
        queryset_list_usd_val = 0

    if queryset_list_eur:
        queryset_list_eur = queryset_list_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_eur.items():
            if val != None:
                queryset_list_eur_val = val
            else:
                queryset_list_eur_val = 0
    else:
        queryset_list_eur_val = 0

    queryset_listsum = queryset_list_eur_val + queryset_list_usd_val
    if queryset_listsum != 0:
        queryset_listknown_egg_ivf_val = queryset_listsum / clinic_count
    else:
        queryset_listknown_egg_ivf_val = 0

    return queryset_listknown_egg_ivf_val


def procedure_region_average_value(cost_name, region_name):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list = queryset_list.filter(clinicRegion__iexact=region_name)

    filter = cost_name + '__' + 'isnull'
    clinic_count = queryset_list.filter(**{ filter: False })
    clinic_count = clinic_count.count()

    queryset_list_usd = queryset_list.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_eur = queryset_list.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_usd:
        queryset_list_usd = queryset_list_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_usd.items():
            if val != None:
                queryset_list_usd_val = val
            else:
                queryset_list_usd_val = 0
    else:
        queryset_list_usd_val = 0

    if queryset_list_eur:
        queryset_list_eur = queryset_list_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_eur.items():
            if val != None:
                queryset_list_eur_val = val
            else:
                queryset_list_eur_val = 0
    else:
        queryset_list_eur_val = 0

    queryset_listsum = queryset_list_eur_val + queryset_list_usd_val
    if queryset_listsum != 0:
        queryset_listknown_egg_ivf_val = queryset_listsum / clinic_count
    else:
        queryset_listknown_egg_ivf_val = 0

    return queryset_listknown_egg_ivf_val

def procedure_city_average_value(cost_name, city_name):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    queryset_list = queryset_list.filter(clinicCity__iexact=city_name)

    filter = cost_name + '__' + 'isnull'
    clinic_count = queryset_list.filter(**{ filter: False })
    clinic_count = clinic_count.count()

    queryset_list_usd = queryset_list.filter(defaultClinicCurrency='USD').filter(ovarian_ivf_treatment_cost__isnull=False)
    queryset_list_eur = queryset_list.filter(defaultClinicCurrency='EUR').filter(ovarian_ivf_treatment_cost__isnull=False)

    if queryset_list_usd:
        queryset_list_usd = queryset_list_usd.aggregate(Sum(cost_name))
        for key, val in queryset_list_usd.items():
            if val != None:
                queryset_list_usd_val = val
            else:
                queryset_list_usd_val = 0
    else:
        queryset_list_usd_val = 0

    if queryset_list_eur:
        queryset_list_eur = queryset_list_eur.aggregate(Sum(cost_name))
        for key, val in queryset_list_eur.items():
            if val != None:
                queryset_list_eur_val = val
            else:
                queryset_list_eur_val = 0
    else:
        queryset_list_eur_val = 0

    queryset_listsum = queryset_list_eur_val + queryset_list_usd_val
    if queryset_listsum != 0:
        queryset_listknown_egg_ivf_val = queryset_listsum / clinic_count
    else:
        queryset_listknown_egg_ivf_val = 0

    return queryset_listknown_egg_ivf_val