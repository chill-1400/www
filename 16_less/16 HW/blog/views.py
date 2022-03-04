# метод render позволяет выводить полноценный html шаблон
from django.shortcuts import render
# импортируем список(таблицу) для вывода на странице
from .models import News
# за счёт след класса мы можем выбрать полностью все записи из опр. табл в БД
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    # передпологается, что мы уже находимся в папке templates
    return render(request, 'blog/home.html', {'title': 'Главная страница'})

def uslugi(request):
    data = {
        'news': News.objects.all(),
        'title': 'Услуги'
    }
    # передпологается, что мы уже находимся в папке templates
    # через запятую используем ф-ал джинджи (data)
    return render(request, 'blog/uslugi.html', data)

def todo(request):
    return render(request, 'blog/todo.html', {'title': 'Список дел'})

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контакты!'})


# в views описываются ф-ии(классы), которые срабатывают при переходе по юрл

# в джанго все html шаблоны находятся в папке templates
# внутри templates должна быть папка с названием приложения

# джинджа - дополнительный функционал, который нам позволяет брать данные со стороны бэкенда(там где мы пишем код на питоне) и дальше в html шаблоне
# мы можем его показать где-то, либо если мы получили массив(список данных)
# мы можем его перебрать через цикл, либо мы можем добавить какие-то фильтры




# django.http - позволяет выводить текст http(на осн. класса HttpResponse)
# from django.http import HttpResponse
# def home(request):
    # return HttpResponse('<h3>Привет всем</h3>')
