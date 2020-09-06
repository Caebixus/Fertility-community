from django.contrib import admin
from django.contrib.auth.models import User
from .models import Packages, TruePackages
from clinic.models import BasicClinic

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Packages
    list_display = ('packagestitle', 'packageOwner', 'packageClinic')


admin.site.register(Packages, PostAdmin)
