import json
from django.shortcuts import render
from django.views import View
import requests


class NewsUK(View):

    def get(self, request):
        uk = requests.get('http://newsapi.org/v2/top-headlines?country=gb&apiKey=8ad1d96bfae14de287f09c15dd469f76')
        uk = json.loads(uk.content)
        return render(request, 'news.html', {'news_api': uk})


class NewsUSA(View):

    def get(self, request):
        usa = requests.get('http://newsapi.org/v2/top-headlines?country=us&apiKey=8ad1d96bfae14de287f09c15dd469f76')
        usa = json.loads(usa.content)
        return render(request, 'news.html', {'news_api': usa})


class NewsPLBusiness(View):

    def get(self, request):
        pl_business = requests.get(
            'http://newsapi.org/v2/top-headlines?country=pl&category=business&apiKey=8ad1d96bfae14de287f09c15dd469f76')
        pl = json.loads(pl_business.content)
        return render(request, 'news.html', {'news_api': pl})

class NewsPLTech(View):

    def get(self, request):
        pl_tech = requests.get('http://newsapi.org/v2/top-headlines?country=pl&category=technology&apiKey=8ad1d96bfae14de287f09c15dd469f76')
        pl = json.loads(pl_tech.content)
        return render(request, 'news.html', {'news_api': pl})

class NewsPLSci(View):

    def get(self, request):
        pl_sci = requests.get('http://newsapi.org/v2/top-headlines?country=pl&category=science&apiKey=8ad1d96bfae14de287f09c15dd469f76')
        pl = json.loads(pl_sci.content)
        return render(request, 'news.html', {'news_api': pl})