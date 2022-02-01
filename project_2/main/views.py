from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Home',
        'panel': 'Control panel',
        'btn_1': 'add',
        'btn_2': 'submit'}
    return render(request, 'main/index.html', data)
