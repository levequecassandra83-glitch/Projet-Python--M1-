from django.shortcuts import render, get_object_or_404
from .models import Project

def liste_projects(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'projects/liste.html', {'projects': projects})

def detail_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
