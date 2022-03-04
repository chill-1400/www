from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

    # магический обьект измения вывода при обращинии к опр. обьекту
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# python manage.py makemigrations - создание миграций
# python manage.py migrate - выполнение миграций

# python manage.py sqlmigrate blog 0001 - введя эту команду,
# мы посмотрим sql код, который б. выполнен при миграции
