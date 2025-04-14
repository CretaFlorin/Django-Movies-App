from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from viewer.forms import MovieForm
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from logging import getLogger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

LOGGER = getLogger()

# Create your views here.
# Functional View

# @login_required
# def hello(request):
#     return render(
#         request, template_name='hello.html',
#         context={'movies': Movie.objects.all()}
#     )

# Class-Based View
class MoviesView(LoginRequiredMixin, View):
    def get(self, request, genre=""): 
        search = request.GET.get("q") or ''
           
        movies = []
        
        
        # Filtrare dupa gen
        if genre and genre.lower() != 'all':
            movies = Movie.objects.filter(genre__name__iexact=genre)
        else:
            movies = Movie.objects.all()
            
        # Filtrare dupa search value, pe titlu si descriere
        movies = movies.filter(Q(title__icontains = search) | Q(description__icontains = search))
        
        return render(
            request, template_name='movies.html',
            context={'object_list': movies , 'genres': Genre.objects.all(), 'genre_filter':genre}
        )
        
# TemplateView Class
# class MoviesView(TemplateView):
#     template_name = 'hello.html'
#     extra_context = {'movies': Movie.objects.all()}
    
        
# ListView Class
# class MoviesView(ListView):
#     template_name = 'movies.html'
#     model = Movie
#     extra_context = {'genres': Genre.objects.all()}
            
            
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
    

class SubmittableLoginView(LoginView):
    template_name = 'accounts/login.html'
    

class SubmittableLogoutView(LoginRequiredMixin, View):
    template_name = 'accounts/confirm_logout.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return (LogoutView.as_view())(request)

class PasswordResetView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_reset.html'
