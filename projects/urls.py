from django.urls import path
from projects import views
from portfolio.auth_decorators import requires_auth


app_name = 'projects'

urlpatterns = [
    path('', requires_auth(views.all_projects), name='all_projects'),
    path('<int:pk>', requires_auth(views.project_detail), name='project_detail'),
    path('<slug:slug>', requires_auth(views.project_detail_by_slug),
         name='project_detail_by_slug'),
]