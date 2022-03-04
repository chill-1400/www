from django.contrib import admin
# импортируем ту модель(таблицу), которую хотим регистрировать
from .models import News

# Register your models here.
# в этом файле мы можем зарегестрировать те таблицы, которые должны отображаться в панели администратора

admin.site.register(News)




# .models - из этой же папки, из файла models
