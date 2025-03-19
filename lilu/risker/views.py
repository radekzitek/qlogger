from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Company,
    Department,
    Position,
    Employee,
    Team,
    EmployeePositionAssignment,
    TeamMembership,
    TeamLeaderAssignment,
)
from .forms import EmployeePositionAssignmentForm, TeamMembershipForm, TeamLeaderAssignmentForm

# Company Views


class CompanyListView(ListView):
    model = Company
    template_name = 'risker/company_list.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'risker/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    # Specify the fields to display in the form
    fields = ['name', 'top_level_department']
    template_name = 'risker/company_form.html'
    # Redirect after successful creation
    success_url = reverse_lazy('company_list')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'top_level_department']
    template_name = 'risker/company_form.html'
    success_url = reverse_lazy('company_list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'risker/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')

# Department Views


class DepartmentListView(ListView):
    model = Department
    template_name = 'risker/department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'risker/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['company', 'name', 'manager_position', 'parent_department']
    template_name = 'risker/department_form.html'
    success_url = reverse_lazy('department_list')


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['company', 'name', 'manager_position', 'parent_department']
    template_name = 'risker/department_form.html'
    success_url = reverse_lazy('department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'risker/department_confirm_delete.html'
    success_url = reverse_lazy('department_list')

# Position Views


class PositionListView(ListView):
    model = Position
    template_name = 'risker/position_list.html'
    context_object_name = 'positions'

    def get_queryset(self):
        return Position.objects.order_by('department__name', 'title')


class PositionDetailView(DetailView):
    model = Position
    template_name = 'risker/position_detail.html'
    context_object_name = 'position'


class PositionCreateView(CreateView):
    model = Position
    fields = ['department', 'title']
    template_name = 'risker/position_form.html'
    success_url = reverse_lazy('position_list')


class PositionUpdateView(UpdateView):
    model = Position
    fields = ['department', 'title']
    template_name = 'risker/position_form.html'
    success_url = reverse_lazy('position_list')


class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'risker/position_confirm_delete.html'
    success_url = reverse_lazy('position_list')

# Employee Views


class EmployeeListView(ListView):
    model = Employee
    template_name = 'risker/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'risker/employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
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
    template_name = 'risker/employee_form.html'
    success_url = reverse_lazy('employee_list')


def form_valid(self, form):
    """
    Overridden to hash the password.
    """
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    user.save()
    return super().form_valid(form)


class EmployeeUpdateView(UpdateView):
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
    template_name = 'risker/employee_form.html'
    success_url = reverse_lazy('employee_list')


def form_valid(self, form):
    """
    Overridden to hash the password.
    """
    user = form.save(commit=False)
    if form.cleaned_data['password']:
        user.set_password(form.cleaned_data['password'])
    user.save()
    return super().form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'risker/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# Team Views


class TeamListView(ListView):
    model = Team
    template_name = 'risker/team_list.html'
    context_object_name = 'teams'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'risker/team_detail.html'
    context_object_name = 'team'


class TeamCreateView(CreateView):
    model = Team
    fields = ['company', 'name']
    template_name = 'risker/team_form.html'
    success_url = reverse_lazy('team_list')


class TeamUpdateView(UpdateView):
    model = Team
    fields = ['company', 'name']
    template_name = 'risker/team_form.html'
    success_url = reverse_lazy('team_list')


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'risker/team_confirm_delete.html'
    success_url = reverse_lazy('team_list')

# EmployeePositionAssignment Views


class EmployeePositionAssignmentListView(ListView):
    model = EmployeePositionAssignment
    template_name = 'risker/employeepositionassignment_list.html'
    context_object_name = 'employee_position_assignments'


class EmployeePositionAssignmentDetailView(DetailView):
    model = EmployeePositionAssignment
    template_name = 'risker/employeepositionassignment_detail.html'
    context_object_name = 'employee_position_assignment'


class EmployeePositionAssignmentCreateView(CreateView):
    model = EmployeePositionAssignment
    form_class = EmployeePositionAssignmentForm  # Use the form
    # fields = ['employee', 'position', 'assigned_date']
    template_name = 'risker/employeepositionassignment_form.html'
    success_url = reverse_lazy('employeepositionassignment_list')


class EmployeePositionAssignmentUpdateView(UpdateView):
    model = EmployeePositionAssignment
    form_class = EmployeePositionAssignmentForm  # Use the form
    # fields = ['employee', 'position', 'assigned_date']
    template_name = 'risker/employeepositionassignment_form.html'
    success_url = reverse_lazy('employeepositionassignment_list')


class EmployeePositionAssignmentDeleteView(DeleteView):
    model = EmployeePositionAssignment
    template_name = 'risker/employeepositionassignment_confirm_delete.html'
    success_url = reverse_lazy('employeepositionassignment_list')

# TeamMembership Views


class TeamMembershipListView(ListView):
    model = TeamMembership
    template_name = 'risker/teammembership_list.html'
    context_object_name = 'team_memberships'


class TeamMembershipDetailView(DetailView):
    model = TeamMembership
    template_name = 'risker/teammembership_detail.html'
    context_object_name = 'team_membership'


class TeamMembershipCreateView(CreateView):
    model = TeamMembership
    form_class = TeamMembershipForm
    # fields = ['employee', 'team', 'joined_date']
    template_name = 'risker/teammembership_form.html'
    success_url = reverse_lazy('teammembership_list')


class TeamMembershipUpdateView(UpdateView):
    model = TeamMembership
    form_class = TeamMembershipForm
    # fields = ['employee', 'team', 'joined_date']
    template_name = 'risker/teammembership_form.html'
    success_url = reverse_lazy('teammembership_list')


class TeamMembershipDeleteView(DeleteView):
    model = TeamMembership
    template_name = 'risker/teammembership_confirm_delete.html'
    success_url = reverse_lazy('teammembership_list')

# TeamLeaderAssignment Views


class TeamLeaderAssignmentListView(ListView):
    model = TeamLeaderAssignment
    template_name = 'risker/teamleaderassignment_list.html'
    context_object_name = 'team_leader_assignments'


class TeamLeaderAssignmentDetailView(DetailView):
    model = TeamLeaderAssignment
    template_name = 'risker/teamleaderassignment_detail.html'
    context_object_name = 'team_leader_assignment'


class TeamLeaderAssignmentCreateView(CreateView):
    model = TeamLeaderAssignment
    form_class = TeamLeaderAssignmentForm
    # fields = ['team', 'leader', 'assigned_date']
    template_name = 'risker/teamleaderassignment_form.html'
    success_url = reverse_lazy('teamleaderassignment_list')


class TeamLeaderAssignmentUpdateView(UpdateView):
    model = TeamLeaderAssignment
    form_class = TeamLeaderAssignmentForm
    # fields = ['team', 'leader', 'assigned_date']
    template_name = 'risker/teamleaderassignment_form.html'
    success_url = reverse_lazy('teamleaderassignment_list')


class TeamLeaderAssignmentDeleteView(DeleteView):
    model = TeamLeaderAssignment
    template_name = 'risker/teamleaderassignment_confirm_delete.html'
    success_url = reverse_lazy('teamleaderassignment_list')


def dashboard(request):
    companies = Company.objects.all()
    return render(request, 'risker/dashboard.html', {'companies': companies})


def organization_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    top_level_department = company.top_level_department
    departments = Department.objects.filter(company=company).exclude(pk=top_level_department.pk if top_level_department else None)

    def build_department_structure(department):
        structure = {
            'department': department,
            'manager_position': department.manager_position,
            'positions': [],
            'sub_departments': []
        }
        for position in Position.objects.filter(department=department):
            employee_assignment = EmployeePositionAssignment.objects.filter(position=position).first()
            employee = employee_assignment.employee if employee_assignment else None
            structure['positions'].append({'position': position, 'employee': employee})

        for sub_department in Department.objects.filter(parent_department=department):
            structure['sub_departments'].append(build_department_structure(sub_department))
        return structure

    organization_structure = {
        'company': company,
        'top_level_department': top_level_department,
        'departments': []
    }

    if top_level_department:
        organization_structure['departments'].append(build_department_structure(top_level_department))

    return render(request, 'risker/organization.html', {'organization': organization_structure})