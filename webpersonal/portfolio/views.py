from django.shortcuts import render
from .models import ProjectPortfolio

# Create your views here.
def portfolio(request):
    projectsportfolio = ProjectPortfolio.objects.all()
    return render(request, 'portfolio/portfolio.html',{'projectsportfolio':projectsportfolio})