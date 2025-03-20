from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import (
    Company,
)

# Company Views


class CompanyListView(ListView):
    model = Company
    template_name = 'org/company_list.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'org/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    # Specify the fields to display in the form
    fields = ['name', 'address', 'top_level_department']
    template_name = 'org/company_form.html'
    # Redirect after successful creation
    success_url = reverse_lazy('company_list')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'address', 'top_level_department']
    template_name = 'org/company_form.html'
    success_url = reverse_lazy('company_list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'org/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')
