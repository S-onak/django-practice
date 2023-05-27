from django.urls import path
from todo.views import create_todo, todos, index, update_todo, delete_todo

urlpatterns = [
    path('', todos, name="todos"),
    path('index/', index),
    path('create_todo/', create_todo, name="create"),
    path('update_todo/<int:pk>/', update_todo, name='update'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete'),
]