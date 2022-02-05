from django.shortcuts import render
from .models import Input


# Create your views here.
def index(request):
    inputs = Input.objects.all()

    data = {
        'title': 'Home',
        'panel': 'Control panel',
        'btn_1': 'add',
        'btn_2': 'submit',
        'input': inputs}
    return render(request, 'main/index.html', data)
