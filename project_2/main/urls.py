from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view/', views.view, name='view')
]
