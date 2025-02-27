from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root(response):
    return redirect('/blogs')

def index(response):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(response):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(response):
    return redirect('/')

def show(response, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(response, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(response, number):
    return redirect('/blogs')

def json(response):
    return JsonResponse({'title': "My first blog", 'content': 'Lorem ipsum is typically a corrupted version of De finibus bonorum et malorum'})