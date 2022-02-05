from .models import View
from django.forms import ModelForm, TextInput


class InputForm(ModelForm):
    class Meta:
        model = View
        fields = ['data']

        widgets = {
            'data': TextInput(attrs={
                'class': 'form-control input'
            })
        }
