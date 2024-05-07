import datetime
from django import forms
from webapp.models import Tasks


class TaskForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'super_description', 'status', 'date_done']
