# метод render позволяет выводить полноценный html шаблон
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# импортируем список(таблицу) для вывода на странице
from .models import News, Message
# за счёт след классов мы можем выбрать полностью все записи(доб. доп парам.) из опр. табл в БД (CreateView - описание внизу)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# для того чтобы создание публ. б. доступны только польз. импорт. след.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Импортируем нашу форму
from users.forms import ContactForm
# Добавлем библиотеку для отправки почты
from django.core.mail import send_mail


# Create your views here.
def home(request):
    # передпологается, что мы уже находимся в папке templates
    return render(request, 'blog/home.html', {'title': 'Главная страница'})

def interesting(request):
    data = {
        'news': News.objects.all(),
        'title': 'Интересное'
    }
    # передпологается, что мы уже находимся в папке templates
    # через запятую используем ф-ал джинджи (data)
    return render(request, 'blog/interesting.html', data)

def todo(request):
    return render(request, 'blog/todo.html', {'title': 'Список дел'})


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/interesting.html'
    context_object_name = 'news'
    # -date значит от более новых к старым
    ordering = ['-date']
    # пагинация
    paginate_by = 5

    # чтобы передавать доп. парам. нужна след. ф-я
    def get_contexr_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Услуги'
        return ctx

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    # пагинация
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    # чтобы передавать доп. парам. нужна след. ф-я
    def get_contexr_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx

class NewsDetailView(DetailView):
    model = News
    # template_name = 'blog/news_detail.html' это можно не писать
    # context_object_name = 'post' мы сделали проще изменив имя в html

    # чтобы передавать доп. парам. нужна след. ф-я
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Оновление статьи'
        ctx['btn_text'] = 'Оновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False


    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = 'interesting'
    template_name = 'blog/delete_news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


# Обработка страницы контактов
def contacti(request):
    # Если есть POST данные, то обрабатываем их
    if request.method == "POST":
        # Получаем все данные
        form = ContactForm(request.POST)
        # Проверяем на правильность
        if form.is_valid():
            # Если все хорошо, то сохраняем данные в БД,
            form.save()

            # а также создаем отправку письма.
            # В качестве значений для письма берем данные из формы
            subject = form.cleaned_data.get('subject')
            plain_message = form.cleaned_data.get('text')
            from_email = f'From <{form.cleaned_data.get("email")}>'
            to = 'admin@itproger.com'

            # Отправляем письмо
            send_mail(subject, plain_message, from_email, [to])

            # Выводим успешное сообщение
            messages.success(request, 'Сообщение было успешно отправлено')
            # Делаем редирект
            return redirect('blog-contacti')
    else:
        # Если пост данные не передаются, то просто
        # создаем объект на основе класса с формой.
        # И далее все эти данные выводим на странице шаблона
        form = ContactForm()
        return render(request, 'blog/contacti.html', {'title':'Страничка про нас', 'form': form})


# в views описываются ф-ии(классы), которые срабатывают при переходе по юрл

# в джанго все html шаблоны находятся в папке templates
# внутри templates должна быть папка с названием приложения

# джинджа - дополнительный функционал, который нам позволяет брать данные со стороны бэкенда(там где мы пишем код на питоне) и дальше в html шаблоне
# мы можем его показать где-то, либо если мы получили массив(список данных)
# мы можем его перебрать через цикл, либо мы можем добавить какие-то фильтры

# CreateView позволяет создать страницу, на кот-ой б. форма,
# при помощи котромы сразу б. добавлять записи в опр. таблицу



# django.http - позволяет выводить текст http(на осн. класса HttpResponse)
# from django.http import HttpResponse
# def home(request):
    # return HttpResponse('<h3>Привет всем</h3>')
