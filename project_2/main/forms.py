from django.forms import ModelForm, TextInput
from django import forms


class InputForm(forms.Form):
    data = forms.CharField(label='data', max_length=30)
    fields = ['data']
    widgets = {
        'data': TextInput(attrs={
            'class': 'form-control input'
        })
    }
