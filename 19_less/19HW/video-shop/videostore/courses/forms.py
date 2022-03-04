from django import forms
from .models import Course, Comment
from django.forms import ModelForm, Textarea


# создаем класс для отображения формы
class CourseAddForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Название URL',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL'})
    )  # Для создания своего URL адреса
    title = forms.CharField(
        label='Название курса',
        max_length=120,
        required=True
    )
    description = forms.CharField(
        label='Описание курса',
        required=True,
        max_length=2000,
        widget=forms.Textarea
    )
    img = forms.ImageField(
        label='Изображение курса',
        required=False,
        widget=forms.FileInput
    )


    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title:
            return title

        if not title[0].isupper():
            self.add_error("title", "Название курса должно начинаться с заглавной буквы")

        if title.endswith("."):
            self.add_error("title", "Название курса не должно заканчиваться точкой")

        if "&" in title:
            self.add_error("title", "Используйте «и» вместо «&»")

        return title


    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'user', 'lesson']

        widgets = {'user': forms.HiddenInput(), 'lesson': forms.HiddenInput(), 'text': Textarea(attrs={'rows':3})}
