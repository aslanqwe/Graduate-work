from django.shortcuts import render

from .models import Articles


def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'main/index.html', {'title': 'Детский сад "ДиАми"', 'news': news})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})
