from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import RiskCategoryLevel2
from django.contrib.auth.mixins import LoginRequiredMixin

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

# RiskCategoryLevel2 Views
class RiskCategoryLevel2ListView(LoginRequiredMixin, ListView):
    model = RiskCategoryLevel2
    template_name = 'risk/riskcategorylevel2_list.html'
    context_object_name = 'riskcategorylevel2_list'


class RiskCategoryLevel2DetailView(LoginRequiredMixin, DetailView):
    model = RiskCategoryLevel2
    template_name = 'risk/riskcategorylevel2_detail.html'
    context_object_name = 'riskcategorylevel2'


class RiskCategoryLevel2CreateView(LoginRequiredMixin, CreateView):
    model = RiskCategoryLevel2
    fields = ['level1', 'name', 'description', 'relevant_eu_regulations']
    template_name = 'risk/riskcategorylevel2_form.html'
    success_url = reverse_lazy('riskcategorylevel2_list')


class RiskCategoryLevel2UpdateView(LoginRequiredMixin, UpdateView):
    model = RiskCategoryLevel2
    fields = ['level1', 'name', 'description', 'relevant_eu_regulations']
    template_name = 'risk/riskcategorylevel2_form.html'
    success_url = reverse_lazy('riskcategorylevel2_list')


class RiskCategoryLevel2DeleteView(LoginRequiredMixin, DeleteView):
    model = RiskCategoryLevel2
    template_name = 'risk/riskcategorylevel2_confirm_delete.html'
    success_url = reverse_lazy('riskcategorylevel2_list')