from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

@admin.register(models.Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'lastname',
        'gender',
        'age',
        'Educationlevel',
        'department',
    ]