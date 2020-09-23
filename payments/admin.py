from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer

# Register your models here.
class PostAdmin3(admin.ModelAdmin):
    list_display = ('customerClinic', 'cancel_at_period_end')
    search_fields = ('customerClinic',)


admin.site.register(Customer, PostAdmin3)
