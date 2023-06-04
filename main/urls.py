from django.urls import path, include
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('director_words/', views.director, name='director'),
    path('news/<int:pk>', views.detail_view, name='news_detail'),
    path('clubs/<int:pk>', views.clubs_detail, name='clubs_detail'),
    path('forparents/<str:title>', views.for_parents, name='for_parents'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
