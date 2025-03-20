from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    TeamLeaderAssignment
)
from ..forms import TeamLeaderAssignmentForm


# TeamLeaderAssignment Views


class TeamLeaderAssignmentListView(ListView):
    model = TeamLeaderAssignment
    template_name = 'org/teamleaderassignment_list.html'
    context_object_name = 'team_leader_assignments'


class TeamLeaderAssignmentDetailView(DetailView):
    model = TeamLeaderAssignment
    template_name = 'org/teamleaderassignment_detail.html'
    context_object_name = 'team_leader_assignment'


class TeamLeaderAssignmentCreateView(CreateView):
    model = TeamLeaderAssignment
    form_class = TeamLeaderAssignmentForm
    # fields = ['team', 'leader', 'assigned_date']
    template_name = 'org/teamleaderassignment_form.html'
    success_url = reverse_lazy('teamleaderassignment_list')


class TeamLeaderAssignmentUpdateView(UpdateView):
    model = TeamLeaderAssignment
    form_class = TeamLeaderAssignmentForm
    # fields = ['team', 'leader', 'assigned_date']
    template_name = 'org/teamleaderassignment_form.html'
    success_url = reverse_lazy('teamleaderassignment_list')


class TeamLeaderAssignmentDeleteView(DeleteView):
    model = TeamLeaderAssignment
    template_name = 'org/teamleaderassignment_confirm_delete.html'
    success_url = reverse_lazy('teamleaderassignment_list')

