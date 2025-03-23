from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

class RiskDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'risk/dashboard.html'