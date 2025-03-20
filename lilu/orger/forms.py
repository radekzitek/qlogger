from django import forms
from .models import EmployeePositionAssignment, TeamMembership, TeamLeaderAssignment, Employee


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


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'company',
            'first_name',
            'last_name',
            'user_name',
            'password',
            'email',
            'phone',
            'address',
        ]
