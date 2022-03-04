from django.contrib import admin
# указываем папку из кот-ой б. брать опр-ю модель
from .models import Course, Lesson, Comment

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
