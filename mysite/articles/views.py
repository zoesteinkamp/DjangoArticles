from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Article




def home(request):
    latest_article_list = Article.objects.order_by('uuid')[:5]
    context = {'latest_article_list': latest_article_list,}
    return render(request, 'articles/home.html', context)

def article(request, article_uuid):
    article = get_object_or_404(Article, pk=article_uuid)
    return render(request, 'articles/article.html', {'article': article})

def stocks(request):
    return HttpResponse("Welcome to the stock page")
