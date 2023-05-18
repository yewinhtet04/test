from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDoApp
# Create your views here.
def todo_list(request):
    all_data={'todo_list':ToDoApp.objects.all()}
    return render(request,'todolist.html',all_data)

def insert(request):
    todo=ToDoApp(content=request.POST['content'])
    todo.save()
    return redirect('/todo/list/')

def delete(requeset,todo_id):
    todo=ToDoApp.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todo/list/')
def nothin(request):
    return redirect('todo/list')