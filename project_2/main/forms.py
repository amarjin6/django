from django import forms


class InputForm(forms.Form):
    data = forms.CharField(label='data', max_length=30)
