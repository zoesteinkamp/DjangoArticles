from django.shortcuts import render
from django.http import HttpResponse

# from datetime import datetime
#
# try:
#   valid_datetime = datetime.strptime(request.POST['date'], '%d-%m-%Y')
# except ValueError:
#   # handle th


def home(request):
    return HttpResponse("Welcome to the home page")

def articles(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)

def stocks(request):
    return HttpResponse("Welcome to the stock page")
