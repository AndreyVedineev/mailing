from django.shortcuts import render
from django.views.generic import ListView

from clients.models import Client


# Create your views here.


class IndexListView(ListView):
    model = Client
    # extra_context = {
    #     'Клиенты': 'Клиенты - наше все'
    # }
