from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# для переадресования используем след. метод
from django.urls import reverse

# Create your models here.
# в этом файле мы можем создавать модели, а каждая модель представляет собой таблицу в базе данных

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    # авт. подставляется текущее время
    date = models.DateTimeField('Дата', default=timezone.now)
    # on_delete=models.CASCADE - если польз. удалён, статьи удалятся тоже
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    # магический обьект измения вывода при обращинии к опр. обьекту
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Создадим новую модель в БД (контакты)
class Message(models.Model):
    # Каждое сообщение будет содержать поля:
    # почта отправителя, тема, текст сообщения и дата
    sender = models.EmailField('E-mail отправителя', max_length=100, default="")
    subject = models.CharField('Тема сообщения', max_length=100)
    text = models.TextField('Письмо')
    # file = models.FileField(label="Загрузить файл")
    date = models.DateTimeField('дата отправки', default=timezone.now)

    # При обращении к объекту на основе модели будет выводиться отправитель и тема сообщения
    def __str__(self):
        return [self.sender.sendername, '    ' ,self.subject]

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

# python manage.py makemigrations - создание миграций
# python manage.py migrate - выполнение миграций

# python manage.py sqlmigrate blog 0001 - введя эту команду,
# мы посмотрим sql код, который б. выполнен при миграции
