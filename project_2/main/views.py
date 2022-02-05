from django.shortcuts import render, redirect
from .models import Input
from .forms import InputForm
import json


# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data['data']
            input_convert = json.dumps(input_data)
            Input.objects.create(data=str(input_data), convert=input_convert)

            for count in range(1, len(request.POST) - 1):
                name = 'name' + str(count)
                input_data = request.POST[name]
                if input_data:
                    input_convert = json.dumps(input_data, ensure_ascii=False)
                    Input.objects.create(data=input_data, convert=input_convert)
                count += 1

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
