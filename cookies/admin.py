from django.contrib import admin

from .models import CookiesConsents


class CookiesConsentsAdmin(admin.ModelAdmin):
    model = CookiesConsents


admin.site.register(CookiesConsents, CookiesConsentsAdmin)
