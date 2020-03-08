from django.contrib import admin
from django.contrib.auth.models import User
from .models import contactClinic, claimClinic, contactWebsite

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'contactTitle',)
    search_fields = ('clinicOwner__username',)

class PostAdmin2(admin.ModelAdmin):
    list_display = ('id', 'clinicOwner', 'claimTitle', 'claimUrl')
    search_fields = ('clinicOwner__username',)

class PostAdmin3(admin.ModelAdmin):
    list_display = ('contactTitle', 'contactMessage')
    search_fields = ('clinicOwner__username',)


admin.site.register(contactClinic, PostAdmin)
admin.site.register(claimClinic, PostAdmin2)
admin.site.register(contactWebsite, PostAdmin3)
