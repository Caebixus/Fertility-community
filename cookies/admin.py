from django.contrib import admin

from .models import CookiesConsents, CookieSettings


class CookiesConsentsAdmin(admin.ModelAdmin):
    model = CookiesConsents

class CookieSettingsAdmin(admin.ModelAdmin):
    model = CookieSettings


admin.site.register(CookiesConsents, CookiesConsentsAdmin)
admin.site.register(CookieSettings, CookieSettingsAdmin)
