from django.contrib import admin
from django.contrib.auth.models import User
from .models import Packages, TruePackages, Package
from clinic.models import BasicClinic

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    model = Package
    list_display = ('id', 'packagetitle', 'packageclinic', 'is_package_active', 'package_list_date', 'package_end_list_date')


admin.site.register(Package, PackageAdmin)
