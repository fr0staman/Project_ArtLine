from .models import Task, Orders
from django.forms import  ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть щось бубласочка'
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['P','I','B','email','phone','zona', 'DodPoslugu','Descrip']
        widgets = {
            "P": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прізвище'
            }),
            "I": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ім`я'
            }),
            "B": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'По-батькові'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Електронна пошта'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "zona": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть зону фотосесії'
            }),
            "DodPoslugu": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Додаткові послуги'
            }),
            "Descrip": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть щось бубласочка'
            }),
        }