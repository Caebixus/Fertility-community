from django.contrib import admin
from django.contrib.auth.models import User
from .models import ownerProInterested, ProUser


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'owner_interested')

class PostAdmin2(admin.ModelAdmin):
    list_display = ('id', 'user', 'paidPropublished')

admin.site.register(ownerProInterested, PostAdmin)

admin.site.register(ProUser, PostAdmin2)
