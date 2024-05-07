from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Tasks, status_choices
from webapp.forms import TaskForms


def task_page(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_page.html', {'tasks': tasks})


def home(request):
    return render(request, 'home.html')


def task_create(request):
    if request.method == 'GET':
        form = TaskForms()
        return render(request, 'task_create.html', {'form': form})
    elif request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = Tasks.objects.create(
                description=form.cleaned_data.get('description'),
                super_description=form.cleaned_data.get('super_description'),
                status=form.cleaned_data.get('status'),
                date_done=form.cleaned_data.get('date_done')
            )
            return redirect('task_page')
        else:
            return render(request, 'task_create.html', {'form': form})


def detail_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, 'detail_view.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('task_page')


def update_new(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "GET":
        form = TaskForms(initial={
            'description': task.description,
            'super_description': task.super_description,
            'status': task.status,
            'date_done': task.date_done
        })
        return render(request, 'task_update.html', {'form': form})
    elif request.method == "POST":
        form = TaskForms(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.super_description = form.cleaned_data.get('super_description')
            task.status = form.cleaned_data.get('status')
            task.date_done = form.cleaned_data.get('date_done')
            task.save()
            return redirect('task_page')
        else:
            task.save()
            return render(request, 'task_update.html', {'form': form})