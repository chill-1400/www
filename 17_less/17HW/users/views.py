from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
# импортируем класс для вывода сообщений(успеха, ошибки и т.д.)
from django.contrib import messages
# импортируем декоратор
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    # получаем данные из формы
    if request.method == "POST":
        form= UserRegisterForm(request.POST)
        # проверка данных(на корректность)
        if form.is_valid():
            # если всё ок - сохранение формы
            form.save()
            # получаем значение поля
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')

    else:
        #(срабатывает, когда просто переходим на страницу)
        # создаём обьект форм на осн-ве UserRegisterForm без передачи параметров
        form = UserRegisterForm()

    # передаём форму
    return render(
        request,
        'users/registration.html',
         {
             'title': 'Страница регистрации',
             'form': form
         }
     )

# добавим декоратор(обёртку) к ф-и
@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлён!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)

# если нужно создать форму, которая будет связанна с БД, то нужно создать отдельный класс(в нем сказать, с какой таблицей идёт взаимодействие, сказать какие поля должны быть в этой форме)
# потом можно создать обьект на основе этого класса
# и дальше можно его передать в шаблон(а там вывести его)

# для создания емаил создадим файл forms.py в приложении users

# для перевода пользователя на главную стр. нужен метод redirect
