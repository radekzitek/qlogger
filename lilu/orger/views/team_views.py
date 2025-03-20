from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    Team,
)

# Team Views


class TeamListView(ListView):
    model = Team
    template_name = 'orger/team_list.html'
    context_object_name = 'teams'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'orger/team_detail.html'
    context_object_name = 'team'


class TeamCreateView(CreateView):
    model = Team
    fields = ['company', 'name']
    template_name = 'orger/team_form.html'
    success_url = reverse_lazy('team_list')


class TeamUpdateView(UpdateView):
    model = Team
    fields = ['company', 'name']
    template_name = 'orger/team_form.html'
    success_url = reverse_lazy('team_list')


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'orger/team_confirm_delete.html'
    success_url = reverse_lazy('team_list')
