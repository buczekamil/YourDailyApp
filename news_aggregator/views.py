import json
from datetime import date
from urllib import request

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
import requests
import api
from events.models import Event
from to_do_list.models import Task, Note


class HomePage(View):

    def get(self, request):
        url_warsaw = f'http://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&appid={api.weather_api}'
        city = "Warsaw"
        Warsaw_weather = requests.get(
            url_warsaw.format(city)).json()
        weather = {
            'city': city,
            'temperature': Warsaw_weather['main']['temp'],
            'description': Warsaw_weather['weather'][0]['description'],
            'icon': Warsaw_weather['weather'][0]['icon']
        }

        url_NY = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api.weather_api}'
        city = "New York"
        NewYork_weather = requests.get(
            url_NY.format(city)).json()
        weatherNY = {
            'city': city,
            'temperature': NewYork_weather['main']['temp'],
            'description': NewYork_weather['weather'][0]['description'],
            'icon': NewYork_weather['weather'][0]['icon']
        }

        url_TY = f'http://api.openweathermap.org/data/2.5/weather?q=Tokyo&units=metric&appid={api.weather_api}'
        city = "Tokyo"
        Tokyo_weather = requests.get(
            url_TY.format(city)).json()
        weatherTY = {
            'city': city,
            'temperature': Tokyo_weather['main']['temp'],
            'description': Tokyo_weather['weather'][0]['description'],
            'icon': Tokyo_weather['weather'][0]['icon']
        }

        url_RO = f'http://api.openweathermap.org/data/2.5/weather?q=Rome,IT&units=metric&appid={api.weather_api}'
        city = "Rome"
        Rome_weather = requests.get(
            url_RO.format(city)).json()
        weatherRO = {
            'city': city,
            'temperature': Rome_weather['main']['temp'],
            'description': Rome_weather['weather'][0]['description'],
            'icon': Rome_weather['weather'][0]['icon']
        }
        if request.user.is_authenticated:
            user = request.user
            user_id = user.pk
            today = date.today()
            events = Event.objects.filter(user_id=user_id, end_time__day=today.day, end_time__month=today.month,
                                          end_time__year=today.year)
            tasks = Task.objects.filter(user_id=user_id, to_date__day=today.day, to_date__month=today.month,
                                        to_date__year=today.year)
            notes = Note.objects.all()
            if len(notes) < 1:
                note_1 = Note.objects.create(user_id=user_id, text="Make")
                note_2 = Note.objects.create(user_id=user_id, text="Note")
                note_3 = Note.objects.create(user_id=user_id, text="Here")
            else:
                note_1 = Note.objects.filter(user_id=user_id).order_by('id')[0]
                note_2 = Note.objects.filter(user_id=user_id).order_by('id')[1]
                note_3 = Note.objects.filter(user_id=user_id).order_by('id')[2]
                context = {'weather': weather, "weatherNY": weatherNY, "weatherTY": weatherTY, "weatherRO": weatherRO,
                           "events": events, "tasks": tasks,
                           "note1": note_1, "note2": note_2, "note3": note_3, 'user':user
                           }
        else:
            context = {'weather': weather, "weatherNY": weatherNY, "weatherTY": weatherTY, "weatherRO": weatherRO}

        return render(request, 'index.html'
                      , context
                      )


def update_note(request, pk):
    pk = pk
    if request.method == "POST":
        text = request.POST['note']
        note = Note.objects.filter(id=pk)
        note_updated = note.update(text=text)
        return redirect('home')


class NewsUK(View):
    def get(self, request):
        uk = requests.get(f'http://newsapi.org/v2/top-headlines?country=gb&apiKey={api.news_api}')
        uk = json.loads(uk.content)
        return render(request, 'news.html', {'news_api': uk})


class NewsUSA(View):

    def get(self, request):
        usa = requests.get(f'http://newsapi.org/v2/top-headlines?country=us&apiKey={api.news_api}')
        usa = json.loads(usa.content)
        return render(request, 'news.html', {'news_api': usa})


class NewsPLBusiness(View):

    def get(self, request):
        pl_business = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=business&apiKey={api.news_api}')
        pl = json.loads(pl_business.content)
        return render(request, 'news.html', {'news_api': pl})


class NewsPLTech(View):

    def get(self, request):
        pl_tech = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=technology&apiKey={api.news_api}')
        pl = json.loads(pl_tech.content)
        return render(request, 'news.html', {'news_api': pl})


class NewsPLSci(View):

    def get(self, request):
        pl_sci = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=pl&category=science&apiKey={api.news_api}')
        pl = json.loads(pl_sci.content)
        return render(request, 'news.html', {'news_api': pl})


def home_page_mail_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        text = request.POST['message']
        subject = f"Home Page, {name} just sent the form!"
        message = f"{name} wants contact \n\n Message:\n{text} \n\nPersonal data:\nName: {name}\n E-mail address: {mail}"
        send_mail(subject, message, 'umsiziapp@gmail.com', ["umsiziapp@gmail.com"], fail_silently=False)
        return redirect('home')
