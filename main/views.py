from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import ArticlesForm
from .models import Articles
from .models import Director


def index(request):
    news = Articles.objects.order_by('-date')
    director = Director.objects.first()
    return render(request, 'main/index.html', {'title': 'Детский сад "ДиАми"', 'news': news, 'director': director})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

def director(request):
    director = Director.objects.first()
    return render(request, 'main/director.html', {'title': 'Приветственное слово директора', 'director': director})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

