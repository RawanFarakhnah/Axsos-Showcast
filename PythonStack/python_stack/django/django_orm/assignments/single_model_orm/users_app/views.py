from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.
def root(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == 'POST':
       User.objects.create(
           first_name=request.POST['first_name'],
           last_name=request.POST['last_name'],
           email_address=request.POST['email_address'],
           age=request.POST['age'],
       )       
          
    return redirect('root')