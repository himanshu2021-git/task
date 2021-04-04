from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

admin.site.register(City, CityAdmin)
                
            
admin.site.register(User)