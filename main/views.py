from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Детский сад "ДиАми"'})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})