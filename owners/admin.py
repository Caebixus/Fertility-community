from django.contrib import admin
from django.contrib.auth.models import User
from .models import ownerProInterested


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'owner_interested')

admin.site.register(ownerProInterested, PostAdmin)
