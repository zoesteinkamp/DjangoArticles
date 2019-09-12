from django.urls import path

from . import views
app_name = 'articles'

urlpatterns = [
    path('home', views.home, name='home'),
    path('stocks', views.stocks, name='stocks'),
    path('authors', views.authors, name='authors'),
    path('<uuid:article_uuid>/', views.article, name='article'),
    path('authors/<uuid:author_uuid>/', views.author, name='author'),

]
