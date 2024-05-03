from django.urls import path
from webapp.views import home, task_page, task_create

urlpatterns = [
    path('', home, name='home'),
    path('task_page/', task_page, name='task_page'),
    path('task_create/', task_create, name='task_create')
]
