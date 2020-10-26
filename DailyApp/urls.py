from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from to_do_list import views
from news_aggregator import views as news
from events import views as events
from events import views as cal
from geo_location import views as food



urlpatterns = [
    path('aadminn/', admin.site.urls),
    path('', news.index, name='home'),

    path('todo/', views.ToDoView.as_view(), name='todo'),
    path('task/<int:pk>', views.TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),

    path('news/uk/', news.NewsUK.as_view(), name="uk_news"),
    path('news/usa/', news.NewsUSA.as_view(), name="usa_news"),
    path('news/pl/business/', news.NewsPLBusiness.as_view(), name="pl_news_business"),
    path('news/pl/tech/', news.NewsPLTech.as_view(), name="pl_news_tech"),
    path('news/pl/sci/', news.NewsPLSci.as_view(), name="pl_news_sci"),

    path('calendar/', cal.CalendarView.as_view(), name='calendar'),
    # path('calendar/create/', cal.EventAddView.as_view(), name='create_event'),
    # path('calendar/update/<int:pk>/', cal.EventUpdateView.as_view(), name='update_event'),
    # path('calendar/delete/<int:pk>', cal.EventDeleteView.as_view(), name='delete_event'),

    path('food/', food.FindRestaurantView.as_view(), name = "food"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
