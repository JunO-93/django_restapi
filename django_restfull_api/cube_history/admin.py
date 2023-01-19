from django.contrib import admin
from .models import data

# Register your models here.
class chracterName(admin.ModelAdmin):
    search_fields=['character_name']

admin.site.register(data, chracterName)
