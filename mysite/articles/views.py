from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core import serializers
from .forms import CommentForm
from .models import Article, Quote, Comment, Author, Instrument
import itertools
import json
from django.db.models import Q


def home(request):
    qs1 = Article.objects.filter(tags__slug ="10-promise")[:1]
    # i know that .order_by('?') can be heavy on larger datasets, but its fine for this small project
    qs2 = Article.objects.all().order_by('?').exclude(pk=qs1)[:3]
    latest_article_list = itertools.chain(qs1, qs2)
    context = {'latest_article_list': latest_article_list}
    return render(request, 'articles/home.html', context)


def article(request, article_uuid):
    article = get_object_or_404(Article, pk=article_uuid)
    comments = article.comments.order_by('-created')[:10] # set a reasonable amount and have the newest at the top
    suggested_articles = Article.objects.all()[:3]
    insturments = article.insturments.all()
    symbolset = set(instrument.symbol for instrument in insturments)
    companyset = set(instrument.company_name for instrument in insturments)
    stock_list = json.dumps([{
        'company_name': quote.company_name,
        'symbol': quote.symbol,
        'exchange_name': quote.exchange_name,
        'currentpriceamount': quote.currentpriceamount,
        'changeamount': quote.change_amount,
        'changepercent': quote.percent_change
    } for quote in Quote.objects.filter(Q(symbol__in= symbolset) | Q(company_name__in= companyset)) ])
    # the code above will grab only the relevant Stocks to this article, with the symbol
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            context = {'article': article, 'suggested_articles': suggested_articles, 'stock_list': stock_list,'comments': comments, 'form': form}
            return render(request, 'articles/article.html', context )
    else:
        form = CommentForm()
        context = {'article': article, 'suggested_articles': suggested_articles, 'stock_list': stock_list, 'comments': comments, 'form': form}
    return render(request, 'articles/article.html', context)


def stocks(request):
    stocks = Quote.objects.all()
    context = {'stocks': stocks}
    return render(request, 'articles/stocks.html', context)

def authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'articles/authors.html', context)


def author(request, author_uuid):
    author = get_object_or_404(Author, pk=author_uuid)
    recent_article = author.authors.order_by('-publish_at')[:1]
    print(author)
    context = {'author': author, 'recent_article': recent_article}
    return render(request, 'articles/author.html', context)
