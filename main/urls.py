from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('director_words/', views.director, name='director'),
    path('english/', views.english, name='english'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
]