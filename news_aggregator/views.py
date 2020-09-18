import json
from django.shortcuts import render
from django.views import View
import requests
import config

def index(request):
    url_warsaw = f'http://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&appid={config.weather_api}'
    city="Warsaw"
    Warsaw_weather = requests.get(
        url_warsaw.format(city)).json()
    weather = {
        'city': city,
        'temperature': Warsaw_weather['main']['temp'],
        'description': Warsaw_weather['weather'][0]['description'],
        'icon': Warsaw_weather['weather'][0]['icon']
    }

    url_NY = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={config.weather_api}'
    city = "New York"
    NewYork_weather = requests.get(
        url_NY.format(city)).json()
    weatherNY = {
        'city': city,
        'temperature': NewYork_weather['main']['temp'],
        'description': NewYork_weather['weather'][0]['description'],
        'icon': NewYork_weather['weather'][0]['icon']
    }

    url_TY = f'http://api.openweathermap.org/data/2.5/weather?q=Tokyo&units=metric&appid={config.weather_api}'
    city = "Tokyo"
    Tokyo_weather = requests.get(
        url_TY.format(city)).json()
    weatherTY = {
        'city': city,
        'temperature': Tokyo_weather['main']['temp'],
        'description': Tokyo_weather['weather'][0]['description'],
        'icon': Tokyo_weather['weather'][0]['icon']
    }

    url_RO = f'http://api.openweathermap.org/data/2.5/weather?q=Rome&units=metric&appid={config.weather_api}'
    city = "Rome"
    Rome_weather = requests.get(
        url_RO.format(city)).json()
    weatherRO = {
        'city': city,
        'temperature': Rome_weather['main']['temp'],
        'description': Rome_weather['weather'][0]['description'],
        'icon': Rome_weather['weather'][0]['icon']
    }
    context = {'weather': weather, "weatherNY": weatherNY, "weatherTY": weatherTY, "weatherRO": weatherRO}

    return render(request, 'index.html', context)  # returns the index.html template


class NewsUK(View):
    def get(self, request):
        uk = requests.get(f'http://newsapi.org/v2/top-headlines?country=gb&apiKey={config.news_api}')
        uk = json.loads(uk.content)
        return render(request, 'news.html', {'news_api': uk})


class NewsUSA(View):

    def get(self, request):
        usa = requests.get(f'http://newsapi.org/v2/top-headlines?country=us&apiKey={config.news_api}')
        usa = json.loads(usa.content)
        return render(request, 'news.html', {'news_api': usa})


class NewsPLBusiness(View):

    def get(self, request):
        pl_business = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=business&apiKey={config.news_api}')
        pl = json.loads(pl_business.content)
        return render(request, 'news.html', {'news_api': pl})


class NewsPLTech(View):

    def get(self, request):
        pl_tech = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=technology&apiKey={config.news_api}')
        pl = json.loads(pl_tech.content)
        return render(request, 'news.html', {'news_api': pl})


class NewsPLSci(View):

    def get(self, request):
        pl_sci = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=science&apiKey={config.news_api}')
        pl = json.loads(pl_sci.content)
        return render(request, 'news.html', {'news_api': pl})
