from django.contrib import admin
from django.contrib.auth.models import User
from .models import Packages
from clinic.models import BasicClinic

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Packages
    list_display = ('packagestitle', 'packageOwner')

admin.site.register(Packages, PostAdmin)
