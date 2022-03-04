# необходимо из джанго импортировать формс(для создания шаблона формы)
from django import forms
# дальше импрт. модель юзерс, с которой мы работаем
from django.contrib.auth.models import User
from .models import Profile
# импортируем базовую форму рег. польз.
from django.contrib.auth.forms import UserCreationForm
from blog.models import Message


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


CHOICES = (
        ('male', 'Мужской пол'),
        ('female', 'Женский пол')
    )


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )
    sex = forms.ChoiceField(
        label='Выберите пол',
        choices=CHOICES,
        required=True,
    )
    mails = forms.BooleanField(
        label='Согласие на отправку почты',
        required=True,
        # widget=forms.TextInput(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Profile
        fields = ['img', 'sex', 'mails']


# Создадим новый шаблон формы Message
class ContactForm(forms.ModelForm):
    sender = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    subject = forms.CharField(
        label='Тема письма',
        max_length=100,
        required=True
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea,
        required=False,
        max_length=2000,
        # widget = forms.Textarea(attrs = {'class': 'form-control'})
    )
    # пока не знаю, как это реализовать
    # file = forms.FileField(
    #     label="Загрузить файл",
    #     required=False,
    # )


    class Meta:
        model = Message
        fields = ['sender', 'subject', 'message']
