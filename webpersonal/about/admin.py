from django.contrib import admin
from .models import ProjectAbout

# Register your models here.
class ProjectAboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(ProjectAbout, ProjectAboutAdmin)