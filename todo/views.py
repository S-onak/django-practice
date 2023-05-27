from django.shortcuts import render

from todo.models import TodoList

# Create your views here.
def todos(request):
    todolist = TodoList.objects.all()
    return render(
        request,
        'todo/todos.html',
        {
            'todolist': todolist,
        }
    )
    
def index(request):
    todolist = TodoList.objects.all()   # todolist의 모든 레코드를 가져옴
    return render(
        request,
        'todo/index.html',
        {
            # HTML에서 todolist라는 이름으로 TodoList를 넘겨줌
            'todolist': todolist,
        }
    )