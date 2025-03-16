from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.create_team, name='create_team'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('members/create/', views.create_member, name='create_member'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.create_task, name='create_task'),
]