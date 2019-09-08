from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.stocks, name='stocks'),
    path('<int:article_id>/', views.articles, name='articles'),
]
