from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Team, Member, Task
from .forms import TeamForm, MemberForm, TaskForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tasker/team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'tasker/team_detail.html', {'team': team})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'tasker/member_list.html', {'members': members})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'tasker/member_detail.html', {'member': member})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasker/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasker/task_detail.html', {'task': task})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('team_list'))
    else:
        form = TeamForm()
    return render(request, 'tasker/create_team.html', {'form': form})

def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_list'))
    else:
        form = MemberForm()
    return render(request, 'tasker/create_member.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
    return render(request, 'tasker/create_task.html', {'form': form})
