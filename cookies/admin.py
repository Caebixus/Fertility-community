from django.contrib import admin

from .models import CookiesConsents, CookieSettings


class CookiesConsentsAdmin(admin.ModelAdmin):
    list_display = (
        'custom_cookie',
        'ip_address',
        'analytical_cookies',
        'marketing_cookies',
        'consent_created',
    )
    model = CookiesConsents


class CookieSettingsAdmin(admin.ModelAdmin):
    model = CookieSettings


admin.site.register(CookiesConsents, CookiesConsentsAdmin)
admin.site.register(CookieSettings, CookieSettingsAdmin)
