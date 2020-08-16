from django.contrib import admin
from django.contrib.auth.models import User
from .models import Packages, TruePackages
from clinic.models import BasicClinic

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Packages
    list_display = ('packagestitle', 'packageOwner', 'packageClinic')

class PostAdmin2(admin.ModelAdmin):
    model = Packages
    list_display = ('Truepackagetitle', 'packageClinic')

admin.site.register(Packages, PostAdmin)
admin.site.register(TruePackages, PostAdmin2)
