from django.contrib import admin
from .models import ProjectTrayectoria

# Register your models here.
class ProjectTrayectoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(ProjectTrayectoria, ProjectTrayectoriaAdmin)