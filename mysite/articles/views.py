from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core import serializers
from .forms import CommentForm
from .models import Article, Quote, Comment
import itertools

def home(request):
    qs1 = Article.objects.filter(article_type ="10-promise-series")[:1]
    qs2 = Article.objects.all()[:3]
    latest_article_list = itertools.chain(qs1, qs2)
    context = {'latest_article_list': latest_article_list}
    return render(request, 'articles/home.html', context)


def article(request, article_uuid):
    article = get_object_or_404(Article, pk=article_uuid)
    comments = article.comments.order_by('-created')[:10] # set a reasonable amount and have the newest at the top 
    suggested_articles = Article.objects.all()[:3]
    stock_list = serializers.serialize('json', Quote.objects.all())
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return render(request, 'articles/article.html', {'article': article, 'suggested_articles': suggested_articles, 'stock_list': stock_list,'comments': comments, 'form': form})
    else:
        form = CommentForm()
    # return HttpResponse(request, 'articles/article.html', {'article': article, 'suggested_articles': suggested_articles},stock_list, content_type='application/json')
    return render(request, 'articles/article.html', {'article': article, 'suggested_articles': suggested_articles, 'stock_list': stock_list, 'comments': comments, 'form': form})


def stocks(request):
    return HttpResponse("Welcome to the stock page")
