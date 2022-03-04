from django.urls import path
from . import views

# отслеживание инф-ии, куда перешёл пользователь(этот файл связан с views.py)
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.contacti, name='contacti'),
    path('uslugi', views.uslugi, name='uslugi'),
    path('todo', views.todo, name='todo'),
]
