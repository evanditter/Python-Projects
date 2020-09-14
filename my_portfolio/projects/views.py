from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from projects.models import Projects

def projects_index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects_index.html', context)

def projects_detail(request, pk):
    projects = Projects.objects.get(pk=pk)
    context = {
         'projects': projects
    }
    return render(request, 'projects_detail.html', context)
