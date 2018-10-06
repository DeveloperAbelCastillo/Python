from django.contrib import admin
from .models import ProjectPortfolio

# Register your models here.
class ProjectPortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(ProjectPortfolio, ProjectPortfolioAdmin)