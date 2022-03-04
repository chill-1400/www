from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from PIL import Image


# Создадим табл. в БД

class Course(models.Model):
    # в slug б. полное название url, по которому б.д. курс
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    # description - описание
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='course_images')
    free = models.BooleanField(default=True)

    # магический метод, который позволит менять title
    def __str__(self):
        return self.title

    # созд ф-ю которая позволит нам создать абсолютный url
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})




class Lesson(models.Model):
    slug = models.SlugField()  # Для создания своего URL адреса
    title = models.CharField(max_length=120)
    # description - описание
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    # намбэр для сортировки уроков
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    # магический метод, который позволит менять title
    def __str__(self):
        return self.title

    # созд ф-ю которая позволит нам создать абсолютный url
    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})


# Создание новой таблицы
class Comment(models.Model):
    # Три поля: ссылка на автора, ссылка на урок и текст сообщения
    user = models.ForeignKey(User, verbose_name='Пользователь', help_text='Укажите пользователя', on_delete=models.CASCADE, null=True)
    lesson = models.ForeignKey(Lesson, verbose_name='Урок', on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name='Сообщение')
    create_date = models.DateTimeField(auto_now=True)

    # магический метод, который позволит менять title
    def __str__(self):
        return self.lesson.title


# slug исп. для созздания url адреса
# поле SlugField() с проверами на $&*.. - в него мы можем
# помещать текст
