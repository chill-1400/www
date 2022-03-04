from django.urls import path
from . import views

# отслеживание инф-ии, куда перешёл пользователь(этот файл связан с views.py)
urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('interesting', views.ShowNewsView.as_view(), name='interesting'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('about', views.contacti, name='contacti'),
]
