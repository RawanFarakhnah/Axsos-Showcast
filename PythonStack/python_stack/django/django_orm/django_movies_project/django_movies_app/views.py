from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.
def root(request):
    movies = Movie.objects.all()
    return render(request, 'index.html' , {'movies': movies})