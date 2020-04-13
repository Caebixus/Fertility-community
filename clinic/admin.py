from django.contrib import admin
from .models import BasicClinic

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id', 'clinicName', 'clinicOwner', 'list_date', 'is_published', 'is_published_list_date', 'pro_is_published', 'pro_is_published_list_date', 'type', 'clinicRegion', 'clinicState')
    list_filter = ('is_published', 'pro_is_published', 'verified_is_published', 'clinicOwner', 'clinicRegion', 'clinicState', 'clinicCity')
    search_fields = ('clinicName', 'clinicOwner__username', 'clinicRegion', 'clinicState', 'clinicCity')

admin.site.register(BasicClinic, PostAdmin)
