from django.shortcuts import redirect, render
from .models import Project
from .forms import AddProjectForm

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project/index.html', context)

def detail(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tag.all()
    # for tag in tags:
    #     print('==================', tag)
    context = {'project':project, 'tags':tags}
    return render(request, 'project/detail.html', context) 


def addproject(request, ):
    form = AddProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'project/add_project.html', context)

def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = AddProjectForm(instance=project)

    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'project/add_project.html', context)

def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')
    context = {'project':project}
    return render(request, 'project/deleteproject.html', context)