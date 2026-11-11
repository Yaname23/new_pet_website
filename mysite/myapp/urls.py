from django.contrib import admin
from django.urls import path
from .views import home_view, about, lk

app_name = 'myapp'

urlpatterns = [

    path("", home_view, name='home'),
    path('about/', about, name='about'),
    path('lk/', lk, name='lk'),
]