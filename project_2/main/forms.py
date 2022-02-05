from .models import Input
from django.forms import ModelForm


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['data', 'convert']
