from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    Department,
)

# Department Views


class DepartmentListView(ListView):
    model = Department
    template_name = 'org/department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'org/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['company', 'name', 'manager_position', 'parent_department']
    template_name = 'org/department_form.html'
    success_url = reverse_lazy('department_list')

    def get_initial(self):
        initial = super().get_initial()
        parent_department_id = self.request.GET.get('parent_department')
        if parent_department_id:
            initial['parent_department'] = parent_department_id
            try:
                parent_department = Department.objects.get(
                    pk=parent_department_id)
                initial['company'] = parent_department.company.pk
            except Department.DoesNotExist:
                pass  # Handle the case where the parent department doesn't exist
        return initial


class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['company', 'name', 'manager_position', 'parent_department']
    template_name = 'org/department_form.html'
    success_url = reverse_lazy('department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'org/department_confirm_delete.html'
    success_url = reverse_lazy('department_list')
