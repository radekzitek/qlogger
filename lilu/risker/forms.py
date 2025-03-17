from django import forms
from .models import EmployeePositionAssignment, TeamMembership, TeamLeaderAssignment


class TeamMembershipForm(forms.ModelForm):
    class Meta:
        model = TeamMembership
        fields = ['employee', 'team', 'joined_date']
        widgets = {
            'joined_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TeamLeaderAssignmentForm(forms.ModelForm):
    class Meta:
        model = TeamLeaderAssignment
        fields = ['team', 'leader', 'assigned_date']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
        }


class EmployeePositionAssignmentForm(forms.ModelForm):
    class Meta:
        model = EmployeePositionAssignment
        fields = ['employee', 'position', 'assigned_date']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
        }
