from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todolist.models import Todo

# Create your views here.

def index(request):
    all_todos = Todo.objects.all()
    context = dict(
        todos = all_todos
    )
    return render(request, 'todolist/index.html', context)


def add(request: HttpRequest):
    new_todo = request.POST['todo']
    todo = Todo(text=new_todo)
    todo.save()
    return HttpResponseRedirect(reverse('todo-index'))


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.status = not todo.status
    todo.save()
    return HttpResponseRedirect(reverse('todo-index'))


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo-index'))