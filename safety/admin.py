# DJANGO IMPORTS
from django.contrib import admin

# MY IMPORTS
from . import models

# Register your models here.

@admin.register(models.RiskChemical)
class RiskChemicalAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.RiskAccident)
class RiskAccidentAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.RiskBiological)
class RiskBiologicalAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.RiskErgonomic)
class RiskErgonomicAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.RiskPhysical)
class RiskPhysicalAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.ExpositionRisk)
class ExpositionRiskAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',
    ordering = 'name',
    search_fields = 'name', 'description',
    list_per_page = 10

@admin.register(models.TypeEpi)
class TypeEpiAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name',
    search_fields = 'name',
    list_per_page = 10

@admin.register(models.Epi)
class EpiAdmin(admin.ModelAdmin):
    list_display = 'name', 'type_epi', 'description',
    ordering = 'name',
    search_fields = 'name', 'type_epi__name',
    list_per_page = 10
    # filter_horizontal = 'type_epi',