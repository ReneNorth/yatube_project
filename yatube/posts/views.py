from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, pk):
    return HttpResponse(f'This is a post №{pk}')
