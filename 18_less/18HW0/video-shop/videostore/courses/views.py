from django.shortcuts import render
from .models import Course, Lesson
from .forms import CourseAddForm
from django.views.generic import ListView, DetailView, CreateView


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

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())

        #print(lesson)
        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split("=")[1]
        return ctx



# В этом классе все наследуем от CreateView
class CourseAdd(CreateView):
    # model = Course
    # Остается лишь указать форму что будет показана,
    form_class = CourseAddForm
    # а также шаблон, что будет использован для формы
    template_name = 'courses/course_form.html'









# DetailView - нужен, чтобы вывести опр. класс на опр. странице
