from django.shortcuts import render
from django.views.generic import DetailView


from .models import Articles
from .models import Director
from .models import Clubs
from .models import ForParents
from .models import About

def index(request):
    news = Articles.objects.order_by('-date')
    director = Director.objects.first()
    clubs = Clubs.objects.all()
    forparents = ForParents.objects.all()
    return render(request, 'main/index.html', {'title': 'Детский сад "ДиАми"', 'news': news, 'director': director, 'clubs': clubs, 'forparents': forparents})
def about(request):
    about = About.objects.all()
    return render(request, 'main/about.html', {'title': 'О нас', 'about': about})
def detail_view(request, pk):
    article = Articles.objects.get(pk=pk)
    return render(request, 'main/details_view.html', {'title': 'Новости', 'article': article})
def blog(request):
    blog = Articles.objects.order_by('-date')
    return render(request, 'main/blog.html', {'title': 'Новости', 'blog': blog})


def director(request):
    director = Director.objects.first()
    return render(request, 'main/director.html', {'title': 'Приветственное слово директора', 'director': director, })

def clubs_detail(request, pk):
    clubs = Clubs.objects.get(pk=pk)
    return render(request, 'main/clubs.html', {'title': clubs.name_clubs, 'clubs': clubs,})

def for_parents(request, pk):
    forparents = ForParents.objects.get(pk=pk)
    return render(request, 'main/forparents.html', {'title': forparents.title, 'forparents': forparents})



# class NewsDetailView(DetailView):
#     model = Articles
#     template_name = 'main/details_view.html'
#     context_object_name = 'article'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Новости'
#         return context

# class ClubsDetailView(DetailView):
#     model = Clubs
#     template_name = 'main/clubs.html'
#     context_object_name = 'clubs_kids'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.object.name_clubs
#         return context


