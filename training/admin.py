# DJANGO IMPORTS
from django.contrib import admin

# MY IMPORTS
from . import models

# Register your models here.

@admin.register(models.Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = 'name', #'mandatory'
    ordering = 'name',
    search_fields = 'name', #'mandatory',
    list_per_page = 10
