from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    EmployeePositionAssignment,
)
from ..forms import EmployeePositionAssignmentForm

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
    template_name = 'risker/employeepositionassignment_form.html'
    success_url = reverse_lazy('employeepositionassignment_list')

    def get_initial(self):
        initial = super().get_initial()
        position_id = self.request.GET.get('position')
        if position_id:
            initial['position'] = position_id
        return initial


class EmployeePositionAssignmentUpdateView(UpdateView):
    model = EmployeePositionAssignment
    form_class = EmployeePositionAssignmentForm
    template_name = 'risker/employeepositionassignment_form.html'
    success_url = reverse_lazy('employeepositionassignment_list')


class EmployeePositionAssignmentDeleteView(DeleteView):
    model = EmployeePositionAssignment
    template_name = 'risker/employeepositionassignment_confirm_delete.html'
    success_url = reverse_lazy('employeepositionassignment_list')
