from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Genre, Movie
from django.views import View

# Create your views here.
# Functional View
def hello(request):
    return render(
        request, template_name='hello.html',
        context={'movies': Movie.objects.all()}
    )

# Class-Based View
class MoviesView(View):
    def get(self, request):
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