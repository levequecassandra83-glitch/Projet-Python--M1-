from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'type_project', 'date')
    list_filter = ('type_project', 'date')
    search_fields = ('titre', 'description')
