from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import RiskCategoryLevel1, RiskCategoryLevel2, Risk, Asset, Control, MitigationAction, ProgressTracking
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RiskForm, AssetForm  # Import AssetForm
import datetime

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

# Risk Views


class RiskListView(LoginRequiredMixin, ListView):
    model = Risk
    template_name = 'risk/risk_list.html'
    context_object_name = 'risk_list'


class RiskDetailView(LoginRequiredMixin, DetailView):
    model = Risk
    template_name = 'risk/risk_detail.html'
    context_object_name = 'risk'


class RiskCreateView(LoginRequiredMixin, CreateView):
    model = Risk
    # fields = ['risk_id', 'risk_name', 'risk_category', 'risk_description', 'potential_impact', 'likelihood_of_occurrence',
    #           'inherent_risk_score', 'risk_owner', 'date_identified', 'status', 'relevant_eu_regulations', 'associated_assets', 'associated_controls']
    form_class = RiskForm
    template_name = 'risk/risk_form.html'
    success_url = reverse_lazy('risk_list')


class RiskUpdateView(LoginRequiredMixin, UpdateView):
    model = Risk
    # fields = ['risk_id', 'risk_name', 'risk_category', 'risk_description', 'potential_impact', 'likelihood_of_occurrence',
    #           'inherent_risk_score', 'risk_owner', 'date_identified', 'status', 'relevant_eu_regulations', 'associated_assets', 'associated_controls']
    form_class = RiskForm
    template_name = 'risk/risk_form.html'
    success_url = reverse_lazy('risk_list')


class RiskDeleteView(LoginRequiredMixin, DeleteView):
    model = Risk
    template_name = 'risk/risk_confirm_delete.html'
    success_url = reverse_lazy('risk_list')

# Asset Views


class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = 'risk/asset_list.html'
    context_object_name = 'asset_list'


class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    template_name = 'risk/asset_detail.html'
    context_object_name = 'asset'


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm  # Use AssetForm
    template_name = 'risk/asset_form.html'
    success_url = reverse_lazy('asset_list')


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm  # Use AssetForm
    template_name = 'risk/asset_form.html'
    success_url = reverse_lazy('asset_list')


class AssetDeleteView(LoginRequiredMixin, DeleteView):
    model = Asset
    template_name = 'risk/asset_confirm_delete.html'
    success_url = reverse_lazy('asset_list')

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
    fields = ['progress_tracking_id', 'mitigation_action', 'date_of_update', 'progress_update', 'percentage_completion',
              'actual_start_date', 'actual_end_date', 'effectiveness_assessment', 'updated_residual_risk', 'updated_by']
    template_name = 'risk/progresstracking_form.html'
    success_url = reverse_lazy('progresstracking_list')


class ProgressTrackingUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgressTracking
    fields = ['progress_tracking_id', 'mitigation_action', 'date_of_update', 'progress_update', 'percentage_completion',
              'actual_start_date', 'actual_end_date', 'effectiveness_assessment', 'updated_residual_risk', 'updated_by']
    template_name = 'risk/progresstracking_form.html'
    success_url = reverse_lazy('progresstracking_list')


class ProgressTrackingDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgressTracking
    template_name = 'risk/progresstracking_confirm_delete.html'
    success_url = reverse_lazy('progresstracking_list')


class RiskDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'risk/dashboard.html'
