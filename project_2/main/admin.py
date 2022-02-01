from django.contrib import admin
from .models import Input
from django.shortcuts import render

# Register your models here.

admin.site.register(Input)


def input_home(request):
    str = Input.data()
    return render(request, {'str':str})
