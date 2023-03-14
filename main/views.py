from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html',  {'title' : "Главная страница сайта", 'tasks' : tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ""
    if request.method == 'POST':

        form = TaskForm(request.POST, request.FILES)
        """images = request.FILES.getlist('images')
        for image in images:
            task = Task.objects.create(image = image)"""





        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'неверная форма'

    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'main/create.html', context)


