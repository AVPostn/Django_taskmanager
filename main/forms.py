from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "status", "finalTime"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "status": Select(choices=Task.STATUSES, attrs={
                'class': 'form-control'
               })
        }
