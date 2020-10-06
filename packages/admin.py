from django.contrib import admin
from django.contrib.auth.models import User
from .models import Packages, TruePackages, Package
from clinic.models import BasicClinic

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Packages
    list_display = ('packagestitle', 'packageOwner', 'packageClinic')

class PackageAdmin(admin.ModelAdmin):
    model = Package
    list_display = ('packagetitle', 'packageclinic')


admin.site.register(Package, PackageAdmin)


admin.site.register(Packages, PostAdmin)
