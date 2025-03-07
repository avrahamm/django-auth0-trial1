from django.shortcuts import render, redirect
from projects.models import Project


# Create your views here.
def all_projects(request):
    # print(f"all_projects cur session user =  {request.session.get("user")}")
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',
                  {'project': project})


def project_detail_by_slug(request, slug):
    # project = Project.objects.get(pk=pk)
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/detail.html',
                  {'project': project})