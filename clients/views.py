from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.models import Client


class ClientsListView(ListView):
    model = Client

    extra_context = {
        'Клиенты': 'Клиенты - Клиенты - Клиенты!'
    }


class ClientsCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'gender', 'age')
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Client
    fields = ('full_name', 'email', 'gender', 'age')
    success_url = reverse_lazy('clients:clients_list')


class ClientsDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')
