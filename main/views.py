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

class NewsEditView(UpdateView):
    model = Articles
    template_name = 'main/edit.html'
    form_class = ArticlesForm
    context_object_name = 'article'
    # перенаправит на ту же новость, которую редактировал
    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование статьи'
        return context