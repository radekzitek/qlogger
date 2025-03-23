from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import MitigationAction
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import MitigationActionForm

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
    form_class = MitigationActionForm
    template_name = 'risk/mitigationaction_form.html'
    success_url = reverse_lazy('mitigationaction_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user.username
        form.instance.updated_by = self.request.user.username
        return super().form_valid(form)

class MitigationActionUpdateView(LoginRequiredMixin, UpdateView):
    model = MitigationAction
    form_class = MitigationActionForm
    template_name = 'risk/mitigationaction_form.html'
    success_url = reverse_lazy('mitigationaction_list')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user.username
        return super().form_valid(form)

class MitigationActionDeleteView(LoginRequiredMixin, DeleteView):
    model = MitigationAction
    template_name = 'risk/mitigationaction_confirm_delete.html'
    success_url = reverse_lazy('mitigationaction_list')