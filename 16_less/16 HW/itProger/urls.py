"""itProger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
# импортируем библиотеку для работы с классами(авторизация 2лк)
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

# отслеживание инф-ии, куда перешёл пользователь
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    # в работе с классами дописывают - .as_view()
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# python manage.py startapp (название приложения) - создание приложения
# в views описываются ф-ии(классы), которые срабатывают при переходе по юрл

# в этом файле говорится, что если пользователь перешёл на гл. страницу
# то дальнейшая проверка переходов по юрл будет осуществлятся в приложении blog, в файле urls.py

# include - содержать в себе(подключать)

# 6 урок
# проведение миграций
# python manage.py makemigrations - создание миграций
# python manage.py migrate - выполнение миграций

# чтобы авторизоваться от имени администратора:
# python manage.py createsuperuser
