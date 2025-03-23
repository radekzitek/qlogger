from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import MitigationAction
from django.contrib.auth.mixins import LoginRequiredMixin

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# MitigationAction Views
class MitigationActionListView(LoginRequiredMixin, ListView):
    model = MitigationAction
    template_name = 'risk/mitigationaction_list.html'
    context_object_name = 'mitigationaction_list'


class MitigationActionDetailView(LoginRequiredMixin, DetailView):
    model = MitigationAction
    template_name = 'risk/mitigationaction_detail.html'
    context_object_name = 'mitigationaction'


class MitigationActionCreateView(LoginRequiredMixin, CreateView):
    model = MitigationAction
    fields = ['mitigation_action_id', 'risk', 'action_description', 'priority', 'assigned_to', 'target_start_date',
              'target_end_date', 'status', 'estimated_cost', 'actual_cost', 'expected_outcome', 'created_by', 'updated_by']
    template_name = 'risk/mitigationaction_form.html'
    success_url = reverse_lazy('mitigationaction_list')


class MitigationActionUpdateView(LoginRequiredMixin, UpdateView):
    model = MitigationAction
    fields = ['mitigation_action_id', 'risk', 'action_description', 'priority', 'assigned_to', 'target_start_date',
              'target_end_date', 'status', 'estimated_cost', 'actual_cost', 'expected_outcome', 'created_by', 'updated_by']
    template_name = 'risk/mitigationaction_form.html'
    success_url = reverse_lazy('mitigationaction_list')


class MitigationActionDeleteView(LoginRequiredMixin, DeleteView):
    model = MitigationAction
    template_name = 'risk/mitigationaction_confirm_delete.html'
    success_url = reverse_lazy('mitigationaction_list')