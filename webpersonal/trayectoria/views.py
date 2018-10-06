from django.shortcuts import render
from .models import ProjectTrayectoria

# Create your views here.
def trayectoria(request):
    projectstrayectoria = ProjectTrayectoria.objects.all()
    return render(request, 'trayectoria/trayectoria.html',{'projectstrayectoria':projectstrayectoria})