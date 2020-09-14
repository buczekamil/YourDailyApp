"""DailyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from to_do_list import views
from news_aggregator import views as news
from events import views as events


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('todo/', views.ToDoView.as_view(), name='todo'),
    path('task/<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),
    path('news/uk/', news.NewsUK.as_view(), name="uk_news"),
    path('news/usa/', news.NewsUSA.as_view(), name="usa_news"),
    path('news/pl/business/', news.NewsPLBusiness.as_view(), name="pl_news_business"),
    path('news/pl/tech/', news.NewsPLTech.as_view(), name="pl_news_tech"),
    path('news/pl/sci/', news.NewsPLSci.as_view(), name="pl_news_sci"),
    path('calendar/', events.CalendarView.as_view(), name='calendar'),

]
