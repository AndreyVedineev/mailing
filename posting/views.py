from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import clients.models
from clients.models import Client
from posting.models import Letter
from posting.services import send_posting_email


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

    def form_valid(self, form):
        obj = form.save()
        send_posting_email(obj)
        return super().form_valid(form)


    # def get_success_url(self):
    #     return reverse('posting:letter_list', args=[self.kwargs.get('pk')])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['letter'] = get_object_or_404(Letter, pk=self.kwargs.get('pk'))
    #     return context_data


class LetterUpdateView(UpdateView):
    model = Letter
    fields = ('topic_letter', 'body_letter', 'tining', 'logic', 'clients')
    success_url = reverse_lazy('posting:letter_list')

    def get_queryset(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormst = inlineformset_factory(Letter, Client, form=...., extra=1)
        context_data['formset'] = SubjectFormst
        return context_data

    def form_valid(self, form):
        dd = super().get_queryset()
        print(dd)
        obj = form.save()
        print(obj)

        send_posting_email(obj)
        return super().form_valid(form)


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('posting:letter_list')
