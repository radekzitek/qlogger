from django.shortcuts import render,  get_object_or_404

from django.urls import reverse_lazy
from ..models import (
    Company,
    Department,
    Position,
    EmployeePositionAssignment,
)


def form_valid(self, form):
    """
    Overridden to hash the password.
    """
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    user.save()
    return super().form_valid(form)


def dashboard(request):
    companies = Company.objects.all()
    return render(request, 'org/dashboard.html', {'companies': companies})


def organization_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    top_level_department = company.top_level_department
    departments = Department.objects.filter(company=company).exclude(
        pk=top_level_department.pk if top_level_department else None)

    def build_department_structure(department):
        structure = {
            'department': department,
            'manager_position': department.manager_position,
            'positions': [],
            'sub_departments': []
        }
        for position in Position.objects.filter(department=department):
            employee_assignments = EmployeePositionAssignment.objects.filter(
                position=position).order_by('assigned_date')
            assignments_data = []
            for assignment in employee_assignments:
                assignments_data.append({
                    'employee': assignment.employee,
                    'assigned_date': assignment.assigned_date
                })
            assignments_data.reverse()  # Reverse the order here
            structure['positions'].append(
                {'position': position, 'employee_assignments': assignments_data})

        for sub_department in Department.objects.filter(parent_department=department):
            structure['sub_departments'].append(
                build_department_structure(sub_department))
        return structure

    organization_structure = {
        'company': company,
        'top_level_department': top_level_department,
        'departments': []
    }

    if top_level_department:
        organization_structure['departments'].append(
            build_department_structure(top_level_department))

    return render(request, 'org/organization.html', {'organization': organization_structure})
