from django.shortcuts import render, get_object_or_404
from .models import Task, Category

def index(request):
    tasks = Task.objects.filter(done=False)
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def category_tasks(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {'tasks': category.tasks.all()}
    return render(request, 'task_list.html', context)


def task_detail(request, category_slug, pk):
    category = get_object_or_404(Category, slug=category_slug)
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task, 'category': category}
    return render(request, 'task_detail.html', context)
