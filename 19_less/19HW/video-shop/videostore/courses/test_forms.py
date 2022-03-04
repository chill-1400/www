from django.test import TestCase
from .forms import CourseAddForm

class CourseAddFormTests(TestCase):

    def test_title_starting_lowercase(self):
        form = CourseAddForm(data={"title": "название в нижнем регистре"})

        self.assertEqual(
            form.errors["title"], ["Название курса должно начинаться с заглавной буквы"]
        )

    def test_title_ending_full_stop(self):
        form = CourseAddForm(data={"title": "Последний символ title."})

        self.assertEqual(form.errors["title"], ["Название курса не должно заканчиваться точкой"])

    def test_title_with_ampersand(self):
        form = CourseAddForm(data={"title": "Dart & Flutter"})

        self.assertEqual(form.errors["title"], ["Используйте «и» вместо «&»"])
