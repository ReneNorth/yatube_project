from django.shortcuts import render
from django.urls import path
from . import views


# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template)

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

def group_posts(request, pk):
    return HttpResponse(f'This is a post №{pk}')

# Create your views here.

def group_list(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)
