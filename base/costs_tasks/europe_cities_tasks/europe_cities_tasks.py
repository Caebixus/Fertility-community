from __future__ import absolute_import, unicode_literals
from celery import task

from clinic.models import BasicClinic

from location.models.europe_city_models import *
from location.views_country.functions import procedure_region_average_value
from django.apps import apps

import logging
logger = logging.getLogger(__name__)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

region_name = {
    'Prague': 'Prague',
    'Brno': 'Brno',
    'Alicante': 'Alicante',
    'Barcelona': 'Barcelona',
    'Madrid': 'Madrid',
    'Malaga': 'Malaga',
    'Seville': 'Seville',
    'Valencia': 'Valencia',
    'Bratislava': 'Bratislava',
    'Lisbon': 'Lisbon',
    'Riga': 'Riga',
    'Thessaloniki': 'Thessaloniki',
    'Athens': 'Athens',
    'Copenhagen': 'Copenhagen',
    'Berlin': 'Berlin',
    'Girne': 'Girne',
    'Nicosia': 'Nicosia',
    'Aberdeen': 'Aberdeen',
    'Bath': 'Bath',
    'Belfast': 'Belfast',
    'Birmingham': 'Birmingham',
    'Bournemouth': 'Bournemouth',
    'Brighton': 'Brighton',
    'Bristol': 'Bristol',
    'Cambridge': 'Cambridge',
    'Cardiff': 'Cardiff',
    'Colchester': 'Colchester',
    'Derby': 'Derby',
    'Exeter': 'Exeter',
    'Glasgow': 'Glasgow',
    'Hull': 'Hull',
    'Chelmsford': 'Chelmsford',
    'Leeds': 'Leeds',
    'Leicester': 'Leicester',
    'Liverpool': 'Liverpool',
    'London': 'London',
    'Manchester': 'Manchester',
    'Middlesbrough': 'Middlesbrough',
    'Newcastle': 'Newcastle',
    'Norwich': 'Norwich',
    'Nottingham': 'Nottingham',
    'Oxford': 'Oxford',
    'Peterborough': 'Peterborough',
    'Plymouth': 'Plymouth',
    'Portsmouth': 'Portsmouth',
    'Salisbury': 'Salisbury',
    'Sheffield': 'Sheffield',
    'Southampton': 'Southampton',
    'Swansea': 'Swansea',
}

@task()
def calculate_average_country_costs():
    for k, v in region_name.items():
        queryset_list = BasicClinic.objects.all().exclude(is_published=False)
        region_name_ = k

        queryset_list_natural_ivf_val = procedure_region_average_value(queryset_list, 'ivf_treatment_cost', region_name_)
        queryset_list_mild_ivf_val = procedure_region_average_value(queryset_list, 'mild_ivf_treatment_cost', region_name_)
        queryset_list_standard_ivf_val = procedure_region_average_value(queryset_list, 'ovarian_ivf_treatment_cost', region_name_)
        queryset_list_egg_ivf_val = procedure_region_average_value(queryset_list, 'egg_donor_recipients_cost', region_name_)
        queryset_list_known_egg_ivf_val = procedure_region_average_value(queryset_list, 'known_egg_donor_recipients_cost', region_name_)
        queryset_list_shared_egg_ivf_val = procedure_region_average_value(queryset_list, 'shared_egg_donor_recipients_cost', region_name_)
        queryset_list_embryo_ivf_val = procedure_region_average_value(queryset_list, 'embryo_donor_recipients_cost', region_name_)
        queryset_list_known_embryo_ivf_val = procedure_region_average_value(queryset_list, 'known_embryo_donor_recipients_cost', region_name_)
        queryset_list_sperm_ivf_val = procedure_region_average_value(queryset_list, 'sperm_donor_recipients_cost', region_name_)
        queryset_list_known_sperm_ivf_val = procedure_region_average_value(queryset_list, 'known_sperm_donor_recipients_cost', region_name_)
        queryset_list_icsi_val = procedure_region_average_value(queryset_list, 'icsi_treatment_cost', region_name_)
        queryset_list_iui_val = procedure_region_average_value(queryset_list, 'iui_treatment_cost', region_name_)

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
