from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.models import Client
from posting.models import Letter


class IndexListView(ListView):
    model = Letter

    extra_context = {
        'title': 'Рассылки - наше все'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['client_list'] = Client.objects.all()
        return context


class LetterCreateView(CreateView):
    model = Letter
    fields = ('topic_letter', 'body_letter', 'tining', 'logic', 'clients')
    success_url = reverse_lazy('posting:letter_list')


class LetterUpdateView(UpdateView):
    model = Letter
    fields = ('topic_letter', 'body_letter', 'tining', 'logic', 'clients')
    success_url = reverse_lazy('posting:letter_list')


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('posting:letter_list')


