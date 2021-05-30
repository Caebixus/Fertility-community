from django.db import models

# Create your models here.

class CurrenciesExchangeRates(models.Model):
    usd_to_czk_exchange = models.FloatField(blank=True, null=True)
    usd_to_eur_exchange = models.FloatField(blank=True, null=True)
    usd_to_gbp_exchange = models.FloatField(blank=True, null=True)
    usd_to_mxn_exchange = models.FloatField(blank=True, null=True)
    usd_to_inr_exchange = models.FloatField(blank=True, null=True)
    usd_to_cad_exchange = models.FloatField(blank=True, null=True)
    def __str__(self):
        return str(self.id)
