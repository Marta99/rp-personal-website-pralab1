from django.shortcuts import render
from apps.portfolio.models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project_list.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project':project}
    return render(request, 'project_detail.html', context)