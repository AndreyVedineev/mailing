from django.shortcuts import render
from django.views.generic import ListView

from posting.models import Letter


class IndexListView(ListView):
    model = Letter
    extra_context = {
        'Письма': 'Рассылки - наше все'
    }
