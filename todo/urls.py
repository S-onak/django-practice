from django.urls import path
from todo.views import todos, index

urlpatterns = [
    path('', todos),
    path('index/', index),
]