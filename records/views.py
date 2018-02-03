from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from records.models import Customer

class CustomerList(ListView):
    model = Customer
    template_name = 'records/customer_list.html'

class CustomerDetail(DetailView):
    model = Customer
    template_name = 'records/customer_detail.html'

class CustomerNew(CreateView):
    model = Customer
    template_name = 'records/customer_new.html'
    fields = '__all__'

class CustomerEdit(UpdateView):
    model = Customer
    template_name = 'records/customer_edit.html'
    fields = ['address', 'gallon_code']

class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'records/customer_delete.html'
    success_url = reverse_lazy('customer_list')


