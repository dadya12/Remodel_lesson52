from django.urls import path
from webapp.views import home, task_page, task_create, detail_view, delete_task, update_new

urlpatterns = [
    path('', home, name='home'),
    path('task_page/', task_page, name='task_page'),
    path('task_create/', task_create, name='task_create'),
    path('tasks/<int:pk>/', detail_view, name='detail_view'),
    path('tasks/<int:pk>/delete/', delete_task, name='delete_task'),
    path('tasks/<int:pk>/update/', update_new, name='update_new'),
]
