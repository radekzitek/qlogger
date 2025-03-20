from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    TeamMembership,
)
from ..forms import TeamMembershipForm


# TeamMembership Views


class TeamMembershipListView(ListView):
    model = TeamMembership
    template_name = 'orger/teammembership_list.html'
    context_object_name = 'team_memberships'


class TeamMembershipDetailView(DetailView):
    model = TeamMembership
    template_name = 'orger/teammembership_detail.html'
    context_object_name = 'team_membership'


class TeamMembershipCreateView(CreateView):
    model = TeamMembership
    form_class = TeamMembershipForm
    # fields = ['employee', 'team', 'joined_date']
    template_name = 'orger/teammembership_form.html'
    success_url = reverse_lazy('teammembership_list')


class TeamMembershipUpdateView(UpdateView):
    model = TeamMembership
    form_class = TeamMembershipForm
    # fields = ['employee', 'team', 'joined_date']
    template_name = 'orger/teammembership_form.html'
    success_url = reverse_lazy('teammembership_list')


class TeamMembershipDeleteView(DeleteView):
    model = TeamMembership
    template_name = 'orger/teammembership_confirm_delete.html'
    success_url = reverse_lazy('teammembership_list')
