from django import forms


class HomeForm(forms.ModelForm):
    field = forms.CharField()

    class Meta:
        fields = ('field')
