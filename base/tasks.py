from __future__ import absolute_import, unicode_literals
from celery import task

from django.utils import timezone
from datetime import timedelta

from clinic.calculate_dti import calculate_dti_single
from clinic.models import BasicClinic

import logging
logger = logging.getLogger(__name__)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

import requests
from base.models import CurrenciesExchangeRates


@task()
def calculate_dti():
    clinics = BasicClinic.objects.filter(is_published=True)
    for obj in clinics:
        calculate_dti_single(instance=obj)
        obj.save()


@task()
def currencies_rate_update():

    response = requests.get(f'http://api.currencylayer.com/live?access_key=c36176bb29d50514cb4c0181503a4fb9&currencies=EUR,CZK,GBP, MXN, INR, CAD')
    data = response.json()
    new_usd_to_czk_exchange = data['quotes']['USDCZK']
    new_usd_to_eur_exchange = data['quotes']['USDEUR']
    new_usd_to_gbp_exchange = data['quotes']['USDGBP']
    new_usd_to_mxn_exchange = data['quotes']['USDMXN']
    new_usd_to_inr_exchange = data['quotes']['USDINR']
    new_usd_to_cad_exchange = data['quotes']['USDCAD']


    rate = CurrenciesExchangeRates.objects.get(pk=1)
    rate.usd_to_czk_exchange = new_usd_to_czk_exchange
    rate.usd_to_eur_exchange = new_usd_to_eur_exchange
    rate.usd_to_gbp_exchange = new_usd_to_gbp_exchange
    rate.usd_to_mxn_exchange = new_usd_to_mxn_exchange
    rate.usd_to_inr_exchange = new_usd_to_inr_exchange
    rate.usd_to_cad_exchange = new_usd_to_cad_exchange
    rate.save()


@task()
def calculate_active_clinic():
    last_month = timezone.now() - timedelta(days=30)
    last_3_months = timezone.now() - timedelta(days=90)
    last_6_months = timezone.now() - timedelta(days=180)
    clinics = BasicClinic.objects.filter(is_published=True, is_claimed=True)
    for clinic in clinics:
        if clinic.clinicOwner.last_login > last_month:
            clinic.active_30 = True
            clinic.save()
        else:
            clinic.active_30 = False
            clinic.save()
        if clinic.clinicOwner.last_login > last_3_months:
            clinic.active_90 = True
            clinic.save()
        else:
            clinic.active_90 = False
            clinic.save()
        if clinic.clinicOwner.last_login > last_6_months:
            clinic.active_180 = True
            clinic.save()
        else:
            clinic.active_180 = False
            clinic.save()


# @task()
# def calculate_package_number
#     todayDate = timezone.now()
#     pro_clinics = BasicClinic.objects.filter(is_published=True, ppq_is_published=True).exclude(pro_is_published=True)
#     for clinic in pro_clinics:
#         notactivelisting = Package.objects.filter(package_end_list_date__lte=todayDate)
#         notactivelisting = notactivelisting.filter(packageclinic_id=clinic)
#         clinic.packageClinicCounterNumber = 0 ?
#
#
#     ppq_clinics = BasicClinic.objects.filter(is_published=True, pro_is_published=True).exclude(ppq_is_published=True)
#     for clinic in ppq_clinics: