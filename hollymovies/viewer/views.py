from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Genre

# Create your views here.

def hello(request, genre=''):
    return HttpResponse(f'{genre}')