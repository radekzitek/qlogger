from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from ..models import Asset
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import AssetForm, AssetModalForm
from django.http import JsonResponse
from org.models import Department  # Import Department model

# Mixin to require login for all views
class LoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Replace with your login URL
    redirect_field_name = 'next'

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


class AssetCreateAjaxView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = AssetModalForm(request.POST) # Use AssetModalForm
        if form.is_valid():
            asset = form.save()
            return JsonResponse({
                'success': True,
                'asset_id': asset.asset_id,
                'asset_name': asset.asset_name
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })