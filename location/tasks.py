from __future__ import absolute_import, unicode_literals
from celery import task

from clinic.models import BasicClinic
from .models.country_models import *
from .views_country.functions import procedure_country_average_value, procedure_region_average_value, procedure_city_average_value
from django.apps import apps

import logging
logger = logging.getLogger(__name__)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

country_name = {
    'United States': 'AverageTreatmentCostUsa',
    'Mexico': 'AverageTreatmentCostMexico',
    'United Kingdom': 'AverageTreatmentCostUk',
    'Spain': 'AverageTreatmentCostSpain',
    'Slovakia': 'AverageTreatmentCostSlovakia',
    'Portugal': 'AverageTreatmentCostPortugal',
    'Latvia': 'AverageTreatmentCostLatvia',
    'India': 'AverageTreatmentCostIndia',
    'Greece': 'AverageTreatmentCostGreece',
    'Denmark': 'AverageTreatmentCostDenmark',
    'Germany': 'AverageTreatmentCostGermany',
    'Czech Republic': 'AverageTreatmentCostCzech',
    'Cyprus': 'AverageTreatmentCostCyprus',
}

@task()
def calculate_average_country_costs():
    for k, v in country_name.items():
        queryset_list = BasicClinic.objects.all().exclude(is_published=False)
        country_name_ = k

        queryset_list_natural_ivf_val = procedure_country_average_value(queryset_list, 'ivf_treatment_cost', country_name_)
        queryset_list_mild_ivf_val = procedure_country_average_value(queryset_list, 'mild_ivf_treatment_cost', country_name_)
        queryset_list_standard_ivf_val = procedure_country_average_value(queryset_list, 'ovarian_ivf_treatment_cost', country_name_)
        queryset_list_egg_ivf_val = procedure_country_average_value(queryset_list, 'egg_donor_recipients_cost', country_name_)
        queryset_list_known_egg_ivf_val = procedure_country_average_value(queryset_list, 'known_egg_donor_recipients_cost', country_name_)
        queryset_list_shared_egg_ivf_val = procedure_country_average_value(queryset_list, 'shared_egg_donor_recipients_cost', country_name_)
        queryset_list_embryo_ivf_val = procedure_country_average_value(queryset_list, 'embryo_donor_recipients_cost', country_name_)
        queryset_list_known_embryo_ivf_val = procedure_country_average_value(queryset_list, 'known_embryo_donor_recipients_cost', country_name_)
        queryset_list_sperm_ivf_val = procedure_country_average_value(queryset_list, 'sperm_donor_recipients_cost', country_name_)
        queryset_list_known_sperm_ivf_val = procedure_country_average_value(queryset_list, 'known_sperm_donor_recipients_cost', country_name_)
        queryset_list_icsi_val = procedure_country_average_value(queryset_list, 'icsi_treatment_cost', country_name_)
        queryset_list_iui_val = procedure_country_average_value(queryset_list, 'iui_treatment_cost', country_name_)

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

us_region_name = {
    'Alabama': 'Alabama',
    'Alaska': 'Alaska',
    'Arizona': 'Arizona',
    'Arkansas': 'Arkansas',
    'California': 'California',
    'Colorado': 'Colorado',
    'Connecticut': 'Connecticut',
    'Delaware': 'Delaware',
    'Florida': 'Florida',
    'Georgia': 'Georgia',
    'Hawaii': 'Hawaii',
    'Idaho': 'Idaho',
    'Illinois': 'Illinois',
    'Indiana': 'Indiana',
    'Iowa': 'Iowa',
    'Kansas': 'Kansas',
    'Kentucky': 'Kentucky',
    'Louisiana': 'Louisiana',
    'Maine': 'Maine',
    'Maryland': 'Maryland',
    'Massachusetts': 'Massachusetts',
    'Michigan': 'Michigan',
    'Minnesota': 'Minnesota',
    'Mississippi': 'Mississippi',
    'Missouri': 'Missouri',
    'Montana': 'Montana',
    'Nebraska': 'Nebraska',
    'New Hampshire': 'NewHampshire',
    'New Jersey': 'NewJersey',
    'New Mexico': 'NewMexico',
    'New York': 'NewYork',
    'North Carolina': 'NorthCarolina',
    'North Dakota': 'NorthDakota',
    'Nevada': 'Nevada',
    'Ohio': 'Ohio',
    'Oklahoma': 'Oklahoma',
    'Oregon': 'Oregon',
    'Pennsylvania': 'Pennsylvania',
    'Puerto Rico': 'PuertoRico',
    'Rhode Island': 'RhodeIsland',
    'South Carolina': 'SouthCarolina',
    'South Dakota': 'SouthDakota',
    'Tennessee': 'Tennessee',
    'Texas': 'Texas',
    'Utah': 'Utah',
    'Vermont': 'Vermont',
    'Virginia': 'Virginia',
    'Washington': 'Washington',
    'West Virginia': 'WestVirginia',
    'Wisconsin': 'Wisconsin',
    'Wyoming': 'Wyoming',
    'District of Columbia': 'DistrictOfColumbia',
}

@task()
def calculate_average_north_america_region_costs():
    for k, v in us_region_name.items():
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


us_city_name = {
    'Mexico City': 'MexicoCity',
}

@task()
def calculate_average_north_america_city_costs():
    for k, v in us_city_name.items():
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


eu_region_name = {
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
def calculate_average_european_city_costs():
    for k, v in eu_region_name.items():
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


asia_city_name = {
    'Amdavad': 'Amdavad',
    'Bangalore': 'Bangalore',
    'Bhopal': 'Bhopal',
    'Bhubaneswar': 'Bhubaneswar',
    'Dehradun': 'Dehradun',
    'Faridabad': 'Faridabad',
    'Hyderabad': 'Hyderabad',
    'Chandigarh': 'Chandigarh',
    'Chennai': 'Chennai',
    'Indore': 'Indore',
    'Jaipur': 'Jaipur',
    'Jamshedpur': 'Jamshedpur',
    'Kanpur': 'Kanpur',
    'Kochi': 'Kochi',
    'Kolkata': 'Kolkata',
    'Lucknow': 'Lucknow',
    'Mumbai': 'Mumbai',
    'Nagpur': 'Nagpur',
    'Patna': 'Patna',
    'Raipur': 'Raipur',
    'Trivandrum': 'Trivandrum',
    'Ludhiana': 'Ludhiana',
    'Visakhapatnam': 'Visakhapatnam',
    'Vijayawada': 'Vijayawada',
    'New Delhi': 'NewDelhi',
    'Vadodara': 'Vadodara',
    'Gurugram': 'Gurugram',
    'Rohtak': 'Rohtak',
    'Jammu': 'Jammu',
    'Ranchi': 'Ranchi',
    'Gwalior': 'Gwalior',
    'Pune': 'Pune',
    'Warangal': 'Warangal',
    'Gachibowli': 'Gachibowli',
    'Madhapur': 'Madhapur',
    'Noida': 'Noida',
    'Meerut': 'Meerut',
    'Haldwani': 'Haldwani',
}

@task()
def calculate_average_asian_city_costs():
    for k, v in asia_city_name.items():
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