from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
    path('course-form', views.CourseAdd.as_view(), name='course-form')
]



# с помощью views мы сможем указывать какая ф-я будет обрабатывать
# опр. юрл адрес
