from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import TodoList

from todo.models import TodoList

# Create your views here.

def complete_todo(request, pk):
    curTodo = get_object_or_404(TodoList, pk=pk)
    curTodo.complete = True
    curTodo.save()
    return redirect('todos')

def delete_todo(request, pk):
	delTodo = get_object_or_404(TodoList, pk=pk)
	delTodo.delete()
	return redirect('todos')


def update_todo(request, pk):
    curTodo = get_object_or_404(TodoList, pk=pk)
    
    if request.method == 'POST':
        curTodo.todo = request.POST['todo']
        curTodo.description = request.POST['description']
        curTodo.important = request.POST.get('important') == "on"
        curTodo.complete = request.POST.get('complete') == "on"
        curTodo.save()
        return redirect('todos')

    return render(
        request,
        'todo/todo_update.html',
        {
            'curTodo' : curTodo
        }
    )
    
# def create_todo(request):
#     myTodo = TodoList()
    
#     if request.method == 'POST':
#         myTodo.todo = request.POST['todo']
#         myTodo.description = request.POST['description']
#         myTodo.important = request.POST.get('important') == 'on'
#         myTodo.complete = request.POST.get('complete') == 'on'
#         myTodo.save()
#         return redirect('todos')
    
#     return render(
#         request,
#         'todo/todo_create.html'
#     )

class create_todo(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ['todo', 'description', 'important']
    login_url = '/accounts/signin'
    
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