"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Aplicatia Viewer
from viewer.models import Genre, Movie
from viewer.views import MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, SubmittableLoginView,SubmittableLogoutView


admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/<genre>', MoviesView.as_view(), name='movies_filtered'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout/', SubmittableLogoutView.as_view(), name='logout'),
]