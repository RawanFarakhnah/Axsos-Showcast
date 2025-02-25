from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def root(request):
    return HttpResponse('Hello World')

def another_method(request):
    return redirect('/redirected_route')

def redirected_method(request):
    response_data = {"response": "JSON response from redirected_method", "status": True}
    jsonResponse = JsonResponse(response_data)
    raw_json = json.dumps(response_data) #convert as string
    return HttpResponse(str(response_data))
    