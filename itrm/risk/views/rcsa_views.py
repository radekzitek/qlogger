from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import RCSA
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import RCSAForm

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# RCSA Views
class RCSAListView(LoginRequiredMixin, ListView):
    model = RCSA
    template_name = 'risk/rcsa_list.html'
    context_object_name = 'rcsa_list'


class RCSADetailView(LoginRequiredMixin, DetailView):
    model = RCSA
    template_name = 'risk/rcsa_detail.html'
    context_object_name = 'rcsa'


class RCSACreateView(LoginRequiredMixin, CreateView):
    model = RCSA
    form_class = RCSAForm
    template_name = 'risk/rcsa_form.html'
    success_url = reverse_lazy('rcsa_list')


class RCSAUpdateView(LoginRequiredMixin, UpdateView):
    model = RCSA
    form_class = RCSAForm
    template_name = 'risk/rcsa_form.html'
    success_url = reverse_lazy('rcsa_list')


class RCSADeleteView(LoginRequiredMixin, DeleteView):
    model = RCSA
    template_name = 'risk/rcsa_confirm_delete.html'
    success_url = reverse_lazy('rcsa_list')