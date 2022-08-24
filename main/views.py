from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    userTasks = Task.objects.filter(owner=request.user.id)
    tasks_N = userTasks.filter(status='N')
    tasks_I = userTasks.filter(status='I')
    tasks_R = userTasks.filter(status='R')
    tasks_P = userTasks.filter(status='P')
    tasks = [("Новые", tasks_N),
             ("Запланированные", tasks_P),
             ("В процессе", tasks_I),
             ("Завершенные", tasks_R)
             ]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user.id
            obj.save()
            return redirect('home')
        else:
            error = 'форма не верная'

    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'main/create.html', context)


def edit(request, id):
    task = Task.objects.get(id=id)
    print(task)
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма не верная'

    form = TaskForm(initial={
        "title": task.title,
        "task": task.task,
        "status": task.status,
        "finalTime": task.finalTime})

    context = {
        "form": form
    }

    return render(request, 'main/edit.html', context)

def register(request):
    form = UserCreationForm()
    context = {"form":form}
    return render(request, 'registration/register.html', context)

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

def auth(request):
    render()
