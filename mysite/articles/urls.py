from django.urls import path

from . import views
app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('stocks', views.stocks, name='stocks'),
    path('<uuid:article_uuid>/', views.article, name='article'),

]
