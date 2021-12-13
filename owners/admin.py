from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ownerProInterested, ProUser, AuthenticatedUser, SingleClinicBestArticleText


class AuthenticatedUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_activated')

class SingleClinicBestArticleTextAdmin(admin.ModelAdmin):
    autocomplete_fields = ["clinic_world"]
    list_display = ('id', 'clinic_world', 'best_clinic_world_text')

#class UserAdmin(BaseUserAdmin):
    #inlines = (AuthenticatedUser,)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'owner_interested')

class PostAdmin2(admin.ModelAdmin):
    list_display = ('id', 'user', 'paidPropublished')

admin.site.register(AuthenticatedUser, AuthenticatedUserAdmin)

admin.site.register(SingleClinicBestArticleText, SingleClinicBestArticleTextAdmin)

admin.site.register(ownerProInterested, PostAdmin)

admin.site.register(ProUser, PostAdmin2)
