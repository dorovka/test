from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'Price', 'image', 'image2', 'image3', 'image4', 'image5']
        widgets = {
            'title': TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите название товара"

        }),
            'task': Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите описание товара"

            }),
            'Price': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите цену"

            })
        }
