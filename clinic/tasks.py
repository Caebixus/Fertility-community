from __future__ import absolute_import, unicode_literals
from celery import task

from .models import BasicClinic

import logging
logger = logging.getLogger(__name__)

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
