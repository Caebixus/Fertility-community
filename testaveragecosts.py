import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from clinic.models import BasicClinic
from location.models.country_models import *

from location.views_country.functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value, procedure_city_average_value
from django.apps import apps

city_name = {
    'Amdavad': 'Amdavad',
    'Bangalore': 'Bangalore',
}

for k, v in city_name.items():
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)
    city_name_ = k

    queryset_list_natural_ivf_val = procedure_city_average_value(queryset_list, 'ivf_treatment_cost', city_name_)
    queryset_list_mild_ivf_val = procedure_city_average_value(queryset_list, 'mild_ivf_treatment_cost', city_name_)
    queryset_list_standard_ivf_val = procedure_city_average_value(queryset_list, 'ovarian_ivf_treatment_cost', city_name_)
    queryset_list_egg_ivf_val = procedure_city_average_value(queryset_list, 'egg_donor_recipients_cost', city_name_)
    queryset_list_known_egg_ivf_val = procedure_city_average_value(queryset_list, 'known_egg_donor_recipients_cost', city_name_)
    queryset_list_shared_egg_ivf_val = procedure_city_average_value(queryset_list, 'shared_egg_donor_recipients_cost', city_name_)
    queryset_list_embryo_ivf_val = procedure_city_average_value(queryset_list, 'embryo_donor_recipients_cost', city_name_)
    queryset_list_known_embryo_ivf_val = procedure_city_average_value(queryset_list, 'known_embryo_donor_recipients_cost', city_name_)
    queryset_list_sperm_ivf_val = procedure_city_average_value(queryset_list, 'sperm_donor_recipients_cost', city_name_)
    queryset_list_known_sperm_ivf_val = procedure_city_average_value(queryset_list, 'known_sperm_donor_recipients_cost', city_name_)
    queryset_list_icsi_val = procedure_city_average_value(queryset_list, 'icsi_treatment_cost', city_name_)
    queryset_list_iui_val = procedure_city_average_value(queryset_list, 'iui_treatment_cost', city_name_)

    model = apps.get_model('location', v)

    if not model.objects.exists():
        costs = model.objects.create(pk=1)

        costs.natural_ivf_val = queryset_list_natural_ivf_val
        costs.mild_ivf_val = queryset_list_mild_ivf_val
        costs.standard_ivf_val = queryset_list_standard_ivf_val
        costs.egg_ivf_val = queryset_list_egg_ivf_val
        costs.known_egg_ivf_val = queryset_list_known_egg_ivf_val
        costs.shared_egg_ivf_val = queryset_list_shared_egg_ivf_val
        costs.embryo_ivf_val = queryset_list_embryo_ivf_val
        costs.known_embryo_ivf_val = queryset_list_known_embryo_ivf_val
        costs.sperm_ivf_val = queryset_list_sperm_ivf_val
        costs.known_sperm_ivf_val = queryset_list_known_sperm_ivf_val
        costs.icsi_val = queryset_list_icsi_val
        costs.iui_val = queryset_list_iui_val
        costs.save()
    else:
        costs = model.objects.get(pk=1)

        costs.natural_ivf_val = queryset_list_natural_ivf_val
        costs.mild_ivf_val = queryset_list_mild_ivf_val
        costs.standard_ivf_val = queryset_list_standard_ivf_val
        costs.egg_ivf_val = queryset_list_egg_ivf_val
        costs.known_egg_ivf_val = queryset_list_known_egg_ivf_val
        costs.shared_egg_ivf_val = queryset_list_shared_egg_ivf_val
        costs.embryo_ivf_val = queryset_list_embryo_ivf_val
        costs.known_embryo_ivf_val = queryset_list_known_embryo_ivf_val
        costs.sperm_ivf_val = queryset_list_sperm_ivf_val
        costs.known_sperm_ivf_val = queryset_list_known_sperm_ivf_val
        costs.icsi_val = queryset_list_icsi_val
        costs.iui_val = queryset_list_iui_val
        costs.save()
