from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/edit', views.NewsEditView.as_view(), name='news_edit')
]