from django.shortcuts import render
from .models import Input
from .forms import InputForm


# Create your views here.
def index(request):
    inputs = Input.objects.all()
    form = InputForm
    data = {
        'title': 'Home',
        'panel': 'Control panel',
        'btn_1': 'add',
        'btn_2': 'submit',
        'input': inputs,
        'form': form}
    return render(request, 'main/index.html', data)
