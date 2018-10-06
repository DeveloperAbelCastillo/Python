from django.contrib import admin
from .models import ProjectFormacion

# Register your models here.
class ProjectFormacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(ProjectFormacion, ProjectFormacionAdmin)