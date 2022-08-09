from django.shortcuts import render
from django.urls import path
from . import views


# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

def group_posts(request, pk):
    return HttpResponse(f'This is a post №{pk}')

# Create your views here.
