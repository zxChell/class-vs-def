from django import forms
from app.models import *


class AddTask(forms.Form):
    task = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Task'}))
    data = forms.DateField(widget=forms.DateInput())
    status = forms.BooleanField(required=False)


class AddModelTask(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ['id', 'task', 'data', 'status']
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Task'}),
            'data': forms.DateInput(),
            'status': forms.CheckboxInput(attrs={'class': 'checkboxclass'})
        }


class AddUpdateModelTask(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'status']
