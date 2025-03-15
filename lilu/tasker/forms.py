
from django import forms
from .models import Team, Member, Task

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'lead']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['team', 'name', 'email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'is_completed', 'team', 'member']