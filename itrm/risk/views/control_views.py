from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Control
from django.contrib.auth.mixins import LoginRequiredMixin

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# Control Views
class ControlListView(LoginRequiredMixin, ListView):
    model = Control
    template_name = 'risk/control_list.html'
    context_object_name = 'control_list'


class ControlDetailView(LoginRequiredMixin, DetailView):
    model = Control
    template_name = 'risk/control_detail.html'
    context_object_name = 'control'


class ControlCreateView(LoginRequiredMixin, CreateView):
    model = Control
    fields = ['control_id', 'control_name', 'control_objective', 'control_description', 'control_type',
              'implementation_status', 'effectiveness_rating', 'owner', 'associated_risks', 'associated_assets']
    template_name = 'risk/control_form.html'
    success_url = reverse_lazy('control_list')


class ControlUpdateView(LoginRequiredMixin, UpdateView):
    model = Control
    fields = ['control_id', 'control_name', 'control_objective', 'control_description', 'control_type',
              'implementation_status', 'effectiveness_rating', 'owner', 'associated_risks', 'associated_assets']
    template_name = 'risk/control_form.html'
    success_url = reverse_lazy('control_list')


class ControlDeleteView(LoginRequiredMixin, DeleteView):
    model = Control
    template_name = 'risk/control_confirm_delete.html'
    success_url = reverse_lazy('control_list')