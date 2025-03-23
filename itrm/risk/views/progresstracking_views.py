from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import ProgressTracking
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ProgressTrackingForm

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# ProgressTracking Views
class ProgressTrackingListView(LoginRequiredMixin, ListView):
    model = ProgressTracking
    template_name = 'risk/progresstracking_list.html'
    context_object_name = 'progresstracking_list'


class ProgressTrackingDetailView(LoginRequiredMixin, DetailView):
    model = ProgressTracking
    template_name = 'risk/progresstracking_detail.html'
    context_object_name = 'progresstracking'


class ProgressTrackingCreateView(LoginRequiredMixin, CreateView):
    model = ProgressTracking
    form_class = ProgressTrackingForm
    template_name = 'risk/progresstracking_form.html'
    success_url = reverse_lazy('progresstracking_list')


class ProgressTrackingUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgressTracking
    form_class = ProgressTrackingForm
    template_name = 'risk/progresstracking_form.html'
    success_url = reverse_lazy('progresstracking_list')


class ProgressTrackingDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgressTracking
    template_name = 'risk/progresstracking_confirm_delete.html'
    success_url = reverse_lazy('progresstracking_list')