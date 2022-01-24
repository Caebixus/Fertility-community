from django import template
from base.models import CurrenciesExchangeRates

eur_to_usd_rate = 1.13
eur_to_gbp_rate = 0.83

register = template.Library()

rate = CurrenciesExchangeRates.objects.get(pk=1)

def convert(value, arg):
    if arg == 'USD':
        return value
    elif arg == 'EUR':
        new_value = value * rate.usd_to_eur_exchange
    elif arg == 'GBP':
        new_value = value * rate.usd_to_gbp_exchange
    elif arg == 'CZK':
        new_value = value * rate.usd_to_czk_exchange
    elif arg == 'MXN':
        new_value = value * rate.usd_to_mxn_exchange
    elif arg == 'INR':
        new_value = value * rate.usd_to_inr_exchange
    elif arg == 'CAD':
        new_value = value * rate.usd_to_cad_exchange
    return new_value

register.filter("convert", convert)

def convertEUR(value, arg):
    if arg == 'EUR':
        return value
    elif arg == 'USD':
        new_value = value * eur_to_usd_rate
    elif arg == 'GBP':
        new_value = value * eur_to_gbp_rate
    return new_value

register.filter("convertEUR", convertEUR)