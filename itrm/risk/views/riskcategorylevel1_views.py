from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import RiskCategoryLevel1
from django.contrib.auth.mixins import LoginRequiredMixin

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# RiskCategoryLevel1 Views
class RiskCategoryLevel1ListView(LoginRequiredMixin, ListView):
    model = RiskCategoryLevel1
    template_name = 'risk/riskcategorylevel1_list.html'
    context_object_name = 'riskcategorylevel1_list'


class RiskCategoryLevel1DetailView(LoginRequiredMixin, DetailView):
    model = RiskCategoryLevel1
    template_name = 'risk/riskcategorylevel1_detail.html'
    context_object_name = 'riskcategorylevel1'


class RiskCategoryLevel1CreateView(LoginRequiredMixin, CreateView):
    model = RiskCategoryLevel1
    fields = ['name', 'description']
    template_name = 'risk/riskcategorylevel1_form.html'
    success_url = reverse_lazy('riskcategorylevel1_list')


class RiskCategoryLevel1UpdateView(LoginRequiredMixin, UpdateView):
    model = RiskCategoryLevel1
    fields = ['name', 'description']
    template_name = 'risk/riskcategorylevel1_form.html'
    success_url = reverse_lazy('riskcategorylevel1_list')


class RiskCategoryLevel1DeleteView(LoginRequiredMixin, DeleteView):
    model = RiskCategoryLevel1
    template_name = 'risk/riskcategorylevel1_confirm_delete.html'
    success_url = reverse_lazy('riskcategorylevel1_list')