from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Genre, Movie

# Create your views here.

def hello(request):
    return render(
        request, template_name='hello.html',
        context={'movies': Movie.objects.all()}
    )
    
    
def hello_genre(request, genre):
    return render(
        request, template_name='hello.html',
        context={
            'movies': Movie.objects.filter(genre__name__iexact=genre),
            'genre':genre
        }
    )