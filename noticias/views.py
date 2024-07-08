from django.shortcuts import render
from .models import project
# Create your views here.

def noticias(request):
    projects = project.objects.all()
    return render(request, "noticias/noticias.html", {'projects':projects})
