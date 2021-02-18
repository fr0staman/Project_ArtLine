from django.shortcuts import render, redirect
from .forms import OrderForm

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Ви щось не то тикнули'
#     form = TaskForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/create.html', context)


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

def price(request):
    return render(request, 'main/price.html')

def homeroom(request):
    return render(request, 'main/homeroom.html')

def loftroom(request):
    return render(request, 'main/loftroom.html')

def smileroom(request):
    return render(request, 'main/smileroom.html')

def elleroom(request):
    return render(request, 'main/elleroom.html')

def inroom(request):
    return render(request, 'main/inroom.html')

def freeroom(request):
    return render(request, 'main/freeroom.html')

def formworkers():
    cursor = mysql.connection.cursor()
    cur = cursor.execute("SELECT ID_worker, surname FROM workers")
    return render_template('formworkers.html', workers0=cursor.fetchall())