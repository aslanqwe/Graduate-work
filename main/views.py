from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import ArticlesForm
from .models import Articles


def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'main/index.html', {'title': 'Детский сад "ДиАми"', 'news': news})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

