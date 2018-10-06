from django.shortcuts import render
from .models import ProjectFormacion

# Create your views here.
def formacion(request):
    projectsformacion = ProjectFormacion.objects.all()
    return render(request, 'formacion/formacion.html',{'projectsformacion':projectsformacion})