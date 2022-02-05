from django.shortcuts import render, redirect
from .models import Input
from .forms import InputForm


# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'ERROR!'

    inputs = Input.objects.all()
    form = InputForm
    data = {
        'title': 'Home',
        'panel': 'Control panel',
        'btn_1': 'add',
        'btn_2': 'submit',
        'input': inputs,
        'form': form,
        'error': error}
    return render(request, 'main/index.html', data)
