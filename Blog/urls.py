from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name="blog-home"),
    path('about/',views.About, name="Blog-About"),

]
