from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

]