from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    Position,
)

# Position Views


class PositionListView(ListView):
    model = Position
    template_name = 'org/position_list.html'
    context_object_name = 'positions'

    def get_queryset(self):
        return Position.objects.order_by('department__name', 'title')


class PositionDetailView(DetailView):
    model = Position
    template_name = 'org/position_detail.html'
    context_object_name = 'position'


class PositionCreateView(CreateView):
    model = Position
    fields = ['department', 'title']
    template_name = 'org/position_form.html'
    success_url = reverse_lazy('position_list')

    def get_initial(self):
        initial = super().get_initial()
        department_id = self.request.GET.get('department')
        if department_id:
            initial['department'] = department_id
        return initial


class PositionUpdateView(UpdateView):
    model = Position
    fields = ['department', 'title']
    template_name = 'org/position_form.html'
    success_url = reverse_lazy('position_list')


class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'org/position_confirm_delete.html'
    success_url = reverse_lazy('position_list')
