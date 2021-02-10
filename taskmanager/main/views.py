from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, OrderForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'tasks':tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ви щось не то тикнули'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def addingorder(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ви щось не то тикнули'
    form = OrderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addingorder.html', context)

def photozones(request):
    return render(request, 'main/photozones.html')