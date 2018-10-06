from django.shortcuts import render
from .models import ProjectAbout

# Create your views here.
def about(request):
    projectsabout = ProjectAbout.objects.all()
    return render(request, 'about/about.html',{'projectsabout':projectsabout})