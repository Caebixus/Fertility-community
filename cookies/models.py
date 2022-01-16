from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CookieSettings(models.Model):
    analytical_cookies_header = models.TextField(_("Cookies využívané pro analytiku webu"), max_length=2000, blank=True, null=True)
    analytical_cookies_footer = models.TextField(_("Cookies využívané pro analytiku webu (vložte kód určený do footeru)"), max_length=2000, blank=True, null=True)
    marketing_cookies_header = models.TextField(_("Cookies využívané k reklamním účelům"), max_length=2000, blank=True, null=True)
    marketing_cookies_footer = models.TextField(_("Cookies využívané k reklamním účelům (vložte kód určený do footeru)"), max_length=2000, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class CookiesConsents(models.Model):
    session_id = models.CharField(_("Session ID cookie"), max_length=256, blank=True, null=True, unique=True)
    ip_address = models.CharField(_("IP Adresa"), max_length=64, blank=True, null=True)
    analytical_cookies = models.BooleanField(default=False)
    marketing_cookies = models.BooleanField(default=False)
    consent_created = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return str(self.consent_created)