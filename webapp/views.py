from django.shortcuts import render

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
            status=request.POST.get('status'),
            date_done=date_done
        )
        return HttpResponseRedirect('/task_page')

