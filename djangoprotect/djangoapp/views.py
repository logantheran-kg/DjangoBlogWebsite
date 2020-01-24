from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


post = [
    {
        'author' : 'Logan',
        'time' : '8 Nov, 2019',
        'title' : 'Testing blog 1',
        'content' : 'First post content',
    },
    {
        'author' : 'Suha',
        'time' : '8 Nov, 2019',
        'title' : 'Testing blog 2',
        'content' : 'Second post content',
    }
]


def home(request):
    context = {
        'posts' : Post.objects.all()
        }
    return render(request, 'djangoapp/about.html', context)
    # return HttpResponse('<h1>Home. Hello There!!</h1>')


def about(request):
    context = {
        'posts' : post
        }
    return render(request, 'djangoapp/about.html', context)
    # return HttpResponse('<h1>Home. Hello There!!</h1>')

def secret(request):
    return HttpResponse('<h2>Hello there!, You\'ve uncovered a secret page. Welcome!</h2>')