from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from viewer.forms import MovieForm
from viewer.models import Movie
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from logging import getLogger

LOGGER = getLogger()

# Create your views here.
# Functional View
# def hello(request):
#     return render(
#         request, template_name='hello.html',
#         context={'movies': Movie.objects.all()}
#     )

# Class-Based View
# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='hello.html',
#             context={'movies': Movie.objects.all()}
#         )
        
# TemplateView Class
# class MoviesView(TemplateView):
#     template_name = 'hello.html'
#     extra_context = {'movies': Movie.objects.all()}
    
        
# ListView Class
class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
            
            
# FormView Class
# 1. Handling Data with FormView
# class MovieCreateView(FormView):
#     template_name = 'movie_create.html'
#     form_class = MovieForm
#     success_url = reverse_lazy('movie_create')
    
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description']
#         )
#         return result
    
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data.')
#         return super().form_invalid(form)
    
    
# 3. Handling Data with CreateView
class MovieCreateView(CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    
    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
    
    
class MovieUpdateView(UpdateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('movies')
    
    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
    
class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    
    