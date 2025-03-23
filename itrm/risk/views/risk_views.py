from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from ..models import Risk, Asset, Control, MitigationAction
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import RiskForm, AssetModalForm, ControlForm, MitigationActionForm
from org.models import Department  # Import Department model
from django.http import JsonResponse

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

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
    form_class = RiskForm
    template_name = 'risk/risk_form.html'
    success_url = reverse_lazy('risk_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_assets'] = Asset.objects.all()
        context['available_controls'] = Control.objects.all()
        context['available_mitigation_actions'] = MitigationAction.objects.all()
        context['asset_form'] = AssetModalForm()  # Add AssetForm to context
        context['control_form'] = ControlForm()  # Add ControlForm to context
        context['mitigation_action_form'] = MitigationActionForm()  # Add MitigationActionForm to context
        return context

    def form_valid(self, form):
        risk = form.save()
        asset_ids = self.request.POST.getlist('associated_assets')
        assets = Asset.objects.filter(pk__in=asset_ids)
        risk.associated_assets.set(assets)

        control_ids = self.request.POST.getlist('associated_controls')
        controls = Control.objects.filter(pk__in=control_ids)
        risk.associated_controls.set(controls)

        mitigation_action_ids = self.request.POST.getlist('associated_mitigation_actions')
        mitigation_actions = MitigationAction.objects.filter(pk__in=mitigation_action_ids)
        risk.associated_mitigation_actions.set(mitigation_actions)

        return super().form_valid(form)


class RiskUpdateView(LoginRequiredMixin, UpdateView):
    model = Risk
    form_class = RiskForm
    template_name = 'risk/risk_form.html'
    success_url = reverse_lazy('risk_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_assets'] = Asset.objects.all()
        context['associated_assets'] = self.object.associated_assets.all()
        context['available_controls'] = Control.objects.all()
        context['associated_controls'] = self.object.associated_controls.all()
        context['available_mitigation_actions'] = MitigationAction.objects.all()
        context['associated_mitigation_actions'] = self.object.associated_mitigation_actions.all()
        context['asset_form'] = AssetModalForm()  # Add AssetForm to context
        context['control_form'] = ControlForm()  # Add ControlForm to context
        context['mitigation_action_form'] = MitigationActionForm()  # Add MitigationActionForm to context
        return context

    def form_valid(self, form):
        risk = form.save()
        asset_ids = self.request.POST.getlist('associated_assets')
        assets = Asset.objects.filter(pk__in=asset_ids)
        risk.associated_assets.set(assets)

        control_ids = self.request.POST.getlist('associated_controls')
        controls = Control.objects.filter(pk__in=control_ids)
        risk.associated_controls.set(controls)

        mitigation_action_ids = self.request.POST.getlist('associated_mitigation_actions')
        mitigation_actions = MitigationAction.objects.filter(pk__in=mitigation_action_ids)
        risk.associated_mitigation_actions.set(mitigation_actions)

        return super().form_valid(form)


class RiskDeleteView(LoginRequiredMixin, DeleteView):
    model = Risk
    template_name = 'risk/risk_confirm_delete.html'
    success_url = reverse_lazy('risk_list')

class ControlCreateAjaxView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ControlForm(request.POST)
        if form.is_valid():
            control = form.save()
            return JsonResponse({
                'success': True,
                'control_id': control.pk,
                'control_name': control.control_name
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })

class MitigationActionCreateAjaxView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = MitigationActionForm(request.POST)
        if form.is_valid():
            mitigation_action = form.save()
            return JsonResponse({
                'success': True,
                'mitigation_action_id': mitigation_action.pk,
                'mitigation_action_description': mitigation_action.action_description
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })