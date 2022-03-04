from django.shortcuts import render, redirect
from .models import Course, Lesson, Comment
from .forms import CourseAddForm, CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
# from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login




# Create your views here.
class HomePage(ListView):
        model = Course
        template_name = 'courses/home.html'
        # укажем из какой табл. будут вытягиваться записи
        context_object_name = 'courses'
        ordering = ['-id']

        def get_context_data(self, *, object_list=None, **kwargs):
                ctx = super(HomePage, self).get_context_data(**kwargs)
                # укажем эл-ты, кот-ые б. передавать в словарь
                ctx['title'] = 'Главная страница сайта'
                return ctx



def tarrifsPage(request):
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы на сайте'})

# создадим отображение 1-го курса
class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        # укажем эл-ты, кот-ые б. передавать в словарь
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        # передадим все уроки, которые есть в курсе
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        # print(ctx['lessons'].query)
        return ctx



class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lessons-detail.html'
    success_msg = 'Комментарий успешно создан'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())

        # Передаем в шаблон все комментарии, что соответсвуют id записи, на которой мы находимся
        comments = Comment.objects.filter(lesson=lesson[0]['id']).all()
        ctx['comments'] = comments
        # Также передаем форму в шаблон
        ctx['commForm'] = CommentForm()

        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split("=")[1]
        return ctx

    # Этот метод срабатывает при отправке данных из формы
    def post(self, request, *args, **kwargs):
        # Получаем курс и получаем текущий урок
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).first()

        post = request.POST.copy() # Копируем POST данные прежде, чем их валидировать
        post['user'] = request.user # Устаналвиаем свои данные – указываем авторизованного пользователя
        post['lesson'] = lesson # Указываем урок, на котором сейчас находимся
        request.POST = post # Меняем request.POST данные на новые, измененные данные

        # Создаем объект на основе класса формы
        form = CommentForm(request.POST)
        if form.is_valid(): # Проверяем его
            form.save() # Сохраняем новый комментарий

        # Выполняем переадресацию
        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']

        return redirect('/course/' + url)
        



# В этом классе все наследуем от CreateView
class CourseAdd(CreateView):
    # model = Course
    # Остается лишь указать форму что будет показана,
    form_class = CourseAddForm
    # а также шаблон, что будет использован для формы
    template_name = 'courses/course_form.html'









# DetailView - нужен, чтобы вывести опр. класс на опр. странице
