from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_staff', 'is_authenticated') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# Register your models here.
