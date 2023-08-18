from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="blog-home"),
    path('about/',views.About, name="Blog-About"),

]
