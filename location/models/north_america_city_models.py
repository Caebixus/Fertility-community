from django.db import models


class MexicoCity(models.Model):
    natural_ivf_val = models.FloatField(blank=True, null=True)
    mild_ivf_val = models.FloatField(blank=True, null=True)
    standard_ivf_val = models.FloatField(blank=True, null=True)

    egg_ivf_val = models.FloatField(blank=True, null=True)
    known_egg_ivf_val = models.FloatField(blank=True, null=True)
    shared_egg_ivf_val = models.FloatField(blank=True, null=True)

    embryo_ivf_val = models.FloatField(blank=True, null=True)
    known_embryo_ivf_val = models.FloatField(blank=True, null=True)

    sperm_ivf_val = models.FloatField(blank=True, null=True)
    known_sperm_ivf_val = models.FloatField(blank=True, null=True)

    icsi_val = models.FloatField(blank=True, null=True)
    iui_val = models.FloatField(blank=True, null=True)