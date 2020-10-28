from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ownerProInterested, ProUser, AuthenticatedUser


class AuthenticatedUser(admin.StackedInline):
    model = AuthenticatedUser
    can_delete = False
    verbose_name_plural = 'AuthenticatedUsers'

class UserAdmin(BaseUserAdmin):
    inlines = (AuthenticatedUser,)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'owner_interested')

class PostAdmin2(admin.ModelAdmin):
    list_display = ('id', 'user', 'paidPropublished')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(ownerProInterested, PostAdmin)

admin.site.register(ProUser, PostAdmin2)
