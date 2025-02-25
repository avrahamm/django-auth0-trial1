from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from projects.models import Project


# Create your views here.
@login_required
def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})


@login_required
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',
                  {'project': project})


@login_required
def project_detail_by_slug(request, slug):
    # project = Project.objects.get(pk=pk)
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/detail.html',
                  {'project': project})