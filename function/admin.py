# DJANGO IMPORTS
from django.contrib import admin

# MY IMPORTS
from . import models

# Register your models here.



# INLINE MODELS - FUNCTIONS

class FunctionRiskPhysicalInline(admin.TabularInline):
    model = models.FunctionRiskPhysical
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_physical']

class FunctionRiskChemicalInline(admin.TabularInline):
    model = models.FunctionRiskChemical
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_chemical']

class FunctionRiskErgonomicInline(admin.TabularInline):
    model = models.FunctionRiskErgonomic
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_ergonomic']

class FunctionRiskBiologicalIlnie(admin.TabularInline):
    model = models.FunctionRiskBiological
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_biological']
    
class FunctionRiskAccidentInline(admin.TabularInline):
    model = models.FunctionRiskAccident
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_accident']

# INLINE MODELS - SPECIAL ACTIVITIES

class SpecialActivityRiskPhysicalInline(admin.TabularInline):
    model = models.SpecialActivityRiskPhysical
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_physical']

class SpecialActivityRiskChemicalInline(admin.TabularInline):
    model = models.SpecialActivityChemical
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_chemical']

class SpecialActivityRiskErgonomicInline(admin.TabularInline):
    model = models.SpecialActivityErgonomic
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_ergonomic']

class SpecialActivityRiskBiologicalInline(admin.TabularInline):
    model = models.SpecialActivityBiological
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_biological']

class SpecialActivityRiskAccidentInline(admin.TabularInline):
    model = models.SpecialActivityAccident
    extra = 1
    filter_horizontal = 'expositions',
    autocomplete_fields = ['risk_accident']

# PRINCIPAL MODELS

@admin.register(models.SpecialActivity)
class SpecialActivityAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug',
    ordering = 'name',
    search_fields = 'name', 'slug',
    list_per_page = 10
    filter_horizontal = 'trainings', 'epis', 'exams_admissional', \
                        'exams_periodic', 'exams_dismissal', \
                        'exams_return_work', 'exams_change_function',
    readonly_fields = 'slug',
    inlines = [
        SpecialActivityRiskAccidentInline,
        SpecialActivityRiskBiologicalInline,
        SpecialActivityRiskChemicalInline,
        SpecialActivityRiskErgonomicInline,
        SpecialActivityRiskPhysicalInline,
    ]

# TODO: Organize os blocos de campos com o fieldsets.
@admin.register(models.Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = 'name', 'cbo', 'epi_mandatory', 'slug',
    list_display_links = 'name', 'cbo',
    ordering = 'name', 'epi_mandatory',
    search_fields = 'name', 'slug',
    list_per_page = 10
    filter_horizontal = 'special_activities', 'trainings', 'epis',\
                        'exams_admissional', 'exams_periodic', \
                        'exams_dismissal', 'exams_return_work', \
                        'exams_change_function',
    readonly_fields = 'slug',
    inlines = [
        FunctionRiskAccidentInline,
        FunctionRiskBiologicalIlnie,
        FunctionRiskChemicalInline,
        FunctionRiskErgonomicInline,
        FunctionRiskPhysicalInline,
    ]