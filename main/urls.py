from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('director_words/', views.director, name='director'),
    path('clubs/<int:pk>', views.ClubsDetailView.as_view(), name='clubs_detail'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
]
