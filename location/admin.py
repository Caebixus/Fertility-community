from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models.europe_city_models import *
from .models.asia_city_models import *
from .models.country_models import *
from .models.north_america_region_models import *
from .models.north_america_city_models import *

class AverageTreatmentCostUkAdmin(admin.ModelAdmin):
    model = AverageTreatmentCostUk
    list_display = ('id',)


admin.site.register(AverageTreatmentCostUk, AverageTreatmentCostUkAdmin)


class AverageTreatmentCostUsaAdmin(admin.ModelAdmin):
    model = AverageTreatmentCostUsa
    list_display = ('id',)


admin.site.register(AverageTreatmentCostUsa, AverageTreatmentCostUsaAdmin)


class SwanseaAdmin(admin.ModelAdmin):
    model = Swansea
    list_display = ('id',)


admin.site.register(Swansea, SwanseaAdmin)


class BrnoAdmin(admin.ModelAdmin):
    model = Brno
    list_display = ('id',)


admin.site.register(Brno, BrnoAdmin)


class LondonAdmin(admin.ModelAdmin):
    model = London
    list_display = ('id',)


admin.site.register(London, LondonAdmin)


class AmdavadAdmin(admin.ModelAdmin):
    model = Amdavad
    list_display = ('id',)


admin.site.register(Amdavad, AmdavadAdmin)


class BangaloreAdmin(admin.ModelAdmin):
    model = Bangalore
    list_display = ('id',)


admin.site.register(Bangalore, BangaloreAdmin)

class MontanaAdmin(admin.ModelAdmin):
    model = Montana
    list_display = ('id',)


admin.site.register(Montana, MontanaAdmin)

class AlabamaAdmin(admin.ModelAdmin):
    model = Alabama
    list_display = ('id',)


admin.site.register(Alabama, AlabamaAdmin)
