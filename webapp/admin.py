from django.contrib import admin

from django.contrib import admin
from webapp.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_done']
    list_filter = ['status']
    search_fields = ['status', 'id']
    fields = ['description', 'super_description', 'status', 'date_done']
