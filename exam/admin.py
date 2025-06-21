# DJANGO IMPORTS
from django.contrib import admin

# MY IMPORTS
from . import models

# Register your models here.

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = 'exam_name',
    ordering = 'exam_name',
    search_fields = 'exam_name',
    list_per_page = 10