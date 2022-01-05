from django import forms
from .models0 import TaskDb

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task','priority']
