from django.contrib import admin
from django.urls import path, include
from to_do_list import views
from news_aggregator import views as news
from events import views as cal
from geo_location import views as food



urlpatterns = [
    path('aadminn/', admin.site.urls),
    path('', news.HomePage.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact_home/', news.home_page_mail_form, name='contact_home_page'),

    path('todo/', views.ToDoView.as_view(), name='todo'),
    path('task/<str:pk>', views.TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete_task'),

    path('news/uk/', news.NewsUK.as_view(), name="uk_news"),
    path('news/usa/', news.NewsUSA.as_view(), name="usa_news"),
    path('news/pl/business/', news.NewsPLBusiness.as_view(), name="pl_news_business"),
    path('news/pl/tech/', news.NewsPLTech.as_view(), name="pl_news_tech"),
    path('news/pl/sci/', news.NewsPLSci.as_view(), name="pl_news_sci"),

    path('calendar/', cal.CalendarView.as_view(), name='calendar'),
    path('update_event/<str:title>/<int:pk>', cal.EventUpdateView.as_view(), name='update_event'),
    path('delete_event/<str:title>/<int:pk>', cal.EventDeleteView.as_view(), name='delete_event'),

    path('food/', food.FindRestaurantView.as_view(), name = "food"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('accounts.urls')),

    path('note/<int:pk>', news.update_note, name='update_note'),

]
