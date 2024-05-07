from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Tasks, status_choices


def task_page(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_page.html', {'tasks': tasks})


def home(request):
    return render(request, 'home.html')


def task_create(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status': status_choices})
    elif request.method == "POST":
        date_done = request.POST.get('date_done')
        if not date_done:
            date_done = None
        Tasks.objects.create(
            description=request.POST.get('description'),
            super_description=request.POST.get('super_description'),
            status=request.POST.get('status'),
            date_done=date_done
        )
        return redirect('task_page')


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
