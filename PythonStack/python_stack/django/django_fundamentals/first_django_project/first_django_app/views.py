from django.shortcuts import render, HttpResponse

# Create your views here.
def root(request):
    return HttpResponse("This is my main Route!")

def one_method(request):
    return HttpResponse("This is one_method Route!")

def another_method(request, my_val):
    return HttpResponse(f"This is another_method Route! {my_val} ")

def yet_another(request, name):
    return HttpResponse(f"This is yet_another Route! {name}")

def one_more(request, id, color):
    return HttpResponse(f"This is one_more Route! id:{id}, color:{color}")