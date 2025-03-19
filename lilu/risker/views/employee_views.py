from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    Employee,
    Position,
    EmployeePositionAssignment,
)
from ..forms import EmployeeForm
from django.utils import timezone

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

class EmployeeCreateAndAssignView(View):
    template_name = 'risker/employee_create_and_assign.html'

    def get(self, request):
        position_id = request.GET.get('position')
        position = get_object_or_404(Position, pk=position_id)
        form = EmployeeForm(initial={'company': position.department.company})
        return render(request, self.template_name, {'form': form, 'position': position})

    def post(self, request):
        position_id = request.GET.get('position')
        position = get_object_or_404(Position, pk=position_id)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            EmployeePositionAssignment.objects.create(employee=employee, position=position, assigned_date=timezone.now())
            return redirect('employee_detail', pk=employee.pk)  # Or redirect to organization view
        return render(request, self.template_name, {'form': form, 'position': position})
    

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
