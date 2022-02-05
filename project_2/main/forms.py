from .models import Input
from django.forms import ModelForm, TextInput


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['data', 'convert']

        widgets = {
            'data': TextInput(attrs={
                'class': 'form-control'
            })
        }